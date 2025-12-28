class Person:
    # Atrybut klasowy przechowujący wszystkie instancje
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        # Dodawanie instancji do słownika klasowego przy inicjalizacji
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Faza 1: Tworzymy wszystkie instancje Person
    # Dzięki temu Person.people zostanie wypełnione wszystkimi obiektami
    for person_dict in people:
        Person(person_dict["name"], person_dict["age"])

    result_list = []

    # Faza 2: Łączymy małżonków i budujemy listę wynikową
    for person_dict in people:
        name = person_dict["name"]
        instance = Person.people[name]
        
        # Sprawdzamy, czy w słowniku jest klucz 'wife' lub 'husband'
        spouse_key = "wife" if "wife" in person_dict else "husband"
        spouse_name = person_dict.get(spouse_key)

        # Jeśli małżonek istnieje (nie jest None), przypisujemy link do obiektu
        if spouse_name is not None:
            # Używamy setattr, aby dynamicznie ustawić atrybut 'wife' lub 'husband'
            setattr(instance, spouse_key, Person.people[spouse_name])
        
        result_list.append(instance)

    return result_list
