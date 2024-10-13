import os
import time

print('------\nДомашнее задание по теме "Файлы в операционной системе"\n------')

directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        if file == 'module_7_5.py':
            filepath = os.path.join('.', 'module_7_5.py')
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            parent_dir = os.path.dirname(filepath)
            print(f'Обнаружен файл: {file}\nПуть: {filepath}\nРазмер: {filesize} байт\nВремя изменения: {formatted_time}'
                  f'\nРодительская директория: {parent_dir}')
            break
    break

print('------')