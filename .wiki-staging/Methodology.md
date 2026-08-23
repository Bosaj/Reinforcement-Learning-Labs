# Methodology

## HomeWork — grid world introduction

A custom treasure/trap grid world, first solved with a random policy baseline, then with a tabular Q-learning agent. `HomeWorkAnimation.py` renders the learned policy's trajectory as a terminal animation.

## TP1 — CartPole-v1

Introductory notebook covering the basics of a Q-table representation and the RL loop (observe, act, receive reward) on Gymnasium's `CartPole-v1`.

## TP2 — FrozenLake-v1: Q-learning

Tabular Q-learning on `FrozenLake-v1`, with the update rule:

```
Q[s, a] += alpha * (reward + gamma * max(Q[s', :]) - Q[s, a])
```

Hyperparameters: `alpha = 0.1` (learning rate), `gamma = 0.99` (discount factor), `epsilon = 1.0` decaying by `epsilon_decay = 0.995` per episode, over `num_episodes = 1000`.

## TP3 — Custom traffic-light simulation: Q-learning vs. SARSA

A custom `traffic_env.py` environment models a traffic-light control problem. Both algorithms are trained for 5,000 episodes each with `alpha = 0.1`, `gamma = 0.9`, `epsilon = 0.1` (fixed, not decayed):

- **Q-learning** (off-policy): `Q[s,a] += alpha * (reward + gamma * max(Q[s']) - Q[s,a])`
- **SARSA** (on-policy): `Q[s,a] += alpha * (reward + gamma * Q[s', a'] - Q[s,a])`, using the actually-chosen next action `a'` rather than the greedy max

Cumulative rewards for both algorithms are plotted together (`qlearning_vs_sarsa.png`) to visually compare convergence behavior — SARSA's on-policy updates tend to produce more conservative, safer learned behavior than Q-learning's off-policy max, a classic distinction this lab is designed to surface.

## TP4 — Taxi-v3: PPO

A from-scratch Proximal Policy Optimization implementation (not a library like Stable-Baselines3) on `Taxi-v3`. Key settings: `gamma = 0.99`, `clip_epsilon = 0.2` (the PPO clipping range), exploration epsilon decaying from `1.0` to a floor of `0.01` at a rate of `0.995` per episode, trained over `num_episodes = 40000`. Episode rewards are logged every 100 episodes during training, and the trained policy is evaluated separately over 20 evaluation episodes.

## Evaluation approach

All four labs rely on cumulative-reward plots over training episodes as the primary evidence of learning, plus qualitative video demonstrations of the trained agent acting in its environment — the standard, lightweight evaluation approach for tabular/from-scratch RL coursework rather than a benchmark-style statistical comparison across seeds.
