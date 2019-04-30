import unittest
from module_builder.class_builder import ClassBuilder
from module_builder.interpreter import Interpreter
from module_builder.autopep import Pep8Formatter


class MainTests(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        self.file = '../interpreter/class_diagram_plantUML'

    def tearDown(self):
        # be executed after each test case
        print('down')

    def tearDown(self):
        # to be executed after each test case
        print("down")

    # Jin 5
    # Unit test 12 - autopep8
    def test_12(self):
        tester = Pep8Formatter()
        tester.pep8_format('x=            123')
        assert 'x = 123\\n'

    # Unit test 11 - test shelf
    def test_11(self):
        x = Interpreter()
        x.add_file(self.file, "new_module")
        x.shelve_modules('test_shelf')
        assert len(x.my_shelf) > 0

    # Unit test ten
    def test_10(self):
        x = Interpreter()
        x.add_file(self.file, "new_module")
        assert x.all_my_modules[0]

    # Unit test nine - no errors
    def test_09(self):
        x = Interpreter()
        x.add_file(self.file, "new_module")
        x.read_file()
        assert len(x.all_my_errors) is 0
    '''
    # Unit test eight - test modules built
    def test_08(self):
        x = Interpreter()
        x.add_file(self.file, "new_module")
        assert len(x.all_my_modules) > 0

    # Unit test seven - test relationship content found
    def test_07(self):
        x = Interpreter()
        x.add_file(self.file, "new_module")
        assert len(x.my_relationship_content) > 0

    # Unit test Six - test class content list built
    def test_06(self):
        x = Interpreter()
        x.add_file(self.file, "new_module")
        assert len(x.my_class_content) > 0
    '''
    # Unit test five - test file reads
    def test_05(self):
        x = Interpreter()
        x.add_file(self.file, "new_module")
        assert x.my_file is self.file

    # Jin 4
    # Unit Test Four - test relationship list is built
    def test_04(self):
        x = ClassBuilder()
        x.build_class("ClassName",
                      ["attribute1: string"],
                      ["Method1(input):integer"],
                      ("comp", "Class2"))
        assert len(x.relationships) > 0

    # Jin 3
    # Unit Test Three - test method list is built
    def test_03(self):
        x = ClassBuilder()
        x.build_class("ClassName",
                      ["attribute1: string"],
                      ["Method1(input):integer", "Method2(str):hello"],
                      ("extends", "Class2"))
        assert len(x.all_my_methods) is 2

    # Jin 2
    # Unit Test Two - test attribute list is built
    def test_02(self):
        tester = ClassBuilder()
        tester.build_class("ClassName",
                           ["attribute1: string", "attribute2: int"],
                           ["Method1(input):integer"],
                           ("extends", "Class2"))
        assert len(tester.all_my_attributes) is 2

    # Jin 1
    # Unit Test One - test class name is inputted
    def test_01(self):
        tester = ClassBuilder()
        tester.build_class("Name", ["attribute1: string"],
            ["Method1(input):integer"], ("extends", "Class2"))
        assert tester.name is "Name"


if __name__ == '__main__':
    unittest.main(verbosity=2)  # with more details
    # unittest.main()
