class Item :
    def __init__ (self,name="",price=0,desire=0) :
        self.name = name
        self.price = price
        self.priCal = round(price,-1)//10
        self.desire = desire

import sys
print("Shopping with Limit budgets Calculation :")
try :
    budget = int(input("Enter your budgets : ").strip())
    n = int(input("Enter the amount of items you want : ").strip())
    print("Enter the item's name, price and your weighted desire\n"
        +"The price and weighted desire should be rounded off in integer form\n"
        +"For example: Apple, prices ฿20, my weighted desire = 5\n"
        +"     Input : Apple/20/5")
    print("---------------Item's List---------------")
    item = []
    for i in range(n) :
        apple,p,d = input("#"+str(i+1)+" Item : ").strip().split("/")
        item.append(Item(apple,int(p),int(d)))
except :
    print("Wrong Input, Please run this program again")
    sys.exit()

bg = budget//10
DP = []
for i in range(n+1) :
    DP.append([0 for j in range(bg+1)])
try :
    #Bottom-Up
    for i in range(1,n+1) :
        for j in range(1,bg+1) :
            if item[i-1].priCal <= j :
                DP[i][j] = max(DP[i-1][j], DP[i-1][j-item[i-1].priCal] +item[i-1].desire)
            else :
                DP[i][j] = DP[i-1][j]
except :
    print("Error at Bottom-Up")
    print("At (i,j) = ("+str(i)+","+str(j)+")")
    sys.exit()

try :
    #TraceBack
    i=n ; j=bg
    pay=0 ; ans=[]
    while i!=0 and j!=0 :
        if DP[i][j] == DP[i-1][j-item[i-1].priCal] +item[i-1].desire :
            ans.append(item[i-1])
            pay += item[i-1].price
            j -= item[i-1].priCal
        i -= 1
except :
    print("Error at TraceBack")
    print("At (i,j) = ("+str(i)+","+str(j)+")")
    sys.exit()

print("---------------List of Items you should buy---------------")
for e in ans :
    print(e.name+" : "+str(e.price))
print("---> TOTAL PAYMENT : "+str(pay))
print("-----------------------------------------------------------\n"+
      "THANK YOU FOR USING OUR PROGRAMME")
