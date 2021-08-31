import json
import os
import webbrowser

from get_home_page_content import get_home_page_content 
from get_course_list import get_course_list 
from get_course_page_content import get_course_page_content 
from compare_tasks import compare_tasks
from utility_functions import write_json_file,read_json_file

def main_menu(data,item_links):
    menus = ['update course list','show course list','track courses','compare tasks','show to-do','open-link','exit']
    menus_str = ''.join([(f'\n  {index+1}. {i}') for index,i in enumerate(menus)])
    title = '==========vclass-tracker=========='.upper()
    print(f'{title}{menus_str}')
    print('==================================')
    user_input = ''
    try:
        user_input = int(input('masukkan angka : '))
    except ValueError:
        print(f'input salah!, tidak menerima input selain angka\n')
        main_menu(data,item_links)
        return

    available_input = [i for i in range(1,len(menus)+1)]

    if( not (user_input in available_input) ):
        print(f'angka yang boleh dimasukkan hanya 1-{len(menus)} !\n')
        main_menu(data,item_links)
        return
    
    else:
        print(f'selected menu -> "{user_input}. {menus[user_input-1]}"')
        
        # handle userinput
        # update courses
        if(user_input == 1):
            print('updating courses...')
            
            home_page_content = get_home_page_content()
            course_list = get_course_list(home_page_content)

            # buat file json
            write_json_file('course_list.json',course_list)

            print('courses berhasil di update')
            main_menu(data,item_links)

        # show course list
        elif(user_input == 2):
            if(os.path.exists('course_list.json')):
                course_list = read_json_file('course_list.json')

                if(len(course_list)>0):
                    show_course_list(course_list)
                else:
                    show_empty_course_list_message()

            else:
                show_empty_course_list_message()
            
            main_menu(data,item_links)

        # track courses
        elif(user_input == 3):
            print('tracking...')

            get_course_page_content(item_links)

            print('courses berhasil di track')
            main_menu(data,item_links)

        # compare tasks
        elif(user_input == 4):
            print('comparing tasks...')

            directory_names = [i['directory_name'] for i in data]
            compare_tasks(directory_names)
            print('tasks berhasil di compare')
            print('tasks berhasil di compare, silahkan pilih "4. show to-do" di menu\nuntuk mengecek task terbaru\n')
            main_menu(data,item_links)

        # show to-do
        elif(user_input == 5):

            to_do = []
            if( os.path.exists('to_do.json') ):
                # with open('to_do.json') as json_file:
                #     to_do = json.load(json_file)
                to_do = read_json_file('to_do.json')

                # mengecek apakah to_do tidak kosong
                if(len(to_do)>0):
                    show_to_do(to_do)
                else:
                    show_empty_to_do_message()

            else:
                show_empty_to_do_message()

            to_do_menu(data,item_links)

        # buka link
        elif(user_input == 6):

            cwd = os.getcwd()
            url = input('masukkan url yg ingin dituju : ')

            os.chdir("C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python37\\Scripts")

            webbrowser.open(url)
            print('opening url...')
            os.chdir(cwd)
            main_menu(data,item_links)

        else:
            print('exitting program...')
            return

def to_do_menu(data,item_links):
    print('')
    menus = ['hapus task','hapus semua task','kembali ke main menu']
    menus_str = ''.join([(f'\n  {index+1}. {i}') for index,i in enumerate(menus)])
    title = '==========to do menu=========='.upper()
    print(f'{title}{menus_str}')
    print('==================================')
    user_input = ''
    try:
        user_input = int(input('masukkan angka : '))
    except ValueError:
        print(f'input salah!, tidak menerima input selain angka\n')
        to_do_menu(data,item_links)
        return

    available_input = [i for i in range(1,len(menus)+1)]

    if( not (user_input in available_input) ):
        print(f'angka yang boleh dimasukkan hanya 1-{len(menus)} !\n')
        to_do_menu(data,item_links)
        return
    
    else:
        print(f'selected menu -> "{user_input}. {menus[user_input-1]}"')

        to_do = []
        # with open('to_do.json') as json_file:
        #     to_do = json.load(json_file)
        to_do = read_json_file('to_do.json')

        # hapus task
        if( user_input == 1 ):
            no_urut_task = ''
            try:
                no_urut_task = int(input('masukkan nomor urut task yang ingin dihapus : '))
            except ValueError:
                print(f'input salah!, tidak menerima input selain angka\n')
                to_do_menu(data,item_links)
                return

            available_input = [ i for i in range(1,len(to_do)+1) ]
            print(available_input)

            if( not (user_input in available_input) ):
                print(f'angka yang boleh dimasukkan hanya 1-{len(menus)} !\n')
                to_do_menu(data,item_links)
                return
            
            else:
                to_do.pop(no_urut_task-1)
                # with open('to_do.json','w') as wf:
                #     for line in json.dumps(to_do,indent=4,sort_keys=True):
                #         wf.write(line)
                write_json_file('to_do.json',to_do)

                print('task berhasil dihapus')
                show_to_do(to_do)
                to_do_menu(data,item_links)

        # hapus semua task
        if( user_input == 2 ):
            to_do = []
            # with open('to_do.json','w') as wf:
            #         for line in json.dumps(to_do,indent=4,sort_keys=True):
            #             wf.write(line)
            write_json_file('to_do.json',to_do)

            print('-----------------------------')
            print('seluruh task berhasil dihapus')
            print('-----------------------------')
            to_do_menu(data,item_links)
        
        else:
            main_menu(data,item_links)
            return

def show_to_do(to_do):
    for index,i in enumerate(to_do):
        tasks_str = ''.join([f'\t-Task Name : {el["task_name"]}\n\t-Task Link : {el["task_link"]}\n\n' for el in i["tasks"]])
        i_str = f'{index+1}.\ncourse name : {i["course_name"]}\nitem name : {i["item_name"]}\ntasks : \n{tasks_str}'
        print(i_str)

def show_course_list(course_list):
    for index,i in enumerate(course_list):
        i_str = f'{index+1}.\nItem Title : {i["item_title"]}\nItem Name : {i["item_name"]}\nItem Link : {i["item_link"]}\nDirectory Name : {i["directory_name"]}\n'
        print(i_str)

def show_empty_to_do_message():
    print('-------------------')
    print('belum ada task baru')
    print('-------------------')

def show_empty_course_list_message():
    print('------------------')
    print('course list kosong')
    print('------------------')
