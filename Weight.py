import pandas as pd
import plotly.figure_factory as ff
import csv 
import statistics as st 
df =  pd.read_csv("data.csv")
data = df["Weight(Pounds)"].tolist()
fig = ff.create_distplot([data],["Weight"],show_hist=False)
fig.show()

mean = st.mean(data)
print ("MEAN : ", mean ) 
std_deviation = st.stdev(data)
print ("STANDARD DEVIATION :" , std_deviation)
median = st.median(data)
mode = st.mode(data)
print ("MEDIAN :" , median)
print ("MODE : ", mode)

#finding standard deviation 
first_standard_deviation_start,first_standard_deviation_end = mean - std_deviation,mean + std_deviation
list_of_data_within_1_standard_deviation = [result for result in data if result > first_standard_deviation_start and result < first_standard_deviation_end]
print ("{}% of data lieas within first standard deviation".format(len(list_of_data_within_1_standard_deviation)*100.0/len(data)))

second_standard_deviation_start,second_standard_deviation_end = mean - (2* std_deviation),mean + (2 *std_deviation)
list_of_data_within_2_standard_deviation = [result for result in data if result > second_standard_deviation_start and result < second_standard_deviation_end]
print ("{}% of data lieas within second  standard deviation".format(len(list_of_data_within_2_standard_deviation)*100.0/len(data)))

third_standard_deviation_start,third_standard_deviation_end = mean - (3*std_deviation),mean + (3*std_deviation)
list_of_data_within_3_standard_deviation = [result for result in data if result > third_standard_deviation_start and result < third_standard_deviation_end]
print ("{}% of data lieas within third standard deviation".format(len(list_of_data_within_3_standard_deviation)*100.0/len(data)))