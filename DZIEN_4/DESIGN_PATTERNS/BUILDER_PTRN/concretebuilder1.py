from builder import Builder
from prod1 import Product1

class ConcreteBuilder1(Builder):
    def __init__(self)->None:
        self.reset()
        
    def reset(self):
        self._poduct = Product1()
    @property
    def product(self) -> Product1:
        product = self._poduct
        self.reset()
        return product

    def produce_part_a(self):
        self._poduct.add('PartA1')

    def produce_part_b(self):
        self._poduct.add('PartB1')

    def produce_part_c(self):
        self._poduct.add('PartC1')
