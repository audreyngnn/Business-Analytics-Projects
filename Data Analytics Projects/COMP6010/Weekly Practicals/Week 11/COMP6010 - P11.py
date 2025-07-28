class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit (self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw (self, amount):
        self.balance = self.balance - amount
        return self.balance


a = BankAccount('John', 1000)
print(a.name)
print(a.balance)

a.deposit(3000)
print(a.balance)

a.withdraw(2000)
print(a.balance)

class Box:
    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width

    def volume(self, depth, height, width):
        return depth * height * width
    
    def surface(self, depth, width):
        return depth * width
    
    def longest_side(self, depth, height, width):
        longest = depth
        if height > longest:
            longest = height
        if width > longest:
            longest = width
        return longest
    
    def shortest_side(self, depth, height, width):
        shortest = depth
        if height < shortest:
            shortest = height
        if width < shortest:
            shortest = width
        return shortest
    
    def ascending(self, depth, height, width):
        longest = depth
        if height > longest:
            longest = height
        if width > longest:
            longest = width

        shortest = depth
        if height < shortest:
            shortest = height
        if width < shortest:
            shortest = width
        
        middle = depth
        if middle == shortest or middle == longest:
            middle = height
        if middle == shortest or middle == longest:
            middle = width
        
    def __str__(self):
        return "Box ", self.depth, " ", self.height, " ", self.width
    
    def __eq__(self, anotherBox):
        if self.width == anotherBox.width:
            print("same width")


aBox = Box(2, 5, 8)
bBox = Box(5, 4, 6)
print(aBox)
print(aBox==bBox)




