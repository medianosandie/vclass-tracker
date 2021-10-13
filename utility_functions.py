import os,json

def write_json_file(json_file_name,data):
    with open(json_file_name,'w') as wf:
        for line in json.dumps(data,indent=4,sort_keys=True):
            wf.write(line)

def read_json_file(json_file_name):
    with open(json_file_name) as json_file:
        converted_json = json.load(json_file) 
    return converted_json

def write_txt_file(txt_file_name,data):
    with open(txt_file_name,'w') as wf:
        for line in data:
            wf.write(line)
