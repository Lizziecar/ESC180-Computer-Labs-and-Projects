#midterm review stuffs

##Splicing
L = [5, 6, 7, 3, 5, 6]
H = L[1:4:2] #[6,3]
G = L[5:2:-1] #[6, 5, 3]
K = L[3::-1] #[3,7,6,5]

print(H)
print(G)
print(K)

#end point is not included


##Aliasing
L = [1,2,3]
L1 = L #both variables refer to the same place in memory