from abc import ABC, abstractmethod
import json

class JobFiles(ABC):
    @staticmethod
    def read():
        pass

    @staticmethod
    def write():
        pass


class RAWjson(JobFiles):
    '''Read, add, write to json files'''

    @staticmethod
    def read_json():
        with open('vacancies.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    @staticmethod
    def write_json(data):
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def add_json(data):
        all_data = RAWjson.read_json()
        for i in data:
            all_data.append(i)
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(all_data, file, indent=4, ensure_ascii=False)
