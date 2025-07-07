from agents import Agent, Runner, function_tool
from main import config
import os
from dotenv import load_dotenv
import requests



load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")

@function_tool
def get_weather(city: str) -> str:
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}")
    data = response.json() 
    return f"The current weather in {city} is {data['current']['temp_c']}°C with a temperature of {data['current']['condition']['text']}."

agent = Agent(
    name="Weather Agent",    
    instructions="You are a helpful assistant. Your task is to help the user with their queries.",
    tools=[get_weather],
)

result = Runner.run_sync(agent,
                         'what is the current weather in Karachi today?',
                         run_config=config,)

print(result.final_output)