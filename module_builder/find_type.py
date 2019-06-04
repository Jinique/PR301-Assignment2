from abc import ABCMeta, abstractmethod


class FindType:

    @staticmethod
    def find_type(new_type):
        if "string" in new_type:
            print("first check point")
            return TypeStringFactory()
        elif "int" in new_type:
            TypeIntFactory()
        elif "list" in new_type:
            TypeListFactory()
        elif "tuple" in new_type:
            TypeTupleFactory()
        else:
            TypeNoneFactory()


# Product
class Type(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self):
        raise NotImplementedError


# ConcreteProduct A
class TypeString(Type):
    def __str__(self):
        print("third check point")
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
        print("second check point")
        print(TypeString())


# ConcreteCreator B
class TypeIntFactory(Factory):
    def get_type(self):
        TypeInt()


# ConcreteCreator C
class TypeListFactory(Factory):
    def get_type(self):
        TypeList()


# ConcreteCreator D
class TypeTupleFactory(Factory):
    def get_type(self):
        TypeTuple()


# ConcreteCreator E
class TypeNoneFactory(Factory):
    def get_type(self):
        TypeNone()


class Testing:
    def __init__(self):
        self.call()

    def __str__(self):
        return "BBC"

    def call(self):
        return "Abc"


if __name__ == "__main__":  # pragma: no cover
    FindType.find_type("string")
