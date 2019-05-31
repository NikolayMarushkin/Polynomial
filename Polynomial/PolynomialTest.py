from unittest import TestCase, main
from Polynomial import Polynomial

class PolynomialTest(TestCase):

    def setup_method(self):
        self.Poly1 = Polynomial([-2, -1, 4])
        self.Poly2 = Polynomial([3, 2, 1, -4])
        self.Poly3 = Polynomial([-2, 3])
        self.Poly4 = Polynomial([8, -3, 4, 5])

    def test_sum(self):
        self.setup_method()

        Test_1_1 = self.Poly1 + self.Poly1
        Out_1_1 = [-4, -2, 8]
        Test_1_2 = self.Poly1 + self.Poly2
        Out_1_2 = [3, 0, 0, 0]
        Test_1_3 = self.Poly1 + self.Poly3
        Out_1_3 = [-2, -3, 7]
        Test_1_4 = self.Poly1 + self.Poly4
        Out_1_4 = [8, -5, 3, 9]
             
        assert Test_1_1 == Polynomial(Out_1_1)
        assert Test_1_2 == Polynomial(Out_1_2)
        assert Test_1_3 == Polynomial(Out_1_3)
        assert Test_1_4 == Polynomial(Out_1_4)
        
    def test_sum_right_const(self):
        self.setup_method()
        
        Test_1__1_8 = self.Poly1 + 1.8
        Out_1__1_8 = [-2, -1, 5.8]
        
        assert Test_1__1_8 == Polynomial(Out_1__1_8)

    def test_sum_left_const(self):
        self.setup_method()
     
        Test_1__1_8 = 1.8 + self.Poly1
        Out_1__1_8 = [-2, -1, 5.8]

        assert Test_1__1_8 == Polynomial(Out_1__1_8)

    def test_sub(self):
        self.setup_method()

        Test_1_1 = self.Poly1 - self.Poly1
        Out_1_1 = [0]
        Test_1_2 = self.Poly1 - self.Poly2
        Out_1_2 = [-3, -4, -2, 8]
        Test_1_3 = self.Poly1 - self.Poly3
        Out_1_3 = [-2, 1, 1]
        Test_1_4 = self.Poly1 - self.Poly4
        Out_1_4 = [-8, 1, -5, -1]
         
        assert Test_1_1 == Polynomial(Out_1_1)
        assert Test_1_2 == Polynomial(Out_1_2)
        assert Test_1_3 == Polynomial(Out_1_3)
        assert Test_1_4 == Polynomial(Out_1_4)

    def test_mul(self):
        self.setup_method()

        Test_1_1 = self.Poly1 * self.Poly1
        Out_1_1 = [4, 4, -15, -8, 16]
        Test_1_2 = self.Poly1 * self.Poly2
        Out_1_2 = [-6, -7, 8, 15, 8, -16]
        
              
        assert Test_1_1 == Polynomial(Out_1_1)
        assert Test_1_2 == Polynomial(Out_1_2)

    def test_mul_left_const(self):
        self.setup_method()

        Test_1 = 1 * self.Poly1
        Out_1 = [-2, -1, 4]     
        Test_2 = 0 * self.Poly2
        Out_2 = [0]
        Test_3 = 4 * self.Poly3
        Out_3 = [-8, 12]

        assert Test_1 == Polynomial(Out_1)        
        assert Test_2 == Polynomial(Out_2)
        assert Test_3 == Polynomial(Out_3)
        
    def test_mul_right_const(self):
        self.setup_method()

        Test_1 = self.Poly1 * 1
        Out_1 = [-2, -1, 4]     
        Test_2 = self.Poly2 * 0
        Out_2 = [0]
        Test_3 = self.Poly3 * 4
        Out_3 = [-8, 12]

        assert Test_1 == Polynomial(Out_1)        
        assert Test_2 == Polynomial(Out_2)
        assert Test_3 == Polynomial(Out_3)   
        
    def test_eq(self):
        self.setup_method()

        Test_1 = self.Poly1
        Out_1 = [-2, -1, 4]
     
        assert Test_1 == Polynomial(Out_1)

    def test_ne(self):
        self.setup_method()

        Test_1 = self.Poly1
        Out_1 = [-2, -1, -4]

        assert Test_1 != Polynomial(Out_1)
            
    def test_type(self):
        self.setup_method()

        with self.assertRaises(TypeError):
            "a" + self.Poly1
        with self.assertRaises(TypeError):
            "b" == self.Poly1
        with self.assertRaises(TypeError):
            "c" != self.Poly1
        with self.assertRaises(TypeError):
            "d" - self.Poly1
        with self.assertRaises(TypeError):
            "e" * self.Poly1
        with self.assertRaises(TypeError):
            self.Poly1 + "a"
        with self.assertRaises(TypeError):
            self.Poly1 == "b"
        with self.assertRaises(TypeError):
            self.Poly1 != "c"
        with self.assertRaises(TypeError):
            self.Poly1 - "d"
        with self.assertRaises(TypeError):
            self.Poly1 * "e"

    def test_str(self):
        self.setup_method()

        assert str(self.Poly1) == "-2x^2-x+4"

    def test_incorrect_coeffs(self):
        self.assertRaises(TypeError, Polynomial, ["1", 1])

if __name__ == '__main__':
    main()
