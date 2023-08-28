from attribute import Attribute

class DelegationCandidate:

    # Contructor
    def __init__(self, name):
        self.name = name
        self.benefit_attributes = []
        self.cost_attributes = []
        self.risk_attributes = []

    # Benefit CRUD
    def add_benefit(self, benefit):
        self.benefit_attributes.append(benefit)
    
    def edit_benefit(self, benefit):
        b_index = self.benefit_attributes.index(benefit)
        self.benefit_attributes[b_index] = benefit

    def remove_benefit(self, benefit):
        self.benefit_attributes.remove(benefit)

    # Cost CRUD
    def add_cost(self, cost):
        self.cost_attributes.append(cost)
    
    def edit_cost(self, cost):
        c_index = self.benefit_attributes.index(cost)
        self.cost_attributes[c_index] = cost

    def remove_cost(self, cost):
        self.cost_attributes.remove(cost)

    # Risk CRUD
    def add_risk(self, risk):
        self.risk_attributes.append(risk)
    
    def edit_risk(self, risk):
        r_index = self.risk_attributes.index(risk)
        self.risk_attributes[r_index] = risk

    def remove_risk(self, risk):
        self.risk_attributes.remove(risk)

    # Print
    def print_info(self):
        print(f" - Candidate: {self.name}")
        for attr in self.benefit_attributes:
            print(f"    - {attr}")
        for attr in self.cost_attributes:
            print(f"    - {attr}")
        for attr in self.risk_attributes:
            print(f"    - {attr}")

    def score(self):
        estimated_benefit = 0
        estimated_cost = 0
        estimated_risk = 0
        for b in self.benefit_attributes:
            # TODO: Update to utility preference
            estimated_benefit += b.value * b.weight
        for c in self.cost_attributes:
            estimated_cost += c.value * c.weight
        for r in self.risk_attributes:
            estimated_risk += r.value * r.weight
        estimated_desirability = estimated_benefit / estimated_cost
        # TODO: cbr_score = estimated_desirability * Wvfc - estimated_benefit * Wr        
        cbr_score = estimated_desirability - estimated_risk
        return cbr_score