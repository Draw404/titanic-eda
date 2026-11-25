import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlabel, ylabel, savefig

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False



df = pd.read_csv("titanic_clean.csv")
print(df.shape)



rate = df.groupby("Sex")["Survived"].mean()
plt.bar(rate.index.astype(str), rate.values)
plt.title("不同Sex的存活率")
plt.xlabel("Sex")
plt.ylabel("存活率")
plt.ylim(0,1)
# plt.bar(rate.index, rate.values)
plt.savefig("Survived_by_gender.png")
plt.show()

rate = df.groupby("Pclass")["Survived"].mean()
plt.bar(rate.index.astype(str), rate.values)
plt.title("不同Pclass的存活率")
plt.xlabel("Pclass")
plt.ylabel("存活率")
plt.ylim(0,1)
# plt.bar(rate.index, rate.values)
plt.savefig("Survived_by_Pclass.png")
plt.show()

rate = df.groupby("Embarked")["Survived"].mean()
plt.bar(rate.index.astype(str), rate.values)
plt.title("不同Embarked的存活率")
plt.xlabel("Embarked")
plt.ylabel("存活率")
plt.ylim(0,1)
# plt.bar(rate.index, rate.values)
plt.savefig("Survived_by_embarked.png")
plt.show()

plt.hist(df["Age"])
plt.title("乘客的年龄分布")
plt.xlabel("年龄")
plt.ylabel("人数")
plt.savefig("age_distribution.png")
plt.show()


plt.hist(df[df["Survived"] == 1]["Age"],alpha=0.5,label="Survived")
plt.hist(df[df["Survived"] == 0]["Age"],alpha=0.5,label="UnSurvived")
plt.legend()
plt.title("存活与未存活乘客的年龄分布")
plt.xlabel("年龄")
plt.ylabel("人数")
plt.savefig("age_by_survived.png")
plt.show()

