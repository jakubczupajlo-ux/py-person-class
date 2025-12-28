class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = [Person(p.get("name"), p.get("age")) for p in people]

    for p_dict in people:
        instance = Person.people.get(p_dict.get("name"))
        spouse_name = p_dict.get("wife") or p_dict.get("husband")
        spouse_key = "wife" if p_dict.get("wife") else "husband"

        if spouse_name:
            setattr(instance, spouse_key, Person.people.get(spouse_name))

    return person_instances