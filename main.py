#define variables
total_months = 0
total = 0.00
monthly_change = 0
allmonthlychange = []
previous_month = 0.00

months = []
current_mon_proftloss = 0
net_total_proftloss = 0
ave_change_proftloss = 0
great_incr_proft = {}
great_dec_proft = {}

csv_header = str



#open & read csv file https://docs.python.org/3.3/library/csv.html?csv.html?highlight=csv
import os
import csv
with open('budget_data.csv', newline = '') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")

    #store the header row
    csv_header = next(csvfile)

    #for loop to read through each row
    for row in csv_reader:

    #The total number of months included in the dataset 
        total_months = total_months + 1

    #The net total amount of "Profit/Losses" over the entire period 
    #https://stackoverflow.com/questions/17262256/how-to-read-one-single-line-of-csv-data-in-python
        current_mon_proftloss = int(row[1])
        net_total_proftloss += current_mon_proftloss
    

    #https://www.programiz.com/python-programming/break-continue Loops iterate over a 
    #block of code until the test expression is false, but sometimes we wish to terminate 
    #the current iteration or even the whole loop without checking test expression. Get out of loop if there is
    #a change in profit loss
    
    if total_months ==1:
        previous_month = current_mon_proftloss
    elif total_months  !=1:

        monthly_change = current_mon_proftloss - previous_month
    #put all the months together by using append
        months.append(row[0])
     #add in the changes using append so we can do the averages
        allmonthlychange.append(monthly_change)
    #set previous month to current month again for next loop
    previous_month = current_mon_proftloss

    #calculate average change 
    # https://www.geeksforgeeks.org/round-function-python/
    sum_profit_loss = sum(allmonthlychange)
    ave_change_proftloss = round(sum_profit_loss/(total_months - 1), 2)

#Is CurrentGreater than greatestIncrease? https://careerkarma.com/blog/python-min-and-max/
#The index() method returns the position at the first occurrence of the specified value.
    great_incr_proft = max(allmonthlychange)
    great_dec_proft = min(allmonthlychange)
    great_index = allmonthlychange.index( great_incr_proft)
    least_index = allmonthlychange.index (great_dec_proft)
    highest_month = months[great_index]
    lowest_month = months[least_index]

#write data to text file f is the function of x
print("Financial Analysis")
print("-------------------------------")
print(f"Total: ${str(net_total_proftloss)}")
print(f"Average Change: ${str(round(ave_change_proftloss,2))}")
print(f"Greatest Increase in Profits: {highest_month} (${str(great_incr_proft)})")
print(f"Greatest Decrease in Profits: {lowest_month} (${str(great_dec_proft)})")

#Export to text file  https://www.geeksforgeeks.org/reading-writing-text-files-python/
output = open("myOutFile.txt", "w")
line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(net_total_proftloss)}")
line5 = str(f"Average Change: ${str(round(ave_change_proftloss,2))}")
line6 = str(f"Greatest Increase in Profits: {highest_month} (${str(great_incr_proft)})")
line7 = str(f"Greatest Decrease in Profits: {lowest_month} (${str(great_dec_proft)})")

output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))

