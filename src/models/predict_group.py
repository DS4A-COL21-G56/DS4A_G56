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
    

# Open the model dataset and the dataset with ALL students
training_dataset = pd.read_csv('../../data/processed/extended_dataset_final.csv', index_col = 0)
training_dummy = pd.get_dummies(training_dataset.drop(['CODIGO', 'PERIODO_ACADEMICO'], axis = 1), drop_first = True)

training_dataset_full = pd.read_csv('../../data/frontend/frontend_dataset.csv', index_col = 0)
training_dummy_full = pd.get_dummies(training_dataset_full.drop(['CODIGO', 'PERIODO_ACADEMICO'], axis=1),drop_first=True)




# Start prediction algorithm
sw = True
while sw == True:
    
    try:
        # Get the period
        year = input("Please enter a year:\n")
        semester = input('Please specify the semester of the year (1/2) a year:\n')

        if semester == '1':
            period = int(str(year)+'10')
        elif semester == '2':
            period = int(str(year)+'20')

        tresh = float(input("Please select a treshold:\n"))

        # Get a copy to work on
        period_df = training_dataset_full.copy()

        # Keep only the selected period
        period_rows = period_df[period_df['PERIODO_ACADEMICO'] == period].reset_index(drop = True)

        # Transform into dummy array
        period_rows_dummy = pd.get_dummies(period_rows.drop(['CODIGO', 'PERIODO_ACADEMICO'], axis = 1))
        period_rows_dummy = period_rows_dummy.reindex(columns = training_dummy.columns, fill_value=0)

        # Prediction
        result = best_random_model.predict_proba(period_rows_dummy.drop(['ES_DESERTOR_SI'], axis = 1).values)
        dropout_prob = [i[1] for i in result]

        period_rows['dropout_prob'] = dropout_prob

        dropout_period = period_rows[period_rows['dropout_prob']>tresh]

        # Print results
        print('')
        print('There are {} students with more than {}% probabilities to drop out in the selected period'\
                                  .format(len(dropout_period), tresh*100))
        print('')
        
        show_students = input("Do you want preview this students? (y/n)\n")
        
        if show_students == 'y':
            columns = ['CODIGO', 'n_semesters', 'real_cumulative_gpa', \
                       'cumulative_failed', 'GENERO', 'NOMBRE_PROGRAMA', 'dropout_prob']
            
            new_column_names = ['code', 'semesters', 'gpa', 'failed', 'gender', 'program', 'dropout_prob']
            to_show = dropout_period[columns]
            to_show.columns = new_column_names
                
            display(to_show)
            
        elif show_students == 'n':
            pass
        else:
            print('Unkown command')
        
    except:
        print('Period not found')
        
    
    # Keep the program running
    sw_2 = True    
    while sw_2 == True:
        next_step = input("Do you want to check another period? (y/n)\n")

        if next_step == 'y':
            sw_2 = False

        elif next_step == 'n':
            sw_2 = False
            sw = False
            
        else:
            print('')
            print('Unknown command. Try again')