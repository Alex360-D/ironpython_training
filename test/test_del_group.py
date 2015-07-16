# -*- coding: utf-8 -*-

from random import randrange

def test_del_group(app):
    main_window = app.group.open_application()
    if len(app.group.get_group_list(main_window)) == 1:
        app.group.add_new_group(main_window, 'test group')
    old_list = app.group.get_group_list(main_window)
    index = randrange(len(old_list))
    app.group.del_group(main_window, index)
    new_list = app.group.get_group_list(main_window)
    old_list[index:index+1] = []
    app.group.close_application(main_window)
    assert sorted(old_list) == sorted(new_list)