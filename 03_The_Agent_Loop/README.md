<p align="center" draggable="false"><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

## <h1 align="center" id="heading">Module 3: The Agent Loop</h1>

> **Note:** This notebook uses Anthropic Claude for chat/reasoning. Please follow the best practices outlined in the [SRHG AI Usage Guidelines](https://srhg.enterprise.slack.com/docs/T0HANKTEC/F0AB86J3A1L).

### Outline:

**Part 1:**
- Task 1: Dependencies
- Task 2: Environment Variables (Anthropic & OpenAI API Keys)
- Task 3: LangChain Core Concepts (Runnables & LCEL)
- Task 4: Understanding the Agent Loop
- Task 5: Building Your First Agent with `create_agent()`
     - **Activity #1**: Create a Custom Tool

**Part 2:**
- Task 6: Loading & Chunking Documents (Stone Ridge Investor Letter)
- Task 7: Setting up Qdrant Vector Database
- Task 8: Creating a RAG Tool for Investment Knowledge
- Task 9: Introduction to Middleware
- Task 10: Building Agentic RAG with Middleware
     - **Activity #2**: Enhance the Agent

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

Run the notebook to build a Stone Ridge Investment Assistant!

# Ship

- Add one of the following enhancements (or whatever augmentations suit your use case) to the agentic RAG system:
     - Add a new tool (CAGR calculator, return comparison, etc.)
     - Create custom middleware (logging, compliance disclaimers, rate limiting)
     - Improve the RAG tool (metadata filtering, reranking, citations)
     - Add conversation memory to the agent
- Make a simple diagram of your agent architecture
- Run the notebook
- When you're finished with augmentations, compare your enhanced agent to the baseline!
- Record a Loom video walking through the notebook, the questions in the notebook, and your addition!

<details>
<summary><h3>Advanced Build (Optional): Human-in-the-Loop Middleware</h3></summary>

> **Note**: Completing an Advanced Build earns full credit **in place of** doing the base assignment notebook questions/activities.

Implement a Human-in-the-Loop (HITL) component using LangChain's middleware system:

- Use `HumanInTheLoopMiddleware` to pause agent execution before tool calls
- Create a custom approval function that lets users approve, reject, or edit tool inputs
- Add the middleware to your investment agent
- Test with queries that trigger different tools

This pattern is critical for production systems requiring human oversight!

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
2. **IMPORTANT:** Start Cursor from the `03_The_Agent_Loop` folder (you can also use the _File -> Open Folder_ menu option of an existing Cursor window)
3. Answer Questions 1 - 4 using the `##### Answer:` markdown cell below them.
4. Complete Activity #1 and Activity #2 in the notebook.
5. Add, commit and push your modified `The_Agent_Loop_Assignment.ipynb` to your GitHub repository.

When submitting your homework, provide:
- Your Loom video link
- The GitHub URL to your completed notebook
