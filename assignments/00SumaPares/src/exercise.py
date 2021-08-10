def main():
    #escribe tu código abajo de esta línea
    s=0
    for i in range(2,301):
        if i % 2 == 0:
            s=s+i
    print(s)

if __name__=='__main__':
    main()
