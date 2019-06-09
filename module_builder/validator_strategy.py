from abc import ABCMeta, abstractmethod


class Validator:
    def __init__(self, validator):
        self.validate_method = validator

    def run(self, file, root, line):
        self.validate_method.validate(file, root, line)


class AbstractValidator(metaclass=ABCMeta):
    @abstractmethod
    def validate(self, file, root, line):
        pass


class FileValidator(AbstractValidator):
    def validate(self, file, root, line):
        try:
            with open(file, "rt") as my_file:
                if my_file.read().find("@startuml") != -1:
                    if root:
                        print(
                            f"Source file to interpret is: "
                            f"{root}/{line}"
                        )
                    else:
                        print(f"Source file to interpret is: {line}")
                else:
                    print("Error - File must contain plant UML")
                # self.check_class()
        except FileNotFoundError:
            print("Error - File not found")
            print(f"looking for file at {file}")
        except Exception as e:  # pragma: no cover
            print(e)


class ClassValidator(AbstractValidator):
    def validate(self, file, root, line):
        try:
            with open(file, "rt") as new_file:
                content = new_file.read()
                class_count = content.count("class ")
                if class_count < 1:
                    print("there were no class found")
                else:
                    print(f"there are {class_count} class(es) found")
        # except FileNotFoundError:
        #     print("Error - File not found")
        except Exception as e:  # pragma: no cover
            print(e)
        finally:
            print("source file meets minimum requirements")
