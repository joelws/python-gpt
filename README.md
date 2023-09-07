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
Example output using python in terminal:
```
>>> from python_gpt.chat import Chat
>>> chat = Chat("Can you please define what an AI Large Language Model is?")
                                                                                                                                               Response: An AI Large Language Model (LLM) is a type of artificial intelligence system that uses a deep learning technique called transformer architecture to generate human-like text based on the input it receives. It is trained on vast amounts of text data to understand patterns, grammar, and context in order to generate coherent and contextually relevant responses.

LLMs are designed to understand and generate natural language, and they can be used for a variety of tasks such as language translation, text completion, question-answering, summarization, and even creative writing. They are capable of generating long-form text by predicting the most probable next word or sequence of words given the context.

Some well-known examples of AI Large Language Models include OpenAI's GPT-3 (Generative Pre-trained Transformer 3) and Google's BERT (Bidirectional Encoder Representations from Transformers). These models have gained significant attention due to their ability to generate highly coherent and contextually relevant text responses, making them valuable tools for various applications in
```

## Params
- Optional params can be passed to the Chat class
```
class Chat:
    def __init__(
            self, 
            prompt : str,
            model : str = 'gpt-3.5-turbo',
            max_tokens : int = 200,
            top_p : int = 1,
            temperature : int = 0.6,
            frequency_penalty : int = 0,
            presence_penalty : int = 0,
            cost_per_token : int = 0.00003,
            print_cost : bool = False,
        ) -> None:
```