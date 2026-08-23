# FAQ

**Why do TP2 and TP3 use different hyperparameters for Q-learning?**
They're separate exercises targeting different environments and course objectives — TP2 uses a higher discount factor (`gamma = 0.99`) with epsilon decay over 1,000 episodes on `FrozenLake-v1`, while TP3 uses a lower discount (`gamma = 0.9`) with a fixed exploration rate over 5,000 episodes to give a stable, comparable baseline against SARSA. There's no shared configuration across labs.

**What's the actual difference between Q-learning and SARSA in TP3?**
Q-learning updates toward the best possible next action (off-policy, `max(Q[s'])`), while SARSA updates toward the action it will actually take next (on-policy, `Q[s', a']`). This makes SARSA's learned policy more sensitive to its own exploration strategy — it tends to avoid risky actions during training since exploration mistakes get folded into its own value estimates.

**Is TP4's PPO implementation from a library like Stable-Baselines3?**
No — it's a from-scratch implementation of the core PPO update (clipped surrogate objective with `clip_epsilon = 0.2`) built directly in the notebook, not a call into an existing RL library.

**Why isn't full agent training run in CI?**
Training runs from a few thousand (Q-learning/SARSA) to 40,000 episodes (PPO), which is too slow for a CI runner and doesn't need to be re-verified on every push — CI instead checks that the notebooks are valid and the code has no syntax/import errors.

**Where do the demo videos and screenshots come from?**
They're artifacts (`.mp4`, `.png`) produced by running each `TPx` notebook's rendering cells against the trained agent, then committed to the repo so results are visible without rerunning training.

**Do I need a GPU to run these labs?**
No — all four labs are lightweight enough (tabular Q-tables or a small from-scratch PPO) to run on CPU in a reasonable time, unlike deep RL benchmarks that require thousands of parallel environment steps.
