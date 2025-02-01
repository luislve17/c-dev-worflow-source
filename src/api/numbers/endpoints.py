from fastapi import APIRouter
from api.numbers.models import PostSumAndSquareBody
from api.numbers.operations import super_complex_calculation

router = APIRouter()

@router.post("/sum-and-square")
def sum_and_square_numbers(body: PostSumAndSquareBody):
    result = super_complex_calculation(body)
    return {"result": result}
