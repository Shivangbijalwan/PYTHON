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
##########################  Question end  #############################

##########################  Question no 4  #############################
##########################  Question end  #############################

##########################  Question no 5  #############################
##########################  Question end  #############################

##########################  Question no 6  #############################
##########################  Question end  #############################

##########################  Question no 7  #############################
##########################  Question end  #############################

##########################  Question no 8  #############################
##########################  Question end  #############################

##########################  Question no 9  #############################
##########################  Question end  #############################

##########################  Question no 10  #############################
##########################  Question end  #############################

##########################  Question no 11  #############################
##########################  Question end  #############################

##########################  Question no 12  #############################
##########################  Question end  #############################

##########################  Question no 13  #############################
##########################  Question end  #############################

##########################  Question no 14  #############################
##########################  Question end  #############################

##########################  Question no 15  #############################
##########################  Question end  #############################

##########################  Question no 16  #############################
##########################  Question end  #############################

##########################  Question no 17  #############################
##########################  Question end  #############################

##########################  Question no 18  #############################
##########################  Question end  #############################
