import subprocess


# Jin
class Pep8Formatter:
    @staticmethod
    def pep8_format(line):
        """
        Automatically fixing white spaces to comply with pep8 standard using
        autopep8 package
        >>> from autopep8 import fix_code
        >>> code = ('x=            123')
        >>> print(code)
        x=            123\n
        >>> fix_code(code)
        'x = 123\\n'
        >>>
        """
        try:
            subprocess.call("autopep8 --in-place --aggressive --aggressive "
                            + line)
        except FileNotFoundError:
            print("Requested file is not available")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    from doctest import testmod
    testmod()
