#wrong approach taken

import time 
start = time.time()
for i in range(1,101):
    print(i)
print(time.time()-start)

#you can check with this method but it take different time in different system on acc to its configurations......
# not for extremely small input
# time varies have  time problem 
# time varies if implementation changes.....