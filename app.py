from datetime import date
from pprint import pprint
from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

from images import pictures

#Fills local data with NASA API
def fillDataField(field):
    global pictures
    pictures.clear()
    response_API = requests.get('https://api.nasa.gov/planetary/apod?api_key=5D28BHJaqlW7u9okOxk1bFAu6CAhOGPT3629bpBH&start_date=2022-04-30')
    #Link should be: https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=100
    data = response_API.text
    pictures_nasa = json.loads(data)

    #If field is supplied, we assign by it
    dict = {}
    if field == "url":
     for each in pictures_nasa:
        dict = {"date":each['date'],"url":each['url']}
        pictures.append(dict)
    elif field == "hdurl":
      for each in pictures_nasa:
        dict = {"date":each['date'],"hdurl":each['hdurl']}
        pictures.append(dict)
    elif field == "explanation":
      for each in pictures_nasa:
        dict = {"date":each['date'],"explanation":each['explanation']}
        pictures.append(dict)
    elif field == "title":
      for each in pictures_nasa:
        dict = {"date":each['date'],"title":each['title']}
        pictures.append(dict)
    elif field == "general":
      for pic in pictures_nasa: 
       pictures.append(pic)
    
    return jsonify({'response': 'Response successful'})

#Index route
@app.route('/', methods=['GET'])
def ping():
    return jsonify({'General Info': 'http://127.0.0.1:4000/pictures/general'
    ,'explanation': 'http://127.0.0.1:4000/pictures/explanation'
    ,'hdurl': 'http://127.0.0.1:4000/pictures/hdurl'
    ,'title': 'http://127.0.0.1:4000/pictures/title'
    ,'url': 'http://127.0.0.1:4000/pictures/url'
    })

#Pictures routes  
@app.route('/pictures/<string:field>', methods=['GET'])
def searchField(field):
    global pictures
    args = request.args
    page_num = args.get('page_num',default=1, type=int)
    page_size = args.get('page_size',default=10, type=int)
    date_supplied = args.get('date',type=str)

    #Load data
    fillDataField(field)

    #If date is supplied we generate a filtered list   
    start = (page_num - 1) * page_size
    end = start + page_size
    count = len(pictures)
    filtered_pictures = []
    
    if date_supplied != None:
      for each in pictures:
       if each['date'] == date_supplied:
          print("FOUND DATE")
          filtered_pictures.append(each)
          print(filtered_pictures)
      pictures = filtered_pictures 

    #If entry point is supplied we filter
    if end>=count: #last page
      if page_num > 1:
        prev = f"/pictures?page_num={page_num-1}&page_size={page_size}" 
      else: #first page
        prev = 'None'   
      next = 'None'
    else: #not last page
      if page_num > 1:
        prev = f"/pictures?page_num={page_num-1}&page_size={page_size}" 
      else: #first page
        prev = 'None'  
      next = f"/pictures?page_num={page_num+1}&page_size={page_size}" 
    
    general_Info = {'count':count, 'page_num':page_num, 'page_size':page_size, 'next': next, 'prev': prev}

    return jsonify({'info':general_Info},{'pictures': pictures[start:end]})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
   