from abc import ABC, abstractmethod

import requests as requests


class JobAPI(ABC):
    '''Для API'''

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def info(self):
        pass


class HH(JobAPI):
    '''Для API hh.ru'''
    url = 'https://api.hh.ru/vacancies'

    def __init__(self, text: str, per_page: int, city: int):
        self.text = text
        self.per_page = per_page
        self.area = city

    def info(self):
        '''Список вакансий'''
        answer = requests.get(self.url, params= self.__dict__)
        list =answer.json()['items']
        return list