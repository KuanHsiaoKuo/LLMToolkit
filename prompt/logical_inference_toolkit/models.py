# import dspy
from config import config_dspy
from signatures import CheckLogic, CheckPremises


class LogicalReasoner(config_dspy.Module):
    def __init__(self):
        super().__init__()
        self.logical_reasoner = config_dspy.Predict("text -> premises, conclusions")
        self.check_prems = config_dspy.Predict(CheckPremises)
        self.checker = config_dspy.ChainOfThought(CheckLogic)

    def forward(self, text):
        prediction = self.logical_reasoner(text=text)
        sound = self.check_prems(premises=prediction.premises)
        result = self.checker(premises=prediction.premises, conclusions=prediction.conclusions, sound=sound.sound)
        return result
