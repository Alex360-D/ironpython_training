# -*- coding: utf-8 -*-

from model.group import Group
import pytest
import os.path
from fixture.application import Application2

import clr
clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=11.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel

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

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("xlsx_"):
            testdata = load_from_xlsx(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_xlsx(file):
    f = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data\%s.xlsx" % file)
    excel = Excel.ApplicationClass()
    excel.Visible = False
    workbook = excel.Workbooks.Open(r"%s" % f)
    sheet = workbook.Worksheets[1]
    testdata = []
    for i in range(1,7):
        text = sheet.Rows[i].Value2[0,0]
        testdata.append(Group(name = text))
    excel.Quit()
    return testdata