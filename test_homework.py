from datetime import time
import datetime


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    if datetime.time(6) < current_time < datetime.time(22):
        is_dark_theme = False
    else:
        is_dark_theme = True

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    if dark_theme_enabled_by_user is True:  # пользователь включил темную тему сам
        is_dark_theme = True
    elif dark_theme_enabled_by_user is None:  # автоматический выбор темы
        if datetime.time(6) < current_time < datetime.time(22):  # автовыбор и время при этом - от 6 утра до 22 вечера
            is_dark_theme = False
        else:  # автовыбор и время при этом - от 22 вечера до 6 утра
            is_dark_theme = True
    else:  # пользователь выключил темную тему
        is_dark_theme = False

    #is_dark_theme = None
    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_users = []
    for olga_user in users:
        if olga_user['name'] == 'Olga':
            suitable_users = olga_user
    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = []
    for pretwenty_user in users:
        if pretwenty_user['age'] < 20:
            suitable_users.append(pretwenty_user)
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]

    # Сделайте функцию, которая будет печатать
    # читаемое имя переданной ей функции и значений аргументов.
    # Вызовите ее внутри функций, описанных ниже
    # Подсказка: Имя функции можно получить с помощью func.__name__
    # Например, вызов следующей функции должен преобразовать имя функции
    # в более читаемый вариант (заменить символ подчеркивания на пробел,
    # сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
    # >>> open_browser(browser_name="Chrome")
    # "Open Browser [Chrome]"


def new_func(func, *args):
    # step1 = func.__name__
    # step2 = step1.replace('_', ' ')    #замена подчеркивания на пробел в имени функции
    # step3 = step2.title()              #каждое слово начинается с заглавной буквы
    part1 = func.__name__.replace('_', ' ').title()
    part2 = ', '.join([*args])
    result = f'{part1} [{part2}]'
    print(result)
    return result

def test_readable_function():
        open_browser(browser_name="Chrome")
        go_to_companyname_homepage(page_url="https://companyname.com")
        find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

def open_browser(browser_name):
    actual_result = new_func(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = new_func(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = new_func(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
