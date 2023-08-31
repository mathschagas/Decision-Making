import matplotlib.pyplot as plt

class UtilityPreference:

    def __init__(self, name, values = [], preferences = []):
        self.name = name
        self.values = values
        self.preferences = preferences


    def is_set(self):
        if len(self.values) == 0 or len(self.preferences) == 0:
            return False
        else:
            return True

    # Função para calcular a preferência de utilidade para taxa de falha
    def calculate_utility(self, attribute):
        if attribute <= self.values[0]:
            return self.preferences[0]
        elif attribute >= self.values[-1]:
            return self.preferences[-1]
        else:
            for i in range(1, len(self.values)):
                if attribute <= self.values[i]:
                    x0, x1 = self.values[i - 1], self.values[i]
                    y0, y1 = self.preferences[i - 1], self.preferences[i]
                    return y0 + (y1 - y0) * (attribute - x0) / (x1 - x0)

    def plot_utility_preference(self):
        # Plot para taxa de falha
        plt.figure(figsize=(4, 4))
        plt.plot(self.values, self.preferences)
        plt.xlabel(self.name)
        plt.ylabel('Utility Preference')
        plt.title(f"Utility Preference for {self.name}")
        plt.show()

# Calcular a preferência de utilidade para valores específicos
# Exemplo: para taxa de falha igual a 1 e uso de recursos igual a 8

# failure_rates = [0, 1, 2, 3]  # Valores de taxa de falha
# failure_preference = [100, 30, 0, 0]  # Preferência de utilidade para taxa de falha
# failure_rate = 0.5
# fr = UtilityPreference("Failure Rate", failure_rates, failure_preference)
# print("Preferência de utilidade para taxa de falha de 1:", fr.calculate_utility(failure_rate))
# fr.plot_utility_preference()
