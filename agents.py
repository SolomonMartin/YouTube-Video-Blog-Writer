from crewai import Agent
from tools import yt_tool

## creating an agent 

#Agent 1 - Blog researcher

researcher = Agent(
    role = 'Blog Research from Youtube Videos',
    goal = 'Get Relevant video content for the topic {topic} from Youtube channel',
    verbose = True,
    memory = True,
    backstory = {
        "Expert in understanding videos across various technology and educational domains"
    },
    tools = [yt_tool],
    allow_delegation = True
)


## Agent 2 - Blog writer

blog_writer = Agent(
    role = 'Blog writer',
    goal = 'Narrate compelling tech stories about the video {topic} from youtube channel',
    verbose = True,
    memory = True,
    backstory = (
        """With a flair for simplifying complex topics, you 
            craft engaging narratives that captivate and educate,
             bringing new discoveries to light in an accessible manner.
        """
    ),
    tools = [yt_tool],
    allow_delegation = False
)