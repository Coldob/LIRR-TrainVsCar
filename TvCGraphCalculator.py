from xml.dom import minidom
import math

mpg = 'unanswered'
cpg = 'unanswered'
distance = 'unanswered'
hStation = 'unanswered'
yTicket = 'unanswered'
daysTaken = 'unanswered'
file = minidom.parse('TrainPrice.xml');
stations = file.getElementsByTagName('station');
y = "equation"
tickets = ['peak', 'offpeak', 'seniorCitDisMed', 'cityticket', 'oneWayAtlantic', 'weeklyAtlantic', 'monthly', 'weekly', 'tenTripPeak', 'offPeakTenTrip', 'tenTripSeniorDisMed', 'twentyTripPeak', 'mil']


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
        y = month*ticketCost(yTicket)
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
    mpg = input("What is your average MPG:")
    try:
        float(mpg)
        print(mpg)
        MPG = float(mpg)
    except ValueError:
        mpg = 'unanswered'
        print("please enter a valid number")
while cpg == 'unanswered':
    cpg = input("How much do you pay per Gallon:")
    try:
        float(cpg)
        print(cpg)
        CPG = float(cpg)
    except ValueError:
        cpg = 'unanswered'
        print("please enter a valid number")
while distance == 'unanswered':
    distance = input("How far is to the city by car in miles:")
    try:
        float(distance)
        print(distance)
        miles = float(distance)
    except ValueError:
        distance = 'unanswered'
        print("please enter a valid number")
while hStation == 'unanswered':
    hStation = input("What is your normal station:")
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
    yTicket = input("What ticket do you normally use:")
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

print("this is the cost per month:$"+tCostPerMonth(1))
print("this is cost for car:$"+cCostPerMonth(1))
print("this is the cost per year:$"+tCostPerMonth(12))
print("this is cost for car:$"+cCostPerMonth(12))
