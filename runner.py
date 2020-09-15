import os
import pathlib

def runnerWaifu2x(path_to_images,path_to_output):
    cmd = "python src/waifu2x-chainer/waifu2x.py"+ " -m " +str("noise_scale") +" -n " +str(1) +" -i " + str(path_to_images) + " -o "+ str(path_to_output)+ " -a 0 -g 0 -d src/waifu2x-chainer/models/vgg7"
    print(cmd)
    os.system(cmd)

def ruunerISR(path_to_images,path_to_output):
    os.system("cd src/ISR/")
    from ISR.predict import Predictor
    from ISR.models import RDN

    rdn = RDN(arch_params={'C':6, 'D':20, 'G':64, 'G0':64, 'x':2})
    rdn.model.load_weights('weights/rdn-C6-D20-G64-G064-x2_ArtefactCancelling_epoch219.hdf5')

    predictor = Predictor(input_dir=path_to_images, output_dir=path_to_output)
    predictor.get_predictions(model=rdn)
    os.system("cd ../..")