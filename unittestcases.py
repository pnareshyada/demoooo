import unittest
def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c
m=10
n=5
class PythonUnitTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(m,n),10)
    def test_sub(self):
        self.assertEqual(sub(m,n),5)
    def test_mul(self):
        self.assertEqual(mul(m,n),50)
unittest.main()
