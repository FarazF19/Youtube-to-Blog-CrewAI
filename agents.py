from crewai import Agent
from tools import yt_search_tool


from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"

## Creating a Blog Researcher Agent

blog_researcher=Agent(
    role="Blog Researcher for Youtube",
    goal='get the relevant video content for the topic{topic} from YT channel.',
    verbose=True,
    backstory=(
        'Expert in understanding videos in Data Science,Gen AI, Machine Learning and providing suggestions'
    ),
    tools=[yt_search_tool],
    allow_delegation=True,
    memory=True
)

## creating a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_search_tool],
    allow_delegation=False
)

