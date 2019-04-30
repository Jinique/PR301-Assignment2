from pickle import dump, load, HIGHEST_PROTOCOL


class Pickler:

    """Picking a object and output to a file.
    >>> import pickle
    >>> scores = {'korean': 90, 'english': 95, 'mathematics': 85}

    # >>> with open('test.txt', 'wb') as file:
    # ... pickle.dump(scores, file)
    """

    # >>> pickle.dump(list, f)
    @staticmethod
    def pickling(new_object, outfile):
        with open(outfile, 'wb+') as f:
            dump(new_object, f, HIGHEST_PROTOCOL)
            # implement try catch on everything;
            # for data in new_object:
            #     dump(data, f, HIGHEST_PROTOCOL)
            f.close()

    @staticmethod
    def unpickling(source):
        with open(source, "rb") as f:
            data_list = []
            while True:  # while True << BAD practice
                try:
                    data = load(f)
                except EOFError:
                    break
                data_list.append(data)
        print(data_list)
        f.close()


if __name__ == "__main__":
    from doctest import testmod
    testmod()
