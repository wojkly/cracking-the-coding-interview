class Node:
    def __init__(self, v = None) -> None:
        self._v = v
        self._next = None
        
class Queue:
    def __init__(self) -> None:
        self._first = Node()
        self._last = self._first
        
    def put(self, v) -> None:
        v_node = Node(v)
        self._last._next = v_node
        self._last = v_node
        
    def get(self) -> any:
        # check if no elements??
        if not self._first._next:
            return None
        
        # check if removing last element
        if not self._first._next._next:
            self._last = self._first
        
        v_node = self._first._next
        self._first._next = self._first._next._next
        return v_node._v
        
    def first(self) -> any:
        # check if no elements??
        if not self._first._next:
            return None
        
        return self._first._next._v
        
import datetime

class Animal:
    DOG = 'DOG'
    CAT = 'CAT'
    
    def __init__(self, t, n) -> None:
        self._type = t
        self._name = n
        self._date = datetime.datetime.now()
        
class AnimalShelter:
    def __init__(self) -> None:
        self._cats = Queue() 
        self._dogs = Queue() 
        
        
    def enqueue(self, animal: Animal):
        if animal._type == Animal.DOG:
            self._dogs.put(animal)
        elif animal._type == Animal.CAT:
            self._cats.put(animal)
        pass
    
    def dequeueAny(self) -> Animal:
        first_dog = self._dogs.first()
        first_cat = self._cats.first()
        
        if not first_cat and not first_dog:
            return None
        
        if not first_cat:
            return self._dogs.get()
        if not first_dog:
            return self._cats.get()
        
        # return newest
        if first_cat._date < first_dog._date:
            return self._cats.get()
        else:
            return self._dogs.get()
            
    
    def dequeueDog(self) -> Animal:
        return self._dogs.get()
    
    def dequeueCat(self) -> Animal:
        return self._cats.get()
    
# test queue implementation
q = Queue()
assert q.get() == None
assert q.get() == None
q.put(1)
q.put(2)
q.put(3)
assert q.get() == 1
assert q.get() == 2
assert q.get() == 3
assert q.get() == None
q.put(4)
q.put(5)
q.put(6)
assert q.get() == 4
assert q.get() == 5
assert q.get() == 6
assert q.get() == None
assert q.first() == None
q.put(7)
q.put(8)
q.put(9)
assert q.first() == 7
assert q.get() == 7
assert q.first() == 8


# test animal shelter
ash = AnimalShelter()
assert ash.dequeueAny()  == None
assert ash.dequeueCat()  == None
assert ash.dequeueDog()  == None

dog1 = Animal(Animal.DOG, 'dog1')
cat1 = Animal(Animal.CAT, 'cat1')
cat2 = Animal(Animal.CAT, 'cat2')
dog2 = Animal(Animal.DOG, 'dog2')

ash.enqueue(dog1)
ash.enqueue(cat1)
ash.enqueue(cat2)
ash.enqueue(dog2)

assert ash.dequeueAny()  == dog1
assert ash.dequeueCat()  == cat1
assert ash.dequeueDog()  == dog2
assert ash.dequeueAny()  == cat2
