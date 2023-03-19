import view
from os import path, stat
import csv, re

filename = "phones.csv"
last_id = 0
all_data = []


def main_menu():
    play = True

    while play:
        if read_csv_to_list(filename):
            break
        answer = view.get_menu()
        match answer:
            case "1":
                view.show_all(all_data)
            case "2":
                to_find = view.search_string()
                view.search(all_data, to_find)
            case "3":
                add_new_contact()
            case "4":
                to_change = view.get_id_for_change(last_id, 'edit')
                if to_change:
                    edit(to_change)
            case "5":
                delete(view.get_id_for_change(last_id, 'delete'))
            case "6":
                export()
            case "7":
                pass
                # imp()
            case "0":
                play = False
            case _:
                print("Try again!")

        wr_csv(filename)


def add_new_contact():
    global last_id
    global all_data
    array = ["firstname", "patrinymic", "lastname"]
    string = ""
    for i in array:
        string += view.get_line(i).capitalize()

    print(string)
    string += view.get_phone_number()
    print(string)
    string = str(last_id) + ' ' + string + '\n'
    print(string)

    # all_data.append(f"{last_id} {string}\n")
    all_data.append(string)
    last_id += 1


def wr_csv(filename):  # write file
    global all_data
    csvfile = open(filename, 'w', newline='')
    fieldnames = ['userid', 'firstname', 'patrinymic', 'lastname', 'phone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for x in all_data:
        nline = x.split()
        if ' [deleted] [deleted] [deleted] [deleted]' in x or len(x.split()) == 1:
            # nline = x.split()
            writer.writerow(
                {'userid': nline[0],
                 'firstname': '',
                 'patrinymic': '',
                 'lastname': '',
                 'phone': ''})
        else:
            # nline = x.split()
            writer.writerow(
                {'userid': nline[0],
                 'firstname': nline[1],
                 'patrinymic': nline[2],
                 'lastname': nline[3],
                 'phone': nline[4]})
    csvfile.close()


def read_csv_to_list(filename):
    global all_data, last_id
    all_data = []
    if not path.exists(filename):
        # print("No file exists")
        # return -1
        with open(filename, "w", encoding="utf-8") as _:
            pass
    else:
        r_file = open(filename, encoding='utf-8')
        file_reader = csv.DictReader(r_file, delimiter=",")
        if stat(filename).st_size != 0:
            for row in file_reader:
                all_data.append(row['userid'] + ' ' + row['firstname'] + ' '
                                + row['patrinymic'] + ' ' + row['lastname'] + ' ' + row['phone'])
            last_id = int(row['userid'])+1
        r_file.close()


# export all_data to text file
def export():
    global all_data
    filename_to_export = view.get_export_filename()
    if len(all_data) > 0:
        with open(filename_to_export, 'w', encoding='utf-8') as fe:
            fe.write('userid firstname patrinymic lastname phone\n')
            for i in all_data:
                fe.write(i+'\n')
    view.exported()


def delete(id_for_clear):
    really = view.confirm_delete(all_data[id_for_clear])
    if really:
        all_data[id_for_clear] = str(id_for_clear+1) + ' [deleted] [deleted] [deleted] [deleted]'


def edit(id_for_edit):
    really = view.edited_data(all_data[id_for_edit])
    if really:
        all_data[id_for_edit] = really
