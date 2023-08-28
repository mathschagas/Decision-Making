class Attribute:

    def __init__(self, name, value = 0, weight = 1):
        self.name = name
        self.value = value
        self.weight = weight
    
    def __str__(self) -> str:
        return f"Attribute: {self.name}, Value: {self.value}, Weight: {self.weight}"

