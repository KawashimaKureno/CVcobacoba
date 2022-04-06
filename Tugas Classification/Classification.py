import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from  tensorflow.keras import datasets,layers,models
import cv2 as cv
import sklearn
from sklearn.model_selection import train_test_split
 
 
 X =  df
 Y = labels



X_train, X_test, Y_train, Y_test = train_test_split ( X, Y, test_size=0.2, random_state=4)

