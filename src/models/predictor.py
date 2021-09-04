#Import libraries
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle
import json
import codecs
from src import abs_path

def load_model():

    rf_model_file = abs_path + 'models/best_random_model.pkl'
    with open(rf_model_file, 'rb') as file:
        best_random_model = pickle.load(file)

    return best_random_model

best_random_model = load_model()

def load_feature_names():
    
    # training_dataset = pd.read_csv('data/processed/extended_dataset_final.csv', index_col = 0)
    # training_dummy = pd.get_dummies(training_dataset.drop(['CODIGO', 'PERIODO_ACADEMICO'], axis = 1), drop_first = True)
    # columns_names = training_dummy.columns

    with codecs.open(abs_path + 'models/columns.json', encoding='utf-8') as columns_file:
        columns_str = columns_file.read()
    
    columns_names = json.loads(columns_str)

    return columns_names

feature_names = load_feature_names()

def load_data():

    training_dataset_full = pd.read_csv(abs_path + 'data/frontend/frontend_dataset.csv', index_col = 0)
    # training_dummy_full = pd.get_dummies(training_dataset_full.drop(['CODIGO', 'PERIODO_ACADEMICO'], axis=1),drop_first=True)

    return training_dataset_full

training_dataset_full = load_data()

def predictFromFeatures(features: dict):

    features_df = pd.DataFrame.from_dict(features)
    features_df = pd.get_dummies(features_df)
    features_df = features_df.reindex(columns=feature_names, fill_value=0)
    features_df = features_df.drop(['ES_DESERTOR_SI'], axis = 1)

    # Prediction
    prob = best_random_model.predict_proba(features_df.values)[0][1]*100

    return prob

def predictFromDataset(year, semester, treshold):

        if semester == 1:
            period = int(str(year)+'10')
        elif semester == 2:
            period = int(str(year)+'20')

        # Get a copy to work on
        period_df = training_dataset_full.copy()

        # Keep only the selected period
        period_rows = period_df[period_df['PERIODO_ACADEMICO'] == period].reset_index(drop = True)

        # Transform into dummy array
        period_rows_dummy = pd.get_dummies(period_rows.drop(['CODIGO', 'PERIODO_ACADEMICO'], axis = 1))
        period_rows_dummy = period_rows_dummy.reindex(columns=feature_names, fill_value=0)

        # Prediction
        result = best_random_model.predict_proba(period_rows_dummy.drop(['ES_DESERTOR_SI'], axis = 1).values)
        dropout_prob = [i[1] for i in result]

        period_rows['dropout_prob'] = dropout_prob

        dropout_period = period_rows[period_rows['dropout_prob']>treshold]

        num_predicted = len(dropout_period)

        # def show_students():
        columns = ['CODIGO', 'n_semesters', 'real_cumulative_gpa', \
                    'cumulative_failed', 'GENERO', 'NOMBRE_PROGRAMA', 'dropout_prob']
        
        new_column_names = ['code', 'semesters', 'gpa', 'failed', 'gender', 'program', 'dropout_prob']
        to_show = dropout_period[columns]
        to_show.columns = new_column_names

        return num_predicted, to_show

def predictFromStudent(student_code):

    # Get a copy to work on
    student_df = training_dataset_full.copy()

    # Keep only the selected student
    student_df = student_df[student_df['CODIGO'] == student_code].reset_index()
    student_row = student_df.iloc[student_df['n_semesters'].idxmax():1,:]

    # Transform into dummy array
    student_row_dummy = pd.get_dummies(student_row.drop(['CODIGO', 'PERIODO_ACADEMICO'], axis = 1))
    student_row_dummy = student_row_dummy.reindex(columns = feature_names, fill_value=0)

    # Prediction
    result = best_random_model.predict_proba(student_row_dummy.drop(['ES_DESERTOR_SI'], axis = 1).values)[0][1]*100
    
    return result



