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
def ping():
    #fillDataField("general")
    print(type(pictures))
    response_APOC = requests.get('http://127.0.0.1:4000/pictures/general') #probar
    #traer desde index, page num y asignarlo en el request, validar si este es vacio, 
    #o si viene con algo hacer con un boton summit get a esta ruta
    data_response = response_APOC.text
    pictures_content = json.loads(data_response)
    print(type(pictures_content))
    print(type(pictures_content[1]['pictures']))
   

    for each in pictures_content[1]['pictures']:
      print(each['title'])
  
    print(pictures_content[0]['info']['prev'])

    return render_template("index.html", content = pictures_content) 
    
    return jsonify({'General Info': 'http://127.0.0.1:4000/pictures/general'
    ,'explanation': 'http://127.0.0.1:4000/pictures/explanation'
    ,'hdurl': 'http://127.0.0.1:4000/pictures/hdurl'
    ,'title': 'http://127.0.0.1:4000/pictures/title'
    ,'url': 'http://127.0.0.1:4000/pictures/url'
    })

#Fills local data with NASA API
def fillDataField(field):
    global pictures
    pictures.clear()
    today = date.today().isoformat()
    sub_today = str(date.today() - timedelta(days=36))
    response_API = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=5D28BHJaqlW7u9okOxk1bFAu6CAhOGPT3629bpBH&start_date={sub_today}&end_date={today}')
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

#Pictures routes *API*
@app.route('/pictures/<string:field>', methods=['GET'])
def searchField(field):
    #prev_num = 0
    #next_num = 0
    global pictures
    args = request.args
    page_num = args.get('page_num',default=1, type=int)
    page_size = args.get('page_size',default=10, type=int)
    date_supplied = args.get('date',type=str)

    if len(pictures) < 1 :
      fillDataField(field)
    
    #If date is supplied we generate a filtered list   
    start = (page_num - 1) * page_size
    end = start + page_size
    count = len(pictures)
    filtered_pictures = []
   
    
    if date_supplied != None:
      for each in pictures:
        if each['date'] == date_supplied:
          filtered_pictures.append(each)
        pictures = filtered_pictures 

    #Defining header
    if end>=count: #last page
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
    #fillDataField("general")
    print(type(pictures))
    response_APOC = requests.get(f'http://127.0.0.1:4000/pictures/general?page_num={page_num}') #probar
    #traer desde index, page num y asignarlo en el request, validar si este es vacio, 
    #o si viene con algo hacer con un boton summit get a esta ruta
    data_response = response_APOC.text
    pictures_content = json.loads(data_response)
    print(type(pictures_content))
    print(type(pictures_content[1]['pictures']))
   

    for each in pictures_content[1]['pictures']:
      print(each['title'])
  
    print(pictures_content[0]['info']['prev'])

    return render_template("index.html", content = pictures_content) 
    
    return jsonify({'General Info': 'http://127.0.0.1:4000/pictures/general'
    ,'explanation': 'http://127.0.0.1:4000/pictures/explanation'
    ,'hdurl': 'http://127.0.0.1:4000/pictures/hdurl'
    ,'title': 'http://127.0.0.1:4000/pictures/title'
    ,'url': 'http://127.0.0.1:4000/pictures/url'
    })


if __name__ == '__main__':
    app.run(debug=True, port=4000)
   