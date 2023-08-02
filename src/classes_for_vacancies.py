from abc import ABC, abstractmethod
import datetime


class Vac(ABC):
    '''Абс. класс для вакансий'''

    @abstractmethod
    def __init__(self):
        pass


class Vac_for_HH(Vac):
    '''Для вакансий с HH'''
    def __init__(self, info):
        self.url = info['alternate_url']
        self.title = info['name']
        self.city = info['area']['name']
        if info['salary'] == None:
            self.salary_int = 0
            self.salary = 'Зарплата не указана'
        else:
            if info['salary']['from'] != None:
                self.salary_int = info['salary']['from']
                self.salary = f"Зарплата от {info['salary']['from']} {info['salary']['currency']}"
            else:
                self.salary_int = info['salary']['to']
                self.salary = f"Зарплата до {info['salary']['to']} {info['salary']['currency']}"
        self.requirements = f"{info['snippet']['requirement']} {info['snippet']['responsibility']}"
        self.date = self.date_convesion(info['created_at'])

    @staticmethod
    def date_convesion(data):
        data_format = datetime.datetime.strptime(data, '%Y-%m-%dT%H:%M:%S%z')
        return f"Дата создания вакансии: {datetime.datetime.strftime(data_format, '%d %B %Y %H:%M:%S %Z')}"



class JsonVac:
    '''Класс для работы с вакансиями в формате json'''
    def __init__(self, url: str, title: str, city: str, salary_int: int, salary: str, requirements: str, date: str):
        self.url = url
        self.title = title
        self.city = city
        self.salary_int = salary_int
        self.salary = salary
        self.requirements = requirements
        self.date = date

    def __lt__(self, other):
        '''Сравнения вакансий по зарплате'''
        return self.salary_int < other.salary_int