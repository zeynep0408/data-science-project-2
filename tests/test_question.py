from decimal import Decimal
import pytest
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.question import (  # kendi modül ismini buraya yaz
    question_1_query,
    question_2_query,
    question_3_query,
    question_4_query,
    question_5_query,
    question_6_query,
    question_7_query,
    question_8_query,
    question_9_query,
    question_10_query,
    question_11_query,
    question_12_query,
    question_13_query,
    question_14_query,
    question_15_query,
)

def test_question_1_query():
    result = question_1_query()
    assert result, "Query result is empty!"
    assert isinstance(result, list)

def test_question_2_query():
    result = question_2_query()
    assert result, "Query result is empty!"
    assert all(r[2] == 'Veritabanı' for r in result)

def test_question_3_query():
    result = question_3_query()
    assert result, "Query result is empty!"
    assert all(r[1].startswith('A') for r in result)

def test_question_4_query():
    result = question_4_query()
    assert result, "Query result is empty!"
    assert any('SQL' in r[1] for r in result)

def test_question_5_query():
    result = question_5_query()
    assert result, "Query result is empty!"
    assert all(22 <= r[4] <= 24 for r in result)

def test_question_6_query():
    result = question_6_query()
    assert result, "Query result is empty!"
    assert all(len(r) == 2 for r in result)

def test_question_7_query():
    result = question_7_query()
    assert result, "Query result is empty!"
    assert all(isinstance(r[1], int) for r in result)

def test_question_8_query():
    result = question_8_query()
    assert result, "Query result is empty!"
    assert all(len(r) == 2 for r in result)

def test_question_9_query():
    result = question_9_query()
    assert isinstance(result, list)
    assert all(isinstance(r, tuple) for r in result)

def test_question_10_query():
    result = question_10_query()
    assert result, "Query result is empty!"
    assert all(isinstance(r, tuple) and len(r) == 2 for r in result)
    for _, avg_age in result:
        assert isinstance(avg_age, (int, float, Decimal))
        assert avg_age > 0 

def test_question_11_query():
    result = question_11_query()
    assert result, "Query result is empty!"
    assert all(isinstance(r[2], int) for r in result)

def test_question_12_query():
    result = question_12_query()
    assert result, "Query result is empty!"
    assert all(r[1] > 1 for r in result)

def test_question_13_query():
    result = question_13_query()
    assert result, "Query result is empty!"
    assert all(isinstance(r[1], int) for r in result)

def test_question_14_query():
    result = question_14_query()
    assert all(len(r) == 2 for r in result)

def test_question_15_query():
    result = question_15_query()
    assert result, "Query result is empty!"
    assert all(len(r) == 5 for r in result)


class ResultCollector:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            if report.passed:
                self.passed += 1
            elif report.failed:
                self.failed += 1

def send_post_request(url: str, data: dict, headers: dict = None):
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # hata varsa exception fırlatır
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
    except Exception as err:
        print(f"Other error occurred: {err}")

def run_tests():
    collector = ResultCollector()
    pytest.main(["tests"], plugins=[collector])
    print(f"\nToplam Başarılı: {collector.passed}")
    print(f"Toplam Başarısız: {collector.failed}")
    
    user_score = (collector.passed / (collector.passed + collector.failed)) * 100
    print(round(user_score, 2))
    
    url = "https://edugen-backend-487d2168bc6c.herokuapp.com/projectLog/"
    payload = {
        "user_id": 403,
        "project_id": 35,
        "user_score": round(user_score, 2),
        "is_auto": False
    }
    headers = {
        "Content-Type": "application/json"
    }
    send_post_request(url, payload, headers)
    

if __name__ == "__main__":
    run_tests()
