class Help:

    @staticmethod
    def help_setup(self):
        print("""
setup default root/source/write_folder
    root : interpreter
    source : class_diagram_plantUML
    write_folder : out
        """)

    @staticmethod
    def help_interpret(self):
        print("""
Translates your SOURCE plantUML file to a python file in the ROOT 
directory provided

    Update ROOT directory: root [folder_name]
    Example : >>> root interpreter

    Update SOURCE file: source [source_file_name]
    Example : >>> source class_diagram_plantUML
""")
        # print("Translates your SOURCE plantUML file to a python file")
        # print("in the ROOT directory provided")
        # print("Update ROOT directory: root [file_location]")
        # print("Update SOURCE file: source [source_file]")

    @staticmethod
    def help_current_setting(self):
        print("displays current path settings on execution")

    @staticmethod
    def help_source(self):
        print("Update SOURCE file: source [source_file]")
        print("This file will be interpreted")

    @staticmethod
    def help_root(self):
        print("Update ROOT directory: root [file_location]")
        print("Files will be read and written to this location")

    @staticmethod
    def help_write_folder(self):
        print("The folder to which your files will be written")
        print("PLEASE create this folder prior to interpreting your file")

    @staticmethod
    def help_check_file(self):
        print("Use this function to check if your file is suitable for translation")

    """
    def help_print_uml(self):
        print("Print your source PlantUML file to a PNG")
    """

    @staticmethod
    def help_i_shelve(self):
        print("Store the class data in a \'shelf\' for later use")

    @staticmethod
    def help_make_db(self):
        print("Save the program data to a database")

    @staticmethod
    def help_pickle(self):
        print("""
Pickles source file in to target file.                
    Syntax : pickle <source file> <target file>                
    Example : pickle test_uml test_uml.dat
        """)

    @staticmethod
    def help_unpickle(self):
        print("""
Unpickles the source file                
    Syntax : unpickle <source file>                
    Example : unpickle test_uml.dat
        """)

    @staticmethod
    def help_convert(self):
        print("""
Interprets plantUML file to a python code file.                
    Syntax : convert <source file> <target folder>                
    Example : convert test_uml ./output
        """)

    @staticmethod
    def help_pep8(self):
        print("""
Fix target file with PEP8 standard. (re:pycodestyle)
    NOTE : original file will be automatically back up to
           filename.extension.bak                
    Syntax : pep8 <source file>                
    Example : pep8 test_format.py
        """)

    @staticmethod
    def help_quit(self):
        print("Quit the program")

    @staticmethod
    def help_cmd(self):
        print("""
            ***Plant UML to Python Interpreter***

            check_file      Checks that the surce file is a text file and that it contains plantUML
            i_shelve        Shelves all the classes in the module as objects
            make_db         Write the module to a database
            source          Sets the source file to interpret
            write_folder    Sets the folder to write the module to
            interpret       Reads the source file, and writes each class to a seperate Python file
            print_uml       Prints a png file of the PlantUML diagram from the source file
            root            Change the root directory for the source file and written files
            quit            Quit the program
            """)
