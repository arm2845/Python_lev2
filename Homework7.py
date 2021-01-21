import os
import requests


class ImageFromText():

	def __init__(self, text_file, image_list):
		self.text_file = text_file
		self.image_list = []

	def readfile(self):
		path = os.path.join(os.getcwd(), self.text_file)
		with open(path, "r") as textfile:
			data = textfile.read()
		list_for_data = data.split()
		positions_list = []
		for i in list_for_data:
			if ".png" in i:
				while i.endswith(".png") is False:
					i = i[:-1]
				if "https:" in i:
					while i.startswith("https:") is False:
						i = i[1:]
				else:
					while i.startswith("/") is False:
						i = i[1:]
					i = "https:" + i
				self.image_list.append(i)
			if ".jpg" in i:
				while i.endswith(".jpg") is False:
					i = i[:-1]
				if "https:" in i:
					while i.startswith("https:") is False:
						i = i[1:]
				else:
					while i.startswith("/") is False:
						i = i[1:]
					i = "https:" + i
				self.image_list.append(i)
		return self.image_list

class Image_jpg():
	def __init__(self, image_list):
		self.image_list = image_list
	
	def download(self):
		for i in self.image_list:
			if ".jpg" in self.image_list:
				getimage = requests.get(i)
				with open(f"{self.image_list[i]}.jpeg", "wb") as imagefile:
					imagefile.write(getimage.content)

class Image_png():
	def __init__(self, image_list):
		self.image_list = image_list

	def download(self):
		for i in self.image_list:
			if ".png" in self.image_list:
				getimage = requests.get(i)
				with open(f"{self.image_list[i]}.png", "wb") as imagefile:
					imagefile.write(getimage.content)


example = ImageFromText("sourcecode.txt", [])
image_list = example.readfile()
print(image_list)
jpegfile = Image_jpg(image_list)
jpegfile.download()
pngfile = Image_png(image_list)
pngfile.download()