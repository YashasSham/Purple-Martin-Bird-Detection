# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:51:01 2018

@author: Yasha
"""
import glob
import video
import pandas as pd
import os
import datetime
from os import path
import predict

predict.init()

video_list = []
for infile in sorted(glob.glob('/projects/academic/jistroke/video/ch02_20180526/*.mp4')):
    video_list.append(infile)
    
   
DATE_FORMAT = '%Y%m%d%H%M%S'
dateStart = '20180525174010'
dateEnd = '20180609205000'

video_infoDF = pd.DataFrame()
for file in video_list:
    file_date = os.path.basename(file)
    file_date = os.path.splitext(file_date)[0]
    file_date = file_date.replace('\\', '/')

    try:  
        if '_' in file_date and int(file_date.split('_',1)[1]) >= int(dateStart) and int(file_date.split('_',1)[1]) <= int(dateEnd):
            print(file_date.split('_',1)[1])
            output_file_name = 'video_proccesing_output/' + file_date.split('_',1)[1] + '.csv'
            result, prediction= video.video_proccessing(file)
            #*******************video Info***********
            print(len(prediction))
            name = file_date + '.mp4'
            duration = len(prediction)
            timeStamp = datetime.datetime.strptime(file_date.split('_',1)[1] , '%Y%m%d%H%M%S')
            date = timeStamp.strftime('%Y-%m-%d')
            time = timeStamp.strftime('%H:%M:%S')            
            nest_attentiveness = prediction.count('incubating')
            
            row = [ name ,date, time, duration, nest_attentiveness/duration, prediction ]
            rowDF = pd.DataFrame(row).T
            rowDF.columns = ['Name', 'Date', 'Time', 'Duration', 'Nest Attentiveness', 'prediction'] 
            rowDF.to_pickle(output_file_name)
            
            #video_infoDF = video_infoDF.append(rowDF)
            #*****************************************
            #resultdf = pd.DataFrame(result)
            #predictiondf = pd.DataFrame(prediction)
            #resultdf.to_csv('result.csv', sep=',', encoding='utf-8', index = False)
            #predictiondf.to_csv('prediction.csv', sep=',', encoding='utf-8', index = False)
    except ValueError:
        print('Non-numeric data found in the file.')
    except IndexError:
        print('IndexError')
       
#video_infoDF.to_csv('video_proccesing_output/video_infoDF.csv', sep=',', encoding='utf-8', index = False)

    