import xmltodict
import json
import xml.etree.ElementTree as ET

xml_file_path = "meerkat_CIF_trace.xml"

with open(xml_file_path, 'r') as fp:
    doc = xmltodict.parse(fp.read())

for picture in doc['AVCTrace']['Picture']:
    picture_id = picture['@id']
    json_doc = json.dumps(picture, indent=4)

    # Path to save the JSON file
    json_file_path = f"json_traces/meerkat_CIF_{picture_id}_trace.json"

    # Save the JSON data to a file
    with open(json_file_path, 'w') as json_file:
        json_file.write(json_doc)

    print("JSON data saved to:", json_file_path)
