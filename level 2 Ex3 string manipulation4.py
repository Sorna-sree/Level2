#Get user input for dinner one day at a time. 
# If the user enters the same meal as before,
#ask him to enter a different one. Also print all the dinners 
# he had before.

dinnerlist=[]

for index in range(0,5):
    dinner=input(f"enter the dinner for day{index+1} : ")
    if(dinner in dinnerlist ):
        print(f' you  already had {dinner} for dinner. you had {dinnerlist} so far .Enter diffirent dinner for  day{index+1} ')
    dinnerlist.append(dinner)
print(f"you had {dinnerlist}  for dinner last week")    
