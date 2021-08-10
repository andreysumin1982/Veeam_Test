
def hash_files(path_file_hash_sum, path_files_to_check):
    if not os.path.isfile(path_file_hash_sum): # Проверяем на на личие файла с хеш-суммами.
        return print(f'Файл не найден.')
    with open(path_file_hash_sum) as file:
        for name in file.readlines():
            # Читаем файл и в цыкле бужим по строкам.
            file_name = name.strip().split()[0] # имя файла
            hash_file = name.strip().split()[1] # хеш (md5, sha1,.,)
            check_sum = name.strip().split()[2] # контр. сумма
            #
            # Метод algorithms_available создает список всех алгоритмов шифрования
            # Добавляю в словарь  {'хеш' : hashlib.new(i) - Функция new() принимет имя в качестве строки желаемого алгоритма хеширования как первый параметр}
            dict_hash = {i : hashlib.new(i) for i in hashlib.algorithms_available}
            #
            if hash_file in dict_hash:
                h = dict_hash[hash_file]
                #print(h.name)
                if not os.path.isfile(f'{path_files_to_check}/{file_name}'):
                    print(f'{file_name} NOT FOUND')
                    continue
                #
                with open(f'{path_files_to_check}/{file_name}', 'rb') as fil:
                    while True:
                        data = fil.read(1024)
                        if not data:
                            break
                        h.update(data)
                        #print(f'{file_name} - {h.hexdigest()}')
                        if check_sum == h.hexdigest():
                            print(f'{file_name} OK')
                        else:
                            print(f'{file_name} FAIL')
#
if __name__=='__main__':
   #
   #path_file = '/home/asumin/Документы/Программирование_Python/test_files/hashfile.txt'
   #path_file_check = '/home/asumin/Документы/Программирование_Python/test_files'
   #
   #path_file = '/home/asumin/Документы/Программирование Python/files_of_test/hashfile.txt'
   #path_file_check = '/home/asumin/Документы/Программирование Python/files_of_test'
   #
   path_file, path_file_check = input().split()
   hash_files(path_file, path_file_check) # Вызываем ф-цию.
