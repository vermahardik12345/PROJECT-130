import pandas as pd
import csv
df=pd.read_csv('total_stars.csv')

df.drop(['Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity'],axis=1,inplace=True)
df.to_csv('Main.csv')