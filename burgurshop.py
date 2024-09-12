checklist = ["0828042646","0865212221","0838290808","191","070910712446","0968497243"]
borgarsize = [1,1.5,2,3]
meat = {"pork":30, "chicken":25 , "beef":50, "synth": 500}
sauce = {"tomato":5 ,"mayo":5,"mustard":10}


drinks = {"cokee": 20 , "split":17, "redwater":18}



def chooseyourburgur():
    addition = []
    total_price = 0
    saucenum = 0
    print("choose your burger size(1,2,3,4)") 
    inputsize = input(":")
    #print(size)
    size = borgarsize[inputsize-1]
    print("choose your sauce")

	
    for i in sauce:
    	saucenum = saucenum +1
    	print(f"\n{i} price = {sauce[i]} press {saucenum}")
    saucetype = int(input(":")) - 1
    choosensauce = list(sauce.keys())[saucetype]
    print(f"you choosed {choosensauce}")
    
    
    meatnum = 0
    for i in meat:
    	meatnum = meatnum +1
    	print(f"\n{i} price = {meat[i]} press {meatnum}")
    meattype = int(input(":")) - 1
    choosenmeat = list(meat.keys())[saucetype]
    print(f"you choosed {choosenmeat}")

    topping = {"french fry": 40, "vegetables":20 , "cheese":20}
    for i in topping:
        if(input(f"do you want {i}").lower() == "y"):
            total_price = total_price + topping[i]
            #print(topping[i])
            #print(total_price)

		

	
    drinknum = 0
    for i in drinks:
    	drinknum = drinknum +1
    	print(f"\n{i} price = {drinks[i]} press {drinknum}")
    drinktype = int(input(":")) - 1
    choosendrinks = list(drinks.keys())[drinktype]
    print(f"you choosed {choosendrinks}")



    print(f"your order is {choosensauce} , {choosenmeat} , {choosendrinks}")
    total_price = (total_price + meat.get(choosenmeat) + sauce.get(choosensauce))*size
    return total_price




price = chooseyourburgur()
print(price)
