# 泰坦尼克乘客数据探索性分析

## 项目介绍

对泰坦尼克乘客数据做探索性分析：清洗 + 分组存活率对比。

## 数据来源

datasciencedojo 的 titanic.csv（https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv）

## 清洗决策

- **Age**：根据 Pclass 的平均年龄对缺失数据进行填充，用 transform 是要把均值放进对应属性里
- **Cabin**：取首字母进行简化分类，U 代表 Unknown，表示缺失
- **Embarked**：因为 Embarked 缺失的数据少，所以对缺失的数据进行删除
- **Fare**：查到了费用小于等于 0 的乘客数据，估计是特殊票，决定保留
- **新增列**：FamilySize / IsAlone——增加数据分析的考虑角度，想了解家庭大小、是否独自一人和存活有没有关系

## 主要结论

- 性别：female 0.74 vs male 0.19（差距最大）
- 舱等：0.626 / 0.473 / 0.242
- 登船港：C 最高，0.554

## 文件说明

- `泰坦尼克数据清洗.py`：数据清洗，输出 titanic_clean.csv
- `eda_plot.py`：分组分析与画图
- `Survived_by_gender.png`：不同性别的存活率对比
- `Survived_by_embarked.png`：不同登船港的存活率对比
- `Survived_by_Pclass.png`：不同舱等的存活率对比
- `age_distribution.png`：乘客的年龄分布
- `age_by_survived.png`：存活与未存活乘客的年龄分布
