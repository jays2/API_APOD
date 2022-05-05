from datetime import date
from pprint import pprint
from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

from images import products
from images import pictures


def fillData():
    global pictures
    pictures.clear()
    response_API = requests.get('https://api.nasa.gov/planetary/apod?api_key=5D28BHJaqlW7u9okOxk1bFAu6CAhOGPT3629bpBH&start_date=2022-04-30')
    #Link should be: https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=100
    data = response_API.text
    pictures_nasa = json.loads(data)

    #Go through recieved data and assign it
    for pic in pictures_nasa: 
      pictures.append(pic)
    
    return jsonify({'response': 'Populated!'})

# Testing Route
@app.route('/', methods=['GET'])
def ping():
    return jsonify({'General Info': 'http://127.0.0.1:4000/pictures'
    ,'explanation': 'http://127.0.0.1:4000/pictures/explanation'
    ,'hdurl': 'http://127.0.0.1:4000/pictures/hdurl'
    ,'title': 'http://127.0.0.1:4000/pictures/title'
    ,'url': 'http://127.0.0.1:4000/pictures/url'
    })

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    print(type(products[0]))
    productsFound = [
        product for product in products if product['name'] == product_name.lower()]
    if (len(productsFound) > 0):
        return jsonify({'product': productsFound[0]})
    return jsonify({'message': 'Product Not found'})

# Get Data Routes
@app.route('/products')
def getProducts():
    # return jsonify(products)
    return jsonify({'products': products})

# Populate data
@app.route('/fill')
def getData():
    response_API = requests.get('https://api.nasa.gov/planetary/apod?api_key=5D28BHJaqlW7u9okOxk1bFAu6CAhOGPT3629bpBH&start_date=2022-05-01')
    #Link simplified: https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&start_date=2022-05-01
    #Link should be: https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=100
    data = response_API.text
    pictures_nasa = json.loads(data)

    #Go through recieved data and assign it
    for pic in pictures_nasa: 
      pictures.append(pic)
    
    return jsonify({'response': 'Populated!'})

@app.route('/pictures', methods=['GET'])
def search():
    global pictures
    args = request.args
    page_num = args.get('page_num',default=1, type=int)
    page_size = args.get('page_size',default=10, type=int)
    date_supplied = args.get('date',type=str)

    #Load data
    fillData()

    #If date is supplied we generate a filtered list   
    start = (page_num - 1) * page_size
    end = start + page_size
    count = len(pictures)
    filtered_pictures = []
    
    if date_supplied != None:
      for each in pictures:
      #print(each['copyright'])
       if each['date'] == date_supplied:
          print("FOUND DATE")
          filtered_pictures.append(each)
          print(filtered_pictures)
      pictures = filtered_pictures 

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

@app.route('/date', methods=['GET'])
def getDate():
    args = request.args
    date_supplied = args.get('prm', type=str)
    fecha = '2020-01-01' 
    print("--")
    print(date_supplied)
    found = 'False'
    if date_supplied != None:
      found = 'True'
    return (found)


if __name__ == '__main__':
    app.run(debug=True, port=4000)
   