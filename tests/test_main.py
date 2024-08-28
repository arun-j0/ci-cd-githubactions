# tests/test_main.py

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_calculator():
    response = client.get("/")
    assert response.status_code == 200
    assert "Calculator" in response.text

def test_calculate_add():
    response = client.get("/calculate?a=5&b=3&operation=add")
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_calculate_subtract():
    response = client.get("/calculate?a=5&b=3&operation=subtract")
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_calculate_multiply():
    response = client.get("/calculate?a=5&b=3&operation=multiply")
    assert response.status_code == 200
    assert response.json() == {"result": 15}

def test_calculate_divide():
    response = client.get("/calculate?a=6&b=3&operation=divide")
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_calculate_divide_by_zero():
    response = client.get("/calculate?a=5&b=0&operation=divide")
    assert response.status_code == 200
    assert response.json() == {"result": "Error: Division by zero"}
