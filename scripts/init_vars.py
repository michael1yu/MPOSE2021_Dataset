# Copyright (C) 2021  Federico Angelini
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details:
# http://www.gnu.org/licenses/gpl.txt

import os
import cv2

# main path of the dataset repository
# (specify an absolute path, leave 'MPOSE2021' to export in the current folder)
dataset_path = 'MPOSE2021_Dataset/'

# path where the data will be extracted 
data_path = dataset_path + 'data/'

# paths where the formers dataset archives will be stored
# which requires around 180 GB of free space
# (leave as it is if you want to store archives into the "'dataset_path'/archives/" folder)
archives_path = data_path + 'archives/'

# temporary folder, which requires 200 GB of free space
# it will contain unzipped archives
# (leave as it is if you want to store temporary files into the "'dataset_path'/temp/" folder)
temp_path = data_path + 'temp/'

logs_path = dataset_path + 'logs/'

'''
########################################################################
################ do NOT modify after this point ########################
########################################################################
'''
max_frame_length = 30
min_frame_length = 20

precursors = ['weizmann',
              'isldas',
              'isld',
              'ixmas',
              'kth',
              'i3dpost',
              'utkinect',
              'utdmhad']

archives_paths = dict(utkinect=archives_path + 'utkinect/',
                      json=archives_path + 'json/',
                      posenet=archives_path + 'posenet/')

former_paths = dict(utkinect=temp_path + 'utkinect/')

paths = dict(video=data_path + 'video/',
             pose=data_path + 'openpose/',
             posenet=data_path + 'posenet/',
             json=data_path + 'json/',
             figures=dataset_path + 'docs/',
             rgb=data_path + 'rgb/')

actions = {'standing': 0,
           'check-watch': 1,
           'cross-arms': 2,
           'scratch-head': 3,
           'sit-down': 4,
           'get-up': 5,
           'turn': 6,
           'walk': 7,
           'wave1': 8,
           'box': 9,
           'kick': 10,
           'point': 11,
           'pick-up': 12,
           'bend': 13,
           'hands-clap': 14,
           'wave2': 15,
           'jog': 16,
           'jump': 17,
           'pjump': 18,
           'run': 19}

fps = dict(utkinect=19)

former_frame_size = dict(utkinect=(640, 480))

frame_size = dict(utkinect=(640, 480))
resize_interpolation = cv2.INTER_CUBIC

misc_paths = dict(utkinect=dataset_path+'scripts/misc/utkinect_splitter.txt',
                  checksum_video=dataset_path+'scripts/misc/cksum_video.csv',
                  checksum_rgb=dataset_path+'scripts/misc/cksum_rgb.csv',
                  checksum_pose=dataset_path+'scripts/misc/cksum_pose.csv',
                  outliers=dataset_path+'scripts/misc/refine_dataset')

video_extention = '.avi'
codec = cv2.VideoWriter_fourcc(*'MPEG')

# OpenPose keypoints index (used for animation only, see scripts.lib_seq.py)
openpose_parts = dict(head=[0, 15, 16, 17, 18],
                      right_foot=[11, 22, 23, 24],
                      left_foot=[14, 19, 20, 21])

def init_vars(verbose=True):
    if not os.path.exists(temp_path):
        os.mkdir(temp_path)    
        
    if not os.path.exists(data_path):
        os.mkdir(temp_path)    
        
    if not os.path.exists(logs_path):
        os.mkdir(temp_path)
        
    for i in archives_paths.keys():
        if not os.path.exists(archives_paths[i]):
            os.makedirs(archives_paths[i])
            
    for i in paths.keys():
        if not os.path.exists(paths[i]):
            os.makedirs(paths[i])
            
    for i in former_paths.keys():
        if not os.path.exists(former_paths[i]):
            os.makedirs(former_paths[i])
            
    if verbose:
        print('All variables have been initialized!')
            
if __name__ == '__main__':
    init_vars()
