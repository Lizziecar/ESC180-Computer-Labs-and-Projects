###Godel's Icompleteness Theorem

#True is intuitive
#Proven is intuitive

# There are true mathematical statements that cannot be proven

#Suppose that every true mathematical statement can be proven
#we'll prove that it follows that we can write halt

def halt(f,x):
    # generate all strings over the latin alphabet of length 1, 2, 3, 4...
    # for every such string s
    #   if s is a proof that f(x) halts, return True
    #   if s is a proof that f(x) doesn't halt return False

# So halt is impossible to write. Contradiction!
# So the assumption that every true mathematical statement can be proven is false