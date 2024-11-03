import random


def generate_integer_in_range(min, max):
    """
    1st argument:
        min-- Number 1
    2nd argument:
        max-- Number 2
    Generates a random integer in range [min,max].
    Raises ValueError if:
    a) min > max
    b) no integer in range
    Raises TypeError if:
    a) min or max are not numbers
    """
    try:
        return random.randint(min, max)
    except TypeError:  # If min or max are not numbers, raise an error
        raise TypeError("Arguments should be numbers")
    except ValueError:
        if min > max:
            raise ValueError("First argument should be smaller than second")
        if type(min) is int:
            min_int = min
        else:  # If min is a float, we need to round it to the ceiling integer
            if min < 0:
                min_int = int(min)
            elif min > 0:
                min_int = int(min + 1)
        if type(max) is int:
            max_int = max
        else:  # If max is a float, we need to round it to the floor integer
            if max < 0:
                max_int = int(max - 1)
            elif max > 0:
                max_int = int(max)
        if min_int > max_int:
            # If the rounded min is greater than the rounded max,
            # there is no integer in range
            raise ValueError("No integer in range")
        return random.randint(min_int, max_int)


def generate_arithmetic_operation():
    """
    Generates one of the arithmetic operations:
    addition/subtraction/multiplication
    Returns operation as a string.
    """
    return random.choice(["+", "-", "*"])


def apply_arithmetic_operation(n1, n2, o):
    """
    1st argument:
        n1-- Number 1
    2nd argument:
        n2-- Number 2
    3rd argument:
        o-- Operator
    Applies the arithmetic operator 'o' on n1 and n2 and returns:
    a) the expression as a string, and
    b) the resulting number.
    Raises ValueError if:
    a) operator is invalid
    Raises TypeError if:
    a) operator is not a string
    b) n1 or n2 are not numbers
    """
    if (type(n1) is not int and type(n1) is not float) or (
        type(n2) is not int and type(n2) is not float
    ):
        raise TypeError("Arguments should be numbers")
    if type(o) is not str:
        raise TypeError("Operator should be a string")

    p = f"{n1} {o} {n2}"
    o = o.strip()  # Remove any leading/trailing whitespaces
    if o == "+":
        a = n1 + n2  # Addition of n1 and n2
    elif o == "-":
        a = n1 - n2  # Subtraction of n2 from n1
    elif o == "*":
        a = n1 * n2  # Multiplication of n1 and n2
    else:
        raise ValueError("Invalid operator")
    return p, a


def math_quiz():
    score = 0
    n_questions = 6
    n1 = 0
    n1_new = 0
    n2 = 0
    n2_new = 0
    o = ""
    o_new = ""

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems.")
    print("Try to provide correct answers for a high score.")

    for _ in range(n_questions):
        while n1_new == n1:
            n1_new = generate_integer_in_range(1, 10)
        n1 = n1_new
        while n2_new == n2:
            n2_new = generate_integer_in_range(1, 5.5)
        n2 = n2_new
        while o_new == o:
            o_new = generate_arithmetic_operation()
        o = o_new

        PROBLEM, ANSWER = apply_arithmetic_operation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = useranswer.strip()
        while type(useranswer) is not float:
            # Keep asking for a number until the user provides one
            try:
                useranswer = float(useranswer)
            except ValueError:
                print("Invalid input. Please enter a number.")
                useranswer = input("Your answer: ")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{n_questions}")


if __name__ == "__main__":
    math_quiz()
