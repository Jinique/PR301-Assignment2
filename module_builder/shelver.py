from shelve import open


class Shelver:

    def __init__(self, shelf_file):
        self.my_shelf_file = shelf_file
        self.all_my_shelved_modules = []

    # Jin
    """
    Note Do not rely on the shelf being closed automatically; 
    always call close() explicitly when you don’t need it any more, 
    or use shelve.open() as a context manager:
    
    https://docs.python.org/3/library/shelve.html#module-shelve
    """
    def shelve_modules(self, new_module):
        with open(self.my_shelf_file) as d:
            d[new_module.write_files()[0]] = new_module
            d.close()
