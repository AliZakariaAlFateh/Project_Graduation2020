import cv2,os
from tkinter import *
from tkinter import messagebox
from tkinter import font
# import pyQt4
# import face_recognition
import numpy as nnn
import pickle
import dlib
import datetime
import time
import numpy as np
import tkinter.ttk as ttk
import tkinter.font as font
import tkinter as tk
from tkinter import Message, Text
import shutil
import csv
import re
from PIL import Image, ImageTk
import pandas as pd
class TrainingPhotosClass():
    def catchimagesandlabels(self,path):
        # get the path of all the files in the folder
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        # print(imagePaths)

        # create empth face list
        faces = []
        # create empty ID list
        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)

        return faces, Ids
    def TrainingPhotos(self,StId,level,Name):
        if os.path.exists("TrainingImageLabel"):
            recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
            if os.path.exists("haarcascade_frontalface_default.xml"):
                harcascadePath = "haarcascade_frontalface_default.xml"
                detector = cv2.CascadeClassifier(harcascadePath)
                # faces, Id = catchimagesandlabels("Data_Set"+level)
                if os.path.exists("Data_Set"+level):
                    if os.path.getsize("Data_Set"+level)==0:
                        messagebox.showerror("error","the directory has not found any images to check about it")
                        return
                    else:
                        faces, Id = self.catchimagesandlabels("Data_Set" + level)
                        recognizer.train(faces, np.array(Id))
                        file1 = open("TrainingImageLabel\Trainner" + level + ".yml", "w")
                        recognizer.save("TrainingImageLabel\Trainner" + level + ".yml")
                        messagebox.showinfo("message","training is done for :\n Name  is : " + Name + "\n ID is : " + StId);
                        return
                else:
                    os.mkdir("Data_Set"+level)
                    messagebox.showinfo("message", "The directory Data_Set"+level+"is created now,\n please take a photo again and make training for it")
                    return
            else:
                messagebox.showerror("error","the file haarcascade_frontalface_default.xml not exists ,\nPlease bring this file to MyProject directory ,\n to generate photos")
                return
        else:
            os.mkdir("TrainingImageLabel")
            messagebox.showinfo("message","The directory TrainingImageLabel  is created now,\n please take a photo again and make training for it")
            return






