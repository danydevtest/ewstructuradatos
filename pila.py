class Pila():
    def __init__(self):
        self.items=[]
    
    def llenadoPila(self):
        return self.items==[]
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    def top(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    
pila=Pila()
#print(pila.llenadoPila())
pila.push(4)
pila.push("hhh")
pila.push(6)
pila.push("jjuh")

print(pila.size())