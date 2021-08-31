from requests import Session
from bs4 import BeautifulSoup as bs
import os

from get_course_page_info import get_course_page_info
from utility_functions import write_txt_file

def get_course_page_content(course_links):

    with Session() as s:

        login_page_url = 'https://v-class.gunadarma.ac.id/login/index.php'
        home_page_url = 'https://v-class.gunadarma.ac.id/my/'
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
        }

        login_page_get_request = s.get(login_page_url, headers=headers)

        login_page_content = bs(login_page_get_request.content, "html.parser")
        token = login_page_content.find("input", {"name":"logintoken"})["value"]
        anchor = login_page_content.find("input", {"name":"anchor"})["value"]

        payload = {
            "username":"your_username",
            "password":"your_password", 
            "logintoken":token,
            "rememberusername":"0",
            "anchor":anchor
        }

        login_page_post_request = s.post(login_page_url, headers=headers, data=payload, cookies= login_page_get_request.cookies)

        for course_link in course_links:

            course_page_get_request = s.get(course_link, headers=headers)

            course_page_content = bs(course_page_get_request.content, "html.parser")

            # buat folder course info bila belum ada
            if(not(os.path.exists(os.getcwd()+f'/course-info'))):
                os.makedirs(os.getcwd()+f'/course-info')

            directory_name = course_page_content.select(".page-header-headings h1")[0].get_text()

            # cek apakah directory_name mengandung karakter '*' atau '/'
            # ini berguna untuk mencegah error pada saat membuat direktori
            if('*' in directory_name or '/' in directory_name):
                directory_name = directory_name.replace('*','').replace('/','').strip()

            directory_name = directory_name.strip().split('|')[2].strip().lower().replace(' ','_') 
            
            course_title = directory_name + '_page.txt'

            directory_path = os.getcwd()+f'/course-info/{directory_name}'
            file_path = os.getcwd()+f'/course-info/{directory_name}/{course_title}'

            # cek apakah direktori tujuan sudah ada atau belum
            if(not(os.path.exists(directory_path))):
                os.makedirs(os.getcwd()+f'/course-info/{directory_name}')

            write_txt_file(file_path,course_page_content.prettify())


            get_course_page_info(course_page_content.prettify())

        s.close()
        