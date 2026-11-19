# Shape Calculator

A small Python object-oriented programming project that models rectangles and squares.
The project demonstrates classes, inheritance, method overriding, calculations, and
basic unit testing.

## Features

- Create rectangles with independent width and height values.
- Create squares as a subclass of `Rectangle`.
- Calculate area, perimeter, and diagonal length.
- Generate an ASCII-art picture of a shape.
- Determine how many whole copies of another shape fit inside a rectangle without rotation.
- Keep a square's width and height equal when changing its dimensions.

## Project structure

```text
shape-calculator/
├── shape_calculator.py
├── README.md
├── .gitignore
└── tests/
    └── test_shape_calculator.py
```

## Requirements

- Python 3.8 or newer
- No third-party packages are required.

## Run the example

From the project directory, run:

```bash
python shape_calculator.py
```

## Example usage

```python
from shape_calculator import Rectangle, Square

rectangle = Rectangle(10, 5)
print(rectangle.get_area())       # 50
print(rectangle.get_perimeter())  # 30

square = Square(4)
print(square.get_area())          # 16

rectangle = Rectangle(16, 8)
print(rectangle.get_amount_inside(square))  # 8
```

## Run the tests

From the project directory, run:

```bash
python -m unittest discover -s tests -v
```

## Concepts practiced

- Classes and objects
- Constructors (`__init__`)
- Inheritance
- Method overriding
- Instance attributes
- String representations (`__str__`)
- Unit testing with `unittest`

## Notes

`get_picture()` returns `"Too big for picture."` when either dimension is greater than
50. `get_amount_inside()` uses whole-number division and does not rotate the shape.

## License

This project is available under the MIT License. See [LICENSE](LICENSE).
