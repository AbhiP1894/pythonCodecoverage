import unittest
from unittest import mock
import src.myFunction  # Import the module containing the functions

class TestRandomFunctions(unittest.TestCase):

    # def test_sum(self):
    #     # Test the Sum function
    #     result = src.myFunction.Sum(3, 5)
    #     self.assertEqual(result, 8, "Sum should be 8")

    #     result = src.myFunction.Sum(-1, 1)
    #     self.assertEqual(result, 0, "Sum should be 0")

    @mock.patch('src.myFunction.os.urandom')  # Mock os.urandom in the context of src.myFunction
    def test_random(self, urandom_mock):
        # Mock os.urandom to return a predictable value
        urandom_mock.return_value = b'abc'
        
        result = src.myFunction.Random(3)
        self.assertEqual(result, '3abc', "Random output should be '3abc'")

        # Test case with another number
        urandom_mock.return_value = b'xyz'
        result = src.myFunction.Random(4)
        self.assertEqual(result, '4xyz', "Random output should be '4xyz'")

# if __name__ == '__main__':
#     unittest.main()
