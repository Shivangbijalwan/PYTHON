#wrong approach 1


import time 
start = time.time()
for i in range(1,101):
    print(i)
print(time.time()-start)

#you can check with this method but it take different time in different system on acc to its configurations......
# not for extremely small input
# time varies have  time problem 
# time varies if implementation changes..... 

#wrong approach 2
#here we will take the code and count the how many operation taken by the code 
#order of growth , it is the graph time and growth 

#questions for time complexity 

##########################  Question no 1  #############################
"""time complicity of the following code ?"""
L=[1,2,3,4,5]
sum = 0
for i in L:
  sum = sum+i
print(sum)

product = 1
for i in L:
 product = product*i
print(product)
"""here the time complicity is O(n)which is linear because the 
   loop is running n times where n is the length of the array """
##########################  Question end  #############################


##########################  Question no 2  #############################
"""time complicity of the following code ?"""
L = [1, 2, 3, 4, 5]
for i in L:
    for j in L:
        print("({}, {})".format(i, j))
"""here the time complicity is O(n^2) which 
   is quadratic because the loop is nested"""
##########################  Question end  #############################

##########################  Question no 3  #############################
"""what will happen here"""
#Linear search
"""if the input size will increase the time will also increase """
##########################  Question end  #############################

##########################  Question no 4  #############################
"""time complicity of the following code ?"""
def intToStr(i):
   digits = "0123456789"
   if i == 0:
      return "0"
   result = ""
   while i > 0:
      result= digits[i%10]+result
      i = i//10
      return result
##########################  Question end  #############################
