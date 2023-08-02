from src.utils import WorkWithUser
from src.job_json import RAWjson


def get_user(user: WorkWithUser, count: int):
    '''Выполняет запрос'''

    user.choice_site()  # выбор ресурса
    user.get_request()  # запрос
    user.city_choice()  # Выбор региона для поиска вакансий
    user.number()  # Количество вакансий

    print(f'\n{user}')  # Показывает запрос

    user.api(count)


def repeat_get(user: WorkWithUser):
    '''Повторяет запрос'''

    while True:
        try:
            choice_user = int(input('\n1 - Да\n2 - Нет\nХотите повторить запрос?'))
            if choice_user == 1:
                get_user(user, 1)
            elif choice_user == 2:
                break
            else:
                raise ValueError
        except ValueError:
            print("Ошибка ввода")


def find_get(user: WorkWithUser):
    while True:
        try:
            choice_user = int(input('\n1 - Да\n2 - Нет\nХотите найти ключевое слово в вакансиях?'))
            if choice_user == 1:
                data = input('Введите Ваш запрос: ')
                print(user.word_finder(data))
            elif choice_user == 2:
                break
            else:
                raise ValueError
        except ValueError:
            print("Ошибка ввода")


def main():

    while input('Нажмите Enter, чтобы начать: ') != '':
        continue

    f = open('vacancies.json', 'w')
    f.close()

    print('\nЗдравствуйте! Подготовим Ваш запрос по поиску вакансий.')

    user = WorkWithUser()

    get_user(user, 0)
    repeat_get(user)
    WorkWithUser.sort_all()
    find_get(user)

    if not RAWjson.read_json():
        print('\nПо Вашему запросу ничего не найдено')
    else:
        print('\nСписок вакансий отсортированных по зарплате Вы можете посмотреть в файле - vacancies.json')
    print('\nХорошего дня!')


if __name__ == "__main__":
    main()