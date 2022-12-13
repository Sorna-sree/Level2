#Ask the user what he likes for breakfast. Ask the question 5 times (one for each weekday).
#Write one print stmt 'user like <all the inputs, comma separated> for breakfast'. 
#If same breakfast item is mentioned, print it only once.

breakfast_list=[]
uniqueList=[]
duplicateList=[]

for index in range(0,5):
    breakfast=input("what do you like for breakfast  ")
    breakfast_list.append(breakfast)
    
#print(f'user likes {set(breakfast_list)} for breakfast')

#find the same breakfast items and print only once
for food in breakfast_list:
    if food not in uniqueList:
        uniqueList.append(food)
    elif food not in duplicateList:
        duplicateList.append(food)

print("breakfast item is: ",uniqueList)

                
