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
    # if(day[0]=='0'):
    #     day=day[1]
    # var = month+'-'+day
    var = day+'-'+month
    print("var",var)
    print("Date",data["Date"][0])

    lis=[]
    st=''
    desc=''
    dic={}
    for i in range(len(data["Date"])):
        if(data["Date"][i]==var):
            '''if(st!=''):
                st=st+', '+data["Name"][i]
            else:
                st=st+data["Name"][i]'''
            dic[data["Name"][i]] = data["Description"][i]
                
    if(len(dic)==0):
        dic["No Events today"] = "No Description"
    # lis.append(st)
    dic_json = json.dumps(dic)
    return dic_json

if ( __name__ == '__main__'):
        app.run(port=7778)



