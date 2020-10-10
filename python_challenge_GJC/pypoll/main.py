# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:57:35 2020

@author: gjcot
"""

import os
import csv

csv_path = os.path.join("Resources","election_data.csv")
candidate=[]
total_votes=0
candidate_votes={}
winner=""
with open(csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    print(f"CSV Header: {header}")
    print(type(header))
    
    for row_reader in csvreader:
        candidate_name= row_reader[2]
        if candidate_name not in candidate:
            candidate.append(candidate_name)
            candidate_votes[candidate_name]=0
            
        total_votes += 1
        candidate_votes[candidate_name]= candidate_votes[candidate_name] + 1
    
print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------") 

for candidate in candidate_votes:
   votes =candidate_votes.get(candidate)
   percentage= round((votes/total_votes)*100,2)
   print(f"{candidate}: {percentage}% ({votes})")
  
max_votes=0
for votes in candidate_votes:
   if candidate_votes.get(votes)>=max_votes:
       max_votes= candidate_votes.get(votes)
  
print("---------------------------")
print(f"Winner: {max_votes}")
print("---------------------------")

output_path = os.path.join("gjc_HW3_pypoll_results")
with open(output_path,"w") as txtFile:
    print("Election Results",file=txtFile)
    print("---------------------------",file=txtFile)
    print(f"Total Votes: {total_votes}",file=txtFile)
    print("---------------------------",file=txtFile) 

    for candidate in candidate_votes:
        votes =candidate_votes.get(candidate)
        percentage= round((votes/total_votes)*100,2)
        print(f"{candidate}: {percentage}% ({votes})",file=txtFile)
  
    max_votes=0
    for votes in candidate_votes:
        if candidate_votes.get(votes)>=max_votes:
            max_votes= candidate_votes.get(votes)
  
    print("---------------------------",file=txtFile)
    print(f"Winner: {max_votes}",file=txtFile)
    print("---------------------------",file=txtFile)

