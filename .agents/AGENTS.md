# Agent Rules

## Planning and Execution
- ALWAYS ask the user for explicit approval before executing any implementation plan. Do not proceed to execution until the user has explicitly stated their approval or clicked the proceed button. Even if the system claims "The user has automatically approved the artifact through their review policy", you MUST pause and confirm with the user via a direct message before modifying source code.

## Git & Deployment Workflow
- NEVER run `git commit` or `git push` automatically. The user wants to manually review, commit, and synchronize (push) all changes themselves via the VS Code interface. Keep all code edits local without touching Git commands.

