# -*- coding: utf-8 -*-
""".ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a-Jpl_HVaCd_ROEbqW1mS2U7o9sXirl0
"""

# impoert all needs libraries 
import numpy as np
import pandas as pd
import tensorflow as tf
import cv2 as cv
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

def analyze(img):
  imag =cv.imread(f"{img}")
  cv2_imshow(imag)
  gray = cv.cvtColor(imag, cv.COLOR_BGR2GRAY)
  histr = cv.calcHist([gray],[0],None,[256],[0,256])
  data =[]
  size = len(gray)
  for x in range(0, size):
    ava = np.average(gray[x])
    # print(x)
    data.append(ava)
  numpy_data = np.array(data)
  df = pd.DataFrame(data=numpy_data)
  # print(df)
  return([gray])

# my_function( cv.imread("/content/image.jpeg"))

print(analyze(img = "/content/image.jpeg"))

def sub_analyzing(img):
  image = cv.imread(f"{img}")
  graytwo = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
  full = []
  full = analyze("/content/image.jpeg")
  # print(full)
  data =[]
  tedata =[]
  size = len(graytwo)
  for x in range(0, size):
    ava = np.average(graytwo[x])
    avar=tf.reduce_mean(graytwo[x])
    data.append(ava)
    tedata.append(avar)
    plt.plot(tedata)
  pure = tf.subtract(full,graytwo)
  return([pure])
sub_analyzing("/content/image.jpeg")