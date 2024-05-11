from domain.Person import Person


class Test:

    person = Person(None,  None,  None, None, None)

    person.create_person()
    print(person._str_())