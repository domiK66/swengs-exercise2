class Stack:
    def __init__(self):
        self.numbers = []
        self.current_size: int = 0
    
    def __str__(self) -> str:
        return f"Stack with {self.current_size} object(s)" 
    
    def size(self) -> int:
        return self.current_size

    def pop(self) -> int:
        if self.current_size == 0:
            raise ValueError
        self.current_size -= 1
        return self.numbers.pop()

class PositiveNumberStack(Stack):
    def push(self, n) -> None:
        if n < 0 or self.current_size == 3:
            raise ValueError
        self.current_size += 1        
        self.numbers.append(n)

class NegativeNumberStack(Stack):
    def push(self, n) -> None:
        if n > 0 or self.current_size == 3:
            raise ValueError
        self.current_size += 1
        self.numbers.append(n)
        