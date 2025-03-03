import pytest
from fastapi.testclient import TestClient
from main import app

from api.numbers.models import CpuType


class TestSumAndSquare:
    @pytest.fixture
    def api(self):
        client = TestClient(app)
        return client
    
    @pytest.mark.parametrize("cpu_type", [v for v in CpuType])
    def test_returns_200_and_calculates_sum_and_square_from_cpu_type(self, api, cpu_type):
        response = api.post(
            url="/sum-and-square",
            json={"nums": [1,2,3,4,5,6,7,8], "cpu_type": cpu_type}
        )
        assert response.status_code == 200
        assert response.json() == {"result": 6.0}
