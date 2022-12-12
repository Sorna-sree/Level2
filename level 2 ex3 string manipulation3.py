#Ask the user what he likes for breakfast. Ask again for dinner. 
#Ask the questions 5 times (one for each weekday).
#Print if the user gave the same input for breakfast and dinner.

food_list=[]
uniqueList=[]
duplicateList=[]

#store the breakfast and dinner for food list
for index in range(0,5):
    breakfast=input("what he likes for breakfast: ")
    food_list.append(breakfast)
    dinner=input("what he likes for dinner: ")
    food_list.append(dinner) 

print(food_list)

#find the same input for breakfasr and dinner
for index in food_list:
    if index not in uniqueList:
        uniqueList.append(index)
    elif index not in duplicateList:
        duplicateList.append(index)

print("breakfast and dinner is: ",duplicateList)
