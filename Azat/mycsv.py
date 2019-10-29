#!/usr/bin/python

import os
#Here Azat import os module
def read_csv(filename,delimeter:str) -> list:
#As I understood, he wrot function and make it write results as a list
	table = []
#Making an empty list
	if os.path.exists(filename):
#Doing it for writing an error if input file doesn't exist
		with open(filename) as file:
#Open file for reading
			for line in file:
				lst_line = []
#Making list in a loop
				quote = 0
#For not spliting "0,5" in example
				for i in line:
#Treat lines by symbols
					if i == delimeter:
						if quote:
#If we open quote ", we add delimeter symbol, not whitespace  
							lst_line.append(delimeter)
						else:
#Substitute delimeter by spaces
							lst_line.append(' ')

					elif i == '"':
#If he has '"0,5"'
						quote = (quote + 1) % 2
					else:
#If i is not delimeter or quote, he just append it
						lst_line.append(i)
#Join and split by spaces the result string and add result list in 'table' 
				table.append(''.join(lst_line).split())
	else:
		print("Error, such file doesn't exist")

#(From Azat) P.S. I suppose throw of exception instead printing is better approach
	
	return table 




def write_csv(filename,data,delimeter:str):

# What is incorrect call for write_csv?

	with open(filename,'w') as file:
#Opening file for writing
		for row in data:
			file.write(delimeter.join(row)+"\n")
#Joining adelinetor and making split for next row



