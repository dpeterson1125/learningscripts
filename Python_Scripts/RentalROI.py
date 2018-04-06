#!/usr/bin/python
#This is a calcualtor that will look at rental income for 4 square finance.
#Specifically, given the inputs of the deal, what is the cash on cash return or ROI.
#You will need the following numbers to input.
#Rental Income
#expenses
#down payment
#closing costs
#rehab budget

## import sys imports needed module
import sys


# from tkinter import *

# master = Tk()
# Label(master, text="Please insert your projected rental income").grid(row=0)
# Label(master, text="Please insert your projected monthly on going expenses from all sources").grid(row=1)
# #Label(master, text="Please insert your projected projected closing costs ").grid(row=2)
# #Label(master, text="Please insert your rehab budget").grid(row=3)
# Label(master, text="Please insert your total cost to obtain").grid(row=2)
# Label(master, text="Your ROI is").grid(row=3)


# e1 = Entry(master)
# e2 = Entry(master)
# e3 = Entry(master)
# blank = Entry(master)
# #e5 = Entry(master)

# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# e3.grid(row=2, column=1)
# #e4.grid(row=3, column=1)
# #e5.grid(row=4, column=1)
# blank.grid(row=3, column=1)
# # e1.grid(row=2, column=1)
# # e2.grid(row=3, column=1)



# rental_income = e1
# expenses = e2
# #down_payment = e3
# #sales_price =
# #closing_costs = e3
# #rehab_budget = e4 
# total_cost_obtain = int(e3)


total_investment = total_cost_obtain
mcashflow = int(rental_income) - int(expenses)
acashflow = mcashflow *12

def showroi():
	ROI = float(acashflow) / float(total_investment) *100
	blank.insert(0, ROI)


Button(main, text='Show', command=showroi).grid(row=4, column=1, sticky=W, pady=4)

# rental_income = raw_input('Please insert your projected rental income ')
# expenses = raw_input('Please insert your projected monthly on going expenses from all sources, mortgage, taxes, HOA, Insurance ')

# #down_payment = raw_input('Please insert your down payment ')
# #sales_price = raw_input('Please insert total sales price ')
# #closing_costs = raw_input('Please insert your projected projected closing costs ')
# #rehab_budget = raw_input('Please insert your rehab budget ')
# total_cost_obtain = raw_input('Please insert your total cost to obtain ')


# mcashflow = int(rental_income) - int(expenses)
# acashflow = mcashflow *12

#total_investment = int(down_payment) + int(closing_costs) + int(rehab_budget)

#total_investment = int(total_cost_obtain)
# ROI = float(acashflow) / float(total_investment) *100
# print 'your monthly cashflow is ', mcashflow
# print 'your annual cashflow is ', acashflow
# print 'your total investment is ', total_investment
# print 'your ROI is', ROI, "%"

mainloop( )


