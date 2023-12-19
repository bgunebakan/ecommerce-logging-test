from random import choice


class PaymentError(Exception):
    pass

def pay(cart):
    """
    Returns True if payment is succeeded.
    Returns False if payment is rejected.
    Raises exception if there is a technical error.
    """

    result = choice(["OK"] * 6 + ["REJECTED"] * 3 + ["ERROR"])
    if result == "ERROR":
        raise PaymentError("There is a technical error on the payment step")
    elif result == "REJECTED":
        return False
    else:
        return True