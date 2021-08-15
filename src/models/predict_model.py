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

rf_model_file = '../../models/best_random_model.pkl'

with open(rf_model_file, 'rb') as file:
    best_random_model = pickle.load(file)
    


training_dataset = pd.read_csv('../../data/processed/extended_dataset_final.csv', index_col = 0)
training_dummy = pd.get_dummies(training_dataset.drop(['CODIGO', 'PERIODO_ACADEMICO'], axis = 1), drop_first = True)


student_code = input("Please enter a student's code:\n")
student_code = int(student_code)


student_df = training_dataset.copy()

student_df = student_df[student_df['CODIGO'] == student_code].reset_index()
student_row = student_df.iloc[student_df['n_semesters'].idxmax():1,:]

student_row_dummy = pd.get_dummies(student_row.drop(['CODIGO', 'PERIODO_ACADEMICO'], axis = 1))
student_row_dummy = student_row_dummy.reindex(columns = training_dummy.columns, fill_value=0)

result = best_random_model.predict_proba(student_row_dummy.drop(['ES_DESERTOR_SI'], axis = 1).values)[0][1]*100

print('This student has {:.3f}% probabilities to drop out'.format(result))