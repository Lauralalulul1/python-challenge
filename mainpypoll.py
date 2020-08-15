
#The percentage of votes each candidate won
#The winner of the election based on popular vote.

#create variables - 
candidateList = []
currentCandidate = ""
numberVotes = 0


election_data = ['1','2']

percentVotes =  []
voteCounts = []
maxVotes = voteCounts
maxindex = 0
import os
import csv

#open CSV for read
election_data =  os.path.join("../Resources/" + "netflix_ratings.csv")
import csv
with open('election_data.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
#store the header row
    csv_header = next(csvfile)

#for loop to read through each row #for each row
    for row in csv_reader:

#increase vote for candidate + 1
#The total number of votes cast #totalvotes = totalVotes +1
       numberVotes = numberVotes + 1
    
#if candidateList.index(current row candidate) <1 
#A complete list of candidates who received votes
    if currentCandidate in candidateList:
                currentcandidate_index = candidateList.index(currentCandidate)
                voteCounts[currentCandidate_index] = voteCounts[currentCandidate_index] + 1
    else:
        candidateList.append(currentCandidate)
        voteCounts.append(1)

#find one with most votes ( accumulator? )
#calc and print percentage
#
    for count in range(len(candidateList)):
        votePercent = voteCounts[count]/numberVotes*100
        votePercent.append(votePercent)
        if voteCounts[count] > mostVotes:
            max_votes = voteCounts[count]
            print(mostVotes)
            maxIndex = count
    winner = candidateList[maxindex]
   
    votePercent = [round(i,2) for i in votePercent]
        
        
#print outPut
print("Election Results")
print("-------------------------------")
print(f"Total Votes: ${totalVotes}")
print("-------------------------------")
for count in range(len(candidateList)):
    print(f"{candidateList[count]}: {votePercent[count]}% ({voteCounts[count]})")
print(f"candidateList: ${str(round(votePercent,2))}")
print("-------------------------------")
print(f"Winner: {winner}")
print("-------------------------------")



#Export to text file  https://www.geeksforgeeks.org/reading-writing-text-files-python/
output = open("myOutFile.txt", "w")
line1 = "Election Results"
line2 = "---------------------"
line3 =str(f"Total Votes: {numberVotes}")
line4 = "---------------------"
for count in range(len(candidateList)):
    line = (f"{candidateList[count]}: {votePercent[count]}% ({voteCounts[count]}")
line6 = ("---------------------------------")
line6 = (f"Winner: {winner}")
line7 = ("-------------------------------")
output.writeout('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))