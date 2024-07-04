# YouTube Video Blog Writer

This project is a YouTube Video Blog Writer using Crew AI. It consists of two agents: one for researching relevant video content and another for writing engaging blog posts based on the researched content. The agents utilize Crew AI's capabilities to perform their tasks efficiently.

## Features

- **Blog Researcher Agent**: Gathers detailed information about the given topic from a specified YouTube channel.
- **Blog Writer Agent**: Writes compelling blog posts based on the researched video content.
- **Sequential Process**: Ensures that the research is completed before the writing begins.
- **Memory and Caching**: Utilizes Crew AI's memory and caching capabilities for efficient task management.
- **Customizable Tools**: Uses a YouTube Channel Search Tool to find relevant video content.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/YouTube-Video-Blog-Writer.git
    cd YouTube-Video-Blog-Writer
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Create a `.env` file in the root directory.
    - Add your API keys and other environment variables in the `.env` file.

## Usage

To run the project, execute the following command:
```bash
python crew.py


