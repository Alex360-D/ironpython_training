# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application2

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application2()
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.close_application()
    request.addfinalizer(fin)
    return fixture