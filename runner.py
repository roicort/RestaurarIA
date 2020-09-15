import os
import pathlib

def runnerWaifu2x(path_to_images,path_to_output):
    cmd = "python waifu2x-chainer/waifu2x.py"+ " -m " +str("noise_scale") +" -n " +str(1) +" -i " + str(path_to_images) + " -o "+ str(path_to_output)+ " -a 0 -g 0 -d waifu2x-chainer/models/vgg7"
    print(cmd)
    os.system(cmd)