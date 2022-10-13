from urllib import response
import requests
import json
import PyWallpaper

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# ======================= Data in JSON ====================
response = requests.get(api_url)
content_in_byte = response.content
# print(type(content_in_byte))
content_in_str = response.content.decode("UTF-8")
# print(type(content_in_str))
content_in_dictonary = json.loads(content_in_str)

# ======================= Image URL ====================
img_url = content_in_dictonary["url"]

res = requests.get(img_url)

# ======================= Save Image ====================
with open("apod.png","wb") as image:
    image.write(res.content)

# ======================= Save Image ====================
PyWallpaper.change_wallpaper("E:\Phitron\Python\Week 02\Module-6(lab)\apod.png")