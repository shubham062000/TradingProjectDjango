from email.utils import parsedate_to_datetime
from django.shortcuts import render
import pandas as pd
from requests import request
# Create your views here.

def myview(request):
    df = pd.read_csv("/home/shubham/Desktop/NIFTY.csv", sep=',', error_bad_lines=False, index_col=False, dtype='unicode', parse_dates = [["DATE", "TIME"]])
    #df.resample("10T").mean() # 10T means after 10 minutes this will give us ten minutes candle data from csv file
    return render(request, 'my_view.html', {'columns': df.columns, 'rows': df.to_dict('records')})
    
    