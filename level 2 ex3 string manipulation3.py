#Ask the user what he likes for breakfast. Ask again for dinner. 
#Ask the questions 5 times (one for each weekday).
#Print if the user gave the same input for breakfast and dinner.


breakfast_list=[]
dinner_list=[]
same_food=[]
dates=["monday","Tuesday","Wednesday","Thursday","friday"]
#store the breakfast and dinner for breakfast list and dinner list
for index in range(0,5):
    breakfast=input(f"what he likes for breakfast {dates[index]}: ")
    breakfast_list.append(breakfast)
    dinner=input(f"what he likes for dinner {dates[index]}: ")
    dinner_list.append(dinner) 

print(breakfast_list)
print(dinner_list)

#find the same input for breakfasr and dinner print the same food 
for food in breakfast_list:
    if food in dinner_list:
        same_food.append(food)
print(same_food)
