import re


def get_menu():
    return input("\nТелефонный справочник. Выберите операцию:\n\n"
                   "1. Показать все записи\n"
                   "2. Найти запись\n"
                   "3. Добавить запись\n"
                   "4. Редактировать запись\n"
                   "5. Удалить запись\n"
                   "6. Экспортировать справочник\n"
                   "7. Импортировать\n\n"
                   "0. Закончить работу\n")


# Show records by row_counter if number of records more row_counter
def show_all(all_data, row_counter=10):
    if all_data:
        # print(*all_data, sep="\n")
        records = len(all_data)
        i = 0
        while i < records:
            j = 0
            while j < row_counter and i < records:
                print(all_data[i])
                i += 1
                j += 1
            ans = input('Еще? 1 — да > ').lower()
            if ans != '1':
                break
    else:
        print("В справочнике нет данных")


def get_export_filename():
    while True:
        file_for_export = input('Имя файла для экспорта >')
        only_name = re.match('^[a-zA-Z0-9_-]*', file_for_export).group()
        if len(only_name) == 0:
            print("Такое имя использовать невозможно, используйте английский язык")
        return only_name + '.txt'


def get_import_filename():
    while True:
        file_for_import = input('Имя файла для импорта >')
        only_name = re.match('^[a-zA-Z0-9_-]*', file_for_import).group()
        if len(only_name) == 0:
            print("Такое имя использовать невозможно, файл должен быть назван по-английски")
        return only_name + '.txt'


def exported():
    print('Экспорт завершен')


def imported(count):
    print(f'Импортировано {count} новых записей')


# Search records by any part
def search(lissy, instr):   # find number
    founded = len([x for x in lissy if instr in x])
    if founded > 0:
        print(f'Найдено {founded} записей', end="\n\t")
        print(*[x for x in lissy if instr in x], sep="\n\t")
    else:
        print('Ничего не найдено')


def search_string():
    return input('Введите строку для поиска ? > ')


def get_phone_number():
    numb = False
    while not numb:
        numb = if_phone(input('Введите номер телефона > '))
        if not numb:
            print('\033[31mНеверный номер телефона, используйте формат' 
                  '\n\033[31m +7 123 123-11-11 или 8 123 123-11-11\033[0m\n\033[0m')
    return numb


def get_line(textfield):
    inp = False
    while not inp:
        inp = if_string(input(f'Введите {textfield} > '))
        if not inp:
            print('\033[31mОшибка! Используйте только кириллицу\033[0m')
    return inp.title() + ' '


def if_phone(phone):
    s_temp = "".join(phone.replace("-", "").replace("(", "").replace(")", "").split())
    match = re.search(r'[8][\d]{10}', s_temp)
    if match and len(s_temp) == 11:
        return re.sub(r'^8', '+7', match.string)
    match = re.search(r'[+7][\d]{11}', s_temp)
    if match and len(s_temp) == 12:
        return match.string
    return False


def if_string(stri):
    match = re.search(r"^([А-Я]?[а-я]*[ -]?)*", stri)
    if match:
        if len(match.group()) > 1 and len(stri) > 1:
            return match.string
    return False


def get_id_for_change(max_id, operation):
    loop = True
    operation_ru = 'редактировать' if operation == 'edit' else 'удалять'
    while loop:
        id_for_operation = int(input(f'Что будем {operation_ru}? Введите ID записи >'))-1
        if 0 < id_for_operation < max_id:
            return id_for_operation
        else:
            return False
        print(f'Id = {id_for_operation} нет в справочнике')


def confirm_delete(data_str):
    print(data_str)
    ans = input('Удалить данные? Введите 1 для подтверждения > ').lower()
    if ans == '1':
        return True
    return False


def edited_data(data_str):
    fields_to_edit = data_str.split()
    array = ["id", "firstname", "patrinymic", "lastname"]
    print('-------------------------------  Edit ---------------------------\n'
          'ID\t1. имя\t2. отчество\t3. фамилия\t4. телефон\t\t\033[33m\033[1m5 — сохранить изменения\033[0m 0 — выйти\n',
          data_str, '\n')

    while True:
        field_to_edit = input('Что хотите редактировать? Укажите номер поля > ')

        match field_to_edit:
            case '0':
                return
            case '1' | '2' | '3':
                fields_to_edit[int(field_to_edit)] = get_line(array[int(field_to_edit)])
            case '4':
                fields_to_edit[4] = get_phone_number()
            case '5':
                edited_string = ''
                for x in fields_to_edit:
                    edited_string = edited_string + x.strip() + ' '
                return edited_string.strip()


def no_file_for_import():
    print('\033[31mНет файла для импорта\033[0m')



