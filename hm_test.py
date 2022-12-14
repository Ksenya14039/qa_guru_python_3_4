def name_function(func, *args):
    print('Название функции: ' + func.__name__.title().replace('_', ' '))
    print('Значение аргументов: ', *args)


def open_browser(browser_name):
    name_function(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    name_function(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    name_function(find_registration_button_on_login_page, page_url, button_text)

open_browser(browser_name='Chrome')
go_to_companyname_homepage(page_url='yandex.ru')
find_registration_button_on_login_page(page_url='yandex.ru', button_text='login')