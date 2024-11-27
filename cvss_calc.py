class CVSSCalc:
    def __init__(self, base_score, temporal_score, environmental_score):
        self.base_score = base_score
        self.temporal_score = temporal_score
        self.environmental_score = environmental_score

    def calculate(self):
        return (self.base_score + self.temporal_score + self.environmental_score) / 3

def assess_cvss(vulnerability):
    base_score = vulnerability.impact * 0.6 + vulnerability.exploitability * 0.4
    temporal_score = base_score * 0.9
    environmental_score = base_score * 1.1
    calculator = CVSSCalc(base_score, temporal_score, environmental_score)
    return calculator.calculate()
