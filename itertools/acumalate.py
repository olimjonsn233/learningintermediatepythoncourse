from itertools import accumulate
import operator
a= [1,2,3,4]
# add to the number before it
acc=accumulate(a)
print(list(acc))
#multiple to the number before it
amm=accumulate(a,func=operator.mul)
print(list(amm))