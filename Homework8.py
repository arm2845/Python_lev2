import os
import json
import requests
import threading
import random


file_path = os.path.join(os.getcwd(), "ImageURL.json")

def ReadJsonfile(path):
	with open(path, "r") as jsonfile:
		data = json.load(jsonfile)
	URL_list = []
	for dict_ in data["images"]:
		URL_list.append(dict_["URL"])
	return URL_list

URL_list = ReadJsonfile(file_path)

def downloadimage(URL):
	getimage = requests.get(URL)
	with open(f"{random.randint(0, 1000)}.jpeg", "wb") as file:
		file.write(getimage.content)

for i in URL_list:
	x = threading.Thread(target = downloadimage, args = (i, ))
	x.start()