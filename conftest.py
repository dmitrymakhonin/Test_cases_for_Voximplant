from fixture import test_function
import pytest


@pytest.fixture(scope="session")
def req(request):
    link=request.config.getoption("--client_list") #Использование опции
    fixture=test_function.Test_function
    return fixture

# Возможность добавить различные опции для прогона тестов реализуется следующим образом
def pytest_addoption(parser):
    parser.addoption("--client_list", action="store",default="client_list.json")

