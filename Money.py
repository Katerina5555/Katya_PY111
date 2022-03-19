import random
from typing import Union
import requests
import json


class Money:
    def __init__(self, name: Union[str, None], sum_of_money: float):
        self.name = name
        self.sum_of_money = sum_of_money

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, ' \
               f'{self.__class__.__name__}({self.sum_of_money})'


    def convert_to_valute(self):
        """
        метод для конвертации рублей в иную валюту
        :return:
        возвращает
        """
        answer = input("Есть возможность загрузить файл с сайта ЦБ РФ?")

        if answer == "Да" or answer == "да":
            url = "https://www.cbr-xml-daily.ru/daily_json.js"
            price = requests.get(url, allow_redirects=True)
            open("CBR.json", 'wb').write(price.content)


        dict_ = json.load(open("CBR.json"))
        # print(dict.items(dict_['Valute']['USD']))
        print("Время последней загрузки файла из источника: "
              + dict_["Date"])
        valute_name = input("Введите валюту в которую хотите "
                            "конвертировать (международное обозначение): ")
        b = dict_['Valute'][valute_name]['Value']
        # print(b)
        print(round((self.sum_of_money / b), 2))

class Rubles(Money):
    def __init__(self, name="RUB", sum_of_money=0):
        self.name = name
        self.sum_of_money = sum_of_money
        super().__init__()

class Euro(Money):
    pass


if __name__ == '__main__':
    money1 = Money('RUB', 1234.56)
    rubles1 = Rubles('RUB', 1234.56)
    Money.convert_to_valute(rubles1)


