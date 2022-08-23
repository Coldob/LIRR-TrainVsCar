from xml.dom import minidom
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import numpy as np

mpg = 'unanswered'
cpg = 'unanswered'
distance = 'unanswered'
hStation = 'unanswered'
yTicket = 'unanswered'
daysTaken = 'unanswered'
file = minidom.parse('TrainPrice.xml')
stations = file.getElementsByTagName('station')
y = "equation"
tickets = ['peak', 'offpeak', 'seniorCitDisMed', 'cityticket', 'oneWayAtlantic', 'weeklyAtlantic', 'monthly', 'weekly', 'tenTripPeak', 'offPeakTenTrip', 'tenTripSeniorDisMed', 'twentyTripPeak', 'mil']
xAxis = [1,2,3,4,5,6,7,8,9,10,11,12]
tyAxis = []
cyAxis = []
fig, ax = plt.subplots()

print("Welcome!\n" +
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"+
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"+
"⠀⠀⠀⠀⢀⣀⣠⣤⣤⣤⣤⣼⣷⣿⣿⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"+
"⠀⠀⢠⣾⢟⣭⣝⢿⣿⣿⣿⣿⠟⠩⢒⠂⠀⠀⠀⠤⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"+
"⠀⠀⣸⣸⣯⣻⣿⣾⣿⣿⣿⠏⠀⠈⡉⠙⠄⠀⠐⠉⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"+
"⠀⠀⣿⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈⠛⠁⠀⠀⠀⠿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"+
"⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢀⣠⣤⡤⠒⠺⠛⢄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀\n"+
"⠀⠀⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣍⠁⠀⠤⠤⠤⠂⣹⣿⠀⠀⠀⠀⠀⠀⠀⠀\n"+
"⠀⠀⣿⣧⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣾⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀\n"+
"⠀⢀⣿⣿⣿⣿⡇⣽⡿⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀\n"+
"⢀⣸⣿⣿⣿⠉⠑⠛⠀⠄⠀⠙⠛⢿⣿⡿⠿⢿⠿⢿⣿⠛⠛⠛⢠⠀⠀⠀⠀⠀\n"+
"⣿⣿⣿⣿⣿⡄⠀⣀⣀⣀⣀⣀⣀⣈⣿⣆⣀⣸⣀⣘⣿⣀⣀⣀⣸⣀⣀⣀⡀⠀\n"+
"⠛⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀\n"+
"⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠛⠛⠛⠛⠀\n"+
"⠀⠀⠀⢿⣿⣿⣿⣿⣿⡟⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀\n"+
"not my ascii cred to amazing artist\n"+
"-----------------------------------------------------------------")

def findStation(station):
    i = 0
    for i in range(125):
        X = stations[i].attributes['id'].value
        if station == X:
            return(i)
        else:
            i = i+1
    return("not found")

def ticketCost(tickettype):
    inlist = str(tickets.index(tickettype))
    if inlist.isnumeric():
        if tickettype == 'mil':
            return(stations[i].getElementsByTagName('offpeak')[0].firstChild.nodeValue)
        return(stations[i].getElementsByTagName(tickettype)[0].firstChild.nodeValue)

def tCostPerMonth(month):
    if yTicket == 'monthly':
        y = month*cTicket
        sCost = str(y)
        return(sCost)
    if yTicket == 'peak':
        z = daysTaken*cTicket
        y = month*z*2
        sCost = str(y)
        return(sCost)
    if yTicket == 'offpeak':
        z = daysTaken*cTicket
        y = month*z*2
        sCost = str(y)
        return(sCost)
    if yTicket == 'seniorCitDisMed':
        z = daysTaken*cTicket
        y = month*z*2
        sCost = str(y)
        return(sCost)
    if yTicket == 'cityticket':
        z = daysTaken*cTicket
        y = month*z
        sCost = str(y)
        return(sCost)
        #not sure n/a for seaford
    if yTicket == 'oneWayAtlantic':
        z = daysTaken*cTicket
        y = month*z
        sCost = str(y)
        return(sCost)
        #not sure n/a for seaford
    if yTicket == 'weeklyAtlantic':
        z = daysTaken*cTicket
        y = month*z
        sCost = str(y)
        return(sCost)
        #not sure n/a for seaford
    if yTicket == 'weekly':
        z = math.ceil(daysTaken/7)
        V = z* cTicket
        y = month*V
        sCost = str(y)
        return(sCost)
        #assumes all are taken within same week
    if yTicket == 'tenTripPeak':
        z = math.ceil(daysTaken/10)
        V = z* cTicket
        y = month*V
        sCost = str(y)
        return(sCost)
    if yTicket == 'offPeakTenTrip':
        z = math.ceil(daysTaken/10)
        V = z* cTicket
        y = month*V
        sCost = str(y)
        return(sCost)
    if yTicket == 'tenTripSeniorDisMed':
        z = math.ceil(daysTaken/10)
        V = z* cTicket
        y = month*V
        sCost = str(y)
        return(sCost)
    if yTicket == 'twentyTripPeak':
        z = math.ceil(daysTaken/20)
        V = z* cTicket
        y = month*V
        sCost = str(y)
        return(sCost)
    if yTicket == 'mil':
        z = daysTaken*cTicket
        y = month*z
        sCost = str(y)
        return(sCost)

def cCostPerMonth(month):
    roundtrip = miles*2
    milesPerMonth = roundtrip*daysTaken
    gallonsNeeded = milesPerMonth/MPG
    totalCost = gallonsNeeded * CPG * month
    printed = str(totalCost)
    return(printed)

#maybe correct center to centre
while mpg == 'unanswered':
    mpg = input("What is your cars average city MPG:")
    try:
        float(mpg)
        print(mpg)
        MPG = float(mpg)
    except ValueError:
        mpg = 'unanswered'
        print("please enter a valid number")
while cpg == 'unanswered':
    cpg = input("How much do you typically pay per Gallon:")
    try:
        float(cpg)
        print(cpg)
        CPG = float(cpg)
    except ValueError:
        cpg = 'unanswered'
        print("please enter a valid number")
while distance == 'unanswered':
    distance = input("How far is it to drive by car to manhattan in miles:")
    try:
        float(distance)
        print(distance)
        miles = float(distance)
    except ValueError:
        distance = 'unanswered'
        print("please enter a valid number")
while hStation == 'unanswered':
    hStation = input("What station are you using:")
    hStation = hStation.lower()
    if " " in hStation:
        print("spaces")
        hStation = hStation.replace(" ", "")
    if "-" in hStation:
        hStation = hStation.replace("-","")
        print("dashes")
    if "not found" == findStation(hStation):
        hStation = 'unanswered'
        print("please answer a valid station")
    else:
        i = findStation(hStation)
        print(hStation)
while yTicket == 'unanswered':
    yTicket = input("What ticket do you normally use (press enter for spelling and options):")
    try:
        inlist = str(tickets.index(yTicket))
        print(ticketCost(yTicket))
        cTicket = float(ticketCost(yTicket))
    except ValueError:
        yTicket = 'unanswered'
        print("valid tickets include: peak, offpeak, seniorCitDisMed, cityticket, oneWayAtlantic, weeklyAtlantic, monthly, weekly, tenTripPeak, offPeakTenTrip, tenTripSeniorDisMed, twentyTripPeak, mil")
while daysTaken == 'unanswered':
    daysTaken = input("How many days do you normally commute per month:")
    if not daysTaken.isnumeric():
        daysTaken = 'unanswered'
        print("please enter a valid number of whole days")
    else:
        daysTaken = int(daysTaken)
        print(daysTaken)

print("this is the cost per month for the train:$"+tCostPerMonth(1))
print("this is cost per month for driving:$"+cCostPerMonth(1))
print("this is the cost per year for the train:$"+tCostPerMonth(12))
print("this is cost per year for driving:$"+cCostPerMonth(12))

if float(tCostPerMonth(12)) > float(cCostPerMonth(12)):
    toplimit = float(tCostPerMonth(12)) + 50
    plt.ylim(0,toplimit)
    print("train")
else:
    toplimit = float(cCostPerMonth(12)) + 50
    plt.ylim(0,toplimit)
    print("car")

def yaxis(vehicle):
    x=0
    if vehicle == "train":
        for x in range(12):
            result = float(tCostPerMonth(x))
            tyAxis.append(result)
    else:
        for x in range(12):
            result = float(cCostPerMonth(x))
            cyAxis.append(result)
yaxis("train")
yaxis("car")

print(cyAxis)
print(tyAxis)

plt.step(xAxis, tyAxis, label='Train')
plt.step(xAxis, cyAxis, label='Car')

ax.legend(loc='lower right')

plt.xlim(1,12)

plt.xticks(np.arange(1, 12, 1))
plt.yticks(np.arange(0, toplimit, 300.00))

ax.yaxis.set_minor_locator(MultipleLocator(100.00))

ax.grid(True, linestyle='-.')

plt.xlabel('Month')
plt.ylabel('Cost in USD')

ax.yaxis.set_major_formatter('${x:1.2f}')

plt.title('The estimated cost to drive to Manhattan compared to taking the LIRR to Pennstation (*not including parking*)')
plt.show()
