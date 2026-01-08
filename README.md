# Robotic-ARM_Pick-cube
# Trajectory Generation & Cube Manipulation

## Problems

**Problem 1: Trajectory Generation**
- Move robot arm in X, Y, Z directions
- Record joint and gripper states

**Problem 2: Cube Pick-up**
- Pick up cube from table
- Record end-effector (x, y, z) positions

**Demo**

https://github.com/Danyabm/Robotic-ARM_Pick-cube/blob/main/pick.mp4

## Installation

```bash
conda create -n maniskill_env python=3.9
conda activate maniskill_env
pip install --upgrade mani_skill
pip install torch torchvision torchaudio
```

## Usage

```bash
python trajectory_generation.py
python pickup.py
```

## Files

```
├── problem1_trajectory_generation.py
├── problem2_cube_pickup.py
├── Videos/
└── plots/
```

## Results

- Videos: Movement demonstrations
- Plots: Joint states and end-effector trajectories in lab1.pdf

## References

- [ManiSkill Docs](https://maniskill.readthedocs.io/en/latest/)
- [ManiSkill GitHub](https://github.com/haosulab/ManiSkill)
