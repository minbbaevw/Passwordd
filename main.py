import string, random

def password2():
  with open('pw.txt', 'a') as f:
    f.write(password + "\n")

password1 = int(input("Длина пароля: "))
suum = input("Допускаются символы?(Да/Нет): ")
figures = input("Допускаются цифры?(Да/Нет): ")

syuum = [".", ",", ":", ";", "?", "!", "*", "+", "%", "-", "<", ">", "[", "]", "/", "_", "{", "}",]

first = string.ascii_lowercase
summm = ''.join(suum)
stand = string.ascii_uppercase
digits = string.digits

password = ''

list2 = [first]

if suum == "Да":
  list2.append(summm)
if figures == "Да":
  list2.append(digits)

me = random.sample(''.join(list2), password1)
password += ''.join(me)
print("Сгенерированный пароль: " + password)

txt3 = input("Сохраняем пароль?(Да/Нет): ")

if txt3 == "Да":
  password2()
  print("Пароль сохранен!")
else:
  exit