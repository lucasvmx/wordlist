'''Gerador de números de telefone aleatórios'''

'''
prefixos:

VIVO 67,71,72,95,96,97,98,99
CLARO 68,73,74,75,76,91,92,93,94
TIM 69,79,80,81,82,83
OI 84,85,86,87,88,89 '''


class numero:
    def __init__(self):
        self.prefixo = (0)

    def validar_prefixo(self, prefixo):
        if (prefixo > 99 or prefixo < 10):
            return False
        return True

class NumeroDeTelefone:

    def gerador(self):
        arquivo = open("list", 'w')
        nove = 9

        for (x) in range(0,10000000):
            print ("%d%d%06d"%(nove,prefixo,x))
            arquivo.write("%d%d%06d\n"%(nove,prefixo,x))
        arquivo.close()





numero = NumeroDeTelefone()

numero.gerador()



