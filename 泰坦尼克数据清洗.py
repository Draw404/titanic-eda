import pandas as pd
import numpy as np

df = pd.read_csv("titanic.csv")

print(df.shape)
print(df.dtypes)
print(df.head())

print(df.isnull().sum())
print(df.duplicated().sum())
print(df["Survived"].value_counts())

df["Age"] = df["Age"].fillna(df.groupby('Pclass')['Age'].transform('mean'))    #根据pclass的平均年龄对缺失数据进行填充，用transform是要把均值放进对应属性里
df["Cabin"] = df["Cabin"].str[0].fillna("U")   #取首字母进行简化分类，u代表Unknown，表示缺失
df =df.dropna(subset=["Embarked"])  #因为embarked类缺失的数据少，所以对缺失的数据进行删除

print(df.isnull().sum())
print(df["Cabin"].value_counts())

print(df["Survived"].value_counts())
print(df["Sex"].unique())
print(df["Embarked"].unique())
print(df[df["Fare"] <= 0])   #查到了费用小于等于0的乘客数据,估计是特殊票决定保留

df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df["IsAlone"] = np.where(df["FamilySize"]==1,1,0)    #增加数据分析的考虑角度，想了解家庭大小、是否独自一人和存活有没有关系
print(df[["SibSp", "Parch", "FamilySize", "IsAlone"]].head(10))

print(df.groupby("Pclass")["Survived"].mean())
print(df.groupby("Sex")["Survived"].mean())
print(df.groupby("Embarked")["Survived"].mean())

df.to_csv("titanic_clean.csv",index=False)
