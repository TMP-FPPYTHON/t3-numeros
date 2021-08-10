def main():
    #escribe tu código abajo de esta línea
    lista=[4, 3, 7, 2, 9, 10, 15, 1, 6, 7, 2, 1, 20, 5, 8]

    s=0
    for n in lista:
        s += n

    p=s / len(lista)

    print(p)

if __name__=='__main__':
    main()
