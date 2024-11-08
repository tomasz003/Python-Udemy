#import csv
#
# with open("weather_data.csv") as file:
#     data=csv.reader(file)
#     temperatures=[]
#     for row in data:
#         try:
#             temperatures.append(int(row[1]))
#         except ValueError:
#             pass
#     print(temperatures)



#import pandas

#data=pandas.read_csv("weather_data.csv")

###Changing type
#data_dict=data.to_dict()
#print(data_dict)

#temp_list=data.temp.to_list()
#print(temp_list)

###Accessing by rows and columns
#column
#print(data.condition)

#row
#hottest=data.temp.max()
#print(data[data.temp==hottest])

# monday=data[data.day=="Monday"]
# temp_fahr=monday.temp[0]*9/5+32
# print(temp_fahr)

### Creating a dataframe from scratch

# data_dict={
#     "students": ["Amy", "Ben", "Chuck"],
#     "scores": [76,56,65]
# }
#
# data=pandas.DataFrame(data_dict)
# data.to_csv("new_file.csv")
