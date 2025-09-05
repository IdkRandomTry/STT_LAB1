"""Simple program to demonstrate pylint compliance."""

X_VAL = 10
Y_VAL = 20


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def main():
    """Main function."""
    z_val = add(x_val, y_val)
    print(f"Result is {z_val}")

    print("Always true")

    for _ in range(5):
        print("hello world")


if __name__ == "__main__":
    main()
