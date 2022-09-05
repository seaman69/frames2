import os
import zipfile
import cv2
#from skimage.metrics import structural_similarity
import sys




if __name__ == '__main__':
    # Opens the inbuilt camera of laptop to capture video.
    video=sys.argv[1]
    pathdestino=sys.argv[2]
    cap = cv2.VideoCapture(video)
    #os.mkdir(pathdestino)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    i = 0
    primero = 0
    cant=0
    if(length>150):
        cant=int(length/150)
    else:
        cant=1
    frameanterior=""
    nombre=1
    while (cap.isOpened()):
        ret, frame = cap.read()

        # This condition prevents from infinite looping
        # incase video ends.
        if ret == False:
            break
        if i%cant==0:
            cv2.imwrite(pathdestino+"/"+str(nombre)+".jpg", frame)
            nombre=nombre+1
        i=i+1
        print(i)


    cap.release()
