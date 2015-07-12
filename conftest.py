# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app():
    global fixture
    if fixture is None:
        fixture = Application()
    return fixture