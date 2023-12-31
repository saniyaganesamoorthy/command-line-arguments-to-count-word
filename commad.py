'''
#Program for getting the word count from the contents of a file using command line arguments
#Developed by: SANIYA G
#RegisterNumber: 212223240147
'''
````
import sys
file=open(sys.argv[1])
data=file.read()
words=data.split()
print("Total Words:",len(words))
python commad.py py.txt
````