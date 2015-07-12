# -*- coding: utf-8 -*-

from fixture.group import GroupHelper
from fixture.application import Application

app = Application()
group = GroupHelper(app)

def test_add_group():
    main_window = group.open_application()
    old_list = group.get_group_list(main_window)
    group.add_new_group(main_window, 'test group')
    new_list = group.get_group_list(main_window)
    old_list.append('test group')
    assert sorted(old_list) == sorted(new_list)
    group.close_application(main_window)