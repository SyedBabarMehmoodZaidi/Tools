from agents import Agent, Runner
from main import config

agent = Agent(
    name="General Agent",    
    instructions="You are a helpful assistant. Your task is to help the user with their queries.",
)

result = Runner.run_sync(agent,
                         'who is the founder of Pakistan?',
                         run_config=config,)

print(result.final_output)