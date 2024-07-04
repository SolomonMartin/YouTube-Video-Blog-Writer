from crewai import Task
from tools import yt_tool
from agents import researcher,blog_writer

## Research Task

research_task = Task(
    description = (
        """        Identify the video {topic}. Get detailed information about
        the video from the channel
        """
    ),
    expected_output = 'A comprehensive 3 paragraph long report based on the {topic} of video content',
    tools = [yt_tool],
    agent = researcher,
)

write_task = Task(
    description = (
        "get the info from the youtube channela on the topic {topic}"
    ),
    expected_output = 'Summarize the info from the youtube channel video on the topic {topic} and create content for the blog',
    tools = [yt_tool],
    agent = blog_writer,
    async_execution = False,
    output_file = 'new-blog-post.md'
)