from .playground import Playground

class Zenji:

    def __init__(self, size=5):
        self.size = size
        self.playground = Playground(size)


if __name__ == "__main__":
    
    print('hello world')
    
    zenji = Zenji()

    # print some tiles
    zenji.playground.print()

    print('finished')