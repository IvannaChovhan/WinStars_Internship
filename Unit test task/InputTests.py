import unittest
from math import floor
import numpy as np


class InputTests(unittest.TestCase):

    def setUp(self):
        '''
        Reading data from file
        '''
        self.data = np.genfromtxt('nba2k20-full_preprocess.csv', delimiter=',')

    def test_number_of_columns(self):
        '''
        Testing number of columns
        '''
        self.assertEqual(83, self.data.shape[1])

    def test_data_normalization(self):
        '''
        Testing if data is normalized
        '''
        self.data = self.data.T
        for i in range(self.data.shape[0]):
            self.assertEqual(round(np.std(self.data[i])), 0)
            self.assertEqual(floor(np.mean(self.data[i])), 0)

    def test_datatype_columns(self):
        '''
        Testing datatype of each column
        '''
        self.assertEqual(np.float64, type(self.data[0, 0]))

    def test_datatype_dataset(self):
        '''
        Testing if data is multidimensional array
        '''
        self.assertEqual(np.ndarray, type(self.data))


if __name__ == '__main__':
    unittest.main()
