#Ask the user what he likes for breakfast. Ask the question 5 times (one for each weekday).
#Write one print stmt 'user like <all the inputs, comma separated> for breakfast'. 
#If same breakfast item is mentioned, print it only once.

breakfast_list=[]
for index in range(0,5):
    breakfast=input("what he likes for breakfast: ")
    breakfast_list.append(breakfast)
    
print(f'user likes {set(breakfast_list)} for breakfast')
