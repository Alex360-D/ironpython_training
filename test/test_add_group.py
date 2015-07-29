# -*- coding: utf-8 -*-

def test_add_group(app, xlsx_groups):
    group = xlsx_groups
    old_list = app.group.get_group_list(app.main_window)
    app.group.add_new_group(app.main_window, group)
    new_list = app.group.get_group_list(app.main_window)
    old_list.append(group.name)
    assert sorted(old_list) == sorted(new_list)