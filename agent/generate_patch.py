import os
from mini_swe_agent import MiniSWEAgent

def main():
    # Environment variables set in the GitHub Action
    issue_number = os.environ.get("ISSUE_NUMBER")
    repo_path = os.environ.get("REPO", ".")
    gh_token = os.environ.get("GH_TOKEN")

    if not issue_number:
        raise ValueError("ISSUE_NUMBER not set in environment variables")

    print(f"Generating patch for issue #{issue_number} in {repo_path}")

    # Initialize the agent
    agent = MiniSWEAgent(
        repo_path=repo_path,
        github_token=gh_token
    )

    # Get the issue content from GitHub
    issue_url = f"https://github.com/{os.environ['REPO']}/issues/{issue_number}"
    issue_content = agent.get_github_issue(issue_url)

    # Generate a patch to fix the issue
    patch = agent.fix_issue(issue_content)

    # Save patch locally (optional)
    patch_file = f"agent_patch_issue_{issue_number}.diff"
    with open(patch_file, "w") as f:
        f.write(patch)

    print(f"Patch generated and saved to {patch_file}")
    print("Patch content:\n")
    print(patch)

if __name__ == "__main__":
    main()
