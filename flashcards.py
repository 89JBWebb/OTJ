#import
import csv
import numpy as np
import random
import webbrowser

#define variables
url = 'https://scryfall.com/card/otj/'

#load csv
with open('Data/grade.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
data_array = np.array(data)

#repeat until user says Q
imp = ""
while imp != "Q":

    #display card
    r = random.randint(1,271)
    webbrowser.open_new_tab(url + str(r))

    #wait until user imput
    imp = input()

    #print answer
    print(data_array[r-1])


