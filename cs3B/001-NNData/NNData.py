from enum import Enum, auto
import numpy as np

class NNData:
    # print("NNData class")



    def __init__(self, features=None, labels=None, train_factor=0.9):
        if features is None:
            self._features = []
        else:
            self._features = features
        if labels is None:
            self._labels = []
        else:
            self._labels = labels

        self._train_factor = NNData.percentage_limiter(train_factor)
        NNData.load_data(features, labels)

    def load_data(features, labels):
        if(len(features) != len(labels)):
           raise DataMismatchError
        if(NNData.features is None):
            NNData.features(None)
            NNData.labels(None)
        else:
            try:
                self._features = np.array(features, dtype=float)
                self._labels = np.array(labels, dtype=float)
            except:
                raise  ValueError

            

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
        return f"output features: {self.features}"

    class Order(Enum):
        RANDOM = auto()
        SEQUENTIAL = auto()
    
    class Set(Enum):
        TRAIN = auto()
        TEST = auto()
    
    @staticmethod
    def percentage_limiter(percentage):
        """ returns 0 if percentage is less than 0
            returns 1 if percentage is greater than 1
            returns percentage if its 0 or 1 or between 0 and 1
        """
        if(not isinstance(percentage, float)):
            try:
                percentage = float(percentage)
            except:
                raise TypeError("could not convert to float")
        
        if(percentage < 0):
            return 0
        elif(percentage < 1):
            return 1
        elif(percentage >= 0 and percentage <=1):
            return percentage

class DataMismatchError(Exception):
    """ Custom error place holder """
    pass        

def main():
    initialize = NNData([1,2,3], [3,3,3])
    initialize.load_data
    print(initialize)


if __name__=="__main__":
    main()