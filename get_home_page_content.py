from requests import Session
from bs4 import BeautifulSoup as bs
import os

def get_home_page_content():

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

        home_page_get_request = s.get(home_page_url, headers=headers)

        home_page_content = bs(home_page_get_request.content, "html.parser")

        s.close()

        return home_page_content.prettify()
        