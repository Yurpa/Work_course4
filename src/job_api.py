from abc import ABC, abstractmethod

import requests as requests
import os


class JobAPI(ABC):
    '''Абс. класс для API'''

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

class SJ(JobAPI):
    """Для API SuperJob"""

    API_KEY = {'X-Api-App-Id': os.getenv('SUPERJOB_API_KEY')}
    url = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self, text: str, t=None, c=None):
        self.keyword = text
        self.t = t
        self.c = c

    def get_info(self):
        response = requests.get(self.url, headers=self.API_KEY, params=self.__dict__)
        info = response.json()['objects']
        return info