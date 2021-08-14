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

SEED = 1111


df = pd.read_csv('../../data/processed/extended_dataset_final.csv', index_col = 0)

gpas_dummy = pd.get_dummies(df.drop(['CODIGO', 'PERIODO_ACADEMICO'], axis = 1), drop_first = True)


df_desertor = gpas_dummy[gpas_dummy['ES_DESERTOR_SI'] == 1]
df_no_desertor = gpas_dummy[gpas_dummy['ES_DESERTOR_SI'] == 0]

df_no_desertor = df_no_desertor.sample(n=len(df_desertor))

df_new = pd.concat([df_desertor, df_no_desertor])
df_new = df_new.sample(frac=1)

y1 = df_new['ES_DESERTOR_SI'].values
X1 = df_new.drop('ES_DESERTOR_SI', axis = 1).values
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size = 0.26, random_state = SEED, stratify = y1)

y1 = df_new['ES_DESERTOR_SI'].values
X1 = df_new.drop('ES_DESERTOR_SI', axis = 1).values
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size = 0.26, random_state = SEED, stratify = y1)

rf_with_best_params = RandomForestClassifier(n_estimators = 733 , min_samples_split = 2, random_state =SEED,\
                    min_samples_leaf = 1, max_features = 'sqrt', max_depth = 70, bootstrap = False)

rf_with_best_params.fit(X1_train, y1_train)

