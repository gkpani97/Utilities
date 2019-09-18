import os
import xml.etree.ElementTree as ET

var_path=os.path.dirname(os.path.abspath(__file__))

xml_list={x for x in os.listdir(var_path) if x.endswith('.xml')}

for file_name in xml_list:
	
	tree = ET.parse(file_name)
	root = tree.getroot()

	for folder in root.iter('folder'):
		folder.text='test'

	for filename in root.iter("filename"):
		filename.text=file_name.split(".")[0] + ".jpg"

	for path in root.iter("path"):	
		path.text=var_path + "\\" + file_name.split(".")[0] + ".jpg"
	
	tree.write(file_name)

	