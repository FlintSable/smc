from enum import Enum, auto
import numpy as np
import random
import unittest

class DataMismatchError(Exception):
    """ Custom error place holder """


class NNData:

    class Order(Enum):
        RANDOM = auto()
        SEQUENTIAL = auto()
    
    class Set(Enum):
        TRAIN = auto()
        TEST = auto()

    @staticmethod
    def percentage_limiter(percentage):
        return min(1, max(percentage, 0))

    def __init__(self, features=None, labels=None, train_factor=.9):
        self._train_indices = []
        self._test_indices = []
        self._train_pool = []
        self._test_pool = []
        self._train_factor = NNData.percentage_limiter(train_factor)
        if features is None:
            features = []
        if labels is None:
            self._labels = []
        self._features = None
        self._labels = None
        try:
            self.load_data(features, labels)
            self.split_set()
        except (ValueError, DataMismatchError):
            pass


    def load_data(self, features=None, labels=None):
        """ changes _features and _labels to numpy arrays"""
        if(len(features) != len(labels)):
           raise DataMismatchError("Label and example lists have different lengths")
        if(features is None or labels is None):
            self._features = None
            self._labels = None
            return

        try:
            self._features = np.array(features, dtype=float)
            self._labels = np.array(labels, dtype=float)
        except ValueError:
            self._features = None
            self._labels = None
            raise ValueError("Label and example lists must be homogeneous and numeric lists of lists")

    def split_set(self, new_train_factor=None):
        if(new_train_factor is not None):
            self._train_factor = NNData.percentage_limiter(new_train_factor)
            feature_size = len(self._features)
            self._train_indices = random.sample(range(0, feature_size), int(feature_size * self._train_factor))
            self._test_indices = [x for x in range(0, feature_size) if x not in self._train_indices]
            self._train_indices.sort()
            self._test_indices.sort()
            # print(self._train_indices)
            # print(self._test_indices)

    @property
    def features(self):
        return self._features
    
    @features.setter
    def features(self, features: [[]]):
        if(features is None):
            self._features = []
        elif(isinstance(features, list) and isinstance(features[0], list)):
            self._features = features
        else:
            self._features = []

    @property
    def labels(self):
        return self._labels

    @labels.setter
    def labels(self, labels: [[]]):
        if(labels is None):
            self._labels = []
        elif(isinstance(labels, list) and isinstance(labels[0], list)):
            self._labels = labels
        else:
            self._labels = []


    def __str__(self):
        return f"features: {self._features} \nlables: {self._labels} \nfactor: {self._train_factor}"



def load_XOR():
    XOR_X = [[0,0], [1,0], [0,1], [1,1]]
    XOR_Y = [[0],[1],[1],[0]]
    new_data = NNData(XOR_X, XOR_Y, 1)

def unit_test():
    errors = False
    try:
        # Create a valid small and large dataset to be used later
        x = list(range(10))
        y = x
        our_data_0 = NNData(x, y)
        print(our_data_0._features)
        x = list(range(100))
        y  = x
        our_big_data = NNData(x, y, .5)

    except:
        print("There are errors that likely com from __init__ or at method called by __init__")
        errors = True

    # Test split_set to make sure the correct number of samples are in
    # each set, and that the indicies do not overlap.
    try:
        our_data_0.split_set(.3)
        assert len(our_data_0._train_indices) == 3
        assert len(our_data_0._test_indices) == 7
        assert (list(set(our_data_0._train_indices + our_data_0._test_indices))) == list(range(10))
    
    except:
        print("There are errors that likely come from split_set")
        errors = True # Summary
    if errors:
        print("You have one or more errors. Please fix them before "
                "submitting")
    else:
        print("No errors were identified by the unit test.")
        print("You should still double check that your code meets spec.")
        print("You should also check that PyCharm does not identify any PEP-8 issues.")

def main():
    load_XOR()
    unit_test()



if __name__=="__main__":
    main()


"""
Sample run

[0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
No errors were identified by the unit test.
You should still double check that your code meets spec.
You should also check that PyCharm does not identify any PEP-8 issues.

"""