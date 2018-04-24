class Matrix:
    def __init__(self, cells):
        self.cells = cells

    @classmethod
    def zero_matrix(cls, width, height):
        cells = [[0 for x in range(width)] for y in range(height)]

        for x in range(width):
            for y in range(height):
                cells[x][y] = Cell(x, y)

        return Matrix(cells)

    def get_empty_cells(self):
        empty_cells = list()
        for x in range(len(self.cells)):
            for y in range(len(self.cells[0])):
                cell = self.cells[x][y]
                if cell.empty():
                    empty_cells.append(cell)

        return empty_cells

    def get_size(self):
        return len(self.cells), len(self.cells[0])

    def get_agents(self):
        agents = list()
        for x in range(len(self.cells)):
            for y in range(len(self.cells[0])):
                cell = self.cells[x][y]
                if not cell.empty():
                    agents.append(cell.agent)
        return agents


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.agent = None

    def set_agent(self, agent):
        self.agent = agent
        self.agent.x = self.x
        self.agent.y = self.y

    def empty(self):
        if self.agent is None:
            return True

        return False
