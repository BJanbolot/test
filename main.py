"""
1)	В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.
"""

# with open('test.txt', 'r') as f:
#     text = f.read()
#     print(len(text))
# with open('test.txt', 'r') as f:
#     text = f.readlines()
#     res = []
#     for x in text:
#         t = ''
#         n = ''
#         for y in x:
#             if y.isalpha():
#                 t += y
#             else:
#                 n += y
#         res.append(
#             {''}
#         )
#     print(len(t))    
#     print(len(n))

"""
2)	Спарсить vesti.kg только названия новостей(title) и записать результат в csv файл
"""

# import requests
# from bs4 import BeautifulSoup as bs
# import csv

# BASE_URL = 'https://vesti.kg/itemlist.html?start='
# CSV = 'test.csv'


# def get_html(url):
#     source = requests.get(url).text
#     soup = bs(source, 'lxml')
#     return soup 

# def get_last_page():
#     soup = get_html(BASE_URL)
#     t = soup.find('li', {'class':'pagination-end'}).find('a').get('href')
#     s = ''
#     for x in t:
#         if x.isdigit():
#             s += x
#     return int(s)

# def get_links(url):
#     soup = get_html(url)
#     links = []
#     title = soup.find_all('div', {'class':'itemBody'})
#     for x in title:
#         links.append(
#             {
#                 'title':x.find('a').get_text(strip=True)
#             }
#         )
#     return links


# def get_all_links(url):
#     last_page = get_last_page()
#     all_links = []
#     for x in range(0, 61, 30):
#         links = get_links(url + str(x))
#         all_links += links
#     return all_links


# def save_doc():
#     title = get_all_links(BASE_URL)
#     with open(CSV, 'w') as f:
#         writer = csv.writer(f)
#         writer.writerow(['Название'])
#         for t in title:
#             writer.writerow([t['title']])
# save_doc()




# with open('test.txt', 'r') as f:
#     text = f.read()
#     count_ = 0
#     for x in text:
#         if '\n' in x:
#             count_ += 1
#     print(count_)

# with open('test.txt', 'r') as f:
#     text_line = f.readline()
#     count_text = 0
#     count_symbol = 0
#     for x in text_line:
#         if x.isalpha():
#             count_text += 1
#         else:
#             count_symbol += 1
#     print('text: ', count_text)
#     print('symbol: ', count_symbol)

    # print(text_line)




count_ = 1
with open('test.txt', 'r') as f:
    text = f.read()
    for x in text:
        if '\n' in x:
            count_ += 1
    print(f'количество строк: {count_}')
with open('test.txt', 'r') as f:
    count_text = 0
    count_ = 1
    while True:
        line = f.readline()
        text = []
        symbol = []
        for x in line:
            if x.isalpha():
                text.append(x)
            else:
                symbol.append(x)
        if len(text) == 0 and len(symbol) == 0:
            break
        print(f'строкa {count_}, количество в ней букв: {len(text)}, количество в ней символов: {len(symbol)}')
        count_ += 1

