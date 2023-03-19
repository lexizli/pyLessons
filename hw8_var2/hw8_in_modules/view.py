import re


def get_value():
    return int(input('Input some Int value > '))

def get_menu():
    return input("\nPhone book. Select operation:\n\n"
                   "1. Show all\n"
                   "2. Search\n"
                   "3. Add a record\n"
                   "4. Edit\n"
                   "5. Delete\n"
                   "6. Export\n"
                   "7. Import\n\n"
                   "0. Exit\n")


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
            ans = input('More? Y — Yes > ').lower()
            if ans != 'y' and ans != 'н':
                break
    else:
        print("No records yet")


def get_export_filename():
    while True:
        file_for_export = input('File name for export >')
        only_name = re.match('^[a-zA-Z0-9_-]*', file_for_export).group()
        if len(only_name) == 0:
            print("Sorry, I can't use this file name")
        return only_name + '.txt'


def exported():
    print('Export done')


# Search records by any part
def search(lissy, instr):   # find number
    founded = len([x for x in lissy if instr in x])
    if founded > 0:
        print(f'Founded {founded}', end="\n\t")
        print(*[x for x in lissy if instr in x], sep="\n\t")
    else:
        print('No records founded')


def search_string():
    return input('What do you search ? > ')


def get_phone_number():
    numb = False
    while not numb:
        numb = if_phone(input('Input phone number > '))
        if not numb:
            print('\033[31mIncorrect value. You can use numbers' 
                  '\n\033[31mlike +7 123 123-11-11 or 8 123 123-11-11\033[0m\n\033[0m')
    return numb


def get_line(textfield):
    inp = False
    while not inp:
        inp = if_string(input(f'Input {textfield} > '))
        if not inp:
            print('\033[31mIncorrect value. You can use only cyrillic characters\033[0m')
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
    while loop:
        id_for_operation = int(input(f'What record to {operation}? Input ID, please >'))-1
        if 0 < id_for_operation < max_id:
            return id_for_operation
        else:
            return False
        print(f'Id = {id_for_operation} is absent in dataset')


def confirm_delete(data_str):
    print(data_str)
    ans = input('Delete this record? Press Y for yes > ').lower()
    if ans == 'y' or ans == 'н':
        return True
    return False


def edited_data(data_str):
    fields_to_edit = data_str.split()
    array = ["id", "firstname", "patrinymic", "lastname"]
    print('-------------------------------  Edit ---------------------------\n'
          'userid\t1. firstname\t2. patrinymic\t3. lastname\t4. phone\t\t\033[33m\033[1m5 — save changes\033[0m 0 — exit\n',
          data_str, '\n')

    while True:
        field_to_edit = input('What field do you edit? Input number of field > ')

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



