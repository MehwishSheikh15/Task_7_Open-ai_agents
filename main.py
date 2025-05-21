from dataclasses import dataclass
from openai_agents import Agent, Instruction, Runner

@dataclass
class MyContext:
    user_query: str
    previous_responses: list[str]

def my_instruction(context: MyContext) -> str:
    # Use OpenAI model call internally (pseudo-code)
    response = call_openai_model(prompt=context.user_query)
    return response

agent = Agent(instructions=[my_instruction])
runner = Runner(agent)

context = MyContext(user_query="Hello, what's the weather?", previous_responses=[])
result = runner.run(context)

print(result)
