from sys import argv

from classes.demo import demo
from utils.Terminal import Terminal


def main():
    Terminal.clear()

    DEMO = demo()
    DEMO.long_method(10)

    print(argv[1])


# Lancer la fonction main
if __name__ == '__main__':
    main()
