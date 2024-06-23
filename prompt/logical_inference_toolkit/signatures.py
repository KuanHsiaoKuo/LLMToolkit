import dspy


class CheckLogic(dspy.Signature):
    """给定一个论点的前提和结论，检查结论是否合乎逻辑。"""
    # 创建一个输入字段，用于输入论点的前提
    premises = dspy.InputField(desc="论点的前提")

    # 创建一个输入字段，用于输入论点的结论
    conclusions = dspy.InputField(desc="论点的结论")

    # 创建一个输出字段，用于指示给定前提下结论是否合乎逻辑
    logical = dspy.OutputField(desc="给定前提，结论是否合乎逻辑")


# 定义 check_premises 类，它是一个用于检查前提是否合理的 dspy.Signature。
class CheckPremises(dspy.Signature):
    """
    给定论点的前提，检查前提是否合理。
    """
    premises = dspy.InputField(desc="论点的前提")
    sound = dspy.OutputField(desc="前提是否合理")
