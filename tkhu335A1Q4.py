"""
Name: Khuth Taiyo
Username: tkhu335
StudentID: 929289904

Calculate and print out the future date
"""


prompt1 = input("Enter today's date (dd/mm/yyyy): ")
prompt2 = int(input("Enter the number of days: "))
index1 = (prompt1.find("/"))
index2 = (prompt1.rfind("/"))
date_input = int(prompt1[:index1])
month_input = int(prompt1[3:index2])
year_input = int(prompt1[index2+1:])
total_days = (date_input+ prompt2)
new_months = (total_days) % 30
futuredate= (total_days) % 30
futuremonth = (month_input + new_months) % 12
futureyear = ((total_days + (month_input * 30)) // 360) + year_input 

print ("In "+str(prompt2)+" days, the date will be "+str(futuredate)+"/"+str(futuremonth)+"/"+str(futureyear))











