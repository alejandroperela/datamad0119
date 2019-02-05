import pandas as pd
import numpy as np
from string import ascii_letters
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from numpy import median
import pylab
from numpy import polyfit, poly1d, linspace


def acquire():
    data = pd.read_csv('hfi_cc_2018.csv')
    return data.head()

def wrangle(data):
    null_cols = data.isnull().sum()
    null_cols[null_cols > 0].head()
    data.columns
    new_columns = ['year', 'countries', 'pf_rol_civil', 'pf_association_association', 'pf_expression', 
                   'pf_identity_sex', 'pf_score', 'ef_score', 'hf_score']
    data = data[new_columns]
    data.head()
    data = data.rename(index=str, columns={"year": "Year", "countries": "Country", 
                                           "pf_rol_civil": "Civil_justice", 
                                           "pf_association_association": "Freedom_of_association",
                                           "pf_expression": "Freedom_of_expression", 
                                           "pf_identity_sex": "Same_sex_relationships", 
                                           "pf_score": "Personal_Freedom",
                                           "ef_score": "Economic_Freedom",
                                           "hf_score": "Human_Freedom"})
    data.head()
    null_cols = data.isnull().sum()
    null_cols[null_cols > 0]
    before = len(data)
    data = data.drop_duplicates()
    after = len(data)
    print('Number of duplicate records dropped: ', str(before - after))
    data[data.isnull().any(axis=1)].head()
    data = data.dropna()
    data.head()

def analyze(data):
    years = data["Year"]
    drop_cols = list(years[years < 2016].index)
    data_2016 = data.drop(drop_cols, axis=0)

    data_2016_top5 = data_2016.sort_values(by='Human_Freedom', ascending=False).head()
    data_2016_last5 = data_2016.sort_values(by='Human_Freedom', ascending=True).head()

    display(data_2016_top5)
    display(data_2016_last5)


def wrangle_null(data):
    filtered = data[data['Year']==year]
    return filtered

def analyze(df):
    grouped = filtered.groupby('Make').agg({'Combined MPG':'mean'}).reset_index()
    results = grouped.sort_values('Combined MPG', ascending=False).head(10)
    return results

def visualize(df):
    fig, ax = plt.subplots(figsize=(15,8))
    barchart = sns.barplot(data=results, x='Make', y='Combined MPG')
    plt.title(title + "\n", fontsize=16)
    return barchart

def save_viz(barchart):
    fig = barchart.get_figure()
    fig.savefig(title + '.png')

if __name__ == '__main__':
    data = acquire()
    filtered = wrangle(data)
    results = analyze(filtered)
    barchart = visualize(results)
    save_viz(barchart)