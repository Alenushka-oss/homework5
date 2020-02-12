import func

print('*' *45 )
print ('*      Консольный файловый менеджер         *')
print('*' *45)
while True:
    print(' 1 - Создать папку')
    print(' 2 - Удалить (файл/папку)')
    print(' 3 - Копировать (файл/папку)')
    print(' 4 - Просмотр содержимого рабочей папки')
    print(' 5 - Посмотреть только папки')
    print(' 6 - Посмотреть только файлы')
    print(' 7 - Просмотр информации об операционной системе')
    print(' 8 - Создатель программы')
    print(' 9 - Играть в викторину')
    print(' 10 - Мой банковский счет')
    print(' 0 - Выход')

    choice = input('Select menu item:')
    if choice == '1':
        def ui_create_dir():
            print('Создание папки:\n')
            folder_name = input('Введите имя папки:\n>>> ')
            if func.incorrect_name(folder_name, True):
                print('Некорректное имя папки.')
            else:
                check = input(f'Будет создана папка "{folder_name}". Y/N ?\n>>>').lower()
                if check == 'n':
                    return False
                elif check == 'y':
                    err = func.create_dir(folder_name)
                    if err:
                        print(f'Папка "{folder_name}" уже существует.')
                        return True
                    else:
                        print(f'Папка "{folder_name}" успешно создана.')
                        return False
                else:
                    return True
    elif choice == '2':
            def ui_delete():
                print('Удаление папки:\n')
                file_name = input('Введите имя файла/папки:\n>>> ')
               def nf1 = int(input(f'Будет удален "{file_name}". Y/N ?'))
                if nf1 == 'n':
                    return False
                elif nf1 == 'y':
                    err = func.delete(file_name)
                    if err:
                        print(f'"{file_name}" не существует.')
                        return True
                    else:
                        print(f'"{file_name}" успешно удалена.')
                        return False
                else:
                    return True

    elif choice == '3':
         def copy_file():

            source = input('Вводим имя файла для копирования: ')
            copy_file = input('Вводим  имя папки куда копируем: ')
                  if  source == copy_file:
                           print("ПРЕДУПРЕЖДЕНИЕ. Исходное имя папки совпадает с конечным именем. Введите другое имя.")
                  if source != copy_file:
              source = os.path.join(os.getcwd(), source)
              copy_file = os.path.join(os.getcwd(), copy_file)
            if os.path.exists(source):
            if os.path.isfile(source):          # если копируем файл
                    shutil.copy2(source, copy_file)
                    print("скопировали Файл  ")
                elif os.path.isdir(source):         # если директория -> директорию
                    shutil.copytree(source, copy_file)
                    print("скопировали каталог")
             return copy_file

    elif choice == '4':
        def viewing_all_in_folder():#Просмотр содержимого рабочей директории
        content_folder = []
        print("Список директорий и файлов в текущем каталоге (с вложенными файлами/каталогами):")
        for elem in os.walk(os.getcwd()):
            content_folder.append(elem)

        for address, dirs, files in content_folder:
            for folder in folders:
                for file in files:
                    print(f"директория: {os.path.join(address, folder)}, файл: {file}")

    elif choice == '5':
        from only_folder import
            def get_folders_in_working_folder():
                 print("Список папок в рабочей папке:")
                 print("\n".join(list(filter(lambda x: os.path.isdir(x), os.listdir(".")))))
                 print()
    elif choice == '6':
         def get_files_in_working_dir():
              print("Список файлов в рабочей директории:")
              print("\n".join(list(filter(lambda x: os.path.isfile(x), os.listdir(".")))))
              print()
    elif choice == '7':
         def get_info_of_system():
              print()
              print("Информация о системе:")
              ops, name, oper_ver, build, proc, proc_fam = platform.uname()
              print(f"Операционная система: {ops}")
              print(f"Архитектура: {platform.architecture()}")
              print(f"Платформа: {sys.platform}")
              print(f"Версия операционной системы: {oper_ver}")
              print(f"Релиз операционной системы: {build}")
              print(f"Пользователь системы: {name}")
              print()
              print(f"Архитектура процессора: {proc}")
              print(f"Модель процессора: {proc_fam}")
              print()

    elif choice == '8':
              print("Elena")

    elif choice == '9':
         famous_dataset = [
             {'fp': 'А.С.Пушкин',        'df': '06.06.1799', 'dl': '6 июня 1799 г.'},
             {'fp': 'Т. Эдисон',         'df': '11.02.1847', 'dl': '11 февраля 1847 г.'},
             {'fp': 'Н. Тесла',          'df': '10.07.1856', 'dl': '7 июля 1856 г.'},
             {'fp': 'К. Э. Циолковский', 'df': '17.09.1857', 'dl': '28 сентября 1857 г.'},
             {'fp': 'С.П. Королёв',      'df': '12.01.1907', 'dl': '12 января 1907 г.'},
             {'fp': 'Януш Корчак',       'df': '22.07.1878', 'dl': '22 июля 1878 г.'},
             {'fp': 'А. С. Макаренко',   'df': '13.03.1888', 'dl': '13 марта 1888 г.'},
             {'fp': 'М. Шичида',         'df': '08.09.1929', 'dl': '8 сентября 1929 г.'},
             {'fp': 'Л. Костенко',       'df': '19.03.1930', 'dl': '19 марта 1930 г.'},
             {'fp': 'С. М. Фёдоров',     'df': '08.08.1927', 'dl': '8 августа 1927 г.'}
                  ]
         famous_count = 5
         famous_for_test = random.sample(famous_dataset, famous_count)
         correct_answer = 0
         incorrect_answer = 0

         wish_play = True
         some_counts = 0

        while wish_play:
             for fp in famous_for_test:
                 user_answer = input(f'Введите дату рождения человека {fp["fp"]} , в формате "день.месяц.год"')
             if user_answer == fp["df"]:
                 print(random.sample(['Точно!', 'Отлично!', 'Великолепно!', 'Правильно!'], 1)[0])
                 correct_answer += 1
             else:
                print(random.sample(['Не совсем так :(', 'Почти :(', 'Ошибочка :(', 'Мимо :('], 1)[0])
                incorrect_answer += 1
                print(f'Правильный ответ: {fp ["dl"]}')
             print(
                  f'Верно отвечено на {correct_answer / famous_count * 100}% и неверно отвечено на {incorrect_answer / famous_count * 100}% от заданных вопросов.')
            # счетчик попыток
             some_counts += 1
             wish_play = input('Чтобы попытаться еще раз введите "да", для выхода введите что-нибудь другое :D')
        if wish_play == 'да':
            wish_play = True
        else:
             wish_play = False
        print(f'Благодарим за участие в викторине!')

    elif choice == '10':
         from bank_amount:
             print (bill_sum)
             print ()
    elif choice == '0':
         print ("Выход")
   else:
      print('Invalid menu item')
         print('*' * 45)
         print('*' * 45)

        break
   break



