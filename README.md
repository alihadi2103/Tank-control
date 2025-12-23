# Tank-Control: RL-based Controllers for Industrial Tank Systems




## Overview

**Tank-Control** is a research-oriented project implementing **reinforcement learning (RL) controllers** for industrial tank-level systems. It serves as a **proof-of-concept** to explore whether RL can effectively manage liquid levels in **1, 2, and 6-tank systems**.

The project evaluates both **value-based** and **policy-based RL methods**, as well as traditional controllers like **P-controllers**, to study their performance, stability, and ability to handle disturbances.

**Key Contributions:**

* Multi-agent RL implementations for tank-level regulation
* Comparison of RL vs classical controllers
* Modular framework supporting various RL algorithms and tank configurations
* Baseline implementation for further research in industrial process control

---

## Intuition & Problem Statement

Industrial tank systems are **highly nonlinear** and often exhibit **coupled dynamics** where each tank’s input and output affects others. Manual or classical control strategies face challenges including:

* Managing **interconnected tanks** where a single input impacts multiple outputs
* Coping with **dynamic disturbances** and measurement noise
* Designing controllers without precise models of the process

**Reinforcement Learning Approach:**

* **Value-based RL (DQN):** Approximates the action-value function for discrete actions, learning optimal policies through experience
* **Policy-gradient methods (REINFORCE, Actor-Critic):** Directly optimize policies, suitable for continuous control
* **Multi-agent coordination:** Each tank can be treated as an agent, learning cooperative strategies

**Benefits:**

* Handles **nonlinearity** without explicit system modeling
* Learns **long-horizon strategies** considering cumulative effects
* Multi-agent setup enables **distributed control** for complex systems
* Provides **research insights** for future industrial applications of RL

---

## Technical Details

### 1. RL Algorithms Implemented

#### Off-Policy Value-Based Methods

* **Deep Q-Network (DQN)** with replay buffers
* Supports **multi-agent learning** for multi-tank systems
* Batch updates improve stability

#### Policy-Gradient Methods

* **REINFORCE with Monte Carlo baselines**
* Handles discrete or continuous actions
* Batch processing reduces variance and improves convergence

#### Actor-Critic Methods

* Actor network outputs control signals for tanks
* Critic evaluates state-action pairs
* Combines policy optimization with value-based guidance
* Continuous actions provide **smoother control**

### 2. Traditional Controllers

* **P-controller:** Serves as a baseline
* Provides a benchmark for input smoothness and level stability

### 3. Multi-Agent Design

* Each tank is an agent observing local state
* Agents learn cooperative policies in multi-tank setups
* Handles **partial observability** and non-stationarity

### 4. Training Workflow

1. Initialize environment (1, 2, or 6 tanks)
2. Select RL algorithm and hyperparameters
3. Agents interact with environment, collecting states, actions, and rewards
4. Update policies using chosen RL algorithm
5. Evaluate against traditional P-controller
6. Log rewards, actions, and level trajectories for analysis

### 5. Evaluation Metrics

* Cumulative reward over episodes
* Liquid level tracking error
* Smoothness of control inputs
* Multi-agent coordination effectiveness

---

## Repository Structure

```
.
├── Actor_Critic/          # Actor-Critic RL implementation
├── P_controller/          # Classical P-controller scripts
├── Policy_Gradient/       # REINFORCE and policy-gradient methods
├── Q_learning/            # DQN and multi-agent Q-learning
├── disturbance_200.csv    # Sample disturbance dataset
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## Installation

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

> Note: PyTorch installation should match your OS and CUDA version from [PyTorch](https://pytorch.org/get-started/locally/).

---

## Quick Start

Example: Train a DQN agent for a 2-tank system:

```bash
python Q_learning/train_2tanks.py --episodes 1000 --batch_size 128
```

* For Actor-Critic or REINFORCE, run the respective scripts in `Actor_Critic/` or `Policy_Gradient/`
* Compare performance against the P-controller scripts in `P_controller/`
* Visualize rewards, control inputs, and tank levels using plotting utilities

---

## Key Insights

* RL can **learn effective control policies** for single and multi-tank systems
* Multi-agent setup improves coordination for multi-tank configurations
* Traditional controllers currently outperform RL in **input smoothness** and **oscillation minimization**
* RL provides a **flexible, model-free framework** for experimental industrial control

---

## Future Improvements

* Implement **continuous action RL** for smoother tank control
* Integrate **attention mechanisms** for multi-agent coordination
* Include **safety constraints** to avoid overflows or unsafe states
* Extend to **larger, nonlinear industrial processes**
* Explore **hybrid RL-traditional control strategies**

---

## License

[MIT License](LICENSE)

---

## Author

Ali Hadi — [GitHub](https://github.com/alihadi2103)




