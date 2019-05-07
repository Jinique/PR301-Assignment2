from module_builder.interpreter import Interpreter
from cmd import Cmd
from os import path
import sys
import re
from help import Help


class Main(Cmd, Help):

    def __init__(self, username=None, root=None):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.username = username
        self.root_directory = root
        self.write_folder = None
        self.source_file = None
        self.db = None
        # self.tempsource = None
        # self.temproot = None

    def cmdloop(self, name):
        new_name = "Hello " + name + ". "
        intro = new_name + "Welcome to PlantUML to Python Converter"
        return Cmd.cmdloop(self, intro)

    def do_current_setting(self, line):
        print(f"""
root_directory = {self.root_directory}
write_folder = {self.write_folder}
source_file = {self.source_file}
        """)

    def do_interpret(self, line):
        if self.write_folder is None:
            print("""
Please enter the directory to write files to : 
Syntax : write_folder [folder name]
Example : write_folder out
Result : Folder to write files are <root>/[folder name]
            """)
        elif self.source_file is None:
            print("Please enter the source file : source [file_name]")
        else:
            uml = Interpreter()
            uml.add_file(self.source_file, self.write_folder)
            uml.write_modules()
            if len(uml.all_my_errors) > 0:
                for an_error in uml.all_my_errors:
                    print(an_error)
            print("Interpreting complete")
        
    def do_root(self, line):
        """Change the root directory"""
        self.root_directory = line
        if self.source_file:
            self.source_file = self.root_directory + "/" + self.source_file
        print(f"Root directory to read & write files is:  {line}")

    def do_write_folder(self, line):
        """Change the folder to write files directory"""
        if self.root_directory:
            self.write_folder = self.root_directory + "/" + line
            print(f"Folder to write files is: {self.root_directory}/{line}")
        else:
            self.write_folder = line
            print(f"Folder to write files is: {line}")
        
    def do_source(self, line):
        """Change the source file"""
        if self.root_directory:
            self.source_file = self.root_directory + "/" + line
            self.do_check_file(self.source_file)
        else:
            self.source_file = line
            self.do_check_file(self.source_file)

    def do_check_file(self, line):
        try:
            with open(self.source_file, "rt") as my_file:
                if my_file.read().find("@startuml") != -1:
                    if self.root_directory:
                        print(f"Source file to interpret is: {self.root_directory}/{line}")
                    else:
                        print(f"Source file to interpret is: {line}")
                else:
                    print("Error - File must contain plant UML")
                self.check_class()
        except FileNotFoundError:
            print("Error - File not found")
            print(f"looking for file at {self.source_file}")
        except Exception as e:
            print(e)

    def check_class(self):
        try:
            with open(self.source_file, "rt") as new_file:
                content = new_file.read()
                class_count = content.count("class ")
                if class_count < 1:
                    print("there were no class found")
                else:
                    print(f"there are {class_count} class(es) found")
        except FileNotFoundError:
            print("Error - File not found")
        except Exception as e:
            print(e)
        finally:
            print("source file meets minimum requirements")

    def file_path(self, line):
        path = []
        for a_path in line.split(' '):
            striped_path = re.sub(' ', '', a_path).strip()
            if striped_path != '':
                path.append(striped_path)
                # print(striped_path)
        return path

    def do_convert(self, line):
        arg = self.file_path(line)
        try:
            if not path.isfile(arg[0]):
                print(f"{arg[0]} is not a FILE")
            if path.isdir(arg[1]):
                pass
            else:
                print(f"{arg[1]} is not a DIR")
        except Exception as e:
            print(e)
        if len(arg) == 2:
            converter = Interpreter()
            converter.add_file(arg[0], arg[1])
            converter.write_modules()
            """
            if len(converter.all_my_errors) > 0:
                for an_error in converter.all_my_errors:
                    print(an_error)
            """
            print("process complete")

    def do_quit(self, line):
        print("Closing Down")
        return True


if __name__ == '__main__':

    if len(sys.argv) == 2:  # should not have functional code here. eg java main.
        Main().cmdloop(sys.argv[1])  # so should call method from else where
    elif len(sys.argv) == 3:
        name = sys.argv[1] + " " + sys.argv[2]
        Main().cmdloop(name)
    elif len(sys.argv) > 3:
            print("Error : cannot have more than 1 space in your name")
    else:
        Main().cmdloop("")
