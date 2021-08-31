from bs4 import BeautifulSoup as bs

def get_course_list(home_page_content):
    data = home_page_content

    semester = 'ATA 2020/2021'

    soup = bs(data, "html.parser")

    course_list = []

    for item in soup.select(".unlist li div a"):
        item_link = item['href']
        item_title = item.get_text().strip()
        item_name = item_title.split('|')[2].strip()
        directory_name = item_name.replace('*','').replace('/','').lower().strip().replace(' ','_')
        if(semester in item_title.split('|')[0]):
            dicty = {'item_name':item_name,'item_title':item_title,'item_link':item_link,'directory_name':directory_name}
            course_list.append(dicty)

    index = 1
    course_list = course_list[:26]
    course_list_str = ''
    for item in course_list:
        temp = (f"{index}.\nitem name : {item['item_name']}\nitem link : {item['item_link']}\nitem title : {item['item_title']}\n\n")
        course_list_str = course_list_str + temp
        index = index + 1

    return course_list