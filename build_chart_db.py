'''some interesting charts- heatseekers-songs, r-b-hip-hop-songs, rock-songs, dance-electronic-songs, 
country-songs, adult-contemporary

We are making a csv out of the jsons'''

import billboard
from time import sleep
from dateutil.parser import parse as parse_date
import json
import csv

import pdb

def build_chart_db(chartName='hot-100',filename = 'billboard_data.csv', 
                   StartDate='6-1-2016',EndDate=None,date=None,append=True):
    
    if append:
        f = csv.writer(open(filename,"awb+",0))
    else:
        f = csv.writer(open(filename,"wb+",0))
        
    if date is None and StartDate is None and EndDate is None:
        chart = billboard.ChartData(chartName)
    # we will do some elifs later    
    
    elif StartDate:
        
        chart = billboard.ChartData(chartName)
        
        if EndDate:    
            while chart.previousDate>EndDate:
                chart = billboard.ChartData(chartName,previousDate)
        
       
        #pdb.set_trace()
        while parse_date(chart.date)>parse_date(StartDate):
            js1 = chart.to_JSON()
            bigDict = json.loads(js1)

            f.writerow(['chart_name','date','title','artist','rank','weeks','peakPos','lastPos','change','spotifyLink'])

            for entry in bigDict['entries']:
                
                f.writerow([bigDict['name'],bigDict['date'],entry['title'],entry['artist'],entry['rank'],entry['weeks'],
                      entry['peakPos'],entry['lastPos'],entry['change'],entry['spotifyLink']])
                
            chart = billboard.ChartData(chartName,chart.previousDate)

            if skip:
                for x in range(0,skip):
                    chart = billboard.ChartData(chartName,chart.previousDate)
                    sleep(2)
            sleep(1)