from math import e
import numpy as np
import os
import cv2

# import dataOrganizer from dataOrganizer.py as org
os.chdir("C:/MohammadMahdi/University/Third Yr/ENPH 353/Labs/ENPH353_LAB6/src")
import dataOrganizer as org

# Load the dataset
source_path = "C:/MohammadMahdi/University/Third Yr/ENPH 353/Labs/ENPH353_LAB6/plates/"
target_path = "C:/MohammadMahdi/University/Third Yr/ENPH 353/Labs/ENPH353_LAB6/data/"

dataorg = org.DataOrganizer(source_path, target_path)
dataorg.organize()
