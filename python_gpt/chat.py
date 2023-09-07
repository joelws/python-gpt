'''Chat Class for python-gpt'''
import os
import openai

from python_gpt.loader import Loader



# load openai key from env
OPENAI_KEY = os.getenv("OPENAI_KEY")

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
        self.model = model
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.temperature = temperature
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.cost_per_token = cost_per_token
        self.print_cost = print_cost
        self.chat_log = []
        self.token_usage = 0
        self.cost = 0,

        # ask initial question
        self.ask(prompt)


    def ask(
            self,
            question: str,
        ) -> list:
        '''Ask a question

        Args:'''
        loader = Loader()
        loader.start()

        # handle chat and print response
        self.chat_log.append({"role": "user", "content": question})

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.chat_log,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty
            )
            loader.stop()
        except Exception as e:
            raise Exception(e)
        
        self.chat_log.append({"role" : "assistant", "content": response['choices'][0]['message']['content']})
        self.token_usage += response['usage']['total_tokens']
        self.cost = self.token_usage * self.cost_per_token

        print(f"Response: {self.chat_log[-1]['content']}")
        if self.print_cost:
            print(f"Cost: ${self.cost}")
