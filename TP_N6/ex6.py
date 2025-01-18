def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("division impossible")
    else:
        print("successful division")
        return result
    finally:
        print("successful divisoion")