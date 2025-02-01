from time import sleep
from math import sqrt
from api.numbers.models import PostSumAndSquareBody

def super_complex_calculation(body: PostSumAndSquareBody) -> float:
    if body.cpu_type == "NUCLEAR_REACTOR":
        sleep(3)  # Turning on nuclear reactor

    return sqrt(sum(body.nums))
