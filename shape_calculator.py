class Rectangle:
    """Represent a rectangle with a width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        """Set the rectangle's width."""
        self.width = width

    def set_height(self, height):
        """Set the rectangle's height."""
        self.height = height

    def get_area(self):
        """Return the rectangle's area."""
        return self.width * self.height

    def get_perimeter(self):
        """Return the rectangle's perimeter."""
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        """Return the rectangle's diagonal length."""
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        """Return an ASCII-art picture of the rectangle."""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"

        return picture

    def get_amount_inside(self, shape):
        """Return how many whole copies of shape fit without rotation."""
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    """Represent a square, keeping width and height equal."""

    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"


if __name__ == "__main__":
    rectangle = Rectangle(10, 5)
    print("Rectangle area:", rectangle.get_area())
    rectangle.set_height(3)
    print("Rectangle perimeter:", rectangle.get_perimeter())
    print(rectangle)
    print(rectangle.get_picture())

    square = Square(9)
    print("Square area:", square.get_area())
    square.set_side(4)
    print("Square diagonal:", square.get_diagonal())
    print(square)
    print(square.get_picture())

    rectangle.set_height(8)
    rectangle.set_width(16)
    print("Squares that fit:", rectangle.get_amount_inside(square))
