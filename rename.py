import os
import time


images=input("Enter the Path of the images folder: ")
images_xml=input("Enter the Path of the XML folder for the above folder: ")

image_names={os.path.splitext(x)[0] for x in os.listdir(images)}
image_xml_names={os.path.splitext(x)[0] for x in os.listdir(images_xml)}

for missing in image_names - image_xml_names:
	os.remove(images+"\\"+missing+".jpg")

for missing in image_xml_names:
	os.rename(images_xml+"\\"+missing+".xml",images+"\\"+missing+".xml")

var=time.ctime(time.time()).split(" ")[3].replace(':','')

a=0

for i in os.listdir(images):
	os.rename(images+"\\"+i,images+"\\IMG"+var+"no"+str(int(a))+"."+i.split(".")[1])
	a = a+0.5





