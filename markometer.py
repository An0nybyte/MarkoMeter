##   MarkoMeter	: 	Student Result Management System
##   Author 	: 	Vedant Khandelwal
##   Version 	: 	1.0
##   Github 	: 	https://github.com/An0nybyte/



def art():#To recall art anywhere in program

    print("███╗░░░███╗░█████╗░██████╗░██╗░░██╗░█████╗░███╗░░░███╗███████╗████████╗███████╗██████╗░")
    print("████╗░████║██╔══██╗██╔══██╗██║░██╔╝██╔══██╗████╗░████║██╔════╝╚══██╔══╝██╔════╝██╔══██╗")
    print("██╔████╔██║███████║██████╔╝█████═╝░██║░░██║██╔████╔██║█████╗░░░░░██║░░░█████╗░░██████╔╝")
    print("██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗░██║░░██║██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══╝░░██╔══██╗")
    print("██║░╚═╝░██║██║░░██║██║░░██║██║░╚██╗╚█████╔╝██║░╚═╝░██║███████╗░░░██║░░░███████╗██║░░██║")
    print("╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝")
    print('\t Author:Vedant Khandelwal')
    
#importing Libraries required
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


art()



def init():#taking input from user
    inp = input("Options:\n1 : Show DataFrame\n2 : View plotted graph\n3 : View bar graph\n4 : View Pie Graph \n5 : Drop a row from DataFrame\n6 : Add Data to Dataframe ")
    if inp=='1':
        show()
    elif inp=='2':
        pot()
    elif inp=='3':
        bar()
    elif inp=='4':
        pie()
    elif inp =='5':
        drop()
    elif inp=='6':
        marks()
    elif inp=='END'or inp=='end':
        print('Closing app')
        input("Press enter to quit...")
        
    else:
        print('Invalid Option chosen, please try again!!!')
        inp()
        
    

def marks():#Taking input for marks
    inp = int(input('How many entries do you want to take?:'))
    x = 0
    while x <=inp:
        p = input('How Much did you get in Physics? : \n')
        c = input('How much did you get in chemistry? : \n')
        m = input('How much did you get in Maths? : \n')
        p = int(p)
        c = int(c)
        m = int(m)
        data = pd.read_csv('C:/Users/khand/Documents/1234.csv')
        data = data.append({'Physics':p,'Chemistry':c,'Maths':m},ignore_index=True)
        data.drop(data.filter(regex="Unnamed:"),axis=1, inplace=True)
        data.to_csv("C:/Users/khand/Documents/1234.csv")
        x = x+1
    init()
    

def bar():#To display Bar Graph
    graph = pd.read_csv('C:/Users/khand/Documents/1234.csv')
    inp = input('Choice: \nPhysics: 1\nChemistry: 2\nMaths: 3')
    if inp=='1':
        a = pd.DataFrame(graph)
        input("Press ENTER to continue to Physics marks")
        a.plot(y='Physics',title="Physics",kind="bar")
        plt.show()
    elif inp=='2':
        a = pd.DataFrame(graph)
        input("Press ENTER to continue to Chemistry marks")
        a.plot(y='Chemistry',title="Chemistry",kind="bar")
        plt.show()
    elif inp=='3':
        input("Press ENTER to continue to Maths marks")
        a.plot(y='Maths',title="Maths",kind="bar")
        plt.show()
    elif inp=='END':
        input("Press ENTER to close")
    else:
        print("Invalid Option entered, Please try again!!!")
        bar()
    init()
    
def pot():#to display a plotted graph
    graph = pd.read_csv('C:/Users/khand/Documents/1234.csv')
    inp = input('Options: \nPhysics: 1\nChemistry: 2\nMaths: 3\nMy Choice:')
    if inp=='1':
        a = pd.DataFrame(graph)
        input("Press ENTER to continue to Physics marks")
        a.plot(y='Physics',title="Physics")
        plt.show()
    elif inp=='2':
        a = pd.DataFrame(graph)
        input("Press ENTER to continue to Chemistry marks")
        a.plot(y='Chemistry',title="Chemistry")
        plt.show()
    elif inp=='3':
        a = pd.DataFrame(graph)
        input("Press ENTER to continue to Maths marks")
        a.plot(y='Maths',title="Maths")
        plt.show()
    elif inp=='END':
        input("Press ENTER to close")
    else:
        print("Invalid Option entered, Please try again!!!")
        pot()
        
    init()

def pie():#To display pie graph
    data = pd.read_csv('C:/Users/khand/Documents/1234.csv')
    print(data)
    data.drop(data.filter(regex="Unnamed:"),axis=1, inplace=True)
    inp = int(input("Plot Graph for? :"))
    Phys = data.loc[inp,'Physics']
    Chem = data.loc[inp,'Chemistry']
    
    math = data.loc[inp,'Maths']
    
    total = Phys.item()+math.item()+Chem.item()
    colours=['blue','red','green','red','yellow','red']
    qlabels = 'Physics','Physics Negative','Maths','Maths Negative','Chemistry','Chemistry Negative'
    print(Phys)
    physneg = 100-Phys
    print(Chem)
    chemneg = 100-Chem
    print(math)
    mathneg = 100-math
    print("\n*50")
    legraph = [Phys,physneg,math,mathneg,Chem,chemneg]
    plt.title("Marks")
    plt.pie(legraph,labels=qlabels,autopct='%1.1f%%',colors=colours)
    
    plt.show()
    print(total)
    init()
    
def drop():#Dropping rows from CSV
    
    data = pd.read_csv('C:/Users/khand/Documents/1234.csv')
    data.drop(data.filter(regex="Unnamed:"),axis=1, inplace=True)
    print(data)
    
    inp = int(input('Enter row number to be cleared'))
    data = data.drop([inp])
    print(data)
    
    data.to_csv("C:/Users/khand/Documents/1234.csv")
    init()
    
def show():#To display CSV as a dataframe
    data = pd.read_csv('C:/Users/khand/Documents/1234.csv')
    data.drop(data.filter(regex="Unnamed:"),axis=1, inplace=True)
    print(data)
    init()
    
init()