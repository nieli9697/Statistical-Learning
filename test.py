import os
import pandas as pd
import numpy as np
import csv

par = 'P38.2'
parFolder = 'P38'

# Getting absolute time for ahsans episodes
abstime_list = []
with open('crying_episodes_5_minute_threshold_P38.2.txt') as file: 
    for row in file: 
        if len(row) > 0:
            abstime_list.append(eval(row))

# Converting absolute time to seconds
converted_abstime_list = []

for item in abstime_list:
    tmp_start = list(map(float, item[0].split(":")))
    start_time = round(tmp_start[0] * 3600 + tmp_start[1] * 60 + tmp_start[2], 4)
    tmp_end = list(map(float, item[1].split(":")))
    end_time = round(tmp_end[0] * 3600 + tmp_end[1] * 60 + tmp_end[2], 4)
    converted_abstime_list.append([start_time, end_time])

#print (converted_abstime_list)
#print('\n')

human_labels = []

with open ('P38.2_1.csv') as csvfile:
    for row in csvfile:
        tmp = list(map(str, row.replace('\n', '').split(',')))
        tmp.append(str(float(tmp[0]) + converted_abstime_list[0][0]))
        tmp.append(str(float(tmp[1]) + converted_abstime_list[0][0]))
        human_labels.append(tmp)
            
#print(human_labels)


with open('test.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    #for i, row in enumerate (human_labels):
    writer.writerows(human_labels)  

'''
human_labels = []
# Reading LENA data
fieldnames = ['Begin Time - ss.msec', 'End Time - ss.msec', 'CHN']
fieldnames_1 = ['Begin Time - ss.msec', 'End Time - ss.msec', '*CHN']

try:
    data = pd.read_csv('../../Data/Cross-Sectional/'+parFolder+'/ANNOTATIONS/LENA AFFECT/CSV/P38.2_LENA_Affect_NN_2019-05-10.txt', sep='\t', usecols=fieldnames)
except:
    data = pd.read_csv('../../Data/Cross-Sectional/'+parFolder+'/ANNOTATIONS/LENA AFFECT/CSV/P38.2_LENA_Affect_NN_2019-05-10.txt', sep='\t', usecols=fieldnames_1)

results = []

column_names = ['Start Time', 'End Time', 'Label']

for j in range(len(converted_abstime_list)):

    # Getting ahsans human labels for each episode
    with open ('../Xuewen Yao/ahsans_labels/'+par+'/'+par+'_'+str(j+1)+'.csv') as csvfile:
        if os.path.getsize('../Xuewen Yao/ahsans_labels/'+par+'/'+par+'_'+str(j+1)+'.csv'):
            
            for row in csvfile:
                tmp = list(map(str, row.replace('\n', '').split(',')))
                tmp.append(str(float(tmp[0]) + converted_abstime_list[j][0]))
                tmp.append(str(float(tmp[1]) + converted_abstime_list[j][0]))
                human_labels.append(tmp)
            
            for i in range(len(human_labels)):
                for index, row in data.iterrows():
                    if row[0] >= float(human_labels[i][3]) and row[1] <= float(human_labels[i][4]) and row[2] == row[2] and row[0] != row[1]:
                        res_dict = {'Start Time': round(row[0] - float(human_labels[i][3]) + float(human_labels[i][0]), 2), 
                                    'End Time': round(row[1] - float(human_labels[i][4]) + float(human_labels[i][1]), 2), 
                                    'Label':human_labels[i][2]}
                        results.append(res_dict)
            
            with open ('./Ahsans_LENA_labels/' + par + '_' + str(j+1) +'.csv', 'w') as csvfile:
                myCsvWriter = csv.DictWriter(csvfile, delimiter=',', quotechar='"', fieldnames = column_names)
                myCsvWriter.writeheader()
                for row in results:
                    myCsvWriter.writerow(row)
            print('Done writing csv file!' + par + '_' + str(j+1))

        else:
            pass

    results = []
    human_labels = []nums = [7, 1,2,5,88,9,9]
s = list(set(nums))

print(s[-3])
'''