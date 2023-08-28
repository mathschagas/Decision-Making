from attribute import Attribute
from delegation_candidate import DelegationCandidate
from decision_maker import DecisionMaker

#  OPTION 1: 
benefit_1 = Attribute("Time", 45)
benefit_2 = Attribute("Rating", 4.5)
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
benefit_3 = Attribute("Time", 60)
benefit_4 = Attribute("Rating", 4)
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
benefit_5 = Attribute("Time", 90)
benefit_6 = Attribute("Rating", 4.2)
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

dm.print_options()
print("______________________________________________________________\n")
print("----- BEST OPTION -----")
dm.select_best_candidate().print_info()