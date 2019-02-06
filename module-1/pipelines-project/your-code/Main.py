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

def wrangle(df):
    null_cols = data.isnull().sum()
    null_cols[null_cols > 0].head()
    data.columns
    new_columns = ['year', 'countries', 'pf_rol_civil', 'pf_association_association', 'pf_expression', 
                   'pf_identity_sex', 'pf_score', 'ef_score', 'hf_score']
    data = data[new_columns]
    data = data.rename(index=str, columns={"year": "Year", "countries": "Country", 
                                           "pf_rol_civil": "Civil_justice", 
                                           "pf_association_association": "Freedom_of_association",
                                           "pf_expression": "Freedom_of_expression", 
                                           "pf_identity_sex": "Same_sex_relationships", 
                                           "pf_score": "Personal_Freedom",
                                           "ef_score": "Economic_Freedom",
                                           "hf_score": "Human_Freedom"})
    null_cols = data.isnull().sum()
    null_cols[null_cols > 0]
    before = len(data)
    data = data.drop_duplicates()
    after = len(data)
    print('Number of duplicate records dropped: ', str(before - after))
    data[data.isnull().any(axis=1)].head()
    data = data.dropna()
    return data.head()

def analyze(df):
    years = data["Year"]
    drop_cols = list(years[years < 2016].index)
    data_2016 = data.drop(drop_cols, axis=0)
    data_2016_top5 = data_2016.sort_values(by='Human_Freedom', ascending=False).head()
    data_2016_last5 = data_2016.sort_values(by='Human_Freedom', ascending=True).head()
    return data_2016_top5
    return data_2016_last5

    important_columns = ["Year", "Country", "Civil_justice", "Freedom_of_association", "Freedom_of_expression", 
                     "Same_sex_relationships", "Personal_Freedom","Economic_Freedom","Human_Freedom"]
    stats_top = data_2016_top5[important_columns].describe().transpose()
    stats_last = data_2016_last5[important_columns].describe().transpose()
    return stats_top
    return stats_last

    table_top = pd.pivot_table(data_2016_top5, values=['Civil_justice', 'Human_Freedom'], index=['Year'], 
                       aggfunc={'Civil_justice': np.mean, 'Human_Freedom': np.mean})
    table_last = pd.pivot_table(data_2016_last5, values=['Civil_justice', 'Human_Freedom'], index=['Year'], 
                       aggfunc={'Civil_justice': np.mean, 'Human_Freedom': np.mean})
    return table_top
    return table_last

    data_new_zealand = data[(data['Country']=='New Zealand')]
    data_new_zealand = data_new_zealand.sort_values(by='Year', ascending=False)
    columns_analysis = ['Year', 'Civil_justice', 'Human_Freedom']
    stats_new_zealand = data_new_zealand[columns_analysis]
    stats_new_zealand = stats_new_zealand.set_index('Year')
    return stats_new_zealand
    return stats_new_zealand.pct_change()
    title = 'Evolution of Freedom in New Zealand'
    sns.set(style="whitegrid")
    zea_freedom = sns.barplot(x="Year", y="Human_Freedom", data=data_new_zealand, palette="Blues")
    plt.title(title, fontsize=14)
    zea_civil_year = ((stats_new_zealand.loc[2016, 'Civil_justice']/stats_new_zealand.loc[2008, 'Civil_justice'])**(1/8)-1)*100
    zea_civil = ((stats_new_zealand.loc[2016, 'Civil_justice']/stats_new_zealand.loc[2008, 'Civil_justice'])-1)*100
    zea_freedom_year = ((stats_new_zealand.loc[2016, 'Human_Freedom']/stats_new_zealand.loc[2008, 'Human_Freedom'])**(1/8)-1)*100
    zea_freedom = ((stats_new_zealand.loc[2016, 'Human_Freedom']/stats_new_zealand.loc[2008, 'Human_Freedom'])-1)*100
    print("La variación ANUAL de la Justicia Social y de la Libertad en Nueva Zelanda durante los últimos 8 años ha sido respectivamente de un " + str(round(zea_civil_year, 2)) + "%, y de un " + str(round(zea_freedom_year, 2)) + "%.")
    print("La variación TOTAL de la Justicia Social y de la Libertad en NUeva Zelanda entre 2008 y 2016 ha sido respectivamente de un " + str(round(zea_civil, 2)) + "%, y de un " + str(round(zea_freedom, 2)) + "%.")

    data_spain = data[(data['Country']=='Spain')]
    data_spain = data_spain.sort_values(by='Year', ascending=False)
    stats_spain = data_spain[columns_analysis]
    stats_spain = stats_spain.set_index('Year')
    return stats_spain
    return stats_spain.pct_change()
    title = 'Evolution of Freedom in Spain'
    sns.set(style="whitegrid")
    spa_freedom = sns.barplot(x="Year", y="Human_Freedom", data=data_spain, palette="Greens")
    plt.title(title, fontsize=14)
    spa_civil_year = ((stats_spain.loc[2016, 'Civil_justice']/stats_spain.loc[2008, 'Civil_justice'])**(1/8)-1)*100
    spa_civil = ((stats_spain.loc[2016, 'Civil_justice']/stats_spain.loc[2008, 'Civil_justice'])-1)*100
    spa_freedom_year = ((stats_spain.loc[2016, 'Human_Freedom']/stats_spain.loc[2008, 'Human_Freedom'])**(1/8)-1)*100
    spa_freedom = ((stats_spain.loc[2016, 'Human_Freedom']/stats_spain.loc[2008, 'Human_Freedom'])-1)*100
    print("La variación ANUAL de la Justicia Social y de la Libertad en Venezuela durante los últimos 8 años ha sido respectivamente de un " + str(round(spa_civil_year, 2)) + "%, y de un " + str(round(spa_freedom_year, 2)) + "%.")
    print("La variación TOTAL de la Justicia Social y de la Libertad en Venezuela entre 2008 y 2016 ha sido respectivamente de un " + str(round(spa_civil, 2)) + "%, y de un " + str(round(spa_freedom, 2)) + "%.")

    data_venezuela = data[(data['Country']=='Venezuela')]
    data_venezuela = data_venezuela.sort_values(by='Year', ascending=False)
    stats_venezuela = data_venezuela[columns_analysis]
    stats_venezuela = stats_venezuela.set_index('Year')
    return stats_venezuela
    return stats_venezuela.pct_change()
    title = 'Evolution of Freedom in Venezuela'
    sns.set(style="whitegrid")
    ven_freedom = sns.barplot(x="Year", y="Human_Freedom", data=data_venezuela, palette="Reds")
    plt.title(title, fontsize=14)
    ven_civil_year = ((stats_venezuela.loc[2016, 'Civil_justice']/stats_venezuela.loc[2008, 'Civil_justice'])**(1/8)-1)*100
    ven_civil = ((stats_venezuela.loc[2016, 'Civil_justice']/stats_venezuela.loc[2008, 'Civil_justice'])-1)*100
    ven_freedom_year = ((stats_venezuela.loc[2016, 'Human_Freedom']/stats_venezuela.loc[2008, 'Human_Freedom'])**(1/8)-1)*100
    ven_freedom = ((stats_venezuela.loc[2016, 'Human_Freedom']/stats_venezuela.loc[2008, 'Human_Freedom'])-1)*100
    print("La variación ANUAL de la Justicia Social y de la Libertad en Venezuela durante los últimos 8 años ha sido respectivamente de un " + str(round(ven_civil_year, 2)) + "%, y de un " + str(round(ven_freedom_year, 2)) + "%.")
    print("La variación TOTAL de la Justicia Social y de la Libertad en Venezuela entre 2008 y 2016 ha sido respectivamente de un " + str(round(ven_civil, 2)) + "%, y de un " + str(round(ven_freedom, 2)) + "%.")


def visualize(df):
    correlations = data.corr()
    return correlations

    fig = plt.figure()
    ax = fig.add_subplot(111)
    subplotsize=[8.,8.]
    figuresize=[10.,10.]   
    left = 0.5*(1.-subplotsize[0]/figuresize[0])
    right = 1.-left
    bottom = 0.5*(1.-subplotsize[1]/figuresize[1])
    top = 1.-bottom
    fig.subplots_adjust(left=left,right=right,bottom=bottom,top=top)
    cax = ax.matshow(correlations, vmin=-1, vmax=1)
    fig.colorbar(cax)
    ticks = np.arange(0,8,1)
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(data)
    ax.set_yticklabels(data)
    plt.show()

    data_plot = [[5.257879, 2008, 12],
                 [5.283514, 2009, 12],
                 [5.156619, 2010, 12],
                 [5.332458, 2011, 12],
                 [5.225650, 2012, 12],
                 [5.013857, 2013, 12],
                 [4.573730, 2014, 12],
                 [4.241750, 2015, 12],
                 [4.200724, 2016, 12]]
    freedom = [i[0] for i in data_plot]
    years = [i[1] for i in data_plot]
    plt.plot(years, freedom)
    for i in range(0, len(data)-3):
        # interpolate values
        # you can choose for yourself how many point should be taken into account
        # as well as the degree of interpolation (the last variable mentioned)
        z = polyfit(years[i:i+7],freedom[i:i+7], 1)
        p = poly1d(z)
        # extrapolate interpolation by 1
        start_year = years[i]
        end_year = years[i+3] + 1
        # plot values 
        x = linspace(start_year, end_year, 10)
        y = p(x)
        plt.plot(x, y)
    return plt.show()

    data_year = [2008,2009,2010,2010,2012,2013,2014,2015,2016]
    data_freedom = [5.257879,5.283514,5.156619,5.332458,5.225650,5.013857,4.573730,4.241750,4.200724]
    def holt_alg(h, y_last, y_pred, T_pred, alpha, beta):
        pred_y_new = alpha * y_last + (1-alpha) * (y_pred + T_pred * h)
        pred_T_new = beta * (pred_y_new - y_pred)/1 + (1-beta)*T_pred
        return (pred_y_new, pred_T_new)
    def smoothing(t, y, alpha, beta):
        pred_y = y[1]
        pred_T = (y[1] - y[0])/(t[1]-t[0])
        y_hat = [y[0], y[1]]
        t.append(t[-1]+1)
        for i in range(2, len(t)):
            h = t[i] - t[i-1]
            pred_y, pred_T = holt_alg(h, y[i-1], pred_y, pred_T, alpha, beta)
            y_hat.append(pred_y)
        return y_hat 
    pred = plt.plot(data_year, data_freedom, 'x-')
    plt.show(True)
    pred_y = smoothing(data_year, data_freedom, alpha=.8, beta=.5)
    plt.plot(data_year[:len(pred_y)], pred_y, 'rx-')
    plt.show()





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