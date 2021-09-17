import json,os,webbrowser,requests,sys

from get_home_page_content import get_home_page_content 
from get_course_list import get_course_list 
from get_course_page_content import get_course_page_content 
from compare_tasks import compare_tasks
from utility_functions import write_json_file,read_json_file,read_txt_file

def main_menu(data,item_links):
    menus = ['perbarui daftar matakuliah','tampilkan daftar matakuliah','cek halaman matakuliah','tampilkan daftar tugas','cek tugas terbaru','tampilkan daftar tugas terbaru','buka tautan','keluar']
    menus_str = ''.join([(f'\n  {index+1}. {i}') for index,i in enumerate(menus)])
    title = '\n===============vclass-tracker================'.upper()
    print(f'{title}{menus_str}')
    print('==============================================')
    user_input = ''
    try:
        user_input = int(input('masukkan angka dari menu yang ingin dipilih : '))
    except ValueError:
        input_invalid_other_than_number_message()
        main_menu(data,item_links)
        return

    available_input = [i for i in range(1,len(menus)+1)]

    if( not (user_input in available_input) ):
        input_invalid_out_of_range_message(menus)
        main_menu(data,item_links)
        return
    
    else:
        print(f'\nmenu yang dipilih -> "{user_input}. {menus[user_input-1]}"\n')
        
        # handle userinput
        # perbarui daftar matakuliah
        if(user_input == 1):
            try:
                print('menmperbarui daftar matakuliah...')
                
                home_page_content = get_home_page_content()
                course_list = get_course_list(home_page_content)

                # buat file json
                write_json_file('course_list.json',course_list)
                print('\n------------------------------------------------\n')
                print('daftar matakuliah berhasil di perbarui, pilih menu \n"2. tampilkan daftar matakuliah" untuk melihat daftar matakuliah')
                print('\n------------------------------------------------\n')
            
            except requests.exceptions.ConnectionError:
                check_your_connection_message()
            
            main_menu(data,item_links)

        # tampilkan daftar matakuliah
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

        # cek halaman matakuliah
        elif(user_input == 3):
            try:
                print('sedang mengecek...')

                get_course_page_content(item_links)

                print('halaman matakuliah berhasil dicek')

            except requests.exceptions.ConnectionError:
                check_your_connection_message()
            
            main_menu(data,item_links)

        # tampilkan daftar tugas
        elif(user_input == 4):

            if( os.path.exists('course-info') ):
                tasks_menu()
            else:
                print('\n--------------------------------------')
                print('cek halaman matakuliah terlebih dahulu') 
                print('untuk menampilkan daftar tugas, pilih')
                print('"3. cek halaman matakuliah" di menu')
                print('untuk mengecek')
                print('--------------------------------------\n')

            main_menu(data,item_links)

        # cek tugas terbaru
        elif(user_input == 5):
            try:
                print('mengecek tugas terbaru...')

                directory_names = [i['directory_name'] for i in data]
                compare_tasks(directory_names)
                print('\n--------------------------------------------------------------------')
                print('tugas terbaru berhasil dicek, silahkan pilih "6. tampilkan daftar\ntugas terbaru" di menu untuk melihat daftar tugas terbaru')
                print('--------------------------------------------------------------------\n')

            except FileNotFoundError:
                print('\n----------------------------------------------------------------------')
                print('file tidak ditemukan, cek halaman matakuliah terlebih dahulu \nuntuk mengecek tugas terbaru!')
                print('----------------------------------------------------------------------\n')
            
            main_menu(data,item_links)

        # tampilkan daftar tugas terbaru
        elif(user_input == 6):

            to_do = []
            if( os.path.exists('to_do.json') ):
                try:
                    to_do = read_json_file('to_do.json')
                except:
                    pass

                # mengecek apakah to_do tidak kosong
                if(len(to_do)>0):
                    show_to_do(to_do)
                    to_do_menu(data,item_links)

                else:
                    show_empty_to_do_message()
                    main_menu(data,item_links)
                

            else:
                show_empty_to_do_message()
                main_menu(data,item_links)

        # buka tautan
        elif(user_input == 7):

            cwd = os.getcwd()
            url = input('masukkan tautan yg ingin dituju : ')

            python_path = sys.executable.split('\\')
            python_path[len(python_path)-1] = 'Scripts'

            os.chdir('\\'.join(python_path))

            webbrowser.open(url)
            print('membuka tautan...')
            os.chdir(cwd)
            print('\n----------------------')
            print('tautan berhasil dibuka')
            print('----------------------\n')
            main_menu(data,item_links)

        else:
            print('keluar...')
            return

def to_do_menu(data,item_links):
    print('')
    menus = ['hapus tugas','hapus semua tugas','kembali ke main menu']
    menus_str = ''.join([(f'\n  {index+1}. {i}') for index,i in enumerate(menus)])
    title = '========menu daftar tugas terbaru========'.upper()
    print(f'{title}{menus_str}')
    print('=========================================')
    user_input = ''
    try:
        user_input = int(input('masukkan angka dari menu yang ingin dipilih : '))
    except ValueError:
        input_invalid_other_than_number_message()
        to_do_menu(data,item_links)
        return

    available_input = [i for i in range(1,len(menus)+1)]

    if( not (user_input in available_input) ):
        input_invalid_out_of_range_message(menus)
        to_do_menu(data,item_links)
        return
    
    else:
        print(f'\nmenu yang dipilih -> "{user_input}. {menus[user_input-1]}"\n')
        
        to_do = []
        try:
            to_do = read_json_file('to_do.json')
        except:
            pass

        # hapus tugas
        if( user_input == 1 ):
            no_urut_tugas = ''
            try:
                no_urut_tugas = int(input('masukkan nomor urut tugas yang ingin dihapus : '))
            except ValueError:
                input_invalid_other_than_number_message()
                to_do_menu(data,item_links)
                return

            available_input = [ i for i in range(1,len(to_do)+1) ]

            if( not (user_input in available_input) ):
                input_invalid_out_of_range_message(menus)
                to_do_menu(data,item_links)
                return
            
            else:
                try:
                    to_do.pop(no_urut_tugas-1)
                    write_json_file('to_do.json',to_do)

                    print('tugas berhasil dihapus dari daftar tugas terbaru')
                except IndexError:
                    input_invalid_out_of_range_message(to_do)
                    to_do_menu(data,item_links)
                    return
                
                show_to_do(to_do)
                to_do_menu(data,item_links)

        # hapus semua tugas
        if( user_input == 2 ):
            to_do = []
            write_json_file('to_do.json',to_do)

            print('\n--------------------------------------------------------')
            print('seluruh tugas berhasil dihapus dari daftar tugas terbaru')
            print('--------------------------------------------------------\n')
            to_do_menu(data,item_links)
        
        else:
            main_menu(data,item_links)
            return

def show_to_do(to_do):
    for index,i in enumerate(to_do):
        tasks_str = ''.join([f'\t-nama tugas : {el["task_name"]}\n\t-tautan tugas : {el["task_link"]}\n\n' for el in i["tasks"]])
        i_str = f'{index+1}.\nmatakuliah : {i["course_name"].replace("_"," " ).upper()}\njudul tugas : {i["item_name"]}\ntugas : \n{tasks_str}'
        print(i_str)

def show_course_list(course_list):
    print('\n----------------------------------DAFTAR MATAKULIAH----------------------------------\nberikut daftar matakuliah yang diikuti sesuai dengan yang terdapat di website vclass :\n')
    for index,i in enumerate(course_list):
        i_str = f'{index+1}.\nNama Matakuliah : {i["item_name"]}\nTautan Matakuliah : {i["item_link"]}\n'
        print(i_str)

def show_empty_to_do_message():
    print('\n-----------------------------------------------------------')
    print('belum ada tugas terbaru, pilih menu "5. cek tugas terbaru"')
    print('untuk mengecek tugas terbaru')
    print('-----------------------------------------------------------\n')

def show_empty_course_list_message():
    print('\n------------------------')
    print('daftar mata kuliah kosong')
    print('------------------------\n')

def tasks_menu():
    print('')
    course_list  = read_json_file('course_list.json')
    menus = [i["item_name"] for i in course_list]
    menus_str = ''.join([(f'\n  {index+1}. {i}') for index,i in enumerate(menus)])
    title = '\n==========menu daftar tugas=========='.upper()
    print(f'{title}{menus_str}')
    print('==================================\n')
    user_input = ''
    try:
        user_input = int(input('masukkan nomor urut dari matakuliah yg daftar tugas nya ingin ditampilkan : '))
    except ValueError:
        input_invalid_other_than_number_message()
        tasks_menu()
        return

    available_input = [i for i in range(1,len(menus)+1)]

    if( not (user_input in available_input) ):
        input_invalid_out_of_range_message(menus)
        tasks_menu()
        return
    
    else:
        print(f'\nmenu yang dipilih -> "{user_input}. {menus[user_input-1]}"\n')

        show_tasks(user_input)

def show_tasks(index):
    course_list  = read_json_file('course_list.json')
    directory_name = course_list[index-1]["directory_name"]
    txt_file_path = f'course-info/{directory_name}/{directory_name}_info.txt'
    tasks = read_txt_file(txt_file_path)

    item_name = course_list[index-1]["item_name"]
    print(f'----------------------------------\n{item_name.upper()}\n')
    print(tasks)
    print('----------------------------------\n')

def input_invalid_other_than_number_message():
    print('\n-----------------------------------------------')
    print(f'input salah!, tidak menerima input selain angka')
    print('-----------------------------------------------\n')

def input_invalid_out_of_range_message(menus):
    print('\n------------------------------------------------')
    if(len(menus)>1):
        print(f'angka yang boleh dimasukkan hanya angka 1-{len(menus)}!')
    else:
        print(f'angka yang boleh dimasukkan hanya angka 1!')
    print('------------------------------------------------\n')

def check_your_connection_message():
    print('\n-----------------------------------------------------------------')
    print('untuk menjalankan menu ini, pastikan perangkat terhubung dengan\nkoneksi internet yang stabil terlebih dahulu!')
    print('-----------------------------------------------------------------\n')
