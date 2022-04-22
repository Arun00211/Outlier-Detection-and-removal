import numpy as np
import pandas as pd
from scipy import stats

df=pd.read_csv("weight-height.csv")
df=df.drop("Gender", axis=1)
print(df.boxplot())
z=np.abs(stats.zscore(df))
df1=df.copy()
df1=df1[(z<3).all(axis=1)]
df2=df.copy()
q1=df2.quantile(0.25)
q3=df2.quantile(0.75)
IQR=q3-q1
df2_new=df2[((df2>=q1-1.5*IQR)&(df2<=q3+1.5*IQR)).all(axis=1)]
print(df2_new.boxplot())