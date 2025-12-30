import os
from minisweagent.agents.default import DefaultAgent
from minisweagent.models.litellm_model import LitellmModel
from minisweagent.environments.local import LocalEnvironment

def generate_github_patch(issue_url):
    # 1. Setup Environment Variables
    # Ensure your API key is set in the environment or here:
    # os.environ["ANTHROPIC_API_KEY"] = "your-api-key"
    
    # 2. Initialize the Model (using LiteLLM backend)
    # You can change the model name to "gpt-4o" or others supported by LiteLLM
    model = LitellmModel(name="claude-3-5-sonnet-20240620")

    # 3. Initialize the Environment
    # 'local' environment runs commands in your current shell/directory
    env = LocalEnvironment()

    # 4. Initialize the Agent
    # We use the DefaultAgent which handles the ReAct loop
    agent = DefaultAgent(model=model, env=env)

    # 5. Define the Task
    task = f"Fix the issue described at {issue_url}. " \
           f"Analyze the repository, reproduce the bug, and provide a fix."

    print(f"--- Starting Agent for Issue: {issue_url} ---")
    
    # 6. Run the Agent
    # The run() method returns the exit status and final message
    status, message = agent.run(task=task)

    print(f"\n--- Execution Finished ---")
    print(f"Status: {status}")
    print(f"Final Message: {message}")

    # The agent typically leaves the changes in the local directory.
    # You can generate a git diff to get the actual patch:
    import subprocess
    patch = subprocess.check_output(["git", "diff"]).decode("utf-8")
    
    with open("issue_fix.patch", "w") as f:
        f.write(patch)
    
    print("\nPatch saved to 'issue_fix.patch'")

if __name__ == "__main__":
    ISSUE_LINK = "https://github.com/SeekingDream/AgentTestRepo/issues/109"
    generate_github_patch(ISSUE_LINK)
