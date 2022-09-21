#a dictionary containing keys ranging from 5 to 15 (with both numbers included) 
# and the values are the squares of the keys.

#naming the values
Numbers = {}
for x in range(5,16):
    Numbers[x]=x**2
print(Numbers)  

#or Using dictionary comprehension
Numbers = {x: x*x for x in range(5,16)}
print(Numbers)
