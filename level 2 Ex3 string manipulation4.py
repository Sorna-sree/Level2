#Get user input for dinner one day at a time. 
# If the user enters the same meal as before,
#ask him to enter a different one. Also print all the dinners 
# he had before.

dinnerlist=[]

 
 
for index in range(0,5):
    dinner=input(f"enter the dinner for day{index+1} : ")
    if(dinner in dinnerlist ):
        print(f' you  already had {dinner} for dinner. you had {dinnerlist} so far .Enter diffirent dinner for  day{index+1} ')
        continue
    dinnerlist.append(dinner)

if(len(dinnerlist)<5):
 print("please enter different food for one more time ")


if(len(dinnerlist)==5):
 print(f"you had a {dinnerlist[0]},{dinnerlist[1]},{dinnerlist[2]},{dinnerlist[3]},and {dinnerlist[4]} for dinner last week ")
