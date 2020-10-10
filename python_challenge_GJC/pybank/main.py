# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:57:17 2020

@author: gjcot
"""

import os
import csv

total_months=0
net_total=0
prev_net=0
rev_incr=0
total_change=0
net_change=0
net_change_list=[]
max_incr=0
max_incr_date=""
min_incr=0
min_incr_date=""
prof_loss=[]
date=[]

csv_path = os.path.join("Resources","budget_data.csv")
with open(csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    first_row=next(csvreader)
    print(f"CSV Header: {first_row}")
    print(type(first_row))
    net_total += int(first_row[1])
    prev_net = int(first_row[1])
    
    for rowreader in csvreader:
        date.append(rowreader[0])
        prof_loss.append(int(rowreader[1]))
        net_total+= int(rowreader[1])
        total_months += 1
        rev_incr=int(rowreader[1])-prev_net
        total_change=total_change+rev_incr
        net_change = int(rowreader[1]) - prev_net
        prev_net=int(rowreader[1])
        net_change_list.append(net_change)
         
        if (int(rowreader[1])>max_incr):
            max_incr=int(net_change)
            max_incr_date= rowreader[0]
        if (int(rowreader[1])<min_incr):
            min_incr=int(net_change)
            min_incr_date= rowreader[0]
  
    total_change= round(sum(net_change_list)/len(net_change_list),2)
  
print(f"{max_incr_date}: {max_incr}")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Net Profit: ${net_total}")
print(f"Average  Change: ${total_change}")
print(f"Greatest Increase in Profits: {max_incr_date} ${str(max_incr)}")
print(f"Greatest Decrease in Profits: {min_incr_date} ${str(min_incr)}")

output_path = os.path.join("gjc_HW3_pybank_results")
with open(output_path,"w") as txtFile:
    print(f"{max_incr_date}: {max_incr}",file=txtFile)
    print("Financial Analysis",file=txtFile)
    print("----------------------------",file=txtFile)
    print(f"Total Months: {total_months}",file=txtFile)
    print(f"Net Profit: ${net_total}",file=txtFile)
    print(f"Average  Change: ${total_change}",file=txtFile)
    print(f"Greatest Increase in Profits: {max_incr_date} ${str(max_incr)}",file=txtFile)
    print(f"Greatest Decrease in Profits: {min_incr_date} ${str(min_incr)}",file=txtFile)
