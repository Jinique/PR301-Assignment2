class Help:

    def help_interpret(self):
        print("Translates your SOURCE plantUML file to a python file in the")
        print("ROOT directory provided")
        print("Update ROOT directory: root [folder_name]")
        print("Example : >>> root interpreter")
        print("Update SOURCE file: source [source_file_name]")
        print("Example : >>> source class_diagram_plantUML")

    def help_source(self):
        print("Update SOURCE file: source [source_file]")
        print("This file will be interpreted")

    def help_root(self):
        print("Update ROOT directory: root [file_location]")
        print("Files will be read and written to this location")

    def help_write_folder(self):
        print("The folder to which your files will be written")
        print("PLEASE create this folder prior to interpreting your file")

    def help_check_file(self):
        print("Use this function to check if your file is suitable for translation")

    def help_convert(self):
        print("Interprets plantUML file to a python code file.")
        print("Syntax : convert <source file> <target folder>")
        print("Example : convert test_uml ./output")

    def help_quit(self):
        print("Quit the program")
