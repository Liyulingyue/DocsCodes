# created by Liyulingyue

import os

root_dir = '../paddle'

def find_files_in_root(root_dir = root_dir, record_list = None):
    if record_list == None: record_list = []
    for item in os.listdir(root_dir):
        now_path = os.path.join(root_dir,item)
        if os.path.isdir(now_path):
            find_files_in_root(now_path, record_list)
        else:
            # print(now_path)
            find_PADDLE_API(now_path, record_list)
    return record_list

def find_PADDLE_API(file_dir, record_list):
    with open(file_dir,encoding='utf8') as f:
        for line in f.readlines():
            if 'PADDLE_API ' in line:
                record_list.append([line, file_dir])

if 0:
    record_list = find_files_in_root()

    class_count = 0
    API_count = 0
    other = 0
    with open('tmp.txt','w') as f:
        for item in record_list:
            f.write(item[0][:-1]+' '+item[1]+'\n')
            if item[0].startswith('class'): class_count+=1
            elif item[0].startswith('PADDLE_API'): API_count += 1
            else:
                other+=1
                print(item[0])

    print(class_count,API_count,other)

import CppHeaderParser

cppHeader = CppHeaderParser.CppHeader("../paddle/phi/api/include/strings_api.h")

print(cppHeader.includes)

for classname in cppHeader.classes.keys():
    print(classname)

for func in cppHeader.functions:
    print('name: {}'.format(func['name']))
    print('rtnType: {}'.format(func['rtnType']))
    print('parameters: {}'.format(func['parameters']))
    print('')

