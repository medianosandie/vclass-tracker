from bs4 import BeautifulSoup as bs
import os
import json

from utility_functions import write_json_file,read_json_file,write_txt_file

def get_course_page_info(course_page_content):
    
    data = course_page_content

    soup = bs(data, "html.parser")

    course_items = []

    for item in soup.select(".content"):
        item_name = item.select("a")[0].get_text().strip()
        tasks = []

        # mengisi list tasks
        for i in item.select("a"):
            task_name = i.get_text().strip()
            if('\n' in task_name):
                task_name =  task_name.replace('\n','').split(' ')
                task_name = ' '.join([ i for i in task_name if not i == ''])
            task_link = i['href']
            tasks.append({'task_name':task_name,'task_link':task_link})
        
        course_items.append({'item_name':item_name,'tasks':tasks})

    index = 1
    course_items_str = ''
    for course_item in course_items:
        tasks_str = ''.join([f'\n\t-{i["task_name"]} : {i["task_link"]}' for i in course_item['tasks']])
        course_items_str = course_items_str + (f"{index}.\nitem name : {course_item['item_name']}\ntasks : {tasks_str}\n\n")
        index = index + 1

    directory_name = soup.select(".page-header-headings h1")[0].get_text()

    # cek apakah directory_name mengandung karakter '*' atau '/'
    # ini berguna untuk mencegah error pada saat membuat direktori
    if('*' in directory_name or '/' in directory_name):
        directory_name = directory_name.replace('*','').replace('/','').strip() 

    directory_name = directory_name.strip().split('|')[2].strip().lower().replace(' ','_') 

    file_name_txt = directory_name + '_info.txt'
    file_name_previous_json = directory_name + '_info_previous.json'
    file_name_latest_json = directory_name + '_info_latest.json'

    file_path_txt = os.getcwd()+f'/course-info/{directory_name}/{file_name_txt}'
    file_path_previous_json = os.getcwd()+f'/course-info/{directory_name}/{file_name_previous_json}'
    file_path_latest_json = os.getcwd()+f'/course-info/{directory_name}/{file_name_latest_json}'

    write_txt_file(file_path_txt,course_items_str)

    if(os.path.exists(file_path_latest_json)):

        content_to_be_moved = read_json_file(file_path_latest_json)
        write_json_file(file_path_previous_json,content_to_be_moved)

        write_json_file(file_path_latest_json,course_items)

    else:
        write_json_file(file_path_latest_json,course_items)

    return course_items