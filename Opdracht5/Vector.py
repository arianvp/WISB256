from array import array




class Vector:
    def __init__(self, *args):
        if len(args) == 1:
            self.array = array('d',[0]*args[0])
        elif len(args) == 2:
            if type(args[1]) == int or type(args[1]) == float:
                self.array = array('d',[args[1]]*args[0])
            else:
                #TODO maybe make it so that fixed len
                self.array = array('d',args[1])
        # TODO: write code...
    
    def __str__(self):
        strs = [str(i) for i in self.array]
        return '\n'.join(strs)
        
        
    
    def add(self,other):
        w = array('d', [0]*len(self.array))
        for i in range(len(self.array)):
            w[i] = self.array[i] + other.array[i]
        return Vector(len(self.array),w)


    def scalar(self,alpha):
        w = array('d',[0]*len(self.array))
        
        for i in range(len(self.array)):
            w[i] = alpha * self.array[i]
            
        return Vector(len(self.array),w)
        
    
    def lincomb(self,other,alpha,beta):
        a = self.scalar(alpha)
        b = other.scalar(beta)
        return a.add(b)
        
    
    def inner(self,other):
        inner = 0
        for i in range(len(self.array)):
            inner += self.array[i] * other.array[i]
        return inner


    def norm(self):
        c = 0
        for i in range(len(self.array)):
            c += self.array[i]**2
            
        return c ** 0.5
        
        
def proj(u,v):
    return u.scalar(v.inner(u) / u.inner(u))

def idioamaticGramSchmidt(vs):
    ws = []
    for v in vs:
        u = v
        for w in ws:
            u = u.lincomb(proj(v,w),1,-1)
            ws.append(u.scalar(1/u.norm()))


def old_GramSchmidt(vs):
    xs = []
    for i in range(len(vs)):
        tmp = vs[i]
        for j in xs:
            tmp = tmp.lincomb((proj(vs[i],j)),1,-1)
        xs.append(tmp.scalar(1/tmp.norm()))
        
    return xs
                


def GrammSchmidt(v):
    for i in range(len(v)):
        v[i] = v[i].scalar(1/v[i].norm())
        
        for j in range(i+1,len(v)):
            v[j] = v[j].lincomb(proj(v[i],v[j]),1,-1)
        
    return v