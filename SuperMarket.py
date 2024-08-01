# python program for SuperMarket bill generation
from datetime import datetime
name=input("Enter your name :")
print(127*"=")
print(55*" ","WLECOME")
print(127*"=")
items_list='''

    rice            rs 112/kg
    salt            rs 29/-
    oil             rs 120/kg
    tomato          rs 32/kg
    wheat           rs 28/kg
    egg             rs 5/each
    colgate         rs 49/each
    ginger          rs 35/250 grms
    garlic          rs 20/250 grms
    milk            rs 45/liter
    brinjal         rs 40/kg
    biscuit packet  rs 30
    santoor soap    rs 30
    shampoo         rs 100/150 ml
    onions          rs 29/kg
'''
# declaration 
price=0
item_list=[]
price_list=[]
quantity_list=[]
total_price=0
final_price=0
items=[]

list={
    "rice":112,"oil":120,
    "tomato":32,"wheat":28,
    "egg":5,"colgate":49,
    "ginger":35,"garlic":20,
    "milk":45,"brinjal":40,
    "biscuits packet":30,
    "santoor soap":30,
    "shampoo":100,"onions":29,
    "salt":29
      }

option=int(input("Press 1 for showing list of items :"))
if option==1:
    print(items_list)

for i in range(len(list)):
    print("Press 1 for buy products\nPress 2 for EXIT")
    opt=int(input())
    if opt==1:
        item=input("Enter the product to buy : ")
        quantity=int(input("Enter the quantity : "))
        if item in list.keys():
            price+=quantity*(list[item])
            item_list.append(item)
            quantity_list.append(quantity)
            price_list.append(price)
            items.append((i,item,quantity,price))
            total_price+=price
        else:
            print("SORRY Sir/Madam......you entered product is not available")
    elif opt==2:
        break
    else:
        print("SORRY Sir/Madam you entered wrong number")
gst=(total_price*5)/100
if total_price!=0:
    print("Press 1 for printing BILL")
    bill=int(input())
    if bill==1:
        print(127*"*")
        print()
        print(55*"=","SUPER MARKET",60*"=")
        print(55*" ","VIZIANAGARAM")
        print("name : ",name,62*" ","date and time :",datetime.now())
        print(127*"-")
        print(10*" ","S.no",10*" ","Product",10*" ","Quantity",19*" ","price")
        for i in range(len(item_list)):
            print(11*" ",i+1,13*" ",item_list[i],(20-len(item_list[i]))*" ",quantity_list[i],23*" ",price_list[i])
        print(127*"-")
        print()
        print("GST (5%)",69*" ",gst)
        print("Total Price",66*" ",total_price)
        print(127*"-")
        final_price=total_price+gst
        print()
        print("Final Price",66*" ",final_price)
        print(127*"-")
        print(55*" ","Thank You For Visiting")
        print(127*"-")
    else:print("Please enter 1 for billing")
else:
    print(127*"-")
    print(55*" ","Thank You For Visiting")
    print(127*"-")

            
    
