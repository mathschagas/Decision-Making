from utility_preference import UtilityPreference

class Attribute:

    def __init__(self, name, value = 0, weight = 1, utility_preference = UtilityPreference()):
        self.name = name
        self.value = value
        self.weight = weight
        self.utility_preference = utility_preference
    
    def __str__(self) -> str:
        return f"Attribute: {self.name}, Value: {self.value}, Weight: {self.weight}"

    def get_utility_preference(self):
        self.utility_preference.calculate_utility(self.value)