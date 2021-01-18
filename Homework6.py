import json
import yaml
import os


path_for_json_file = os.path.join(os.getcwd(), "jsonfile.json")
path_for_yaml_file = os.path.join(os.getcwd(), "yamlfile.yml")

# 1. json to text parser

with open(path_for_json_file, "r") as json_file:
	data_in_json = json.load(json_file)

with open("textfile.txt", "w") as text_file:
	text_file.write(str(data_in_json))

# 2. json to yaml parser

with open(path_for_json_file, "r") as json_f:
	json_data1 = json.load(json_f)

with open("yamlfile1.yml", "w") as yaml_file:
	yaml.dump(json_data1, yaml_file, indent=2, sort_keys=False)

# 3. Yaml to json parser

with open(path_for_yaml_file, "r") as yaml_file1:
	data_in_yaml = yaml.load(yaml_file1, Loader=yaml.FullLoader)

with open("jsonfile1.json", "w") as json_file1:
	json.dump(data_in_yaml, json_file1, indent=4)

# 4. Yaml to text parser

with open(path_for_yaml_file, "r") as yaml_file2:
	data_in_yaml1 = yaml.load(yaml_file2, Loader=yaml.FullLoader)

with open("textfile1.txt", "w") as text_file:
	text_file.write(str(data_in_yaml1))