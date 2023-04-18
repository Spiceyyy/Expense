import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
import calendar
from pathlib import Path
from os.path import exists
import os

def ExpenseToList():
    global month_expense
    month_expense = []
    expense = input("Enter month expense ")
    substring = ","
    while substring in expense:
        index = expense.index(substring)
        single_expense = (expense[:index])
        month_expense.append(single_expense)
        expense = expense[index+1:]
        
    sub = ":"
    i=0
    global Grocery_total
    global Fun_total
    global Eating_Out_total
    global Other_total
    global Fun_list
    global Fun_price
    global Eating_Out_list
    global Eating_Out_price
    global Grocery_list
    global Grocery_price
    global Other_list
    global Other_price
    global total
    
    total_price = []
    total = 0
    Grocery_list = []
    Fun_list = []
    Eating_Out_list = []
    Other_list = []
    Grocery_price = []
    Fun_price = []
    Eating_Out_price = []
    Other_price = []

    for i in range(len(month_expense)):
        if month_expense[i].find(sub):
            part = month_expense[i].split(sub)
            type = part[0]
            price = part[1]
            price_number = price.replace("$", "")          
            total_price.append(price_number)
            if str(type).__contains__("Fun"):
                Fun_list.append(type)
                Fun_price.append(price_number)
            elif str(type).__contains__ ("Grocery"):
                Grocery_list.append(type)
                Grocery_price.append(price_number)
            elif str(type).__contains__ ("Food"):
                Eating_Out_list.append(type)
                Eating_Out_price.append(price_number)
            else:
                Other_list.append(type)
                Other_price.append(price_number)
            i+=1
    print(range(len(Eating_Out_list)))

    Grocery_total = sum(list(map(float, Grocery_price)))
    
    Fun_total = sum(list(map(float, Fun_price)))

    Eating_Out_total = sum(list(map(float, Eating_Out_price)))

    Other_total = sum(list(map(float, Other_price)))

    for i in range(len(total_price)):
        total = total + float(total_price[i])
    print("The total expense of the month: %.2f" % total)

def graphs():
    y = np.array([Grocery_total, Fun_total, Eating_Out_total, Other_total])
    mylabels = ["Grocery", "Fun", "Eating Out", "Other"]

    plt.pie(y, labels = mylabels, autopct='%1.1f%%')
    plt.title("Expenses Breakdown of " + month_description)
    plt.show()

def file():
    i = 0
    path = "C:/Users/Kevin/Documents/Visual Studio 2019/Monthly_Expense/" + month_description + str(year) + "Expense.txt"
    if os.path.exists(path) == False:
        expense_file = open(month_description + str(year) + "Expense.txt", "x")
        expense_file = open(month_description + str(year) + "Expense.txt", "a")
        expense_file.write("List of items: \n")
        for i in range(len(Eating_Out_list)):
            expense_file.write( str(Eating_Out_list[i]) + ": " + str(Eating_Out_price[i]) + "\n")
            i=+1          
        expense_file.write("\nEating Out total: " + str(Eating_Out_total) + "\n---------------\n")

        for i in range(len(Grocery_list)):
            expense_file.write( str(Grocery_list[i]) + ": " + str(Grocery_price[i]) + "\n")
            i=+1          
        expense_file.write("\nGrocery total: " + str(Grocery_total) + "\n---------------\n")

        for i in range(len(Fun_list)):
            expense_file.write( str(Fun_list[i]) + ": " + str(Fun_price[i]) + "\n")
            i=+1          
        expense_file.write("\nFun total: " + str(Fun_total) + "\n---------------\n")

        for i in range(len(Other_list)):
            expense_file.write( str(Other_list[i]) + ": " + str(Other_price[i]) + "\n")
            i=+1          
        expense_file.write("\nOther total: " + str(Other_total) + "\n---------------\n")

        expense_file.write("The total expense of " + month_description + " is %.2f" % total + "$")
        expense_file.close()
    else:
        pass

def ThisMonth():
    global month_description
    global year
    today = date.today()
    month = today.month
    year = today.year
    month_description = (calendar.month_name[month])


if __name__ == "__main__":
    ExpenseToList()
    ThisMonth()
    graphs()
    file()
    