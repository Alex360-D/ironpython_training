# -*- coding: utf-8 -*-

import clr
import os.path
project_dir = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.append(os.path.join(project_dir, "TestStack.White.0.13.3\\lib\\net40\\"))
sys.path.append(os.path.join(project_dir, "Castle.Core.3.3.0\\lib\\net40-client\\"))
clr.AddReferenceByName('TestStack.White')

from TestStack.White import Application
from TestStack.White.InputDevices import Keyboard
from TestStack.White.WindowsAPI import KeyboardInput
from TestStack.White.UIItems.Finders import *

clr.AddReferenceByName('UIAutomationTypes, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35')
from System.Windows.Automation import *

from random import randrange

def open_group_editor(main_window):
    main_window.Get(SearchCriteria.ByAutomationId("groupButton")).Click()
    modal = main_window.ModalWindow("Group editor")
    return modal

def close_group_editor(modal):
    modal.Get(SearchCriteria.ByAutomationId("uxCloseAddressButton")).Click()

def close_app(main_window):
    main_window.Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()

def add_new_group(main_window, name):
    modal = open_group_editor(main_window)
    modal.Get(SearchCriteria.ByAutomationId("uxNewAddressButton")).Click()
    modal.Get(SearchCriteria.ByControlType(ControlType.Edit)).Enter(name)
    Keyboard.Instance.PressSpecialKey(KeyboardInput.SpecialKeys.RETURN)
    close_group_editor(modal)

def get_group_list(main_window):
    modal = open_group_editor(main_window)
    tree = modal.Get(SearchCriteria.ByAutomationId("uxAddressTreeView"))
    root = tree.Nodes[0]
    l = [node.Text for node in root.Nodes]
    close_group_editor(modal)
    return l

def test_add_group():
    application = Application.Launch("c:\\Devel\\ironpython_training\\App\\AddressBook\\AddressBook.exe")
    main_window = application.GetWindow("Free Address Book")
    old_list = get_group_list(main_window)
    add_new_group(main_window, 'test group')
    new_list = get_group_list(main_window)
    old_list.append('test group')
    assert sorted(old_list) == sorted(new_list)
    close_app(main_window)

def open_delete_group(main_window):
    main_window.Get(SearchCriteria.ByAutomationId("groupButton")).Click()
    modal = main_window.ModalWindow("Group editor")
    return modal

def del_group(main_window, index):
    modal_group = open_group_editor(main_window)
    tree = modal_group.Get(SearchCriteria.ByAutomationId("uxAddressTreeView"))
    root = tree.Nodes[0]
    root.Nodes[index].Select()
    modal_group.Get(SearchCriteria.ByAutomationId("uxDeleteAddressButton")).Click()
    modal_delete = modal_group.ModalWindow("Delete group")
    modal_delete.Get(SearchCriteria.ByAutomationId("uxOKAddressButton")).Click()
    close_group_editor(modal_group)

def test_del_group():
    application = Application.Launch("c:\\Devel\\ironpython_training\\App\\AddressBook\\AddressBook.exe")
    main_window = application.GetWindow("Free Address Book")
    if len(get_group_list(main_window)) == 1:
        add_new_group(main_window, 'test group')
    old_list = get_group_list(main_window)
    index = randrange(len(old_list))
    del_group(main_window, index)
    new_list = get_group_list(main_window)
    old_list[index:index+1] = []
    assert sorted(old_list) == sorted(new_list)
    close_app(main_window)