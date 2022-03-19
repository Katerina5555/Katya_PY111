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
        Метод для конвертации
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
        exchange_rate = dict_['Valute'][valute_name]['Value']
        # print(b)
        if self.name != "RUB":
            value_converting_valute_to_rub = dict_['Valute'][self.name]['Value']
            # print(value_converting_valute_to_rub)
            value_in_rub = self.sum_of_money * value_converting_valute_to_rub
            print(round((value_in_rub / exchange_rate), 2))
        else:
            print(round((self.sum_of_money / exchange_rate), 2))

    def wallet(self):




class Rubles(Money):
    def __init__(self, name: Union[str, None], sum_of_money: float):
        self.name = name
        self.sum_of_money = sum_of_money
        super().__init__("RUB", sum_of_money)


class Euro(Money):
    def __init__(self, name: Union[str, None], sum_of_money: float):
        self.name = name
        self.sum_of_money = sum_of_money
        super().__init__("EUR", sum_of_money)


if __name__ == '__main__':
    euro = Money('EUR', 1)
    rubles = Rubles('RUB', 1234.56)
    Money.convert_to_valute(euro)


