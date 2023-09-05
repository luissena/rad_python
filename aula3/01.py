with open("crescente.txt", "w") as arquivo:
    # Escreve os números de 1 a 100 separados por ponto e vírgula
    for numero in range(1, 101):
        arquivo.write(str(numero))
        # Adiciona ponto e vírgula, exceto para o último número
        if numero < 100:
            arquivo.write(";")