# Ex04 Places Around Me
## Date:22/09/2025 

## AIM
To develop a website to display details about the places around my house.

## DESIGN STEPS

### STEP 1
Create a Django admin interface.

### STEP 2
Download your city map from Google.

### STEP 3
Using ```<map>``` tag name the map.

### STEP 4
Create clickable regions in the image using ```<area>``` tag.

### STEP 5
Write HTML programs for all the regions identified.

### STEP 6
Execute the programs and publish them.

## CODE
```
map.html

<center><img src="Screenshot 2025-09-20 142121.png" usemap="#image-map"></center>

<map name="image-map">
    <area target="" alt="Farm house" title="Farm house" href="Farm.html" coords="756,471,914,544" shape="rect">
    <area target="" alt="Green tech bio" title="Green tech bio" href="tech.html" coords="1408,765,1567,831" shape="rect">
    <area target="" alt="ramar pannai" title="ramar pannai" href="ramar.html" coords="160,400,71,504,278,480" shape="poly">
    <area target="" alt="coco lagoon" title="coco lagoon" href="lagoon.html" coords="491,661,96" shape="circle">
    <area target="" alt="samyuktha inn" title="samyuktha inn" href="inn.html" coords="1346,377,1503,451" shape="rect">
</map>coco

Farm.html

<html>
    <head><title>Farm house</title></head>
    <body bgcolor="lightcoral">
        <h1>Welcome to Farm house</h1>
        <p>The Farm House is a charming rural retreat located in the countryside, offering a peaceful escape from city life. 
            Surrounded by lush fields and rolling hills, it provides a perfect setting for relaxation and outdoor activities. 
            Guests can enjoy farm-to-table dining experiences, explore nature trails, and participate in various agricultural activities. 
            The Farm House is ideal for families, couples, and anyone looking to reconnect with nature and experience the simplicity of rural living.</p>
</html>

inn.html

<html>
    <head> <title>samyuktha inn</title></head>
    <body bgcolor="lightyellow">
        <h1>Welcome to Samyuktha Inn</h1>
        <p>Samyuktha Inn is a comfortable and budget-friendly stay and dining option, known for its clean rooms, homely atmosphere, 
            and simple yet tasty South Indian food. It offers essential amenities for travelers, a welcoming environment for families, 
            and convenient access to nearby transport and attractions.</p>
    </body>
</html>

lagoon.html

<html>
    <head><title>coco lagoon</title></head>
    <body bgcolor="lightblue">
        <h1>Welcome to Coco Lagoon</h1>
        <p>Coco Lagoon is a charming eco-friendly resort located in the serene backwaters of Kerala, India.
             It offers a tranquil escape with its traditional thatched cottages, lush coconut groves, and scenic waterways.
              Guests can enjoy activities such as boat rides, bird watching, and exploring the local culture while indulging in authentic Kerala cuisine.
               Coco Lagoon is ideal for nature lovers and those seeking a peaceful retreat amidst natural beauty.</p>
    </body>
</html>

ramar.html

<html>
    <head><title>ramar pannai</title></head>
    <body bgcolor="lightgreen">
        <h1>Welcome to Ramar Pannai</h1>
        <p>Ramar Pannai is a picturesque farm stay located in the countryside of Tamil Nadu, India. 
            It offers a serene environment surrounded by lush greenery, traditional farming practices, and rustic charm. 
            Visitors can experience rural life, participate in farming activities, and enjoy fresh organic produce. 
            Ramar Pannai is perfect for those looking to escape the hustle and bustle of city life and reconnect with nature.</p>
</html>

tech.html

<html>
    <head><title>Green tech bio</title></head>
    <body bgcolor="lightgrey">
        <h1>Welcome to Green Tech Bio</h1>
        <p>Green Tech Bio is an innovative agricultural technology company focused on sustainable farming solutions. 
            They specialize in developing eco-friendly products and techniques that enhance crop yield while minimizing environmental impact. 
            Their offerings include organic fertilizers, pest control solutions, and advanced irrigation systems designed to promote healthy plant growth and soil conservation. 
            Green Tech Bio is dedicated to supporting farmers in adopting green practices for a better future.</p>
</html>
```


## OUTPUT
![alt text](<Screenshot 2025-09-24 110737-1.png>)
![alt text](<Screenshot 2025-09-24 110851.png>)
![alt text](<Screenshot 2025-09-24 110911.png>)
![alt text](<Screenshot 2025-09-24 110930.png>)
![alt text](<Screenshot 2025-09-24 111013.png>)
![alt text](<Screenshot 2025-09-24 110949-1.png>)





## RESULT
The program for implementing image maps using HTML is executed successfully.
