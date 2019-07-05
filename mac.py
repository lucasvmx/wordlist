# -*- coding: utf-8 -*-

# Gerador de endereços MAC

class MacAddress:
    
    # Converte um número inteiro decimal para um endereço MAC no formato XX:XX:XX:XX:XX:XX
    def number_to_mac_address(self, number):
        string = "%.2X" % number
        mac_string = ""
        count = 0
        remain = 0
        limit = 5

        for ch in string:
            if count == 2:
                mac_string += ":"
                remain = remain + 1
                count = 0
            else:
                mac_string += ch
                count = count + 1

        remain = limit - remain

        if remain < 5:
            for index in range(0, remain + 1):
                if index == remain:
                    mac_string += "00"
                else:
                    mac_string += "00:"

        print(mac_string) 

        return mac_string
        
    #def generate_mac(self, from, to):

