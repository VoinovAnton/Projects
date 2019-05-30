import random


class Aggregator:

    def __init__(self, lst):
        self.lst = lst
        self.lstres = []
        self.big()
        self.random()
        self.even()
        self.string = ""
        print(self.lstres)

    def big(self):
        for dct in self.lst:
            for key in dct:
                if key == "big":
                    self.lstres.append(dct[key].upper())
                    return self.lstres

    def random(self):
        lstran = []
        str1 = ""
        for dct in self.lst:
            for key in dct:
                if key == "random":
                    for sym in dct[key]:
                        lstran.append(','.join(sym))
                    for sim in lstran:
                        rand = random.randint(0, 1)
                        if rand == 0:
                            str1 += sim.upper()
                        else:
                            str1 += sim
                    self.lstres.append(str1)
                    return self.lstres

    def even(self):
        str1 = ""
        for dct in self.lst:
            for key in dct:
                if key == "even":
                    for i, sym in enumerate(dct[key]):
                        if i % 2 != 0:
                            str1 += str(sym).upper()
                        else:
                            str1 += sym
                    self.lstres.append(str1)
                    return self.lstres


mylist = [
    {"big": "some word"},
    {"random": "another word"},
    {"even": "even word"}
]

agg = Aggregator(mylist)
