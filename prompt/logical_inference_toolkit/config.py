import dspy as config_dspy
import os
from dotenv import load_dotenv

load_dotenv()

llm = config_dspy.OpenAI(
    model='gpt-4',
    api_key=os.environ['OPENAI_API_KEY'],
    api_base=os.environ['OPENAI_BASE_URL'],
    max_tokens=100
)

config_dspy.settings.configure(lm=llm)
