# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:59:16 2019

@author: fddot
"""
import subprocess

def convert_video(video_input, video_output):
    cmds = ['ffmpeg', '-i', video_input, video_output]
    subprocess.Popen(cmds)