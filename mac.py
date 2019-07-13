# -*- coding: utf-8 -*-
#
# Gerador de endereços MAC
# Autor: Lucas Vieira de Jesus

class MacAddress:
	
	# Valida o endereço MAC especificado
	def is_valid_mac(self, mac):
		if len(mac) != 17:
			return False

		for item in mac:
			if item != ":":
				try:
					int(item, 16)
				except ValueError:
					return False

		return True

	# Converte um endereço MAC para um número inteiro
	def mac_address_to_number(self, mac):
		mac_string = str(mac)
		numbers = mac_string.split(":")
		number_str = ""

		for item in numbers:
			number_str += item
		
		# Converte a string para um inteiro
		number = int(number_str, 16)

		return number

	# Converte um número inteiro decimal para um endereço MAC no formato XX:XX:XX:XX:XX:XX
	def number_to_mac_address(self, number):
		string = "%02X" % number
		mac_string = ""
		count = 0
		double_dots = 0
		limit = 5
		max_mac_address_length = 281474976710655
		min_mac_address_length = 0
		
		if number < min_mac_address_length or number > max_mac_address_length:
			print( "Error: Invalid decimal number:" )
			return "FF:FF:FF:FF:FF:FF"
		
		# Completa a string com zeros, se necessário
		if len(string) % 2 != 0:
			string += "0"

		for ch in string:
			if count == 2:
				mac_string += ":"
				double_dots = double_dots + 1
				count = 0
			
			# Coloca os caracteres na string
			mac_string += ch
			count = count + 1
		
		# Termina de realizar a formatação
		if double_dots < 5:
			mac_string += ":"
			
			new_limit = limit - double_dots - 1
			
			for count in range(0, new_limit + 1):
				if count == new_limit:
					mac_string += "00"
				else:
					mac_string += "00:"
		
		return mac_string
		
	# Gera endereços mac dentro de um intervalo especificado
	def generate_mac(self, start, end):
		
		# Verifica se o final é menor do que o início
		if start > end:
			print( "Error: start is less than end")
			return 1
			
		for num in range(start, end):
			MAC = self.number_to_mac_address(num)
			print(MAC)
		
if __name__ == "__main__":
	print( 'This script should not run directly')