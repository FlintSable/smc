from enum import Enum, auto
import numpy as np
import random, math, collections
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
        self._train_factor = NNData.percentage_limiter(train_factor)

        self._train_indices = []
        self._test_indices = []
        self._train_pool = collections.deque()
        self._test_pool = collections.deque()

        try:
            self.load_data(features, labels)
        except (ValueError, DataMismatchError):
            self._features = None
            self._labels = None
            return
        self.split_set()


    def load_data(self, features=None, labels=None):
        """ changes _features and _labels to numpy arrays"""
        if(features is None or labels is None):
            features = []
            labels = []

        if(len(features) != len(labels)):
           raise DataMismatchError("Label and example lists have different lengths")

        try:
            self._features = np.array(features, dtype=float)
            self._labels = np.array(labels, dtype=float)
        except ValueError:
            self._features = []
            self._labels = []
            raise ValueError("Label and example lists must be homogeneous and numeric lists of lists")

    def split_set(self, new_train_factor=None):
        if(new_train_factor is not None):
            self._train_factor = NNData.percentage_limiter(new_train_factor)
            feature_size = len(self._features)
            self._train_indices = random.sample(range(0, feature_size), int(feature_size * self._train_factor))
            self._test_indices = [x for x in range(0, feature_size) if x not in self._train_indices] # maybe change this
            self._train_indices.sort()
            self._test_indices.sort()
    
    def get_one_item(self, target_set=None):
        pass

    def number_of_samples(self, target_set=None):
        pass

    def pool_is_empty(self, target_set=None):
        pass

    def prime_data(self, target_set=None, order=None):
        if(target_set is self.Set.TRAIN):
            if(order is self.Order.RANDOM):
                self._train_pool = random.shuffle(self._train_indices.copy())
                return
            self._train_pool = self._train_indices.copy()
        elif(target_set is self.Set.TEST):
            if(order is self.Order.RANDOM):
                self._test_pool = random.shuffle(self._test_indices.copy())
                return
            self._test_pool = self._test_indices.copy()
        elif(target_set is None):
            if(order is self.Order.RANDOM):
                self._train_pool = self._train_indices.copy()
                # self._train_pool = random.shuffle(self._train_pool)
                # self._test_pool = random.shuffle(self._test_indices.copy())
                self._test_pool = self._test_indices.copy()
            else:
                self._train_pool = self._train_indices.copy()
                self._test_pool = self._test_indices.copy()
        

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
        x = [[i] for i in range(10)]
        y = x
        our_data_0 = NNData(x, y)
        x = [[i] for i in range(100)]
        y = x
        our_big_data = NNData(x, y, .5)

        # Try loading lists of different sizes
        y = [[1]]
        try:
            our_bad_data = NNData()
            our_bad_data.load_data(x, y)
            raise Exception
        except DataMismatchError:
            pass
        except:
            raise Exception

        # Create a dataset that can be used to make sure the
        # features and labels are not confused
        x = [[1.0], [2.0], [3.0], [4.0]]
        y = [[.1], [.2], [.3], [.4]]
        our_data_1 = NNData(x, y, .5)

    except:
        print("There are errors that likely come from __init__ or a "
              "method called by __init__")
        errors = True
    
    # Test split_set to make sure the correct number of examples are in each set, 
    # and that the indicies do not overlap
    try:
        our_data_0.split_set(.3)
        print(f"Train Indicies: {our_data_0._train_indices}")
        print(f"Test Indicies: {our_data_0._test_indices}")

        assert len(our_data_0._train_indices) == 3
        assert len(our_data_0._test_indices) == 7
        assert (list(set(our_data_0._train_indices + our_data_0._test_indices))) == list(range(10))

    except:
        print("There are errors that likely come from split_set")
        errors = True

    # ake sure prime_data sets up the deques correctly, whether
    # sequential or random
    try:
        our_data_0.prime_data(order=NNData.Order.SEQUENTIAL)
        assert len(our_data_0._train_pool) == 3
        assert len(our_data_0._test_pool) == 7
        assert our_data_0._train_indices == list(our_data_0._train_pool)
        assert our_data_0._test_indices == list(our_data_0._test_pool)
        print(our_big_data._train_indices)
        print(list(our_big_data._train_pool))
        our_big_data.prime_data(order=NNData.Order.RANDOM)
        print(our_big_data._train_indices != list(our_big_data._train_pool))
        print(our_big_data._train_indices)
        print(list(our_big_data._train_pool))
        assert our_big_data._train_indices != list(our_big_data._train_pool)
        # assert our_big_data._test_indices != list(our_big_data._test_pool)
    except:
        print("There are errors that likely come from prime_data")
        errors = True
    
    # Make sure get_one_item is returning the correct values, and
    # that pool_is_empty functions correctly.
    # try:
    #     our_data_1.prime_data(order=NNData.Order.SEQUENTIAL)
    #     my_x_list = []
    #     my_y_list = []
    #     while not our_data_1.pool_is_empty():
    #         example = our_data_1.get_one_item()
    #         my_x_list.append(list(example[0]))
    #         my_y_list.append(list(example[1]))
    #     assert my_x_list != my_y_list
    #     my_matched_x_list = [i[0] * 10 for i in my_y_list]
    #     assert my_matched_x_list == my_x_list
    #     assert set(i[0] for i in my_x_list) == set(i[0] for i in x)
    #     assert set(i[0] for i in my_y_list) == set(i[0] for i in y)
    # except:
    #     print("There are errors that may come from prime_data, but could be from another method")
    #     errors = True
    
    # Summary
    if errors:
        print("You have one or more errors. Please fix them before submitting")
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