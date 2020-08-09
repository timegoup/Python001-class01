from abc import ABCMeta
class Animal(metaclass=ABCMeta):
    def __init__(self, kind, size, character):
        self.kind = kind
        self.size = size
        self.character = character
        # “体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
        self.is_fierce_animal = (self.size in ('中等', '大')) and self.type == '食肉' and self.character == '凶猛'


class Cat(Animal):
    def __init__(self, name, meow):
        self.name = name
        self.meow = meow
    @classmethod
    def fit_pet(self):
        return not self.is_fierce_animal

class Zoo(object):
    animals = []
    def __init__(self, name): 
        self.name = name
    @classmethod
    def addanimal(cls):
        if isinstance(cls, Zoo):
            return('ok')
        else: 
            break


