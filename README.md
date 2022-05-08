# PYTHON API TO APOD

## Introduction
This project consist of an API link to the [NASA APOD] (https://api.nasa.gov/#apod) retrieving the last 100 pictures of the day from the current date. 

A flask aplication is also used in order to navigate through the url images.

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
- date: A string in YYYY-MM-DD indicating the date from the APOD image in the last 100 days.
- page_num:  A positive integer indicating the page in which you want to position, default value is 1. Since there's only going to the a hundred images, the response is going to be paginated 10 times.
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
        "copyright": "Marco Lorenzi",
        "date": "2022-01-29",
        "explanation": "Named for the southern constellation toward which most of its galaxies can be found, the Fornax Cluster is one of the closest clusters of galaxies. About 62 million light-years away, it is almost 20 times more distant than our neighboring Andromeda Galaxy, and only about 10 percent farther than the better known and more populated Virgo Galaxy Cluster. Seen across this two degree wide field-of-view, almost every yellowish splotch on the image is an elliptical galaxy in the Fornax cluster. Elliptical galaxies NGC 1399 and NGC 1404 are the dominant, bright cluster members toward the upper left (but not the spiky foreground stars). A standout barred spiral galaxy NGC 1365 is visible on the lower right as a prominent Fornax cluster member.",
        "hdurl": "https://apod.nasa.gov/apod/image/2201/FornaxC1_FB.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "The Fornax Cluster of Galaxies",
        "url": "https://apod.nasa.gov/apod/image/2201/FornaxC1_FB1024.jpg"
      },
      {
        "date": "2022-01-30",
        "explanation": "How can gas float above the Sun?   Twisted magnetic fields arching from the solar surface can trap ionized gas, suspending it in huge looping structures.  These majestic plasma arches are seen as prominences above the solar limb.  In 1999, this dramatic and detailed image was recorded by the Extreme ultraviolet Image Telescope (EIT) on board the space-based SOHO observatory in the light emitted by ionized Helium.  It shows hot plasma escaping into space as a fiery prominence breaks free from magnetic confinement a hundred thousand kilometers above the Sun.  These awesome events bear watching as they can affect communications and power systems over 100 million kilometers away on planet Earth. In late 2020 our Sun passed the solar minimum of its 11-year cycle and is now showing  increased surface activity.",
        "hdurl": "https://apod.nasa.gov/apod/image/2201/sunprom3_soho_2100.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "A Solar Prominence from SOHO",
        "url": "https://apod.nasa.gov/apod/image/2201/sunprom3_soho_960.jpg"
      },
      {
        "copyright": "Roberto Colombari",
        "date": "2022-01-31",
        "explanation": "The Great Carina Nebula is home to strange stars and iconic nebulas. Named for its home constellation, the huge star-forming region is larger and brighter than the Great Orion Nebula but less well known because it is so far south -- and because so much of humanity lives so far north.  The featured image shows in great detail the northern-most part of the Carina Nebula. Visible nebulas include the semi-circular filaments surrounding the active star Wolf-Rayet 23 (WR23) on the far left.  Just left of center is the Gabriela Mistral Nebula consisting of an emission nebula of glowing gas (IC 2599) surrounding the small open cluster of stars (NGC 3324). Above the image center is the larger star cluster NGC 3293, while to its right is the relatively faint emission nebula designated Loden 153.  The most famous occupant of the Carina Nebula, however, is not shown. Off the image to the lower right is the bright, erratic, and doomed star star known as Eta Carinae -- a star once one of the brightest stars in the sky and now predicted to explode in a supernova sometime in the next few million years.",
        "hdurl": "https://apod.nasa.gov/apod/image/2201/CarinaNorth_Colombari_3000.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "Carina Nebula North",
        "url": "https://apod.nasa.gov/apod/image/2201/CarinaNorth_Colombari_960.jpg"
      },
      {
        "date": "2022-02-01",
        "explanation": "What will the Moon phase be on your birthday this year?  It is hard to predict because the Moon's appearance changes nightly.  As the Moon orbits the Earth, the half illuminated by the Sun first becomes increasingly visible, then decreasingly visible. The featured video animates images and altitude data taken by NASA's Moon-orbiting Lunar Reconnaissance Orbiter to show all 12 lunations that appear this year, 2022 -- as seen from Earth's northern (southern) hemisphere. A single lunation describes one full cycle of our Moon, including all of its phases. A full lunation takes about 29.5 days, just under a month (moon-th). As each lunation progresses, sunlight reflects from the Moon at different angles, and so illuminates different features differently.  During all of this, of course, the Moon always keeps the same face toward the Earth. What is less apparent night-to-night is that the Moon's apparent size changes slightly, and that a slight wobble called a libration occurs as the Moon progresses along its elliptical orbit.",
        "media_type": "video",
        "service_version": "v1",
        "title": "Moon Phases 2022",
        "url": "https://www.youtube.com/embed/c4Xky6tlFyY?rel=0&VQ=HD720"
      },
      {
        "date": "2022-02-02",
        "explanation": "What's happening at the center of our galaxy? It's hard to tell with optical telescopes since visible light is blocked by intervening interstellar dust. In other bands of light, though, such as radio, the galactic center can be imaged and shows itself to be quite an interesting and active place.  The featured picture shows the latest image of our Milky Way's center by the MeerKAT array of 64 radio dishes in South Africa. Spanning four times the angular size of the Moon (2 degrees), the image is impressively vast, deep, and detailed.  Many known sources are shown in clear detail, including many with a prefix of Sgr, since the galactic center is in the direction of the constellation Sagittarius.  In our Galaxy's Center lies Sgr A, found here in the image center, which houses the Milky Way's central supermassive black hole.  Other sources in the image are not as well understood, including the Arc, just to the left of Sgr A, and numerous filamentary threads. Goals for MeerKAT include searching for radio emission from neutral hydrogen emitted in a much younger universe and brief but distant radio flashes.   Open Science: Browse 2,700+ codes in the Astrophysics Source Code Library",
        "hdurl": "https://apod.nasa.gov/apod/image/2202/MwCenter_MeerKATMunoz_7530.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "The Galactic Center in Radio from MeerKAT",
        "url": "https://apod.nasa.gov/apod/image/2202/MwCenter_MeerKATMunoz_1080.jpg"
      },
      {
        "copyright": "Juan Luis Cánovas Pérez",
        "date": "2022-02-03",
        "explanation": "ven though Venus (left) was the brightest planet in the sky it was less than 1/30th the apparent size of the Moon on January 29. But as both rose before the Sun they shared a crescent phase, and for a moment their visible disks were each about 12 percent illuminated as they stood above the southeastern horizon. The similar sunlit crescents were captured in these two separate images. Made at different magnifications, each panel is a composite of stacked video frames taken with a small telescope. Venus goes through a range of phases like the Moon as the inner planet wanders from evening sky to morning sky and back again with a period of 584 days. Of course the Moon completes its own cycle of phases, a full lunation, in about 29.5 days.",
        "hdurl": "https://apod.nasa.gov/apod/image/2202/VenusMoonSamePhase.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "Embraced by Sunlight",
        "url": "https://apod.nasa.gov/apod/image/2202/VenusMoonSamePhase1024.jpg"
      },
      {
        "copyright": "Robert Fedez",
        "date": "2022-02-04",
        "explanation": "ven though Jupiter was the only planet visible in the evening sky on February 2, it shared the twilight above the western horizon with the Solar System's brightest moons. In a single exposure made just after sunset, the Solar System's ruling gas giant is at the upper right in this telephoto field-of-view from Cancun, Mexico. The snapshot also captures our fair planet's own natural satellite in its young crescent phase. The Moon's disk looms large, its familiar face illuminated mostly by earthshine. But the four points of light lined-up with Jupiter are Jupiter's own large Galilean moons. Top to bottom are Ganymede, [Jupiter], Io, Europa, and Callisto. Ganymede, Io, and Callisto are physically larger than Earth's Moon while water world Europa is only slightly smaller.",
        "hdurl": "https://apod.nasa.gov/apod/image/2202/IMG_1869Fedez.png",
        "media_type": "image",
        "service_version": "v1",
        "title": "Moons at Twilight",
        "url": "https://apod.nasa.gov/apod/image/2202/IMG_1869Fedez1024.png"
      },
      {
        "date": "2022-02-05",
        "explanation": "Variable star R Aquarii is actually an interacting binary star system, two stars that seem to have a close symbiotic relationship. Centered in this space-based optical/x-ray composite image it lies about 710 light years away. The intriguing system consists of a cool red giant star and hot, dense white dwarf star in mutual orbit around their common center of mass. With binoculars you can watch as R Aquarii steadily changes its brightness over the course of a year or so. The binary system's visible light is dominated by the red giant, itself a Mira-type long period variable star. But material in the cool giant star's extended envelope is pulled by gravity onto the surface of the smaller, denser white dwarf, eventually triggering a thermonuclear explosion, blasting material into space. Astronomers have seen such outbursts over recent decades. Evidence for much older outbursts is seen in these spectacular structures spanning almost a light-year as observed by the Hubble Space Telescope (in red and blue). Data from the Chandra X-ray Observatory (in purple) shows the X-ray glow from shock waves created as a jet from the white dwarf strikes surrounding material.",
        "hdurl": "https://apod.nasa.gov/apod/image/2202/archives_raquarii.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "Symbiotic R Aquarii",
        "url": "https://apod.nasa.gov/apod/image/2202/archives_raquarii.jpg"
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
      {
        "copyright": "CFHT",
        "date": "2022-02-07",
        "explanation": "It's raining stars.  What appears to be a giant cosmic umbrella is now known to be a tidal stream of stars stripped from a small satellite galaxy. The main galaxy, spiral galaxy NGC 4651, is about the size of our Milky Way, while its stellar parasol appears to extend some 100 thousand light-years above this galaxy's bright disk. A small galaxy was likely torn apart by repeated encounters as it swept back and forth on eccentric orbits through NGC 4651. The remaining stars will surely fall back and become part of a combined larger galaxy over the next few million years. The featured image was captured by the Canada-France-Hawaii Telescope (CFHT) in Hawaii, USA.  The Umbrella Galaxy lies about 50 million light-years distant toward the well-groomed northern constellation Coma Berenices.   Almost Hyperspace: Random APOD Generator",
        "hdurl": "https://apod.nasa.gov/apod/image/2202/NGC4651_CFHT_1587.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "NGC 4651: The Umbrella Galaxy",
        "url": "https://apod.nasa.gov/apod/image/2202/NGC4651_CFHT_960.jpg"
      }
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
        "copyright": "Marco Lorenzi",
        "date": "2022-01-29",
        "explanation": "Named for the southern constellation toward which most of its galaxies can be found, the Fornax Cluster is one of the closest clusters of galaxies. About 62 million light-years away, it is almost 20 times more distant than our neighboring Andromeda Galaxy, and only about 10 percent farther than the better known and more populated Virgo Galaxy Cluster. Seen across this two degree wide field-of-view, almost every yellowish splotch on the image is an elliptical galaxy in the Fornax cluster. Elliptical galaxies NGC 1399 and NGC 1404 are the dominant, bright cluster members toward the upper left (but not the spiky foreground stars). A standout barred spiral galaxy NGC 1365 is visible on the lower right as a prominent Fornax cluster member.",
        "hdurl": "https://apod.nasa.gov/apod/image/2201/FornaxC1_FB.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "The Fornax Cluster of Galaxies",
        "url": "https://apod.nasa.gov/apod/image/2201/FornaxC1_FB1024.jpg"
      },
      {
        "date": "2022-01-30",
        "explanation": "How can gas float above the Sun?   Twisted magnetic fields arching from the solar surface can trap ionized gas, suspending it in huge looping structures.  These majestic plasma arches are seen as prominences above the solar limb.  In 1999, this dramatic and detailed image was recorded by the Extreme ultraviolet Image Telescope (EIT) on board the space-based SOHO observatory in the light emitted by ionized Helium.  It shows hot plasma escaping into space as a fiery prominence breaks free from magnetic confinement a hundred thousand kilometers above the Sun.  These awesome events bear watching as they can affect communications and power systems over 100 million kilometers away on planet Earth. In late 2020 our Sun passed the solar minimum of its 11-year cycle and is now showing  increased surface activity.",
        "hdurl": "https://apod.nasa.gov/apod/image/2201/sunprom3_soho_2100.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "A Solar Prominence from SOHO",
        "url": "https://apod.nasa.gov/apod/image/2201/sunprom3_soho_960.jpg"
      },
      {
        "copyright": "Roberto Colombari",
        "date": "2022-01-31",
        "explanation": "The Great Carina Nebula is home to strange stars and iconic nebulas. Named for its home constellation, the huge star-forming region is larger and brighter than the Great Orion Nebula but less well known because it is so far south -- and because so much of humanity lives so far north.  The featured image shows in great detail the northern-most part of the Carina Nebula. Visible nebulas include the semi-circular filaments surrounding the active star Wolf-Rayet 23 (WR23) on the far left.  Just left of center is the Gabriela Mistral Nebula consisting of an emission nebula of glowing gas (IC 2599) surrounding the small open cluster of stars (NGC 3324). Above the image center is the larger star cluster NGC 3293, while to its right is the relatively faint emission nebula designated Loden 153.  The most famous occupant of the Carina Nebula, however, is not shown. Off the image to the lower right is the bright, erratic, and doomed star star known as Eta Carinae -- a star once one of the brightest stars in the sky and now predicted to explode in a supernova sometime in the next few million years.",
        "hdurl": "https://apod.nasa.gov/apod/image/2201/CarinaNorth_Colombari_3000.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "Carina Nebula North",
        "url": "https://apod.nasa.gov/apod/image/2201/CarinaNorth_Colombari_960.jpg"
      },
      {
        "date": "2022-02-01",
        "explanation": "What will the Moon phase be on your birthday this year?  It is hard to predict because the Moon's appearance changes nightly.  As the Moon orbits the Earth, the half illuminated by the Sun first becomes increasingly visible, then decreasingly visible. The featured video animates images and altitude data taken by NASA's Moon-orbiting Lunar Reconnaissance Orbiter to show all 12 lunations that appear this year, 2022 -- as seen from Earth's northern (southern) hemisphere. A single lunation describes one full cycle of our Moon, including all of its phases. A full lunation takes about 29.5 days, just under a month (moon-th). As each lunation progresses, sunlight reflects from the Moon at different angles, and so illuminates different features differently.  During all of this, of course, the Moon always keeps the same face toward the Earth. What is less apparent night-to-night is that the Moon's apparent size changes slightly, and that a slight wobble called a libration occurs as the Moon progresses along its elliptical orbit.",
        "media_type": "video",
        "service_version": "v1",
        "title": "Moon Phases 2022",
        "url": "https://www.youtube.com/embed/c4Xky6tlFyY?rel=0&VQ=HD720"
      },
      {
        "date": "2022-02-02",
        "explanation": "What's happening at the center of our galaxy? It's hard to tell with optical telescopes since visible light is blocked by intervening interstellar dust. In other bands of light, though, such as radio, the galactic center can be imaged and shows itself to be quite an interesting and active place.  The featured picture shows the latest image of our Milky Way's center by the MeerKAT array of 64 radio dishes in South Africa. Spanning four times the angular size of the Moon (2 degrees), the image is impressively vast, deep, and detailed.  Many known sources are shown in clear detail, including many with a prefix of Sgr, since the galactic center is in the direction of the constellation Sagittarius.  In our Galaxy's Center lies Sgr A, found here in the image center, which houses the Milky Way's central supermassive black hole.  Other sources in the image are not as well understood, including the Arc, just to the left of Sgr A, and numerous filamentary threads. Goals for MeerKAT include searching for radio emission from neutral hydrogen emitted in a much younger universe and brief but distant radio flashes.   Open Science: Browse 2,700+ codes in the Astrophysics Source Code Library",
        "hdurl": "https://apod.nasa.gov/apod/image/2202/MwCenter_MeerKATMunoz_7530.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "The Galactic Center in Radio from MeerKAT",
        "url": "https://apod.nasa.gov/apod/image/2202/MwCenter_MeerKATMunoz_1080.jpg"
      },
      {
        "copyright": "Juan Luis Cánovas Pérez",
        "date": "2022-02-03",
        "explanation": "ven though Venus (left) was the brightest planet in the sky it was less than 1/30th the apparent size of the Moon on January 29. But as both rose before the Sun they shared a crescent phase, and for a moment their visible disks were each about 12 percent illuminated as they stood above the southeastern horizon. The similar sunlit crescents were captured in these two separate images. Made at different magnifications, each panel is a composite of stacked video frames taken with a small telescope. Venus goes through a range of phases like the Moon as the inner planet wanders from evening sky to morning sky and back again with a period of 584 days. Of course the Moon completes its own cycle of phases, a full lunation, in about 29.5 days.",
        "hdurl": "https://apod.nasa.gov/apod/image/2202/VenusMoonSamePhase.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "Embraced by Sunlight",
        "url": "https://apod.nasa.gov/apod/image/2202/VenusMoonSamePhase1024.jpg"
      },
      {
        "copyright": "Robert Fedez",
        "date": "2022-02-04",
        "explanation": "ven though Jupiter was the only planet visible in the evening sky on February 2, it shared the twilight above the western horizon with the Solar System's brightest moons. In a single exposure made just after sunset, the Solar System's ruling gas giant is at the upper right in this telephoto field-of-view from Cancun, Mexico. The snapshot also captures our fair planet's own natural satellite in its young crescent phase. The Moon's disk looms large, its familiar face illuminated mostly by earthshine. But the four points of light lined-up with Jupiter are Jupiter's own large Galilean moons. Top to bottom are Ganymede, [Jupiter], Io, Europa, and Callisto. Ganymede, Io, and Callisto are physically larger than Earth's Moon while water world Europa is only slightly smaller.",
        "hdurl": "https://apod.nasa.gov/apod/image/2202/IMG_1869Fedez.png",
        "media_type": "image",
        "service_version": "v1",
        "title": "Moons at Twilight",
        "url": "https://apod.nasa.gov/apod/image/2202/IMG_1869Fedez1024.png"
      },
      {
        "date": "2022-02-05",
        "explanation": "Variable star R Aquarii is actually an interacting binary star system, two stars that seem to have a close symbiotic relationship. Centered in this space-based optical/x-ray composite image it lies about 710 light years away. The intriguing system consists of a cool red giant star and hot, dense white dwarf star in mutual orbit around their common center of mass. With binoculars you can watch as R Aquarii steadily changes its brightness over the course of a year or so. The binary system's visible light is dominated by the red giant, itself a Mira-type long period variable star. But material in the cool giant star's extended envelope is pulled by gravity onto the surface of the smaller, denser white dwarf, eventually triggering a thermonuclear explosion, blasting material into space. Astronomers have seen such outbursts over recent decades. Evidence for much older outbursts is seen in these spectacular structures spanning almost a light-year as observed by the Hubble Space Telescope (in red and blue). Data from the Chandra X-ray Observatory (in purple) shows the X-ray glow from shock waves created as a jet from the white dwarf strikes surrounding material.",
        "hdurl": "https://apod.nasa.gov/apod/image/2202/archives_raquarii.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "Symbiotic R Aquarii",
        "url": "https://apod.nasa.gov/apod/image/2202/archives_raquarii.jpg"
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
      {
        "copyright": "CFHT",
        "date": "2022-02-07",
        "explanation": "It's raining stars.  What appears to be a giant cosmic umbrella is now known to be a tidal stream of stars stripped from a small satellite galaxy. The main galaxy, spiral galaxy NGC 4651, is about the size of our Milky Way, while its stellar parasol appears to extend some 100 thousand light-years above this galaxy's bright disk. A small galaxy was likely torn apart by repeated encounters as it swept back and forth on eccentric orbits through NGC 4651. The remaining stars will surely fall back and become part of a combined larger galaxy over the next few million years. The featured image was captured by the Canada-France-Hawaii Telescope (CFHT) in Hawaii, USA.  The Umbrella Galaxy lies about 50 million light-years distant toward the well-groomed northern constellation Coma Berenices.   Almost Hyperspace: Random APOD Generator",
        "hdurl": "https://apod.nasa.gov/apod/image/2202/NGC4651_CFHT_1587.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "NGC 4651: The Umbrella Galaxy",
        "url": "https://apod.nasa.gov/apod/image/2202/NGC4651_CFHT_960.jpg"
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
Second page and size page = 50:
```
http://apod07nasa.herokuapp.com/pictures/general?page_num=2&page_size=50
```
Only url links:
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
Filtering by field and page_num:
```
http://apod07nasa.herokuapp.com/pictures/url?page_num=5
```
Filtering by field, page_num and page_size:
```
http://apod07nasa.herokuapp.com/pictures/url?page_num=2&page_size=50
```
## Code
App.py is responsible to handle the API calls specifically on the "/pictures/<string:field>" route. Depending on the field supplied, the response is filtered. 

```
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

Connection to NASA API is made by the following call, giving a starting and ending date:
```
https://api.nasa.gov/planetary/apod?api_key=5D28BHJaqlW7u9okOxk1bFAu6CAhOGPT3629bpBH&start_date={sub_today}&end_date={today}
```
## Front-end
Navigating in a visual enviroment can be made with the home route. The API made in the first section is used to collect the data. :
```
http://apod07nasa.herokuapp.com/
```

## Feedback and performance
Please feel free to ask any questions and recommend changes. Keep in mind that NASA API is a little slow with the current 100 requests, this could be solved validating if the list with pictures is already filled. 

