# pip install --trusted-host pypi.python.org moviepy
# python
# import imageio
# imageio.plugins.ffmpeg.download()




import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip



path=input("Enter the Path")

folder_paths=os.listdir(path)

for folder in folder_paths:

	class_path= path + "\\" + folder

	for vid in os.listdir(class_path):

		input_path=class_path+"\\"+vid
		output_path=class_path+"\\"+"trimmed"+"\\"+"NEW"+vid
		ffmeg_extract_subclip(input_path,0,100, targetname=output_path)
