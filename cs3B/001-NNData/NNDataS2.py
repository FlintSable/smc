import random, math, collections
from enum import Enum
import numpy as np

class DataMismatchError(Exception):d4
    """ Label and example lists have different lengths """

class NNData:
    class Order(Enu):
        RANDOM = 0
        SEQUENTIAL = 1
    
    class Set(Enum):
        TRAIN = 0
        TEST = 1
    
    @staticmethod
    def percentage_limiter(factor):
        return min(1, max(factor, 0))

    def __init__(self, features=None, labels=None, train_factor=.9):
