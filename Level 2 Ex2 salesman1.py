#Calculate the salary for the phone salesman.
# Base pay is Rs10000. 
#Based on the years of experience of the saleman  
#the basepay increses.
#Rs 2000 will be added for each year of experience.
#For every 10 phones sold, he gets 13% of 
# the base pay as commission.

base_pay=10000
experience=2000
salary_calculated=0

discount_calculated=0

print("---------------")
exp=int(input(("how many years experience : ")))
phone=int(input(("how many phones sold: ")))

# year experience base pay calculation 
salary_calculated=int(base_pay+exp*experience)

# 10 phone sold 13% discount calculation
while(phone>=10):
 if(phone>=10):
    discount=int(13/100*base_pay)
    phone-=10
    discount_calculated+=discount


salary=(salary_calculated+discount_calculated)
print("Salary of the phone sales man Rs: ",salary)