dfrom moviepy.editor import VideoFileClip
import os
time=0
i=0
path=input()
for folder in os.listdir(path):
	temp = [x for x in os.listdir(os.path.join(path,folder)) if x.endswith('.mp4')]
	a = os.path.join(path,folder)
	os.chdir(a)
	for file in temp:
		i+=1
		clip = VideoFileClip(file)
		time+=clip.duration
		clip.close()
		print(file)

print(i)
hrs = int(time/3600)
mins = int((time - hrs * 3600)/60)
print(hrs,"hrs",mins,"mins")
