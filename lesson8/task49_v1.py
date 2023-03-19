import re
# # [+][7]\d{7}
# print(re.match('[+][7]\d{9}', "+79995552211"))
# print(re.match('[+][7]\d{9}', "+799dfgh2211"))

#
# pho = "+79995552211"
# print(f'{pho[:2]} {pho[2:5]} {pho[5:8]}-{pho[8:10]}-{pho[10:12]}')
#
# x = '21'
# if ' [deleted] [deleted] [deleted] [deleted]' in x:
#     print('!!!!!!!!!!!')
# nline = len(x.split())
# print(nline)

# pattern = re.compile('^[a-zA-Z0-9_-]*')
# result = pattern.findall('sidelDVA_dva- medvedika .')
# print(result)

# file_for_export = input('File name for export >')
# tess = re.match('^[a-zA-Z0-9_-]*', file_for_export).group()
# if len(tess) == 0:
#     print("Sorry, I can't use this file name")
# print(tess)

# phone = input('Phone number >')
# if






# Пример использования re.search с дополнительными методами
# import re
#
#
# def if_phone(phone):
#     s_temp = "".join(phone.replace("-", "").replace("(", "").replace(")", "").split())
#     match = re.search(r'[8][\d]{10}', s_temp)
#     if match and len(s_temp) == 11:
#         return re.sub(r'^8', '+7', match.string)
#     match = re.search(r'[+7][\d]{11}', s_temp)
#     if match and len(s_temp) == 12:
#         return match.string
#     return False
#
#
def if_string(stri):
    match = re.search(r"^([А-Я]?[а-я]*[ -]?)*", stri)
    if match:
        print(match, match.span(), match.string, match.group(), sep='\n')
        if len(match.group()) > 1 and len(stri) > 1:
            print(match, match.span(), match.string, match.group(), sep='\n')
            return match.string
    return False


# numb = False
# while not numb:
#     numb = if_phone(input('Input correct phone number'
#                           '\nlike\t+7 123 123-11-11'
#                           '\nor\t\t 8 123 123-11-11\n> '))
#     print(numb)


arr = ["firstname", "patrinymic", "lastname"]

inp = False
while not inp:
    inp = if_string(input(f'Input text > '))
    print(inp)





