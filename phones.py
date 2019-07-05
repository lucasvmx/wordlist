# -*- coding: utf-8 -*-

# Gerador de números de telefone aleatórios'''
# Autor: Elyakim Klettke Brito

class PhoneNumbers:

    def validar_prefixo(self, num):
        if num < 10 or num > 99:
            return False
        
        return True

    # Gera todos os números de telefone possíveis a partir de um prefixo
    def gerar(self, prefixo):
        
        # Valida o prefixo
        if not self.validar_prefixo(prefixo):
            return False

        arquivo = open("list.dat", 'w')
        nove = 9

        print( "Gerando números ...")

        for (x) in range(0,10000000):
            arquivo.write("%d%d%06d\n"%(nove,prefixo,x))
        
        print( "Números gerados com sucesso" )

        # Fecha o arquivo
        arquivo.close()

        return True



