# LLM-Telegram-Chatbot

This Telegram Chatbot is a Python-based bot that allows users to engage in conversations with a Language Model (LLM) using the GPT4all python library and the python-telegram-bot library. This README provides an overview of the project and instructions on how to get started.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Commands](#commands)
- [Customizing the LLM](#customizing-the-llm)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before using the Telegram Chatbot, ensure you have the following:

- Python 3 installed on your system.
- The necessary Python libraries specified in the [requirements.txt](requirements.txt) file. You can install them using `pip`.

## Getting Started

1. Clone the repository to your local machine:
```bash
git clone https://github.com/Fatal3xcept10n/LLM-Telegram-Chatbot.git
```
2. Change directory to the project folder:
```bash
cd LLM-Telegram-Chatbot
```
3. Install the required Python libraries:
```bash
pip install -r requirements.txt
```
4. Generate a Telegram Bot API key:
   - Visit the BotFather on Telegram to create your bot and obtain the API key.
   - Create a file in the project folder named ``` apikey.py ```
   - Edit this file and include this single line, making sure to replace with your own API key
     ```bash
     API_KEY = '[API key goes here]'
     ```
## Usage

To start the bot, run the [main.py](main.py) file:
```bash
python main.py
```
You can interact with the bot on Telegram using the following commands:
```bash
- /help: Display a help menu.
- /hello: Initiate a conversation with the bot.
- /stop: Stop the current conversation.
- /persistence: (Currently not functional) Toggle conversation persistence (coming soon).
```
![Menu image](https://github.com/Fatal3xcept10n/LLM-Telegram-Chatbot/blob/master/images/helpmenu.png?raw=true)
![Conversation image](https://github.com/Fatal3xcept10n/LLM-Telegram-Chatbot/blob/master/images/conversation.png?raw=true)

## Commands

- The main command handling logic can be found in the [commands.py](commands.py) file.
- You can modify and extend the commands to customize your bot's behavior.

## Customizing the LLM

In the [chatbot.py](chatbot.py) file, you can customize the Language Model (LLM) used by the bot. You can also adjust LLM parameters and settings to suit your preferences.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these guidelines:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Commit your changes and push them to your fork.
- Create a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.
