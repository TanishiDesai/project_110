import pandas as pd
import plotly.figure_factory as ff
import random as rand
import statistics as stat
import csv


df = pd.read_csv("data.csv")
data = df["temp"].tolist()
population_mean = stat.mean(data)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter) :
        random_index = rand.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = stat.mean(dataset)
    return mean 

print("Mean of population : ", population_mean)

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["temp"], show_hist = False)
    fig.show()