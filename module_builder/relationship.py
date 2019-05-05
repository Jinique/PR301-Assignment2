class Relationship:
    # Jin  -- 6 doctest


    def __init__(self, new_type):
        # Jin
        self.name = new_type[1]
        # self.name = new_type[1].lower()
        self.type = new_type[0]

    def __str__(self):
        return f"{self.name}s"


if __name__ == "__main__":
    from doctest import testmod
    testmod()
