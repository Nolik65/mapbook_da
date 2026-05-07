from mapbook_lib.model import users

from mapbook_lib.controler import read_users, add_user, remove_user, update_user

from mapbook_lib.
def mail():
    while True:
        print("===========MENU==========")
        print("0 - Zakończ program")
        print("1 - Wyświetl znajomych")
        print("2 - Dodaj znajomego")
        print("3 - Usuń znajomego")
        print("4 - Zaktualizuj znajomego")
        print("5 - Update posta")
        choice = input('Wybierz opcję menu: ')
        print(f'Wybrano opcję {choice}')
        if choice == '0':
            break

        if choice == '1':
            read_users(users)
        if choice == '2':
            add_user(users)
        if choice == '3':
            remove_user(users)
        if choice == '4':
            update_user(users)
        if choice == '5':
            update_user_post(users)

if __name__ == '__main__':
    mail()
