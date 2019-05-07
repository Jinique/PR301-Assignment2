import re
from module_builder.class_builder import ClassBuilder
from module_builder.module import Module


class Interpreter:

    language = "Plant UML"

    def __init__(self):
        self.my_file = ""
        self.my_shelf = None
        self.my_class_content = []
        self.my_relationship_content = ""
        self.all_my_classbuilders = []
        self.all_my_modules = []
        self.all_my_errors = []
        self.my_db = None

    def add_file(self, file_name, new_module_name):
        self.my_file = file_name
        self.read_file()
        self.find_classes()
        self.add_module(new_module_name, self.all_my_classbuilders)

    def read_file(self):
        try:
            with open(self.my_file, "rt") as my_file:
                contents = my_file.read()
                class_results = re.split(r"}", contents)
                self.my_relationship_content = \
                    class_results[len(class_results) - 1]
                class_results.remove(class_results[len(class_results) - 1])
                for result in class_results:
                    self.my_class_content.append(result)
        except FileNotFoundError as e:
            self.all_my_errors.append(e)
            print("Error - File not found")

    @staticmethod
    def find_relationship(relationship, class_name):
        if relationship.startswith(class_name):
            if re.search(r"\*--", relationship):
                com_class = relationship.split(" ")[2]
                return tuple(("comp", com_class))
            if re.search(r"--", relationship):
                as_class = relationship.split(" ")[2]
                return tuple(("assos", as_class))
        elif relationship.endswith(class_name):
            if re.search(r"<\|--", relationship):
                ext_class = relationship.split(" ")[0]
                return tuple(("extends", ext_class))

    def add_class(self, class_name, attributes, methods, relationships):
        new_class = ClassBuilder()
        new_class.build_class(class_name, attributes, methods, relationships)
        self.all_my_classbuilders.append(new_class)

    def find_classes(self):
        for class_info in self.my_class_content:
            class_name = class_info.split(" ")[1]
            attributes = self.get_attribute(class_info)
            methods = self.get_method(class_info)
            relationships = self.get_relationship(class_name)
            self.add_class(class_name, attributes, methods, relationships)

    @staticmethod
    def get_attribute(class_info):
        attributes = []
        for line in class_info.split("\n"):
            if line.find(":") != -1 and line.find("(") == -1:
                attributes.append(line)
        return attributes

    @staticmethod
    def get_method(class_info):
        methods = []
        for line in class_info.split("\n"):
            if line.find("(") != -1:
                methods.append(line)
        return methods

    def get_relationship(self, class_name):
        relationships = []
        for relationship in self.my_relationship_content.split("\n"):
            if self.find_relationship(relationship, class_name):
                relationships.append(self.find_relationship(relationship,
                                                            class_name))
        return relationships

    def add_module(self, new_module_name, new_classes):
        new_module = Module()
        new_module.create_module(new_module_name, new_classes)
        self.all_my_modules.append(new_module)

    def write_modules(self):
        for a_module in self.all_my_modules:
            root_name = a_module.write_files()[0]
            folder_content = a_module.write_files()[1]
            for a_folder in folder_content:
                try:
                    file_name = f"{root_name}/{a_folder[0]}"
                    with open(file_name, "w+") as f:
                        f.write(a_folder[1])
                except FileNotFoundError as e:
                    self.all_my_errors.append(e)
                    print("Error - Directory does not exist")
