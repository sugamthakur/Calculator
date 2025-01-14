import sys

def main():
   
   
   
   while True:
        z=cal()
        if z==0:
             
             sys.exit("Thank you for using me")
             
        else:
             x=getnumber()
             y=getnumbertwo()   
             calculate(x,y,z)   
        
        


        
   

   
   
   

def calculate(a,b,c):
       match c:
               # '|' is same as or 
                case 1 :
                       print("Sum of the numbers is: ", sumation(a,b))
               
                case 2 :
                       print("Difference of the given number is: ", subtract(a,b))
                #this is the default case
                case 3 :
                       print("Product of the numbers is: ", multipliy(a,b))
                case 4 : 
                       if b!=0:
                        print("Quostione of the given number is: ", divide(a,b))
                       else:
                            while True:
                                 print("divisor must not be zero.")
                                 b=getnumbertwo()
                                 if b!=0:
                                      print("Quostione of the given number is: ", divide(a,b))
                                      break
                                 else:
                                      continue

                                      


    
def cal():
     
     while True:

        print("Select what do to:")

        print("1: Add, 2: Subtract, 3: Multiply, 4: Divide, 0: Exit ")

        try:
            x=  int(input())
            if x == 1 or x==2 or x==3 or x==4 or x==0:
                 return x
            
        except ValueError:
            #pass: cathing the error and not doing anything with this.
            #then it will go back to try because while loop
            print("Enter whole numbers only")
            
     #else:
            #break
     
          
          
        
def sumation(a,b):
    return a+b

def subtract(a,b):
    return a-b

def divide(a,b):
    
         return a/b
   

def multipliy(a,b):
    return a*b

def getnumber():
    while True:
         try:
            return  float(input("Enter number one: "))

         except ValueError:
            print("Enter a valid whole number")

def getnumbertwo():
    while True:
         try:
            return  float(input("Enter number two: "))

         except ValueError:
            print("Enter a valid whole number")


if __name__=="__main__":
    main()
