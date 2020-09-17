import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_data_and_take_required(file):
    all_data = pd.read_csv(file, delimiter=",")
    return all_data[["Sex", "Age"]]


required_data = read_data_and_take_required("train.csv")
averaged_data = required_data.groupby(['Sex'], as_index=False).mean()
sns.barplot(x='Sex', y='Age', data=averaged_data)

plt.show()
