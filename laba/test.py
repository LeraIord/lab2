import main
import unittest


class VectorTest(unittest.TestCase): 
    def test1_vector_dot(self):
        expected = 26
        obtained = main.Vector(1,2,3).dot(main.Vector(3,4,5))
        self.assertEqual(expected, obtained)

    def test2_vector_dot(self):
        expected = -4
        obtained = main.Vector(-2,1,0).dot(main.Vector(3,2,3))
        self.assertEqual(expected, obtained)

    def test3_vector_dot(self):
        expected = 0
        obtained = main.Vector(0,0,0).dot(main.Vector(0,0,0))
        self.assertEqual(expected, obtained)    


    def test1_vector_sub(self):
        expected = main.Vector(-9, -2, -3)
        obtained = main.Vector(1,1,1).__sub__(main.Vector(10,3,4))
        self.assertEqual(expected.getx, obtained.getx)
        self.assertEqual(expected.gety, obtained.gety)
        self.assertEqual(expected.getz, obtained.getz)

    def test2_vector_sub(self):
        expected = main.Vector(4, 3, 0)
        obtained = main.Vector(5,6,7).__sub__(main.Vector(1,3,7))
        self.assertEqual(expected.getx, obtained.getx)
        self.assertEqual(expected.gety, obtained.gety)
        self.assertEqual(expected.getz, obtained.getz)    

    def test3_vector_sub(self):
        expected = main.Vector(0, 0, 0)
        obtained = main.Vector(0,0,0).__sub__(main.Vector(0,0,0))
        self.assertEqual(expected.getx, obtained.getx)
        self.assertEqual(expected.gety, obtained.gety)
        self.assertEqual(expected.getz, obtained.getz) 

    def test1_vector_add(self):
        expected = main.Vector(5, 5, 5)
        obtained = main.Vector(1,1,1).__add__(main.Vector(4,4,4))
        self.assertEqual(expected.getx, obtained.getx)
        self.assertEqual(expected.gety, obtained.gety)
        self.assertEqual(expected.getz, obtained.getz)  

    def test2_vector_add(self):
        expected = main.Vector(2, -2, 420)
        obtained = main.Vector(2,0,120).__add__(main.Vector(0,-2,300))
        self.assertEqual(expected.getx, obtained.getx)
        self.assertEqual(expected.gety, obtained.gety)
        self.assertEqual(expected.getz, obtained.getz)        

    def test3_vector_add(self):
        expected = main.Vector(0, 0, 0)
        obtained = main.Vector(0,0,0).__add__(main.Vector(0,0,0))
        self.assertEqual(expected.getx, obtained.getx)
        self.assertEqual(expected.gety, obtained.gety)
        self.assertEqual(expected.getz, obtained.getz)        

    def test1_vector__product__(self):
        expected = main.Vector(2, 4, 6)
        obtained = main.Vector(1,2,3).__product__(2)
        self.assertEqual(expected.getx, obtained.getx)
        self.assertEqual(expected.gety, obtained.gety)
        self.assertEqual(expected.getz, obtained.getz)
    
    def test2_vector__product__(self):
        expected = main.Vector(26, 0, -108)
        obtained = main.Vector(13,0,-54).__product__(2)
        self.assertEqual(expected.getx, obtained.getx)
        self.assertEqual(expected.gety, obtained.gety)
        self.assertEqual(expected.getz, obtained.getz)

    def test2_vector__product__(self):
        expected = main.Vector(0, 0, 0)
        obtained = main.Vector(0,0,0).__product__(2)
        self.assertEqual(expected.getx, obtained.getx)
        self.assertEqual(expected.gety, obtained.gety)
        self.assertEqual(expected.getz, obtained.getz)



    def test1_vector_modulvector(self):
        expected = 1.4142135623730951
        obtained = main.Vector(-1,1,0).modulvector()       
        self.assertEqual(expected, obtained)

    def test2_vector_modulvector(self):
        expected = 31.68595903550972
        obtained = main.Vector(10,30,-2).modulvector()     
        self.assertEqual(expected, obtained)

    def test3_vector_modulvector(self):
        expected = 0
        obtained = main.Vector(0,0,0).modulvector()     
        self.assertEqual(expected, obtained)          


    def test1_cross_product(self):
        expected = main.Vector(-32, 16, 0)
        obtained = main.Vector(2,4,10).cross_product(main.Vector(4,8,12))
        self.assertEqual(expected.getx, obtained.getx)
        self.assertEqual(expected.gety, obtained.gety)
        self.assertEqual(expected.getz, obtained.getz)

    def test2_cross_product(self):
        expected = main.Vector(-2902, -634, 444)
        obtained = main.Vector(22,-100,1).cross_product(main.Vector(4,2,29))
        self.assertEqual(expected.getx, obtained.getx)
        self.assertEqual(expected.gety, obtained.gety)
        self.assertEqual(expected.getz, obtained.getz)    

    def test3_cross_product(self):
        expected = main.Vector(0, 0, 0)
        obtained = main.Vector(0,0,0).cross_product(main.Vector(0,0,0))
        self.assertEqual(expected.getx, obtained.getx)
        self.assertEqual(expected.gety, obtained.gety)
        self.assertEqual(expected.getz, obtained.getz)   


    def test1_vector_neg(self):
        expected = main.Vector(-1,-2,-3)
        obtained = main.Vector(1,2,3).__neg__()
        self.assertEqual(expected.getx, obtained.getx)
        self.assertEqual(expected.gety, obtained.gety)
        self.assertEqual(expected.getz, obtained.getz)  

    def test2_vector_neg(self):
        expected = main.Vector(0,2,-5)
        obtained = main.Vector(0,-2,5).__neg__()
        self.assertEqual(expected.getx, obtained.getx)
        self.assertEqual(expected.gety, obtained.gety)
        self.assertEqual(expected.getz, obtained.getz)  

    def test3_vector_neg(self):
        expected = main.Vector(0,0,0)
        obtained = main.Vector(0,0,0).__neg__()
        self.assertEqual(expected.getx, obtained.getx)
        self.assertEqual(expected.gety, obtained.gety)
        self.assertEqual(expected.getz, obtained.getz)  


        