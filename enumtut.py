l1 = ["Bhindi","aloo","Chopsticks","chowmein"]
i=1
for item in l1:
   if i%2 != 0:
       print(f"Jarvis Please buy {item}")
   i+=1


#now using enumerate function

for index,item in enumerate(l1):
    if index%2==0:
        print(f"Jarvis please bring {item}")
