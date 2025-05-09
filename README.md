# 🧠 Agentic Youtube Video to Blog Writer with CrewAI

This project automates the process of researching and writing blog posts on technical topics using CrewAI, a framework for building collaborative AI agents. The agents work together to research and generate content on a given topic—in this case, "Agentic AI: A Progression of Language Model Usage" from youtube video.

## 🚀 Features

- 🤖 Multi-agent collaboration: Includes a blog_researcher and blog_writer working in sequence.

- 📄 Task automation: Automatically performs research and writes a blog based on the given topic.

- 🔁 Sequential processing: Tasks are executed in a defined order for coherent output.

- 💾 Memory & caching: Improves response consistency and efficiency.

- 📈 Rate limiting: Limits execution to 100 requests per minute for stability.

- 🌐 Shareable crew: Crew configuration is reusable across tasks.

## 🛠️ Project Structure

.
├── main.py # Entry point for kicking off the Crew
├── agents.py # Contains agent definitions: Researcher and Writer
├── tasks.py # Defines the research and writing tasks
├── .env # Environment variables (e.g., API keys)
├── README.md # Project overview

## 📦 Requirements

- Python 3.10+

- crewai

- python-dotenv

## Install dependencies:

pip install crewai python-dotenv crewai-tools

## ⚙️ Usage

- Add your environment variables to a .env file (e.g., OpenAI API key).

- Modify the topic by copying and pasting any youtube video link in crew.py or also writing channel name e.g @stanfordonline in the place of youtube tool call in tools.py.

- Run the script:
  python main.py

## 📝 Output

The script prints a complete, AI-generated blog post on the specified topic.

## 🔮 Example Input

inputs={'topic': 'Agentic AI: A Progression of Language Model Usage'}

##📚 Inspired By

- CrewAI

- DeepLearning.AI - Building Agentic RAG with LlamaIndex

📌 License
MIT License
