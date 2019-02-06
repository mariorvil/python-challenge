#import modules to read a file
import os
import csv



#Define the function and have it accept the "budgetdata" as its sole parameter
def calculate (budgetdata):

#Total number of months included in data set > need to sum/count rows from 2-87 column A

total_months = 

#Net total amount of "Profit/Losses" over entire period > need to sum all numbers from rows 2-87, column B

net_total=

#Average of the changes in "Profit/Losses" over entire period > total amount of profit/lossess divided by total number of months(86)

average_change= 

#The Greatest increase in profits (date and amount) over entire period

greatest_increase=


#The Greatest decrease in profits (date and amount) over entire period

greatest_decrease= 

#print out the analysis to the terminal and export it as text file with results

    print ("Financial Analysis")

    print (f"Total Months:{str(total_months)}")

    print (f"Total:{str(net_total)}")

    print (f"Average change:{str(average_change)}")

    print (f"Greatest increase profits:{str(greatest_increase)}")

    print (f"Greatest decrease profits:{str(greatest_increase)}")


#set the path for for file
csvpath=os.path.join("..","PyBank","budget_data.csv")
#open the file
with open (csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter+',')
    print (csvreader)

#read the header row first
csvreader=next(csvreader)
    print(f"CSV Header:{csv_header}")

    #read each row of data after the header

    for row in csvreader:
        print (row)

        