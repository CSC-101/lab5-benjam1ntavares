from http.cookiejar import uppercase_escaped_char

import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    # arbitrary test of the add_time function
    def test_add_time1(self):
        time1 = data.Time(1,23,45)
        time2 = data.Time(1,23,45)
        expected = data.Time(2,47,30)
        actual = lab5.time_add(time1,time2)
        self.assertEqual(expected,actual)


    # check to make sure the hours and minutes will change if there is a large number of seconds or a large number of
    # minutes
    def test_add_time2(self):
        time1 = data.Time(0,0,100000000)
        time2 = data.Time(0,0,0)
        expected = data.Time(27777,46,40)
        actual = lab5.time_add(time1,time2)
        self.assertEqual(expected,actual)
    # Part 4
    # test to see if input list can actually detect lists in decending order


    # False test
    def test_is_decending1(self):
        input_list = [1,2,3,4,5]
        expected = False
        actual = lab5.is_decending(input_list)
        self.assertEqual(expected,actual)
    # True Test
    def test_is_decending2(self):
        input_list = [5,4,3,2,1]
        expected = True
        actual = lab5.is_decending(input_list)
        self.assertEqual(expected,actual)
    # Float and negative tests
    def test_is_decending3(self):
        input_list = [-1.1, -2.2, -3.3, -4.4, -5.5]
        expected = True
        actual = lab5.is_decending(input_list)
        self.assertEqual(expected,actual)

    # Part 5

    def test_largest_between1(self):
        numbers = [1,2,3,4,5]
        upper = 4
        lower = 1
        expected = 4 # 4 is the index of 5, the largest number
        actual = lab5.largest_between(numbers,lower,upper)
        self.assertEqual(expected,actual)

    # test largest between with invalid range, lower>upper
    def test_largest_between2(self):
        numbers = [1,2,3,4,5]
        upper = 1
        lower = 4
        expected = 4 # 4 is the index of 5, the largest number
        actual = lab5.largest_between(numbers,lower,upper)
        self.assertEqual(expected,actual)

    # test largest between with range of one value
    def test_largest_between3(self):
        numbers = [1, 2, 3, 4, 5]
        upper = 1
        lower = 1
        expected = 1
        actual = lab5.largest_between(numbers, lower,upper)
        self.assertEqual(expected, actual)

    # test largest between with longer, arbitrary list

    def test_largest_between4(self):
        numbers = [3, 8, 4, 12, 5, 10, 6]
        upper = 5
        lower = 2
        expected = 3
        actual = lab5.largest_between(numbers, lower,upper)
        self.assertEqual(expected, actual)

    # test out of range
    def test_largest_between5(self):
        numbers = [3, 8, 4, 12, 5, 10, 6]
        upper = 10
        lower = 11
        expected = 6



    # Part 6





if __name__ == '__main__':
    unittest.main()
