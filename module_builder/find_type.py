from abc import ABCMeta, abstractmethod


class FindType:

    @staticmethod
    def find_type(new_type):
        if "string" in new_type:
            return str(TypeStringFactory())
        elif "int" in new_type:
            return str(TypeIntFactory())
        elif "list" in new_type:
            return str(TypeListFactory())
        elif "tuple" in new_type:
            return str(TypeTupleFactory())
        else:
            return str(TypeNoneFactory())


# Product
class Type(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self):
        raise NotImplementedError


# ConcreteProduct A
class TypeString(Type):
    def __str__(self):
        return "str"


# ConcreteProduct B
class TypeInt(Type):
    def __str__(self):
        return "int"


# ConcreteProduct C
class TypeList(Type):
    def __str__(self):
        return "list"


# ConcreteProduct D
class TypeTuple(Type):
    def __str__(self):
        return "tuple"


# ConcreteProduct E
class TypeNone(Type):
    def __str__(self):
        return ""


# Creator
class Factory(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        NotImplementedError

    def __str__(self):
        return self.value


# ConcreteCreator A
class TypeStringFactory(Factory):
    def __init__(self):
        self.value = str(TypeString())


# ConcreteCreator B
class TypeIntFactory(Factory):
    def __init__(self):
        self.value = str(TypeInt())


# ConcreteCreator C
class TypeListFactory(Factory):
    def __init__(self):
        self.value = str(TypeList())


# ConcreteCreator D
class TypeTupleFactory(Factory):
    def __init__(self):
        self.value = str(TypeTuple())


# ConcreteCreator E
class TypeNoneFactory(Factory):
    def __init__(self):
        self.value = str(TypeNone())


if __name__ == "__main__":  # pragma: no cover
    # print(TypeStringFactory())
    print(TypeString())
    print(TypeStringFactory())
    print(FindType.find_type("string"))
