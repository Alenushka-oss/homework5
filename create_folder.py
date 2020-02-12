import func

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