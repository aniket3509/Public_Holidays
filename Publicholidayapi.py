import pandas as pd
import datetime

from flask import *
import json, time

app = Flask(__name__)

@app.route('/', methods=['Get'])
def holiday():
    data=pd.read_csv("Public_Holiday.csv")

    x = datetime.datetime.now()
    month=x.strftime("%b")
    day=x.strftime("%d")
    var = day+'-'+month

    lis=[]
    st=''
    for i in range(len(data["Date"])):
        if(data["Date"][i]==var):
            if(st!=''):
                st=st+data["Name"][i].upper()+' - '+data["Description"][i]+'. '
            else:
                st=st+data["Name"][i].upper()+' - '+data["Description"][i]+'. '
             
    if(len(st)==0):
        st= "No events today"    
    lis.append(st)
    lis_json = json.dumps(lis)
    return lis_json

if ( __name__ == '__main__'):
        app.run(port=7778)
