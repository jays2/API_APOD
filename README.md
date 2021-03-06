# PYTHON API TO APOD

## Introduction
This project consist of an API link to the [NASA APOD] (https://api.nasa.gov/#apod) retrieving the last 100 pictures of the day from the current date. 

A flask application is also used in order to navigate through the URL images.

## API Connection

EndPoints: 
- http://apod07nasa.herokuapp.com/pictures/general
- http://apod07nasa.herokuapp.com/pictures/url
- http://apod07nasa.herokuapp.com/pictures/hdurl
- http://apod07nasa.herokuapp.com/pictures/explanation
- http://apod07nasa.herokuapp.com/pictures/title

Field responses:
- pictures/general: every field from the APOD NASA response.
- pictures/url: low definition link to POD.
- pictures/hdurl: high definition link to POD.
- pictures/explanation: full description on pictures.
- pictures/title: picture title.

Parameters used:
- date: A string in YYYY-MM-DD indicating the desired date from the APOD pool.
- page_num:  A positive integer indicating the page in which you want to position, default value is 1. Since there's only going to be a hundred images, the response in this case is going to be paginated 10 times.
- page_size: A positive integer indicating the size of every page delivered, default value is 10. If for example this value would be 50, only 2 pages will be returned.

Examples:

<details><summary>See Return Object</summary>
<p>

```jsoniq
[
  {
    "info": {
      "count": 100,
      "next": "/pictures/general?page_num=2&page_size=10",
      "next_page": 2,
      "page_num": 1,
      "page_size": 10,
      "prev": "None",
      "prev_page": 0
    }
  },
  {
    "pictures": [
       {
        "copyright": "CFHT",
        "date": "2022-02-07",
        "explanation": "It's raining stars.  What appears to be a giant cosmic umbrella is now known to be a tidal stream of stars stripped from a small satellite galaxy. The main galaxy, spiral galaxy NGC 4651, is about the size of our Milky Way, while its stellar parasol appears to extend some 100 thousand light-years above this galaxy's bright disk. A small galaxy was likely torn apart by repeated encounters as it swept back and forth on eccentric orbits through NGC 4651. The remaining stars will surely fall back and become part of a combined larger galaxy over the next few million years. The featured image was captured by the Canada-France-Hawaii Telescope (CFHT) in Hawaii, USA.  The Umbrella Galaxy lies about 50 million light-years distant toward the well-groomed northern constellation Coma Berenices.   Almost Hyperspace: Random APOD Generator",
        "hdurl": "https://apod.nasa.gov/apod/image/2202/NGC4651_CFHT_1587.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "NGC 4651: The Umbrella Galaxy",
        "url": "https://apod.nasa.gov/apod/image/2202/NGC4651_CFHT_960.jpg"
      },
      {
        "date": "2022-02-06",
        "explanation": "Welcome to planet Earth, the third planet from a star named the Sun.  The Earth is shaped like a sphere and composed mostly of rock.  Over 70 percent of the Earth's surface is water.  The planet has a relatively thin atmosphere composed mostly of nitrogen and oxygen.  The featured picture of Earth, dubbed The Blue Marble, was taken from Apollo 17 in 1972 and features Africa and Antarctica.  It is thought to be one of the most widely distributed photographs of any kind.  Earth has a single large Moon that is about 1/4 of its diameter and, from the planet's surface, is seen to have almost exactly the same angular size as the Sun.  With its abundance of liquid water, Earth supports a large variety of life forms, including potentially intelligent species such as dolphins and humans.  Please enjoy your stay on planet Earth.",
        "hdurl": "https://apod.nasa.gov/apod/image/2202/bluemarble_apollo17_3000.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "Blue Marble Earth",
        "url": "https://apod.nasa.gov/apod/image/2202/bluemarble_apollo17_960.jpg"
      },
      ...
    ]
  }
]
```

</p>
</details>

```
http://apod07nasa.herokuapp.com/pictures/general
```
<details><summary>See Return Object</summary>
<p>

```jsoniq

[
  {
    "info": {
      "count": 1,
      "next": "None",
      "next_page": 0,
      "page_num": 1,
      "page_size": 10,
      "prev": "None",
      "prev_page": 0
    }
  },
  {
    "pictures": [
      {
        "copyright": "Carlos Taylor",
        "date": "2022-05-06",
        "explanation": "This cosmic skyscape features glowing gas and dark dust clouds along side the young stars of NGC 3572. A beautiful emission nebula and star cluster it sails far southern skies within the nautical constellation Carina. Stars from NGC 3572 are toward top center in the telescopic frame that would measure about 100 light-years across at the cluster's estimated distance of 9,000 light-years. The visible interstellar gas and dust is part of the star cluster's natal molecular cloud. Dense streamers of material within the nebula, eroded by stellar winds and radiation, clearly trail away from the energetic young stars. They are likely sites of ongoing star formation with shapes reminiscent of the Tadpoles of IC 410 better known to northern skygazers.  In the coming tens to hundreds of millions of years, gas and stars in the cluster will be dispersed though, by gravitational tides and by violent supernova explosions that end the short lives of the massive cluster stars.",
        "hdurl": "https://apod.nasa.gov/apod/image/2205/NGC3572SouthernTadpolesCarlosTaylor.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "NGC 3572 and the Southern Tadpoles",
        "url": "https://apod.nasa.gov/apod/image/2205/NGC3572SouthernTadpolesCarlosTaylor1024.jpg"
      }
    ]
  }
]
```
</p>
</details>

```
http://apod07nasa.herokuapp.com/pictures/general?date=2022-05-06
```

Page number 2:
```
http://apod07nasa.herokuapp.com/pictures/general?page_num=2
```
Second page and page size = 50:
```
http://apod07nasa.herokuapp.com/pictures/general?page_num=2&page_size=50
```
Only URL links:
```
http://apod07nasa.herokuapp.com/pictures/url
```

Only title descriptions:
```
http://apod07nasa.herokuapp.com/pictures/url
```
Filtering by field and date:
```
http://apod07nasa.herokuapp.com/pictures/url?date=2022-05-06
```
Filtering by field and page number:
```
http://apod07nasa.herokuapp.com/pictures/url?page_num=5
```
Filtering by field, page number and page size:
```
http://apod07nasa.herokuapp.com/pictures/url?page_num=2&page_size=50
```
## Code
App.py is responsible to handle the API calls specifically on the "/pictures/<string:field>" route. Depending on the field supplied, the response is filtered. 

```
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
```

Connection to NASA API is made by the following call, giving a starting and ending date, please use a personal KEY on development to avoid crashing this project:
```
https://api.nasa.gov/planetary/apod?api_key=5D28BHJaqlW7u9okOxk1bFAu6CAhOGPT3629bpBH&start_date={sub_today}&end_date={today}
```
## Front-end
Navigating in a visual environment can be made with the home route. The API made in the first section is used to collect the data. :
```
http://apod07nasa.herokuapp.com/
```

## Feedback and performance
Please feel free to ask any questions and recommend changes. Keep in minds that NASA API works very slow with a hundred requests, this was solved keeping a cached list every day. Such improvement shouldn't been necessary but the overall web experience got clogged.

