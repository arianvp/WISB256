def findRoot(f, a, b, epsilon):
    m = ( a + b ) / 2

    if f(m) == 0 or abs(b - a) <= epsilon:
        return m
    if f(a)*f(m) <= 0:
        return findRoot(f,a,m,epsilon)
    else:
        return findRoot(f,m,b,epsilon)

def findAllRoots(f, a, b, epsilon):
    roots = []
    r = findRoot(f,a,b,epsilon)
    roots.append(r)
    while abs(r - b) > epsilon:
        r = findRoot(f,r+0.1,b,epsilon)
        roots.append(r)

    roots.pop() # remove debris
    return roots
        


    


