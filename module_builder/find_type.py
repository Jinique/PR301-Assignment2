from abc import ABCMeta, abstractmethod


class FindType:

    @staticmethod
    def find_type(new_type):
        if "string" in new_type:
            return TypeStringFactory()
        elif "int" in new_type:
            return TypeIntFactory()
        elif "list" in new_type:
            return TypeListFactory()
        elif "tuple" in new_type:
            return TypeTupleFactory()
        else:
            return TypeNoneFactory()


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
    def __init__(self):
        self.get_type()

    @abstractmethod
    def get_type(self):
        raise NotImplementedError


# ConcreteCreator A
class TypeStringFactory(Factory):
    def get_type(self):
        print(TypeString())


# ConcreteCreator B
class TypeIntFactory(Factory):
    def get_type(self):
        print(TypeInt())


# ConcreteCreator C
class TypeListFactory(Factory):
    def get_type(self):
        print(TypeList())


# ConcreteCreator D
class TypeTupleFactory(Factory):
    def get_type(self):
        print(TypeTuple())


# ConcreteCreator E
class TypeNoneFactory(Factory):
    def get_type(self):
        print(TypeNone())


if __name__ == "__main__":  # pragma: no cover
    FindType.find_type("string")
    FindType.find_type("int")
