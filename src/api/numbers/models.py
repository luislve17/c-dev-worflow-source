from pydantic import BaseModel, confloat, BeforeValidator, ValidationError
from typing_extensions import Annotated

def validate_cpu_to_use(cpu_type: str):
    if cpu_type not in ["PYTHON_CPU", "NUCLEAR_REACTOR"]:
        raise ValidationError("Uknown CPU target")

    return cpu_type

class PostSumAndSquareBody(BaseModel):
    nums: list[confloat(ge=0)]
    cpu_type: Annotated[str, BeforeValidator(validate_cpu_to_use)]

