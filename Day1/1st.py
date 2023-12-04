import os
import pprint
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def sol1(input_file):
    sum = 0
    with open(input_file, 'r') as f:
        for line in f:
            for arr in [[int(letter) if letter.isdigit() else None for letter in line.strip() if letter.isdigit()]]:
                if len(arr) ==1:
                    num = int(str(arr[0]) + str(arr[0]))
                else:
                    num = int(str(arr[0]) + str(arr[-1]))
                sum = sum + num
    print(sum)        
    

sol1('./text.txt')