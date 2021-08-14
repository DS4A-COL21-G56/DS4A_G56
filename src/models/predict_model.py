#Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick
from datetime import datetime
import math
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

SEED = 1111

with open(rf_model_file, 'rb') as file:
    best_random_model = pickle.load(file)
    
dataset_2021 = pd.read_csv('../../data/processed/final_dataset_distinct.csv', index_col = 0)
training_dataset = pd.read_csv('../../data/processed/extended_dataset_final.csv', index_col = 0)

training_dummy = pd.get_dummies(training_dataset.drop(['CODIGO', 'PERIODO_ACADEMICO'], axis = 1), drop_first = True)

student_code = input("Please enter a student's code:\n")