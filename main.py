from videoprocessing import *
from runner import *

vid2img("input/input.mp4","frames/")
runnerWaifu2x("frames/","HDframes/")
img2video("HDframes/",save_path="output/")

