'''Gerador de números de telefone aleatórios'''

'''
prefixos:

VIVO 67,71,72,95,96,97,98,99
CLARO 68,73,74,75,76,91,92,93,94
TIM 69,79,80,81,82,83
OI 84,85,86,87,88,89 '''

class NumerosDeTelefone:

    def validar_prefixo(self, num):
        if num < 10 or num > 99:
            return False
        
        return True

    def gerador(self, prefixo):
        
        # Valida o prefixo
        if not self.validar_prefixo(prefixo):
            return False

        arquivo = open("list.dat", 'w')
        nove = 9

        print( "Gerando números ...")

        for (x) in range(0,10000000):
            arquivo.write("%d%02d%06d\n"%(nove,prefixo,x))
        
        print( "Números gerados com sucesso" )

        # Fecha o arquivo
        arquivo.close()

        return True



