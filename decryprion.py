import pyAesCrypt
import os
import sys

#Функция дешифровки файла
def decryprion(file, password):
    
    # задаем размер буфера
    buffer_size = 512 * 1024
    
    # вызываем метод расшифровки
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )
        
    
    # чтобы видеть результат выводим на печать имя зашифрованый файл
    print("[Файл '" + str(os.path.splitext(file)[0]) + " ' зашифрован]")
    
    # удаляем исходный файл
    os.remove(file)
    
    
# функция сканирования директорий
def walking_by_dirs(dir, password):
    
    #перебираем все поддиректории в указанной директории 
    for name in os.listdir(dir):
        path =  os.path.join(dir, name)
        
        #если находим файл, то дешифруем его
        if os.path.isfile(path):
            try:
                decryprion(path, password)
            except Exception as ex: 
                print(ex)
        # если находим директорию то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)
            
            
password = input("Введите пароль для дешифрования: ")
walking_by_dirs("C:/Users/kaxam/Desktop/project/python/File encryption/test", password)
#os.remove(str(sys.argv[0]))
            
            
