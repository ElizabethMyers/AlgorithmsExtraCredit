#declaring variables
items = []
itemList = []
val = []
wt = []
#opening the file of my items
#each line in the file has the name of the item, my value rating, and its weight
file = open('packingList.txt')
list = file.readlines()
file.close()
for index in list:
    #put first line data in a list of items
    items.append(index.split()[0])
    #put second line data in a list of values
    val.append(int(index.split()[1]))
    #put the third line of data in a list of weights
    wt.append(int(index.split()[2]))
#n is the length of the list of values
n = len(val)

def knapSackDynamProgram(cap, wt, val, n):
    #Knap is the array we will store our results in
    Knap = [[0 for w in range(cap+1)] for i in range(n+1)] 
    #Build the array Knap[][] from the bottom up
    for i in range(n+1):
        for w in range(cap+1):
            if i==0 or w==0:
                Knap[i][w] = 0
            elif wt[i-1] <= w:
                Knap[i][w] = max(val[i-1] + Knap[i-1][w-wt[i-1]],  Knap[i-1][w])                
            else:
                Knap[i][w] = Knap[i-1][w]
    # stores the result of Knapsack 
    res = Knap[n][cap]
    print("The resulting value of the items to pack is: ", res)
    print("Pack the following items:")
      
    w = cap
    for i in range(n, 0, -1): 
        if res <= 0:
            break
        if res == Knap[i - 1][w]:
            #this item was not included in the knapsack, keep checking
            continue
        else: 
            #this item is included in the knapsack
            print(items[i - 1]) 
            #move on to the next item so reset the copied array and weight value
            res = res - val[i - 1] 
            w = w - wt[i - 1]

#asks user for input data and runs the function knapSackDynamProgram 
cap = int(input("Enter the weight capacity of your bag/knapsack in lbs: "))
knapSackDynamProgram(cap, wt, val, n)


