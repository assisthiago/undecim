import random

RATING_QUALITIES = ("A", "B", "C", "D", "E", "F")


class Attributes:
    composure: int
    crossing: int
    defending: int
    dribbling: int
    goalkeeping: int
    heading: int
    pace: int
    passing: int
    physical: int
    positioning: int
    shooting: int
    skill_moves: int
    reflexes: int
    weak_foot: int
    work_rate: int
    overall: int

    def __init__(self, rating_points):
        range_points = self.range_quality(rating_points)

        self.composure = random.randint(*range_points)
        self.defending = random.randint(*range_points)
        self.dribbling = random.randint(*range_points)
        self.heading = random.randint(*range_points)
        self.pace = random.randint(*range_points)
        self.passing = random.randint(*range_points)
        self.physical = random.randint(*range_points)
        self.positioning = random.randint(*range_points)
        self.shooting = random.randint(*range_points)
        self.skill_moves = random.randint(*range_points)
        self.weak_foot = random.randint(*range_points)
        self.work_rate = random.randint(*range_points)
        self.goalkeeping = random.randint(*range_points)
        self.reflexes = random.randint(*range_points)
        self.overall = self.calculate_overall()

    def calculate_overall(self):
        attributes = [value for key, value in self.__dict__.items() if key != "overall"]
        return sum(attributes) // len(attributes)

    def range_quality(self, rating_points):
        if rating_points == "A":
            return 90, 99
        elif rating_points == "B":
            return 80, 89
        elif rating_points == "C":
            return 70, 79
        elif rating_points == "D":
            return 60, 69
        elif rating_points == "E":
            return 50, 59
        else:
            return 40, 49

    def rating_quality(self):
        if self.overall <= 39:
            return "F"
        elif self.overall <= 49:
            return "E"
        elif self.overall <= 69:
            return "D"
        elif self.overall <= 79:
            return "C"
        elif self.overall <= 89:
            return "B"
        else:
            return "A"

    def __str__(self):
        attributes = [f"  {key}: {value}" for key, value in self.__dict__.items()]
        return "\n".join(attributes)
