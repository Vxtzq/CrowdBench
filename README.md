<p align="center">
  <a href="https://crowdgpt.net">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Vxtzq/CrowdBench/refs/heads/main/docs/logo-dark.jpeg">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Vxtzq/CrowdBench/refs/heads/main/docs/logo-light.jpeg">
      <img
        src="https://raw.githubusercontent.com/Vxtzq/CrowdGPT/main/res/logo-light.png"
        alt="CrowdGPT"
        width="100%"
        style="width: 100%; max-width: 100%; height: auto; display: block; border-radius: 12px;"
      >
    </picture>
  </a>
</p>


# CrowdBench
Joint project to CrowdGPT - The collaborative LLM benchmark.

Anyone can submit a .crbench file to the folder benchmark/, following this template:

```
# CrowdBench Task
# ID: math.algebra.0001
# Category: mathematics

[question]
Your question here

[answer]
\boxed{Precise deterministic answer}
```

# How it works
The benchmark iterates over all the questions submitted, asks the LLM about it and monitors correctness.

# Leaderboard
Coming soon.
