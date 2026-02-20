import os
#Is python interface of OpenCV(Open Source Compiter vision library).
#A library used to read, process, and analyze images & videos.
#OpenCV is a very powerful computer vision library used for:Image processing 
#Object detection 
#Face recognition 
#Motion tracking
#Video analysis
#Real-time computer vision
import cv2 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import PIL
import seaborn
import sklearn
import torch
import torch.nn as nn #Toolbox to build pytorch neural network
import torch.nn.functional as F #stateless neural network functions.Just pure functions you apply to tensors
import torch.optim as optim #pytorch optimization module.Algorithms that update model weights to reduce loss 
import torchinfo #It is a utility library used for creating a clear summary of pytorch model
import torchvision #Its a computer vision library.tools + datasets + models for image & video tasks
from PIL import Image
from sklearn.metrics import ConfusionMatrixDisplay,confusion_matrix
from torch.utils.data import DataLoader,random_split
from torchinfo import summary
 #datasets contains automatic dataset loaders.
 #For image classification most common is Image Folder.
 #It:Reads images from folders. Automatically assigns labels. Returns (image, label) pairs.
 #transforms is used to preprocess images before feeding them to a neural network.
#Common tasks:
#Resize images
#Convert images to tensors
#Normalize pixel values
#Data augmentation (flip, rotate)
from torchvision import datasets,transforms
from tqdm.notebook import tqdm
