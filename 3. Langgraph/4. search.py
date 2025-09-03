from typing import Annotated
from langgraph.graph import START,END, StateGraph
from langgraph.graph.message import add_messages 
from langchain_ibm import ChatWatsonx 
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv
import os 
from colorama import Fore 
from langchain.tools import tool 
from src.tools.search import GovSearch


load_dotenv()

llm = ChatWatsonx(
    model_id="meta-llama/llama-4-maverick-17b-128e-instruct-fp8",
    project_id=os.environ['WATSONX_PROJECT_ID'],
    params={'max_tokens':5000}
)

tools = [GovSearch]
tool_node = ToolNode(tools) 

llm_with_tools = llm.bind_tools(tools) 

class State(dict):
    messages: Annotated[list, add_messages]

def chatbot(state:State):
    messages = state['messages']
    if not messages or not isinstance(messages[0], SystemMessage):
        system_msg = SystemMessage(content="You are a helpful assistant with access to a range of tools. Use them as needed to help the user accomplish their task as fast as possible.")
        messages = [system_msg] + messages
    
    response = llm_with_tools.invoke(messages)
    return {'messages': [response]}

def router(state:State):
    last_message = state['messages'][-1]
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls: 
        return "tools" 
    else: 
        return END 

graph_builder = StateGraph(State) 
graph_builder.add_node("chatbot", chatbot) 
graph_builder.add_node("tools", tool_node) 
graph_builder.add_edge(START, "chatbot") 
graph_builder.add_edge("tools", "chatbot") 
graph_builder.add_conditional_edges("chatbot", router) 
# memory = InMemorySaver() 
# graph = graph_builder.compile(checkpointer=memory)
graph = graph_builder.compile()

if __name__ == '__main__': 
    while True: 
        prompt = input(Fore.LIGHTCYAN_EX + "⚡️ Enter your prompt here: " + Fore.RESET)
        # Use proper message format
        result = graph.invoke(
            {"messages": [
                {'role':'system', 'content':'You are a helpful assistant designed to assist with user queries'}, 
                {'role':'user', 'content':prompt}
                ]},  
            config={"configurable": {"thread_id": 1234}}
        ) 
        print(Fore.LIGHTMAGENTA_EX + result['messages'][-1].content + Fore.RESET) 

# if __name__ == '__main__': 
#     print(searcher.invoke({"url":"https:hola", "search_term":"abc123"}))
