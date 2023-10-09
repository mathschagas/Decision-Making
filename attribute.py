from utility_preference import UtilityPreference

class Attribute:

    def __init__(self, name, value = 0, weight = 1):
        self.name = name
        self.value = value
        self.weight = weight
        self.utility_preference = UtilityPreference(name=name)
    
    def __str__(self) -> str:
        if self.has_utility_preference():
            return f"Attribute: {self.name}, Value: {self.value}, Weight: {self.weight}, Utility Score: {self.get_utility_preference()}"
        return f"Attribute: {self.name}, Value: {self.value}, Weight: {self.weight}"

    def get_utility_preference(self) -> UtilityPreference:
        return self.utility_preference.calculate_utility(self.value)

    def set_utility_preference(self, utility_preference):
        self.utility_preference = utility_preference
    
    def has_utility_preference(self):
        return self.utility_preference.is_set()