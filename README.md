# Pytho-GPT
- A simple chat gpt tool using the openai library to persist conversions in a [Chat](./python_gpt/chat.py) class

## Install
```
git clone https://github.com/joelws/python-gpt
cd python-gpt
pip install .
```

## Setup
- Set your openai api key in your environment
```
export OPENAI_API_KEY=<your key>
```

## Usage
```
from python_gpt.chat import Chat

chat = Chat("Can you please define what an AI Large Language Model is?")
# response will print either in terminal if using python there, script stdout, or jupyter notebook

# to continue the conversation
chat.ask("Further questions")
```