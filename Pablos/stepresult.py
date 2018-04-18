class StepResult:
    def __init__(self, matrix, agents, empty, percent_unhappy, percent_similar):
        self.matrix = matrix
        self.agents = agents
        self.empty = empty
        self.percent_unhappy = percent_unhappy
        self.percent_similar = percent_similar
