#Program 3 – Imperial to Metric Conversion
#Write a console program that converts a weight given in tons (imperial), stones, pounds, and ounces 
# to the metric equivalent in metric tons, kilograms, and grams.

"""
Student Name:   Andrew Beaver
Program Title:  Metric Converter
Description:    Assignment 1 Program 3
"""

def main():

    #Display welcome message
    print("Imperial To Metric Coversion")

    #Prompt user for tons
    userTons = float(input("\nEnter the number of tons: "))

    #Prompt user for stone
    userStone = float(input("Enter the number of stone: "))

    #Prompt user for pounds
    userPounds = float(input("Enter the number of pounds: "))

    #Prompt user for ounces
    userOunces = float(input("Enter the number of ounces: "))

    #Math to get total ounces then convert to total kilos
    totalTons = 35840 * userTons
    totalStone = 224 * userStone
    totalPounds = 16 * userPounds
    
    totalOunces = totalTons + totalStone + totalPounds + userOunces

    totalKilos = totalOunces / 35.274

    #Convert kilos to metric tons, then get the remaining kilos and grams
    metricTons = int(totalKilos/1000)
    remainingKilos = int(totalKilos % 1000)
    remainingGrams = (totalKilos % 1) * 1000

    #Display the metric weight, remaining kilos and remaining grams
    print("The metric weight is {0} metric tons, {1} kilos, and {2:.1f} grams.".format(metricTons,remainingKilos,remainingGrams))

main()