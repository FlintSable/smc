import unittest
import NNData

class DataMismatchError(Exception):
    """ Custom error place holder """
    pass

class TestNNData(unittest.TestCase):
    def test_data_mismatch(self):
        with self.assertRaises(DataMismatchError):
            NNData.load_data()

if __name__ == "__main__":
    unittest.main()