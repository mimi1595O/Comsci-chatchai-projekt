
checklist = ["0828042646","0865212221","0838290808","191","070910712446","0968497243"] #examples
borgarsize = [1,1.5,2,3]
meat = {"pork":30, "chicken":25 , "beef":50, "synth": 500}
sauce = {"tomato":5 ,"mayo":5,"mustard":10}
drinks = {"cokee": 20 , "split":17, "redwater":18}



def chooseyourburgur():
    #variables assignment
    Notfinish = True
    addition = []
    total_price = 0
    while(Notfinish):
        
        
        

        #choose size
        
        while True:
            print("choose your burger size(1,2,3,4)") 
            try:
                inputsize = int(input(":"))
                size = borgarsize[inputsize-1]
            except(ValueError,IndexError):
                print("Invalid input")
                continue
            break

                
        
        #Choose sauce
        saucenum = 0 
        while True:
            try:       
                print("choose your sauce")
                for i in sauce:
    	            saucenum = saucenum +1
    	            print(f"\n{i} price = {sauce[i]} press {saucenum}")
                saucetype = int(input(":")) - 1
                choosensauce = list(sauce.keys())[saucetype]
                print(f"you choosed {choosensauce}")
            except(ValueError,IndexError):
                print("invalid input")
                continue
            break
    
        
        while True:
            meatnum = 0
            for i in meat:
    	        meatnum = meatnum +1
    	        print(f"\n{i} price = {meat[i]} press {meatnum}")
            try:
                meattype = int(input(":")) - 1
                choosenmeat = list(meat.keys())[meattype]
                print(f"you choosed {choosenmeat}")
            except(ValueError,IndexError):
                print("Invalid input")
                continue
            break

        topping = {"french fry": 40, "vegetables":20 , "cheese":20}
        for i in topping:
            if(input(f"do you want {i} (y/any keys)").lower() == "y"):
                total_price = total_price + topping[i]
            #print(topping[i])
            #print(total_price)

        

        while True:
            drinknum = 0
            for i in drinks:
    	        drinknum = drinknum +1
    	        print(f"\n{i} price = {drinks[i]} press {drinknum}")
            try:
                drinktype = int(input(":")) - 1
                choosendrinks = list(drinks.keys())[drinktype]
                print(f"you choosed {choosendrinks}")
            except(ValueError,IndexError):
                print("Invalid input")
                continue
            break
                
        Notfinish = False #end


    print(f"your order is {choosensauce} , {choosenmeat} , {choosendrinks}")
    total_price = (total_price + meat.get(choosenmeat) + sauce.get(choosensauce))*size
    return total_price
    


def register():
    if(input("Do you want to register? (y/n) : ") == "y"):
        checklist.append(input("enter your phone number : "))
        return True
        
    else:
        return False



def membership():
	#checkmenbership(condition)
	#return discounted_price
    if(input("Are you a member?(y/n)") == "y"):
        if(input("please enter phone number verification") in checklist):
            discounted_price = 0.95
        else:
            print("you are not a member")
            registered = register()
            if registered:
                discounted_price = 0.95
            else:
                discounted_price = 1
    else:
        registered = register()
        if registered:
            discounted_price = 0.95
        else:
            discounted_price = 1
    return discounted_price



    


price = chooseyourburgur()
print(price)
discount = membership()
print(discount)
sumprice = round(price*discount*1.07) #VAT 7%
print(sumprice)
