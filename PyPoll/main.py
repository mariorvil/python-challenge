#PyPoll Exercise
#import modules to read a file
import os
import csv


#set the path for for file
csvpath=os.path.join("..","PyPoll","election_data.csv")
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



#create a list to manipulate data



#the headers of columns are Voter ID, County, Candidate




#determine the total number of votes cast



#generate a complete list of candidates who received votes




#determine the percentage of votes each candidate won



#determine the winner of the election based on popular vote







#Final script should both print the analysis to the terminal and export a text file with the results