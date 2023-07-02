# import csv
#
#
# with open('weather_data.csv', 'r') as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)



# data = pandas.read_csv('weather_data.csv')
# # print(type(data))
# # print(data['temp'])
#
# data_dic = data.to_dict()
# print(data_dic)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# # average = sum(temp_list) / len(temp_list)
# #
# # print(average)
# print(data['temp'].mean())
# print(data['temp'].max())
# # Get Data in Columns
# print(data['condition'])
# print(data.condition)
# Get Data in Row
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# print(monday.temp, (monday.temp * 9 / 5) + 32)

# Create dataframe from scratch


# data_dic = {
#     'students': ['Amy', 'James', 'Angela'],
#     'Scores': [76, 56, 65]
# }
#
# data = pd.DataFrame(data_dic)
# data.to_csv('new.csv')
# print(data)
# print("Hello\nWorld!")

import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

fur_color = data['Primary Fur Color'].value_counts()
Fur = []
print(fur_color)