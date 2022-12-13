#Ask the user what he likes for breakfast. Ask again for dinner. 
#Ask the questions 5 times (one for each weekday).
#Print if the user gave the same input for breakfast and dinner.


breakfast_list=[]
dinner_list=[]
same_food=[]

#store the breakfast and dinner for breakfast list and dinner list
for index in range(0,5):
    breakfast=input("what he likes for breakfast: ")
    breakfast_list.append(breakfast)
    dinner=input("what he likes for dinner: ")
    dinner_list.append(dinner) 

print(breakfast_list)
print(dinner_list)

#find the same input for breakfasr and dinner print the same food 
for food in breakfast_list:
    if food in dinner_list:
        same_food.append(food)
print(same_food)