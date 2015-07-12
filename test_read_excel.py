# -*- coding: utf-8 -*-

from model.group import Group
import os.path
import time

import clr
clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=11.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel

f = "data\\groups.xlsx"
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), f)

excel = Excel.ApplicationClass()
excel.Visible = False

workbook = excel.Workbooks.Open(r"%s" % file)
sheet = workbook.Worksheets[1]

testdata = []
for i in range(1,7):
    text = sheet.Rows[i].Value2[0,0]
    testdata.append(Group(name = text))
    print(testdata[i-1])

time.sleep(2)

excel.Quit()