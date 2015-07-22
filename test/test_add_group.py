# -*- coding: utf-8 -*-

from model.group import Group
import random
import string

def test_add_group(app):
    old_list = app.group.get_group_list(app.main_window)
    group = Group(name=random_string("group_", 10))
    app.group.add_new_group(app.main_window, group)
    new_list = app.group.get_group_list(app.main_window)
    old_list.append(group)
    assert sorted(old_list) == sorted(new_list)

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])