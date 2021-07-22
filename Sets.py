# Program to perform different set operations.
E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}

#Union of sets E and N
x = E | N
print("Union of the sets E and N is",x)

#Intersection of sets E and N

y = E & N
print("Intersection of E and N is ",y)

#Difference of sets E and N

z = E - N
print("Difference of E and N is ",z)

# Symmetric difference of sets E and N

w = E ^ N
print("Symmetric difference of E and N is ",w)
