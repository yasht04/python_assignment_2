
#arithmetic operator
a = 15
b = 3
print("a:",a,"b:",b)
print("add:",a+b)
print("Subtract:",a-b)
print("multiply:",a*b)
print("divide:",a/b)
print("mod:",a%b)
print("exponent:",a**b)
print("floor division:",a//b)

# assignment operator
n = 10
n+= 2
print("Before:",n)
print("after +=:",n)
n = 10
n-= 2
print("Before:",n)
print("after -=:",n)
n = 10
n*= 2
print("Before:",n)
print("after *=:",n)
n = 10
n/= 2
print("Before:",n)
print("after /=:",n)

# comparison (relational) operator
x = 5
y = 10
print("x:",x,"y:",y)
print("Equal:",x==y)
print("not equal:",x!=y)
print("greater than:",x>y)
print("less than:",x<y)

# logical operator
a = True
b = False
print("a:",a,"b:",b)
print("and operator:",a and b)
print("or operator:",a or b)
print("not operator:",not a)

# bitwise operator
a = 8
b = 4
print("a:",a,"b:",b)
print("bitwise and:",a&b)
print("bitwise or:",a|b)
print("bitwise xor:",a^b)
print("right shift:",a>>b)
print("left shift:",a<<b)

# Identity operator
a = 10
b = 10
print("a:",a)
print("is operator:",a is b)
print("is not operator:",a is not 10)

# special (membership) operator
name = "abcde"
print("in operator: ","ab" in name)
print("not in operator: ","ij" not in name)
