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

env = RecordEpisode(env, output_dir="Videos/try", save_trajectory=False,
save_video=True, video_fps=30, max_steps_per_video=100)

obs, _ = env.reset(seed=0)
env.unwrapped.print_sim_details()

cube_position = obs['extra']['obj_pose'][0,:3].cpu().numpy()  
ee_pos_to_cube = obs['extra']['tcp_to_obj_pos'].cpu().numpy() 

print("Initial position of cube: ", cube_position)
print("EE position is : ", ee_pos_to_cube)

ee_pos_to_cube_x = ee_pos_to_cube[0][0]
ee_pos_to_cube_y = ee_pos_to_cube[0][1]
ee_pos_to_cube_z = ee_pos_to_cube[0][2]

action = [ee_pos_to_cube_x, ee_pos_to_cube_y, ee_pos_to_cube_z, 1]
action = np.array(action).reshape(1, 4) 

grip_action = [0,0,0,-1]
grip_action = np.array(grip_action).reshape(1, 4) 

upward_action = [0,0,2.5,-1]
upward_action = np.array(upward_action).reshape(1, 4) 

x_co=[]
y_co=[]
z_co=[]

done = False
truncated = False
start_time = time.time()
while not done and not truncated :
    ee_pos_to_cube = obs['extra']['tcp_to_obj_pos'].cpu().numpy() 
    ee_pos_to_cube_x = ee_pos_to_cube[0][0]
    ee_pos_to_cube_y = ee_pos_to_cube[0][1]
    ee_pos_to_cube_z = ee_pos_to_cube[0][2]

    action = [ee_pos_to_cube_x, ee_pos_to_cube_y, ee_pos_to_cube_z, 1]
    action = np.array(action).reshape(1, 4)

    obs, rew, done, truncated, info = env.step(action)
    position = obs['extra']['tcp_pose'][0, :3].cpu().numpy()
    
    x_co.append(position[0])
    y_co.append(position[1])
    z_co.append(position[2])

done = False
truncated = False
start_time = time.time()

while not done and not truncated :
    obs, rew, done, truncated, info = env.step(grip_action)
    position = obs['extra']['tcp_pose'][0, :3].cpu().numpy()
    
    x_co.append(position[0])
    y_co.append(position[1])
    z_co.append(position[2])

done = False
truncated = False
start_time = time.time()  
while not done and not truncated:
    obs, rew, done, truncated, info = env.step(upward_action)
    position = obs['extra']['tcp_pose'][0, :3].cpu().numpy()
    
    x_co.append(position[0])
    y_co.append(position[1])
    z_co.append(position[2])


env.close()

fig = plt.figure()
ax =fig.add_subplot(111, projection='3d')

ax.plot(x_co, y_co, z_co, label='3D line')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

ax.legend()

plt.show()