---
layout: default
title: Home
---

# Nick's Mega Ultra Fun Watsonx Agentic Crash Course

Welcome to the ultimate crash course on building AI agents with Watsonx! This comprehensive course will take you from zero to hero in the world of agentic AI, covering three different approaches to building agents.

## 🎯 Course Overview

This course is designed to give you hands-on experience with building AI agents using different levels of technical complexity. Whether you're a business user, a low-code developer, or a seasoned programmer, there's a path for you.

## 🚀 What You'll Learn

By the end of this course, you'll be able to:
- Build no-code agents using Watsonx Orchestrate
- Create visual agent workflows with Langflow
- Develop sophisticated agents with Langgraph and Python
- Implement proper AI governance and evaluation strategies

## 📚 Course Structure

This course is organized into four progressive sections:

<div class="course-sections">
{% for section in site.course.sections %}
  <div class="section-card">
    <h3><a href="{{ section.page }}.html">{{ section.title }}</a></h3>
    <p>{{ section.description }}</p>
    <div class="video-placeholder">
      📹 <em>Video tutorial coming soon!</em>
    </div>
  </div>
{% endfor %}
</div>

## 🛠 Prerequisites

Before you begin, make sure you have:
- A basic understanding of AI concepts
- Access to Watsonx services (instructions provided in each section)
- Python 3.8+ installed for the Langgraph section
- Git for cloning the repository

## 📁 Repository Structure

```
6-08-2025-DTA/
├── 1. Orchestrate/     # No-code agent building
├── 2. Langflow/        # Low-code visual development
├── 3. Langgraph/       # Pro-code Python development
├── 4. Governance/      # AI governance and evaluation
└── docs/              # Course documentation (this site)
```

## 🎬 Getting Started

1. **Clone the repository**: 
   ```bash
   git clone https://github.com/nicknochnack/6-08-2025-DTA.git
   cd 6-08-2025-DTA
   ```

2. **Install dependencies**:
   ```bash
   pip install uv
   uv sync
   ```

3. **Choose your learning path**:
   - 🆕 **New to AI agents?** Start with [Orchestrate](orchestrate.html)
   - 🔧 **Want visual development?** Jump to [Langflow](langflow.html)
   - 💻 **Ready for coding?** Go to [Langgraph](langgraph.html)
   - 🛡️ **Interested in governance?** Check out [Governance](governance.html)

## 📧 Support

If you have questions or need help:
- Check the README files in each section folder
- Review the code examples and documentation
- Reach out during the course sessions

---

## 👨🏾‍💻 About the Instructor

**Nick Renotte** - AI Engineer and Content Creator  
📅 **Version**: 1.x  
📜 **License**: MIT License

<style>
.course-sections {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  margin: 20px 0;
}

.section-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  background: #f9f9f9;
}

.section-card h3 {
  margin-top: 0;
  color: #333;
}

.section-card h3 a {
  text-decoration: none;
  color: #0066cc;
}

.section-card h3 a:hover {
  text-decoration: underline;
}

.video-placeholder {
  margin-top: 15px;
  padding: 10px;
  background: #e8f4fd;
  border-radius: 4px;
  font-style: italic;
  color: #666;
}
</style> 