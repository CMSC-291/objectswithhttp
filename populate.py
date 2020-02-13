import requests

from anthropod import Anthropod


def combine_crap(piece1=1, piece2=2):
    return piece1 + piece2


if __name__ == '__main__':
    result = requests.get(url="http://github.com")
    # print(result)
    # print(combine_crap(5))
    # print(combine_crap(piece2=5))
    banded_damo = Anthropod(name="Banded demoiselle", url="https://en.wikipedia.org/wiki/Banded_demoiselle")
    print(banded_damo.html)
