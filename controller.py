from module_builder.interpreter import Interpreter
from module_builder.autopep import Pep8Formatter
from module_builder.pickler import Pickler
# from .junk.database import DbWriter
from cmd import Cmd
# from plantweb.render import render_file
from os import path
import sys
import shutil
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
        self.tempsource = None
        self.temproot = None

    def cmdloop(self, name):
        intro = "Hello " + name + ". Welcome to PlantUML to Python Convertor"
        return Cmd.cmdloop(self, intro)

    # Jin
    def do_current_setting(self, line):
        print(f"""root_directory = {self.root_directory}
write_folder = {self.write_folder}
source_file = {self.source_file}
""")

    def do_interpret(self, line):
        if self.write_folder is None:
            # Jin
            print("""
Please enter the directory to write files to : 
    Syntax : write_folder [folder name]
    Example : write_folder out
    Result : Folder to write files are <root>/[folder name]
    """)
            # print("Please enter the directory to write files to : write_folder xxxx")
        elif self.source_file is None:
            # Jin
            print("Please enter the source file : source [file_name]")
            # print("Please enter the source file : source xxxx")
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

    # Jin
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

    def do_i_shelve(self, line):
        if self.write_folder is None:
            print("Please enter the directory to write files to : write_folder xxxx")
        elif self.source_file is None:
            print("Please enter the source file : source xxxx")
        else:
            uml_shelf = Interpreter()
            uml_shelf.add_file(self.source_file, self.write_folder)
            if self.root_directory:
                uml_shelf.shelve_modules(self.root_directory + "/" + line)
            else:
                uml_shelf.shelve_modules(line)
            print(f"modules shelved to {line}")

    def do_make_db(self, line):
        if self.write_folder is None:
            print("Please enter the directory to write files to : write_folder xxxx")
        elif self.source_file is None:
            print("Please enter the source file : source xxxx")
        else:
            uml_db = Interpreter()
            uml_db.add_file(self.source_file, self.write_folder)
            self.db = uml_db.create_db()

    # Jin
    def file_path(self, line):
        path = []
        for a_path in line.split(' '):
            striped_path = re.sub(' ', '', a_path).strip()
            if striped_path != '':
                path.append(striped_path)
                # print(striped_path)
        return path

    # Jin
    def do_pickle(self, line):
        arg = self.file_path(line)
        if len(arg) == 2:
            pickle = Pickler()
            pickle.pickling(arg[0], arg[1])
            print(f"{arg[0]}", "pickled")
        else:
            print('must have 2 arguments, please use "help" for more info')

    # Jin
    def do_unpickle(self, line):
        arg = self.file_path(line)
        if len(arg) == 1:
            pickle = Pickler()
            data = pickle.unpickling(arg[0])
            print(data)
            print(f"{arg[0]}", "unpickled")
        else:
            print("invalid command. must have 1 args")

    # Jin
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
            '''
            if len(converter.all_my_errors) > 0:
                for an_error in converter.all_my_errors:
                    print(an_error)
            '''
            print("process complete")

    # Jin
    def do_pep8(self, line):
        arg = self.file_path(line)
        if len(arg) == 1:
            formatter = Pep8Formatter()
            source = arg[0]
            dest = source + ".bak"
            shutil.copy(source, dest)
            formatter.pep8_format(source)
            print("Autopep8 complete! original file has been saved to "
                  + dest)
        else:
            print('invalid command. please use "help pep8" for examples')

    def do_quit(self, line):
        print("Closing Down")
        return True
    """
    def do_print_uml(self, line):
        with open(self.source_file, "rt") as my_file:
            contents = my_file.read()
        in_file = self.root_directory + "plant_uml.png"
        with open(in_file, 'wb') as fd:
            fd.write(contents.encode('utf-8'))
        print('==> INPUT FILE:')
        print(in_file)
        outfile = render_file(
            in_file,
            renderopts={
                'engine': 'plantuml',
                'format': 'png'
            },
            cacheopts={
                'use_cache': False
            }
        )
        print('==> OUTPUT FILE:')
        print(outfile)
    """

    # Jin
    def do_setup(self, line):
        from subprocess import run
        # bash = "autopep8 --in-place --aggressive --aggressive " + line
        # import subprocess
        # process = subprocess.Popen(bash.split(), stdout
        #
        # =subprocess.PIPE)
        # output, error = process.communicate()
        # print(output)
        # call("root interpreter")
        # subprocess.call("source class_diagram_plantUML")
        # subprocess.call("write_folder out")
        run(["root interpreter"])


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
