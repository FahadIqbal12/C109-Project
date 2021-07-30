import csv
import plotly.figure_factory as ff
import pandas as pd
import statistics

df = pd.read_csv('data.csv')
data = df['score'].tolist()

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
std_deviation = statistics.stdev(data)

print('Median is : '+str(median))
print('Mean Is : '+str(mean))
print('Mode is : '+ str(mode))
print('Standard Ddeviation is : '+str(std_deviation))

first_std_deviaton_start , first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start , second_std_deviation_end = mean - (2* std_deviation), mean + (2*std_deviation)

list_of_data_within_1_std_deviation =[data for data in data if data > first_std_deviaton_start and data < first_std_deviation_end ]
list_of_data_within_2_std_deviation = [data for data in data if data > second_std_deviation_start and data < second_std_deviation_end]

print('{}% of Data lies within first standard deviation'.format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print('{}% of Data lies within second standard deviation'.format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))

fig =ff.create_distplot([data],["Score"])
fig.show()