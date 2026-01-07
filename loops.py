# while loop = a statement that will execute its block of code, 
#               as long as its condition remains true

name=None

while not name:
    name = input("Enter your name")
print("Hello "+name)


#for loops 
# for loops- limited
# while loops -unlimited

import time

for second in range (10,0,-1):
    print(second)
    time.sleep(1)
print("Happy New Year !")

for i in range(5):
    for j in range(6):
        print("@",end="")#end use to take output on same line
    print()# print use to  take next line 
    
#Loop control statements = change a loop execution from its normal sequence

#break = used to terminate the loop entirely
#continue = skips to the next iteration of the loop .
#pass= does nothing, acts as aplaceholder

while True:
    name= input("Enter your name :")
    if name != "":
        break
    
phone_number="123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i,end="")    
    
for i in range(1,21):
    if i ==13:
        pass
    else:
        print(i)    
    
    
    
           
    
    



    
  