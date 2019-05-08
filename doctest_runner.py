def test():
    import doctest
    doctest.testfile('doctest_files/doctest_attribute', verbose=1)
    doctest.testfile('doctest_files/doctest_class_builder', verbose=1)
    doctest.testfile('doctest_files/doctest_interpreter', verbose=1)
    doctest.testfile('doctest_files/doctest_method', verbose=1)
    doctest.testfile('doctest_files/doctest_module', verbose=1)
    doctest.testfile('doctest_files/doctest_relationship', verbose=1)
    doctest.testfile('doctest_files/doctest_controller', verbose=1)
    doctest.testfile('doctest_files/doctest_find_type', verbose=1)


if __name__ == "__main__":
    test()
