from time import sleep
from math import sqrt
from api.numbers.models import PostSumAndSquareBody

cpu_type_delay_mapping = {
    "PYTHON_CPU": 1,
    "NUCLEAR_REACTOR": 3,
    "HAMSTER_FUELED": 0.5,
    "COAL_BASED": 0.1,
}

def super_complex_calculation(body: PostSumAndSquareBody) -> float:
    cpu_delay = cpu_type_delay_mapping.get(body.cpu_type, 0)
    sleep(cpu_delay)

    return sqrt(sum(body.nums))
