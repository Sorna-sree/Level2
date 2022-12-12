#Calculate the salary for the phone salesman.
# Base pay is Rs10000. 
#Based on the years of experience of the saleman  
#the basepay increses.
#Rs 2000 will be added for each year of experience.
#For every 10 phones sold, he gets 13% of 
# the base pay as commission.
# For eacy day the salesman doesn't go to work,
#subtract Rs200 from the total pay.
#Same as above, but there is a change in the way commission is calculated.
#For the first 10 phones sold, commission is 13%,
#for the next 10 phones sold, it is 15%, 
#and one percent increse for every 5 phones sold after that. 

base_pay=10000
experience=2000
salary_calculated=0

discount_calculated=0

print("---------------")
exp=int(input(("how many years experience : ")))
phone=int(input(("how many phones sold: ")))
leave=int(input("how many days you take a leave: "))

# year experience base pay calculation 
salary_calculated=int(base_pay+exp*experience)

#leave amount calculation
leave_calculated=(salary_calculated-leave*200)


# first 10 phone sold 13% discount calculation
while(phone>=10):
 if(phone>=10):
    discount=int(13/100*base_pay)
    phone-=10
    discount_calculated+=discount
#second 10 phones 15% calculation  
    if(phone>=10):
        discount=int(15/100*base_pay)
        discount_calculated+=discount
        phone-=10
#one percentage increase for every 5 phones sales
    while(phone>=5):
        discount=int(16/100*base_pay)
        discount_calculated+=discount
        phone-=5



salary=(discount_calculated+leave_calculated)
print("Salary of the phone sales man Rs: ",salary)

