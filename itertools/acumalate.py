from itertools import accumulate
a= [1,2,3,4]
# add to the number before it
acc=accumulate(a)
print(list(acc))