import os.path
import matplotlib.pyplot as plt
import numpy as np

def main():
    with open('Параметры.txt', 'r') as f:
        k = f.read()
        k = str(k)
        k = k.split(' ')
        print("Диапазон и шаг выполнения - ", list(map(int,k)))
        D = int(k[0])
        Step= int(k[1])
        x=np.linspace(-D,D,Step)
        y= 4*x+7*x**3
        plt.plot(x, y)
        plt.savefig('График.svg')
        plt.show()
file_path = r'Параметры.txt'
flag = os.path.isfile(file_path)

if flag:
    main()
else:
    print("Файл не найден\n Чтобы создать файл, введите любые два числа")
    a, b = input().split(' ')
    with open('Параметры.txt','w')as f1:
        f1.write(str(a)+" "+str(b))
        f1.close()
        main()
