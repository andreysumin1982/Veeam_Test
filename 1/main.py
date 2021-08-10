#-------------------------------------------------------------------------
def copyFile(path):
    try:
        root = ET.parse(path).getroot()
    except:
        return print(f'Не могу найти XML.\n"{path}"')
    try:
        for atr in root:
            source_path = atr.attrib['source_path']
            destination_path = atr.attrib['destination_path']
            file_name = atr.attrib['file_name']
            #
            if sys.platform == 'linux':
                shutil.copy(f'{source_path}/{file_name}', f'{destination_path}')
                print(f'Файл {file_name} скопирован.')
            elif sys.platform == 'windows':
                shutil.copy(f'{source_path}\\{file_name}', f'{destination_path}')
                print(f'Файл {file_name} скопирован.')
    except:
        if os.path.isdir(source_path) == False:
            return print(f'Папка {source_path} не существует. Укажите правильный путь.')
        elif FileNotFoundError:
            return print(f'Файл {file_name} не найден.')

#
if __name__ == '__main__':
    #path_file_xml = '/home/asumin/Документы/Программирование Python/files_of_test/files.xml'
    path_file_xml = '/home/asumin/Документы/Программирование Python/test_files/files.xml'
    copyFile(path_file_xml)
#--------------------------------------------------------------------
