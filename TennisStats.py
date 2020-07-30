# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 17:51:59 2020

@author: Kimberly Taylor
Description: A Codecademy Project - the goal is to analyze data about tennis pros
and look for linear relationships between variables.
             
"""


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
df = pd.read_csv("./tennis_stats.csv")
print(list(df)) #Prints list of column names






# perform exploratory analysis here:
mlr = LinearRegression()
for i in list(df):
    if (i != 'Winnings') and (i != 'Player'):
        mlr.fit(df[['Winnings']],df[[i]])
        print("Rsq for %s: %.4f" % (i,mlr.score(df[['Winnings']],df[[i]])))



x_train, x_test, y_train, return_y_test = train_test_split(df[['ReturnGamesPlayed']], df[['Winnings']], train_size = 0.8)
mlr.fit(x_train, y_train)
return_games_predict = mlr.predict(x_test)
return_rsq = mlr.score(x_train, y_train)
print("\nRsq for Return Games Played: %.4f" % return_rsq)

x_train, x_test, y_train, service_y_test = train_test_split(df[['ServiceGamesPlayed']], df[['Winnings']], train_size = 0.8)
mlr.fit(x_train, y_train)
service_games_predict = mlr.predict(x_test)
service_rsq = mlr.score(x_train, y_train)
print("\nRsq for Service Games Played: %.4f" % service_rsq)

x_train, x_test, y_train, break_y_test = train_test_split(df[['Wins']], df[['Winnings']], train_size = 0.8)
mlr.fit(x_train, y_train)
break_point_predict = mlr.predict(x_test)
break_rsq = mlr.score(x_train, y_train)
print("\nRsq for Break Points Opportunities: %.4f" % break_rsq)

fig = plt.subplots(figsize = (12,8))
ax1 = plt.subplot(131)
ax1 = plt.scatter(return_y_test, return_games_predict)
ax2 = plt.subplot(132)
ax2 = plt.scatter(service_y_test, service_games_predict, color = "red")
ax3 = plt.subplot(133)
ax3 = plt.scatter(break_y_test, break_point_predict, color = "green")

multi_x = df[['ReturnGamesPlayed','ServiceGamesPlayed']]
multi_y = df[['Winnings']]
x_train, x_test, y_train, service_y_test = train_test_split(multi_x, multi_y, train_size = 0.8)
mlr.fit(x_train, y_train)
multi_y_predict = mlr.predict(x_test)
print("\nRsq for two-x model is %.4f." % mlr.score(x_test,service_y_test))

multi_x = df[['Wins','ServiceGamesPlayed']]
multi_y = df[['Winnings']]
x_train, x_test, y_train, service_y_test = train_test_split(multi_x, multi_y, train_size = 0.8)
mlr.fit(x_train, y_train)
multi_y_predict = mlr.predict(x_test)
print("\nRsq for two-x model is %.4f." % mlr.score(x_test,service_y_test))

triple_x = df[['ReturnGamesPlayed','ServiceGamesPlayed','BreakPointsOpportunities']]
y = df[['Winnings']]
x_train, x_test, y_train, service_y_test = train_test_split(multi_x, y, train_size = 0.8)
mlr.fit(x_train, y_train)
multi_y_predict = mlr.predict(x_test)
print("\nRsq for three-x model is %.4f." % mlr.score(x_test,service_y_test))