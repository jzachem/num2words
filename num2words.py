import sys 

class num_convert: 

	output = "" 

	ones_dict = {"0": "zero", "1":"one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six",
			 "7": "seven", "8": "eight", "9": "nine", "10": "ten", "11": "eleven", "12": "twelve", 
			 "13": "thirteen", "14": "fourteen","15": "fifteen", "16": "sixteen", "17": "seventeen", 
			 "18": "eighteen", "19": "nineteen"}

	tens_dict = {"2": "twenty", "3": "thirty", "4": "fourty", "5": "fifty", "6": "sixty", "7":"seventy",
				"8": "eighty", "9":"ninety"}


	def __init__(self):
		# print("In init")
		return 

	def break_up(self, num):
		# print("In break_into_three_dig")
		hundreds = num % 1000
		thousands = int((num/1000)) % 1000 
		millions = int((num/1000000)) % 1000
		billions = int((num/1000000000)) % 1000
		# print(billions, millions, thousands, hundreds)
		ret = [billions, millions, thousands, hundreds]
		# print (ret)
		return ret

	def handle_billions(self, billions):
		# print("{} billion".format(billions))
		if billions > 0: 
			self.handle_hundreds(billions)
			self.output = self.output + " billion "			
		return

	def handle_millions(self, millions):

		# print("{} million".format(millions))
		if millions > 0: 
			self.handle_hundreds(millions)
			self.output = self.output + " million "
		return 

	def handle_thousands(self, thousands):
		# print("{} thousand".format(thousands))
		if thousands > 0: 
			self.handle_hundreds(thousands)
			self.output = self.output + " thousand "
		return 

	def handle_hundreds(self, hundreds): 
		# print("{} hundred".format(hundreds))
		hunds = int((int(hundreds) / 100))
		tens = int((int(hundreds) % 100))
		# print ("{} hunds".format(hunds))
		# print ("{} tens".format(tens))

		if (hunds > 0 ):
			self.output = self.output + self.ones_dict[str(hunds)] + " " +"hundred "
	
		if int(tens) >= 20: 
			ten = int((int(tens) /10))
			one = (int(tens) % 10)  
			# print ("{} tens".format(ten))
			self.output = self.output + self.tens_dict[str(int(ten))] + " "
			# print ("{} ones".format(one))
			self.handle_ones(one)
		else: 
			self.handle_ones(tens)
		return 

	def handle_ones(self, ones):
		if ones > 0:
			self.output = self.output + self.ones_dict[str(int(ones))]
		return

	def convert(self, orig_num): 
		num = int(orig_num)
		with_commas = ""
		if num != 0: 
			# print("In convert")
			# print("\n")
			# print(num)
			
			num_list = self.break_up(num)
	
			self.handle_billions(num_list[0]) 
			self.handle_millions(num_list[1])
			self.handle_thousands(num_list[2])
			self.handle_hundreds(num_list[3]) 

			for index in range(3): 
				if int(num_list[index]) > 0: 
					with_commas = with_commas + str(num_list[index]) + "," 
			with_commas = with_commas + str(num_list[3]) 
			# print (with_commas)
	
			print ("\n" + with_commas + " is " + self.output + "\n")
		else: 
			print("\n0 is zero\n")			
		return 
		
def main(orig_num): 
	# print("In main")
	# print (2**32 -1)
	if (int(orig_num) <= ((2**32) -1)):
		nc = num_convert()
		nc.convert(orig_num)
	else: 
		print("Numbers larger than a 32 bit unsigned integer ({}) are not supported".format(2**32 -1))
	return 
	

if __name__ == "__main__":
	main(sys.argv[1])