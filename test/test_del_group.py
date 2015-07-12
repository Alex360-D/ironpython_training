# -*- coding: utf-8 -*-

from random import randrange
from fixture.group import GroupHelper
from fixture.application import Application

app = Application()
group = GroupHelper(app)

def test_del_group():
    main_window = group.open_application()
    if len(group.get_group_list(main_window)) == 1:
        group.add_new_group(main_window, 'test group')
    old_list = group.get_group_list(main_window)
    index = randrange(len(old_list))
    group.del_group(main_window, index)
    new_list = group.get_group_list(main_window)
    old_list[index:index+1] = []
    assert sorted(old_list) == sorted(new_list)
    group.close_application(main_window)