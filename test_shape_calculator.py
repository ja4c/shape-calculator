import unittest

from shape_calculator import Rectangle, Square


class TestRectangle(unittest.TestCase):
    def test_initialization_and_string(self):
        self.assertEqual(str(Rectangle(3, 6)), "Rectangle(width=3, height=6)")

    def test_area_perimeter_diagonal(self):
        rectangle = Rectangle(3, 6)
        self.assertEqual(rectangle.get_area(), 18)
        self.assertEqual(rectangle.get_perimeter(), 18)
        self.assertAlmostEqual(rectangle.get_diagonal(), 6.708203932499369)

    def test_setters(self):
        rectangle = Rectangle(3, 6)
        rectangle.set_width(5)
        rectangle.set_height(4)
        self.assertEqual(str(rectangle), "Rectangle(width=5, height=4)")

    def test_picture(self):
        self.assertEqual(Rectangle(3, 2).get_picture(), "***\n***\n")
        self.assertEqual(Rectangle(51, 2).get_picture(), "Too big for picture.")

    def test_amount_inside(self):
        self.assertEqual(Rectangle(15, 10).get_amount_inside(Square(5)), 6)
        self.assertEqual(Rectangle(4, 8).get_amount_inside(Rectangle(3, 6)), 1)
        self.assertEqual(Rectangle(2, 3).get_amount_inside(Rectangle(3, 6)), 0)


class TestSquare(unittest.TestCase):
    def test_initialization_and_string(self):
        square = Square(5)
        self.assertEqual(str(square), "Square(side=5)")
        self.assertIsInstance(square, Rectangle)
        self.assertIsInstance(square, Square)

    def test_inherited_calculations(self):
        square = Square(5)
        self.assertEqual(square.get_area(), 25)
        self.assertEqual(square.get_perimeter(), 20)
        self.assertAlmostEqual(square.get_diagonal(), 7.0710678118654755)

    def test_set_side(self):
        square = Square(5)
        square.set_side(4)
        self.assertEqual(str(square), "Square(side=4)")
        self.assertEqual(square.width, 4)
        self.assertEqual(square.height, 4)

    def test_set_width_and_height_keep_square(self):
        square = Square(5)
        square.set_width(7)
        self.assertEqual((square.width, square.height), (7, 7))
        square.set_height(3)
        self.assertEqual((square.width, square.height), (3, 3))

    def test_picture(self):
        self.assertEqual(Square(2).get_picture(), "**\n**\n")


if __name__ == "__main__":
    unittest.main()
