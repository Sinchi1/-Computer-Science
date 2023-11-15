import json
from json2xml import json2xml
from json2xml.utils import readfromjson

json_file_path = "Расписание.json"

json_data = readfromjson(json_file_path)

xml_data = json2xml.Json2xml(json_data).to_xml()

print(xml_data)