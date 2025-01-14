from time import sleep
from math import sqrt
from fastapi import FastAPI, HTTPException
import json

app = FastAPI()


@app.post("/sum-and-square")
def read_item(body: dict):
    # Get variables
    a = body.get("a")
    b = body.get("b")

    # Process
    try:
        result = super_complex_calculation(a, b)
    except ValueError as e:
        raise HTTPException(
            status_code=422, 
            detail=f"Error handling 'a' and 'b': {str(e)}"
        )

    # Return result
    return {"result": result}


def super_complex_calculation(a, b):
    try:
        num_a = float(a)
        num_b = float(b)
    except (TypeError, ValueError):
        raise ValueError("Invalid inputs for calculation")

    sleep(3)  # Turning on nuclear reactor
    return sqrt(num_a + num_b)
