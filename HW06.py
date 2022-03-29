"""
Напишите программу, осуществляющую проверку логина и пароля для входа в систему. Проверка введеных пользователем
данных должна осуществляться в отдельных функциях, принимающих следующие параметры: имя пользователя, пароль,
количество попыток входа в систему (по умолчанию = 3), сообщение, выводимое пользователю в случае, если все попытки
входа в систему исчерпаны (по умолчанию: "Система заблокирована. Повторите попытку черезе 5 минут.")

"""
login = input("Enter your login: ")
pswd = input("Enter your password: ")


def check_login(t):
    while True:
        if len(t) >= 5:
            print("Login was set")
            return True
        else:
            print("Your login is too short. Try another")