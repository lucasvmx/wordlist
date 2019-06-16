'''Gerador de números de telefone aleatórios'''

'''
prefixos:

VIVO 67,71,72,95,96,97,98,99
CLARO 68,73,74,75,76,91,92,93,94
TIM 69,79,80,81,82,83
OI 84,85,86,87,88,89 '''



class NumeroDeTelefone:

    def gerador(self):
        arquivo = open("list.num", 'w')
        nove = 9
        prefixo = int(input("Entre com o prefixo da sua operadora com dois digitos:\n"))

        while prefixo < 10 or prefixo > 99:
            prefixo = int(input("Entre com o prefixo da sua operadora com dois digitos:\n"))


        for (x) in range(0,10000000):
            print ("%d%d%06d"%(nove,prefixo,x))
            arquivo.write("%d%d%06d\n"%(nove,prefixo,x))
        arquivo.close()





numero = NumeroDeTelefone()

numero.gerador()



