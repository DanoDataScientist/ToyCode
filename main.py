#packages to load/used
import pandas as pd
import random

#read in a parsed version of historical Powerball draws
lottoPB = pd.read_csv('your_path_here/powerBallHx.csv', usecols = ['n1','n2','n3','n4','n5','Powerball'])

#convert dataframe to a nested list so that you can iterate over it for comparision using "set"
listOfDraws = lottoPB.apply(lambda x: x.tolist(), axis=1)

#function to generate a random sample of numbers, without repeat in same sequence
#Generates 5 numbers from 1-69 and one additional number from 1-26 and appends them to "lotteryList" as a list of integers
#flat_list is run to flatten the nested list (output) into a singular list to be used later using "set"
def generate():
    lotteryList = []
    for i in range(1):
        lotteryList.append(random.sample(range(1,70),5))
    for i in range(1):
        lotteryList.append(random.sample(range(1,27),1))
    flat_list = [item for sublist in lotteryList for item in sublist]
    return flat_list

#set number of iterations to run, in the "while i < 15", you can change i < N to whatever number you'd like
#currently set to 15 iterations
i = 0
while i < 15:
    lotteryList = generate()
    for item in listOfDraws:
        result = set(item) == set(lotteryList)
        if result == True:
            lotteryList = generate()
        else:
            break # once it has verified the given new sequence doesn't exist in the previous drawn numbers it breaks this iteration and starts a new one
    print(lotteryList, "new sequence", i+1) #prints N sequences with a numeric counter
    i += 1
