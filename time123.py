import time

initial = time.time()


for i in range(45):
    print("this is Nik")

print("For loop ran in",time.time()-initial,"seconds.")

k=0
initial2 = time.time()
while(k<45):
    time.sleep(2)
    print("this is Nik")
    k+=1

print("While loop ran in",time.time()-initial2,"seconds.")

localtime=time.asctime(time.localtime(time.time()))
print(localtime)
