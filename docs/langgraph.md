---
layout: default
title: "Chapter 3: Langgraph"
---

# Chapter 3: Pro-Code Agent Development with Langgraph

Welcome to the most powerful chapter of our course! Here we dive into **pro-code agent development** using Langgraph - giving you complete control over sophisticated AI agent architectures.

## 🎯 Learning Objectives

By the end of this chapter, you'll be able to:
- Understand Langgraph's graph-based agent architecture
- Build agents with persistent memory and conversation history
- Integrate external tools and APIs into your agents
- Create structured output agents with type safety
- Implement search and web scraping capabilities
- Build complex multi-agent workflows with state management

## 📹 Video Tutorial

<div class="video-container">
  <div class="video-placeholder">
    📹 <strong>Video Tutorial Coming Soon!</strong><br>
    <em>Deep dive into building production-ready agents with Python and Langgraph</em>
  </div>
</div>

## 🚀 What is Langgraph?

Langgraph is a library for building stateful, multi-actor applications with LLMs. Key features include:
- **Graph-based architecture** for complex agent workflows
- **Persistent state management** across conversations
- **Tool integration** for external system access
- **Multi-agent coordination** with shared state
- **Streaming support** for real-time interactions
- **Built-in persistence** for production deployments

## 🛠 Setup Instructions

Before diving into the exercises, ensure your environment is ready:

```bash
# Navigate to the Langgraph directory
cd "3. Langgraph"

# Install dependencies (if not already done)
uv sync

# Set up your environment variables
export OPENAI_API_KEY="your-openai-api-key"
export GITHUB_TOKEN="your-github-token"  # For GitHub integration
```

## 📚 Progressive Learning Path

### 0. Basic Agent (`0. basic.py`)

**Objective**: Understand the fundamental Langgraph structure

**What you'll learn**:
- Basic agent setup and configuration
- Simple conversation flow
- State management basics

**Try this**:
```python
python "0. basic.py"
```

### 1. Memory Agent (`1. memory.py`)

**Objective**: Add persistent memory to your agent

**What you'll learn**:
- Conversation history management
- State persistence across sessions
- Memory retrieval and context handling

**Test prompts**:
1. `"My name is Nick, who is Nick?"`
2. Continue the conversation to test memory retention

**Key concepts**:
- **Checkpointing**: Save conversation state
- **Memory retrieval**: Access previous context
- **State updates**: Modify conversation history

### 2. Tool Integration (`2. tool.py`)

**Objective**: Connect your agent to external tools

**What you'll learn**:
- Tool definition and registration
- GitHub API integration
- Structured tool responses

**Test prompt**:
```
"Get me the trending Python repos on GitHub"
```

**Tools demonstrated**:
- GitHub repository search
- API response processing
- Error handling for external services

### 3. Structured Outputs (`3. structured.py`)

**Objective**: Generate type-safe, structured responses

**What you'll learn**:
- Pydantic model integration
- Type safety for agent outputs
- Structured data validation

**Test prompt**:
```
"What are the trending Python repos on GitHub?"
```

**Key features**:
- **Type safety**: Ensure output conforms to expected structure
- **Validation**: Automatic data validation
- **Serialization**: Easy conversion to JSON/other formats

### 4. Search Capabilities (`4. search.py`)

**Objective**: Add web search and information retrieval

**What you'll learn**:
- Web search integration
- Information synthesis from multiple sources
- Search result processing and ranking

**Test prompts**:
```
"What are the six states of the investment oversight framework from digital.gov.au?"
"Give me a summary of the AGA from here https://architecture.digital.gov.au/purpose"
```

**Features**:
- **Web scraping**: Extract content from URLs
- **Search integration**: Query search engines
- **Content synthesis**: Combine information from multiple sources

### 5. Endpoint Review (`5. endpointreview.py`)

**Objective**: Analyze and review web endpoints

**What you'll learn**:
- Automated website analysis
- Content extraction and summarization
- Technical assessment capabilities

**Test with**:
```
"Analyze digital.gov.au"
```

**Capabilities**:
- **Site analysis**: Understand website structure
- **Content review**: Extract key information
- **Technical assessment**: Evaluate site features

### 6. Project Reporting (`6. projectreporting.py`)

**Objective**: Generate comprehensive project reports

**What you'll learn**:
- Document processing and analysis
- Report generation from multiple sources
- Structured project insights

**Test with**:
```python
# Uses project.pdf as input
python "6. projectreporting.py"
```

## 💡 Advanced Concepts

### Graph Architecture
```python
# Basic graph structure
from langgraph.graph import StateGraph

graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.add_node("tools", tool_node)
graph.add_edge("agent", "tools")
graph.set_entry_point("agent")
```

### State Management
```python
from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List[BaseMessage]
    conversation_id: str
    user_context: dict
```

### Tool Integration
```python
from langchain_core.tools import tool

@tool
def search_github(query: str) -> str:
    """Search for repositories on GitHub."""
    # Implementation here
    return results
```

### Memory Persistence
```python
from langgraph.checkpoint import MemorySaver

memory = MemorySaver()
app = graph.compile(checkpointer=memory)
```

## 🔧 Code Examples

### Basic Agent Flow
```python
# See 0. basic.py for complete implementation
def create_basic_agent():
    model = ChatOpenAI(model="gpt-4")
    agent = create_react_agent(model, tools=[])
    return agent
```

### Memory Integration
```python
# See 1. memory.py for complete implementation
def agent_with_memory(state: AgentState):
    response = model.invoke(state["messages"])
    return {"messages": [response]}
```

### Tool Usage
```python
# See 2. tool.py for complete implementation
@tool
def get_trending_repos(language: str = "python") -> str:
    """Get trending repositories from GitHub."""
    # GitHub API integration
    return formatted_results
```

## 🎯 Practice Projects

### Project 1: Personal Assistant
Build an agent that can:
- Remember personal preferences and context
- Search the web for information
- Integrate with calendar and email APIs
- Generate structured reports

### Project 2: Code Review Agent
Create an agent that:
- Analyzes GitHub repositories
- Reviews code quality and security
- Suggests improvements
- Generates documentation

### Project 3: Research Assistant
Develop an agent that:
- Conducts comprehensive web research
- Synthesizes information from multiple sources
- Generates structured research reports
- Tracks research progress over time

## 🔍 Debugging and Development

### Debug Mode
```python
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)
```

### State Inspection
```python
# Check current state
print(f"Current state: {state}")
print(f"Messages: {state.get('messages', [])}")
```

### Tool Testing
```python
# Test tools independently
result = tool.invoke({"query": "test input"})
print(f"Tool result: {result}")
```

## ➡️ Next Steps

Ready to implement governance and evaluation? Move on to:

**[Chapter 4: Governance →](governance.html)** - Learn AI governance and evaluation strategies

---

## 📁 Code Files

All the complete implementations are available:

```
3. Langgraph/
├── 0. basic.py              # Basic agent setup
├── 1. memory.py             # Memory integration
├── 2. tool.py               # Tool integration
├── 3. structured.py         # Structured outputs
├── 4. search.py             # Search capabilities
├── 5. endpointreview.py     # Endpoint analysis
├── 6. projectreporting.py   # Project reporting
├── project.pdf              # Sample project document
├── README.md                # Setup instructions
└── src/
    ├── tools/
    │   ├── github.py        # GitHub integration
    │   └── search.py        # Search utilities
    └── utils/
        └── linkutils.py     # URL utilities
```

## 🔗 Essential Resources

- [**Langgraph Documentation**](https://langchain-ai.github.io/langgraph/) - Official documentation
- [**LangChain Tools**](https://python.langchain.com/docs/modules/agents/tools/) - Available tools and integrations
- [**GitHub API Docs**](https://docs.github.com/en/rest) - For tool integration

<style>
.video-container {
  margin: 20px 0;
  text-align: center;
}

.video-placeholder {
  background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
  color: white;
  padding: 40px 20px;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.video-placeholder strong {
  font-size: 1.2em;
  display: block;
  margin-bottom: 10px;
}
</style> 