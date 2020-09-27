
import cv2 
import os 
import numpy as np
import glob
from tqdm import tqdm
import moviepy.editor as me

def vid2img(file,output):
    cam = cv2.VideoCapture(file) 
    try:    
        if not os.path.exists(output): 
            os.makedirs(output) 
    except OSError: 
        print ('Error: Creating directory of data') 
    
    currentframe = 0
    
    while(True): 
        ret,frame = cam.read() 
        if ret: 
            name = output + str(currentframe) + '.jpg'
            print ('Creating...' + name) 
            cv2.imwrite(name, frame) 
            currentframe += 1
            os.system("clear")
        else: 
            break
    
    cam.release() 
    cv2.destroyAllWindows() 

def img2video(read_path,save_path):
    files = []
    for r, _, f in os.walk(read_path):
        for file in f:
            if '.png' in file:
                files.append([os.path.join(r, file),file.replace(".png","")])
    print("")
    files.sort(key=lambda x: int(x[1]))
    img = cv2.imread(files[0][0])
    height, width, _ = img.shape
    size = (width,height)
    print("VidSize: ",str(size))
    print("")
    out = cv2.VideoWriter(save_path+"reconstucted.mp4",cv2.VideoWriter_fourcc(*'mp4v'), 60, size)

    for file in tqdm(range(len(files))):
        path = files[file][0]
        img = cv2.imread(path)
        out.write(img)
    out.release()

