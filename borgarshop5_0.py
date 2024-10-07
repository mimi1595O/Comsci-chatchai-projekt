import pyfiglet
import time

#Initiate
print(pyfiglet.figlet_format("Welcome"))
time.sleep(2)


#dictionary example
checklist = ["0828042646","0865212221","0838290808","191","070910712446","0968497243"] #examples

sizelist = {"Small":1, "Medium":1.5 , "Large":2}

#choose size
print("Please choose burgur size")
for key,value in sizelist.items():
    print(f"\n{key}")
finished = False
while not finished:
    finished = False
    while not finished:
        try:
            num = int(input(f"Enter number (1 - {len(sizelist)})"))
            size = list(sizelist.values())[num-1]
            time.sleep(0.3)
            finished = True
        except(ValueError,IndexError):
            print("Invalid input")



meat = {"pork":80*size, "chicken":60*size , "beef":100*size, "synthesis meat": 500*size}
sauce = {"tomato":10 ,"mayo":10,"mustard":20}
drinks = {"cokee": 20 , "split":20, "redwater":25,"Refill":40}
addition = {"French fries normal":30,"French fries Large":50,"mashed potato":45}
appendinglist = []



#def print
""" def storedisplay(yourlist):
    print("Please choose")
    for key,value in yourlist.items():
        print(f"\n{key} price = {value}") """



def addingredient(dict,appendinglist):
    finished = False
    while not finished:
        try:
            print(chooseingredient(dict))
            num = int(input(f"Enter number (1 - {len(dict)})"))
            choosen = list(dict.keys())[num-1]
            appendinglist.append(dict.get(choosen))
            time.sleep(0.5)
            finished = True
        except(ValueError,IndexError):
            print("Invalid input")
        
        #print(appendinglist)


def chooseingredient(yourdict):
    print("Please choose")
    for key,value in yourdict.items():
        print(f"\n{key} price = {value} THB")
        #appendinglist.append(int(input("enter")))
        #print(appendinglist)
    

def register():
    if(input("Do you want to register? (y/n) : ") == "y"):
        checklist.append(input("enter your phone number : "))
        time.sleep(0.2)
        return True
        
    else:
        return False

def membership():
	#checkmenbership(condition)
	#return discounted_price
    print("Member discount 15% Register now get 10% Discount")
    if(input("Are you a member?(y/n)") == "y"):
        if(input("please enter phone number verification") in checklist):
            discounted_price = 0.85
        else:
            print("you are not a member")
            registered = register()
            if registered:
                discounted_price = 0.90
            else:
                discounted_price = 1
    else:
        registered = register()
        if registered:
            discounted_price = 0.90
        else:
            discounted_price = 1
    return discounted_price






#MAIN
addingredient(meat,appendinglist)
addingredient(sauce,appendinglist)
addingredient(drinks,appendinglist)
addingredient(addition,appendinglist)
discount = membership()
#MAIN



sumprice = sum(appendinglist)
#print(sumprice)
finalprice = (round(sumprice*discount)*1.07)

print(f"\n")

print(f"--------------------------")
print(f"|           Bill         |")
print(f"|       price = {sumprice}  THB     |")
print(f"| you get discount = {100 - discount*100}%|")
print(f"|    Net = {finalprice} THB (VAT7%)|")
print(f"--------------------------")
print(pyfiglet.figlet_format("Thank you"))

#end






#debug >
#for i in range (0,3):
#    print(addingredient(appendinglist))


#< debug