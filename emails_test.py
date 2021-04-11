#!/usr/bin/env python3

import unittest
from emails import find_email

class EmailsTest(unittest.TestCase):
    """test_basic tests a simple case where expected parameters are chosen, such as the first and las name
    of a person in the csv file"""
    def test_basic(self):
        """The script file is the first element of input parameters thorugh command line using argv since
        we already imported the function find_email from emails.py earlier, we will pass None in the place
        of the script. Adding to None, we will pass the first name and last name as parameters"""
        testcase = [None, "Blossom", "Gill"]                # First name "Blossom", Last name "Gill"
        expected = "blossom@abc.edu"                        # Blossom Gill's email is 'blossom@abc.edu'
        self.assertEqual(find_email(testcase), expected)
    
    """Tests one name/parameter only (as opposed to two) which should output 'Missing parameters'"""
    def test_one_name(self):
        testcase = [None, "John"]
        expected = "Missing parameters"
        self.assertEqual(find_email(testcase), expected)
    
    """Tests the full name of a user who is not in the list with expected output 'No email address found'"""
    def test_two_name(self):
        testcase = [None, "Roy", "Cooper"]
        expected = "No email address found"
        self.assertEqual(find_email(testcase), expected)
    
    """test_empty tests that if no parameters are passed, the script should return nothing"""
    def test_empty(self):
        testcase = ""
        expected = "Missing parameters"
        self.assertEqual(find_email(testcase), expected)
    
    """Tests an integer input"""
    def test_numbers(self):
        testcase = [None, 5, 6]
        expected = "Parameters can only be letters"
        self.assertEqual(find_email(testcase), expected)

if __name__ == '__main__':
    unittest.main()
