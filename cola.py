class Cola():
    def __init__(self):
        self.items=[]
    def datosdeCola(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.item)
    
    
cola=Cola()
print(cola.datosdeCola())
cola.enqueue(10)
cola.enqueue("jnkjjj")
print(cola.size())
cola.enqueue(10)
cola.enqueue("Darwin Rosado")
print(cola.size())