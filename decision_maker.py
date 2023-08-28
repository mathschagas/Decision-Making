from delegation_candidate import DelegationCandidate

class DecisionMaker:

    def __init__(self):
        self.delegation_candidates = []
        pass

    # Candidate CRUD
    def add_candidate(self, candidate):
        self.delegation_candidates.append(candidate)
    
    def edit_benefit(self, candidate):
        dc_index = self.delegation_candidates.index(candidate)
        self.delegation_candidates[dc_index] = candidate

    def remove_benefit(self, candidate):
        self.delegation_candidates.remove(candidate)

    def print_options(self):
        for dc in self.delegation_candidates:
            dc.print_info()
            print(f"    - SCORE: {dc.score()}")

    def select_best_candidate(self) -> DelegationCandidate:
        best_candidate = self.delegation_candidates[0]
        if len(self.delegation_candidates) > 1:
            for dc in self.delegation_candidates:
                if dc.score() > best_candidate.score():
                    best_candidate = dc
        return best_candidate
    
