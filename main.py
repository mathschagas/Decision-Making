from attribute import Attribute
from delegation_candidate import DelegationCandidate
from decision_maker import DecisionMaker
from utility_preference import UtilityPreference

# Utility Preference Settings
times = [0, 30, 60, 90, 120] 
times_preference = [100, 90, 70, 50, 0]
time_up = UtilityPreference("Time", times, times_preference)

ratings = [2.5, 3.5, 4.5, 5] 
ratings_preference = [0, 20, 40, 100]
ratings_up = UtilityPreference("Rating", ratings, ratings_preference)

#  OPTION 1: 
benefit_1 = Attribute("Time", 60)
benefit_2 = Attribute("Rating", 4.9)
benefit_1.set_utility_preference(time_up)
benefit_2.set_utility_preference(ratings_up)
cost_1 = Attribute("Price", 15)
cost_2 = Attribute("Fuel Consumption", 2)
risk_1 = Attribute("Rain-safe", 1)

option_1 = DelegationCandidate("Car")
option_1.add_benefit(benefit_1)
option_1.add_benefit(benefit_2)
option_1.add_cost(cost_1)
option_1.add_cost(cost_2)
option_1.add_risk(risk_1)

#  OPTION 2: 
benefit_3 = Attribute("Time", 45)
benefit_4 = Attribute("Rating", 3.5)
benefit_3.set_utility_preference(time_up)
benefit_4.set_utility_preference(ratings_up)
cost_3 = Attribute("Price", 12)
cost_4 = Attribute("Fuel Consumption", 0.5)
risk_2 = Attribute("Prone to Traffic", 0)

option_2 = DelegationCandidate("Motorcycles")
option_2.add_benefit(benefit_3)
option_2.add_benefit(benefit_4)
option_2.add_cost(cost_3)
option_2.add_cost(cost_4)
option_2.add_risk(risk_2)

#  OPTION 3: 
benefit_5 = Attribute("Time", 120)
benefit_6 = Attribute("Rating", 3)
benefit_5.set_utility_preference(time_up)
benefit_6.set_utility_preference(ratings_up)
cost_5 = Attribute("Price", 8)
cost_6 = Attribute("Fuel Consumption", 0)
risk_3 = Attribute("Prone to Traffic", 0)

option_3 = DelegationCandidate("Pedestrian")
option_3.add_benefit(benefit_5)
option_3.add_benefit(benefit_6)
option_3.add_cost(cost_5)
option_3.add_cost(cost_6)
option_3.add_risk(risk_3)

dm = DecisionMaker()
dm.add_candidate(option_1)
dm.add_candidate(option_2)
dm.add_candidate(option_3)

time_up.plot_utility_preference()
ratings_up.plot_utility_preference()

dm.print_options()
print("_" * 40 + "\n")
print("----- BEST OPTION -----")
bc = dm.select_best_candidate()
bc.print_info()
print(f"    - SCORE: {bc.score()}")