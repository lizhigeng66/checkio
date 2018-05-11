import re


def Strongpass(password):
    flag = [0, 0, 0]
    if len(password) >= 10:
        for i in password:
            if i.isupper():
                flag[0] = 1
            elif i.islower():
                flag[1] = 1
            elif i.isdigit():
                flag[2] = 1
            else:
                return False
        if sum(flag) == 3:
            return True
    else:
        return False


if __name__ == '__main__':
    print(Strongpass('A1213pok'))
    print(Strongpass('bAse730onE4'))
