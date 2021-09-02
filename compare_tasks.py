import os
import json
from utility_functions import write_json_file,read_json_file

def compare_tasks(directory_names):
    for directory_name in directory_names:
        to_do = []
        latest_info_length = 0
        previous_info_length = 0
        latest_info = []

        # mengecek apakah file to_do.json sudah ada atau belum
        # jika sudah assign valuenya ke list to_do
        if(os.path.exists(os.getcwd()+'/to_do.json')):
            to_do = read_json_file(os.getcwd()+'/to_do.json')

        if(len(os.listdir(os.getcwd()+f'/course-info/{directory_name}')) == 4):

            latest_info = read_json_file(os.getcwd()+f'/course-info/{directory_name}/{directory_name}_info_latest.json')
            latest_info_length = len(latest_info)
            
            previous_info = read_json_file(os.getcwd()+f'/course-info/{directory_name}/{directory_name}_info_previous.json')
            previous_info_length = len(previous_info)

            if( latest_info_length > previous_info_length):
                # data yg akan ditambahkan ke to_do
                data_to_be_assigned = latest_info[previous_info_length - latest_info_length:]
                for i in data_to_be_assigned:
                    i['course_name'] = directory_name
                    # jika i belum ada di dalam to_do tambahkan
                    # i ke to_do
                    if(not i in to_do):
                        to_do.append(i)
                
                write_json_file(os.getcwd()+f'/course-info/{directory_name}/{directory_name}_info_latest.json',latest_info)

                write_json_file('to_do.json',to_do)
