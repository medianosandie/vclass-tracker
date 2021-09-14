import requests,os,json,webbrowser
from bs4 import BeautifulSoup as bs

from get_home_page_content import get_home_page_content 
from get_course_list import get_course_list
from show_menu import main_menu
from utility_functions import write_json_file,read_json_file

def main():
    if(not(os.path.exists('course_list.json'))):
        try:
            home_page_content = get_home_page_content()
            course_list = get_course_list(home_page_content)

            write_json_file('course_list.json',course_list)

        except requests.exceptions.ConnectionError:
            print('\n-----------------------------------------------------------------')
            print('pastikan perangkat terhubung dengan koneksi internet\n yang stabil terlebih dahulu!')
            print('-----------------------------------------------------------------\n')
            input('\ntekan tombol manapun untuk keluar')

    course_list = read_json_file('course_list.json')

    item_links = [i['item_link'] for i in course_list]

    main_menu(course_list,item_links) 

main()
