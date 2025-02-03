from enum import StrEnum
from pydantic import BaseModel, confloat, BeforeValidator, ValidationError
from typing_extensions import Annotated

class CpuType(StrEnum):
    PYTHON_CPU = "PYTHON_CPU"
    NUCLEAR_REACTOR = "NUCLEAR_REACTOR"
    HAMSTER_FUELED = "HAMSTER_FUELED"
    COAL_BASED = "COAL_BASED"


class PostSumAndSquareBody(BaseModel):
    nums: list[confloat(ge=0)]
    cpu_type: CpuType

