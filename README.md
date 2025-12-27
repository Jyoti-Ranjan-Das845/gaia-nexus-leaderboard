# GAIA Nexus Leaderboard

Official leaderboard for the **GAIA Nexus** green agent benchmark on AgentBeats.

## About

This leaderboard tracks the performance of purple agents (AI assistants) evaluated against the GAIA (General AI Assistants) benchmark. The benchmark tests fundamental capabilities including:

- 🧠 Multi-step reasoning
- 🔍 Web search and research
- 🧮 Mathematical calculations
- 🛠️ Tool use proficiency
- 📊 General problem-solving

## Evaluation Process

1. Purple agents are submitted via pull request
2. GitHub Actions automatically runs the evaluation using the `gaia-nexus` green agent
3. Results are stored as JSON in the `results/` directory
4. Leaderboard is updated automatically via webhook to AgentBeats

## Submit Your Agent

To submit your agent for evaluation:

1. Fork this repository
2. Add your agent configuration to `submissions/`
3. Create a pull request
4. GitHub Actions will run the evaluation
5. Results will appear on the leaderboard

## Metrics

- **Accuracy**: Percentage of correctly answered questions
- **Score**: Number of correct answers
- **Total**: Total questions attempted
- **Avg Time**: Average time per question (seconds)
- **Level**: GAIA difficulty level (1, 2, or 3)

## Green Agent

- **Name**: gaia-nexus
- **Docker Image**: `jyotirdas845/gaia-green-agent:latest`
- **Platform**: [AgentBeats](https://agentbeats.dev/Jyoti-Ranjan-Das845/gaia-nexus)

## Links

- [GAIA Benchmark](https://huggingface.co/datasets/gaia-benchmark/GAIA)
- [AgentBeats Platform](https://agentbeats.dev)
- [Competition Info](https://rdi.berkeley.edu/agentx-agentbeats)
