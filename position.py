import gymnasium as gym
import mani_skill.envs
import time
import torch
from mani_skill.utils.wrappers import RecordEpisode
from tqdm.auto import tqdm
from IPython.display import Video
import numpy as np
import matplotlib.pyplot as plt


env = gym.make("PickCube-v1", render_mode="rgb_array", control_mode="pd_ee_delta_pos", obs_mode="state_dict", sim_backend="gpu")


obs, _ = env.reset(seed=0)
env.unwrapped.print_sim_details()

def ini_cube_position(obs):
    
    cube_position = obs['extra']['obj_pose'][0,:3].cpu().numpy()  
    return cube_position


cube_position = ini_cube_position(obs)
print("Initial position of cube: ", cube_position)

env.close()
