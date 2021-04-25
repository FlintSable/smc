import numpy as np
from enum import Enum


class DataMismatchError(Exception):
    """ Label and example lists have different lengths"""


class NNData:

    class Order(Enum):
        RANDOM = 0
        SEQUENTIAL = 1

    class Set(Enum):
        TRAIN = 0
        TEST = 1

    @staticmethod
    def percentage_limiter(factor):
        return min(1, max(factor, 0))

    def __init__(self, features=None, labels=None, train_factor=.9):
        self._train_factor = NNData.percentage_limiter(train_factor)
        if features is None:
            features = []
        if labels is None:
            labels = []
        self._features = None
        self._labels = None
        try:
            self.load_data(features, labels)
        except (ValueError, DataMismatchError):
            pass

    def load_data(self, features=None, labels=None):
        if features is None or labels is None:
            self._features = None
            self._labels = None
            return
        if len(features) != len(labels):
            raise DataMismatchError("Label and example lists have "
                                         "different lengths")

        try:
            self._features = np.array(features, dtype=float)
            self._labels = np.array(labels, dtype=float)
        except ValueError:
            self._features = None
            self._labels = None
            raise ValueError("Label and example lists must be homogeneous "
                             "and numeric lists of lists")


def load_XOR():
    XOR_X = [[0,0],[0,1],[1,0],[1,1]]
    XOR_Y = [[0],[1],[1],[0]]
    data = NNData(XOR_X, XOR_Y, 1)
