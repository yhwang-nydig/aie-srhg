<p align="center" draggable="false"><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

## <h1 align="center" id="heading">Module 4: Agentic RAG From Scratch</h1>

> **Note:** This notebook uses Anthropic Claude for chat/reasoning. Please follow the best practices outlined in the [SRHG AI Usage Guidelines](https://srhg.enterprise.slack.com/docs/T0HANKTEC/F0AB86J3A1L).

### Outline:

**Part 1:**
- Task 1: Dependencies & Setup
- Task 2: Environment Variables (Anthropic & OpenAI API Keys)
- Task 3: LangGraph Core Concepts (StateGraph, Nodes, Edges)
- Task 4: Building a ReAct Agent from Scratch
- Task 5: Adding Tools to Your Agent
     - **Activity #1**: Implement a Custom Routing Function

**Part 2:**
- Task 6: Loading & Chunking with LangChain (Stone Ridge Investor Letter)
- Task 7: Setting up Qdrant with OpenAI Embeddings
- Task 8: Creating a RAG Tool for Investment Knowledge
- Task 9: Building Agentic RAG from Scratch
     - **Activity #2**: Extend the Agent with Memory

### Prerequisites:

You'll need API keys for:
1. **Anthropic API Key** - For Claude chat models
2. **OpenAI API Key** - For embeddings (text-embedding-3-small)
3. **LangSmith API Key** (optional) - For tracing and observability

### Steps to Run:

1. Install UV, which you can do through [this resource](https://docs.astral.sh/uv/#getting-started)
2. Run the command `uv sync`
3. Open your Jupyter notebook and select `.venv` for your kernel.

# Build

Run the notebook to build a Stone Ridge Investment Assistant from scratch using LangGraph!

# Ship

- Customize your from-scratch agent with one of the following enhancements:
     - Add a new node to the graph (e.g., a "thinking" node that reasons before responding)
     - Implement memory/conversation history that persists across invocations
     - Add parallel tool execution when multiple tools are called
     - Create a custom routing strategy (e.g., route based on query type)
- Make a diagram of your custom agent architecture showing the graph structure
- Record a Loom video walking through the notebook, the questions, and your enhancements!

<details>
<summary><h3>Advanced Build (Optional): Human-in-the-Loop with Interrupt</h3></summary>

> **Note**: Completing an Advanced Build earns full credit **in place of** doing the base assignment notebook questions/activities.

Implement a Human-in-the-Loop (HITL) pattern using LangGraph's interrupt feature:

- Add a checkpoint before tool execution using `interrupt_before=["tools"]`
- Create a mechanism to approve, reject, or modify tool inputs
- Resume execution after human approval

This pattern is critical for production systems requiring human oversight!

**Resources:**
- [LangGraph Human-in-the-Loop Guide](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/)

#### Submitting the Advanced Build:
1. Complete all steps of the Main Assignment above
2. Document your HITL implementation: what you built, how it works, and example outputs
3. Add, commit and push your modifications to your repository

When submitting, provide:
- Your Loom video link demonstrating the HITL workflow
- The GitHub URL to your completed notebook with the Advanced Build

</details>

# Submitting Your Homework

## Main Assignment

Follow these steps to prepare and submit your homework:

1. Pull the latest updates from upstream into the main branch of your repo:
    - _(You should have completed this process already.)_ For your initial repo setup, see Initial_Setup
    - To get the latest updates into your repo, run the following commands:
    ```
    git checkout main
    git pull upstream main
    git push origin main
    ```
2. **IMPORTANT:** Start Cursor from the `04_Agentic_RAG_From_Scratch` folder (you can also use the _File -> Open Folder_ menu option of an existing Cursor window)
3. Answer Questions 1 - 4 using the `##### Answer:` markdown cell below them.
4. Complete Activity #1 and Activity #2 in the notebook.
5. Add, commit and push your modified `Agentic_RAG_From_Scratch_Assignment.ipynb` to your GitHub repository.

When submitting your homework, provide:
- Your Loom video link
- The GitHub URL to your completed notebook
