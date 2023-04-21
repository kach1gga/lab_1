import os.path


def main():
    with open('data/app.conf', 'r') as f:
        k = f.read()
        k = str(k)
        k = k.split(' ')
        print("Данные нам числа - ", list(map(int,k)))
        N = int(k[0])
        arr = [0] * N
        for i in range(0, int(k[0])):
            arr[i] = int(k[1]) * i + int(k[2])
        with open('data/vivod.conf','w') as f2:
            f2.write(str(arr))
        print("Вывод программы-",arr)


file_path = r'data/app.conf'
flag = os.path.isfile(file_path)

if flag:
    main()
else:

    print("Файл не найден\n Чтобы создать файл, введите любые три числа")
    a,b,c=input().split(' ')
    k1=a+' '+b+' '+c
    print(k1)
    with open('data/app.conf','w')as f1:
        f1.write(str(k1))
        f1.close()
        main()
