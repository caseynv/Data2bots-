import pandas as pd;
import datetime as dt;
import json;

#Question 1
df = pd.read_csv("python hands-on - dataset.csv", parse_dates=['date']);

#Question 2
df['obsolete'] = df['date'] < dt.datetime(2021,1,1);

#Question 3 & 4
with open('python hands-on - dataset.json', 'w') as f:
    f.write(df.to_json(orient='records', date_format = 'iso'));