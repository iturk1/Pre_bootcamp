#1 Print all integers from 0 to 150
for x in range(0, 151,1):
    print(x)
    
    
    
#2 Print all the multiples of 5 from 5 to 1,000
for x in range(5,1001):
    x*=5
    print(x)  
    
    
#3 Print integers 1 to 100. If divisible by 5, print "Coding" instead.
#If divisible by 10, print "Coding Dojo".
for x in range(1,100+1):
    if x % 5 == 0:
        print("Coding")
    if x % 10 == 0:
        print("Coing Dojo")
        
        
#4 Add odd integers from 0 to 500,000, and print the final sum.
sum =0
for x in range(500_000+1):
    if(x % 2 !=0): 
        sum+=x   
print(sum)  


#5 Print positive numbers starting at 2018, counting down by fours.
for x in range(2018,0,-4):
    if x % 2 ==0:
        print(x)
        
#6 Print only the integers that are a multiple of mult
lowNum = int(input("Statring at: "))
highNum = int(input("Ending the loop at: "))
mult = int(input("Enter a value of mult"))

for x in range (lowNum, highNum+1):
    if x % mult ==0:
        print(x)