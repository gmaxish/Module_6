"""
Напишите программу, осуществляющую проверку логина и пароля для входа в систему. Проверка введеных пользователем
данных должна осуществляться в отдельных функциях, принимающих следующие параметры: имя пользователя, пароль,
количество попыток входа в систему (по умолчанию = 3), сообщение, выводимое пользователю в случае, если все попытки
входа в систему исчерпаны (по умолчанию: "Система заблокирована. Повторите попытку черезе 5 минут.")
"""


def check_login(login, trys=2, reminder="Система заблокирована. Повторите попытку черезе 5 минут."):
    while True:
        l = input(login)
        if len(l) >= 5:
            print("Login was set")
            return True
        else:
            print("Login is too short. Try another")
            trys -= 1
        if trys < 0:
            print(reminder)
            break


def check_password(pas, trys=2, reminder="Система заблокирована. Повторите попытку черезе 5 минут."):
    while True:
        p = input(pas)
        if len(p) >= 5:
            print("Password was set")
            return True
        else:
            print("Password is too short. Try another")
            trys -= 1
        if trys < 0:
            print(reminder)
            break


if check_login("Enter your login: ") is True and check_password("Enter your password: ") is True:
    print("OK!")
