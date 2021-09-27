import os
import csv
from collections import defaultdict


ARGS = {
    'file_path': 'Corp_Summary.csv',
    'save_path': './'
}


def add_team_to_depart(department_teams: dict, department: str, team: str) -> int:
    """величиваем на 1 количество сотрудников в команде team, принадлежащей департаменту department"""

    if team not in department_teams[department]:
        return 1
    else:
        return department_teams[department][team] +  1


def get_department_number(department_info: dict, department: str) -> int:
    """Считаем сотрудников в департаменте department"""

    return department_info[department]['number'] + 1


def get_total_salary(department_info: dict, department: str, salary: float) -> float:
    """Считаем суммарную зп департамента"""

    return department_info[department]['total_salary'] + salary


def get_min_salary(department_info: dict, department: str, salary: float) -> float:
    """Считаем минимальную зп"""

    if 'min_salary' not in department_info[department]:
        return salary
    else:
        return min(department_info[department]['min_salary'], salary)
        

def get_max_salary(department_info: dict, department: str, salary: float) -> float:
    """Считаем максимальную зп"""

    return max(department_info[department]['min_salary'], salary)


def get_mean_salary(department_info: dict, department: str) -> float:
    """Считаем среднюю зп"""

    return department_info[department]['total_salary'] / department_info[department]['number']


def update_department_info(department_info: dict, department_teams: dict, person_details: dict) -> list([dict, dict]):
    """Обновляем информацию по департаментам"""

    department = person_details['Департамент']
    salary = float(person_details['Оклад'])
    team = person_details['Отдел']
    
    if department not in department_info:
        department_info[department] = defaultdict(number=0,  max_salary=0., total_salary=0.)

    department_info[department]['number'] = get_department_number(department_info, department)
    department_info[department]['total_salary'] = get_total_salary(department_info, department, salary)
    department_info[department]['min_salary'] = get_min_salary(department_info, department, salary)
    department_info[department]['max_salary'] = get_max_salary(department_info, department, salary)    
    department_teams[department][team] = add_team_to_depart(department_teams, department, team)
    
    return department_info, department_teams
    
    
def display_department_teams(department_teams: dict) -> None:
    """Выводим информацию о командах внутри департамента.
    Департаменты сортируем по алфавиту.
    Команды сортируем по размеру (по убыванию)."""

    print('\nИерархия команд (размер):')
    for i, (department, teams) in enumerate(sorted(department_teams.items(), key=lambda items: items[0])):
        print(f'{i+1}. {department.upper()}:')
        for j, (team, number) in enumerate(sorted(teams.items(), key=lambda items: -items[1])):
            print(f'\t{j+1}. {team} ({number})')
        print()


def display_department_info(department_info: dict) -> None:
    """Выводим информацию по департаментам"""
    
    print('\nИнформация по департаментам:')
    for i, (department, info) in enumerate(sorted(department_info.items(), key=lambda items: items[0])):
        print(f"""{i + 1}. {department.upper()}
        Численность: {info['number']}
        Вилка: {info['min_salary']} - {info['max_salary']}
        Средняя з/п: {info['mean_salary'] :.1f}\n""")


def create_dict_for_writer(idx:int, department: str, info: dict) -> dict:
    """Создаем строку для writer"""

    return {
        'id': idx,
        'number': info['number'], 
        'department': department, 
        'min_salary': info['min_salary'],
        'max_salary': info['max_salary'], 
        'mean_salary': info['mean_salary']
    }


def get_save_path(save_path: str) -> str:
    """Путь для сохранения информации по департаментам """

    do = 1
    while do:
        print('\nВведите путь до директории или оставьте поле пустым:')
        save_path = input()
        if save_path == '':
            do = 0
        elif  os.path.isfile(save_path):
            print(f'{save_path} не директория')
        else:
            if  not os.path.exists(save_path):
                os.mkdir(save_path)
            do = 0
    return os.path.join(save_path, 'out.csv')
    

def save_department_info(department_info: dict, save_path: str) -> str:
    """Сохраняем информацию по департаментам в save_path"""

    header = ['id', 'department', 'number', 'min_salary', 'max_salary', 'mean_salary']
    save_path = get_save_path(save_path)
    with open(save_path, 'w', newline='') as csvfile:
        file_writer = csv.DictWriter(csvfile, header, delimiter=';')
        file_writer.writeheader()
        
        for i, department  in enumerate(sorted(department_info.keys())):
                row_dict = create_dict_for_writer(i+1, department, department_info[department])
                file_writer.writerow(row_dict)
    return save_path
    

def choose_option() -> str:
    """Выводим меню и выбираем из 3х опций """
    action = ''
    options = ['1', '2', '3']

    while action not in options:
        print('\nВыберите')
        print('1. Вывести иерархию команд')
        print('2. Вывести сводный отчёт по департаментам')
        print('3. Сохранить сводный отчёт')
        action = input()
    return action


def stop() -> bool:
    """Останавливаемся или продолжаем выбор из 3х опций"""

    finish = ''
    while finish not in ('yes', 'no'):
        print('Завершить (yes == пустая строка / no)?')
        finish = input()
        if finish in ('yes', ''):
            return True
        elif finish == 'no':
            return False


def main(args):
    finish = False
    department_info = defaultdict(dict)
    department_teams = defaultdict(dict)
    
    with open(args['file_path']) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for person_details in reader:
            department_info, department_teams = update_department_info(department_info, department_teams, person_details)

    for department in department_info:
        department_info[department]['mean_salary'] = get_mean_salary(department_info, department)

    while not finish:
        action = choose_option()
        
        if action == '1':
            display_department_teams(department_teams) 
        elif action == '2':
            display_department_info(department_info)
        elif action == '3':
            save_path = save_department_info(department_info, args['save_path'])
            print(f'Файл сохранен: {save_path}\n')
        
        finish = stop()


if __name__ == '__main__':
    main(ARGS)

    