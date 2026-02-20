from typing import List, Dict, Any


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: List[Dict[str, Any]]) -> List[Person]:
    Person.people = {}

    for person_dict in people_data:
        Person(person_dict["name"], person_dict["age"])

    result_list = []
    for person_dict in people_data:
        name = person_dict["name"]
        person_instance = Person.people[name]

        if person_dict.get("wife"):
            person_instance.wife = Person.people[person_dict["wife"]]
        elif person_dict.get("husband"):
            person_instance.husband = Person.people[person_dict["husband"]]

        result_list.append(person_instance)

    return result_list
