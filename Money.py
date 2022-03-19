import random
from typing import Union
import requests



class Money:
    def __init__(self, name: Union[str, None], sum_of_money: float):
        self.name = name
        self.sum_of_money = sum_of_money

