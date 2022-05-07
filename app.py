from datetime import date
from pprint import pprint
from datetime import date, timedelta
from flask import Flask, jsonify, request, redirect, url_for, render_template

import requests
import json

app = Flask(__name__)

from images import pictures

#Index route
@app.route('/', methods=['GET'])
def home():
    response_APOC = requests.get('https://apod07nasa.herokuapp.com/pictures/general')  
    data_response = response_APOC.text
    pictures_content = json.loads(data_response)
    return render_template("index.html", content = pictures_content) 
    
#Fills local data with NASA API
def fillDataField(field):
    global pictures
    pictures.clear()
    today = date.today().isoformat()
    sub_today = str(date.today() - timedelta(days=16))
    response_API = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=5D28BHJaqlW7u9okOxk1bFAu6CAhOGPT3629bpBH&start_date={sub_today}&end_date={today}')
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

#Pictures routes *API*
@app.route('/pictures/<string:field>', methods=['GET'])
def searchField(field):
    global pictures
    args = request.args
    page_num = args.get('page_num',default=1, type=int)
    page_size = args.get('page_size',default=10, type=int)
    date_supplied = args.get('date',type=str)
    fillDataField(field)
  
    start = (page_num - 1) * page_size
    end = start + page_size
    filtered_pictures = []
     
    if date_supplied != None:
      for each in pictures:
        if each['date'] == date_supplied:
          filtered_pictures.append(each)
        pictures = filtered_pictures 

    count = len(pictures)

    #There's only one date per day
    if date_supplied != None:
      prev = "None" 
      prev_num = 0
      next = "None"
      next_num = 0
    elif end>=count: #last page
      if page_num > 1:
        prev = f"/pictures/{field}?page_num={page_num-1}&page_size={page_size}" 
        prev_num = page_num - 1
      else: #first page
        prev = 'None'  
        prev_num = 0 
      next = 'None'
      next_num = 0
    else: #not last page
      if page_num > 1:
        prev = f"/pictures/{field}?page_num={page_num-1}&page_size={page_size}" 
        prev_num = page_num - 1
      else: #first page
        prev = 'None'  
        prev_num = 0
      next = f"/pictures/{field}?page_num={page_num+1}&page_size={page_size}" 
      next_num = page_num + 1
    
    general_Info = {'count':count, 'page_num':page_num, 'page_size':page_size, 'next': next, 'next_page':next_num, 'prev': prev, 'prev_page':prev_num}

    return jsonify({'info':general_Info},{'pictures': pictures[start:end]})

#Next or previous route to address 
@app.route('/apod/<string:page_num>', methods=['GET'])
def paginate(page_num):
    response_APOC = requests.get(f'https://apod07nasa.herokuapp.com/pictures/general?page_num={page_num}') 
    data_response = response_APOC.text
    pictures_content = json.loads(data_response)
   
    return render_template("index.html", content = pictures_content) 
    

#Look for a specific date
@app.route('/apod/look', methods=['GET'])
def look():
    args = request.args
    date_supplied = args.get('fdate',type=str)
  
    if date_supplied == "":
      response_APOC = requests.get(f'https://apod07nasa.herokuapp.com/pictures/general')  
    else:
      response_APOC = requests.get(f'https://apod07nasa.herokuapp.com/pictures/general?date={date_supplied}') 

    data_response = response_APOC.text
    pictures_content = json.loads(data_response)

    return render_template("index.html", content = pictures_content) 

if __name__ == '__main__':
    app.run(debug=True, port=4000)
   