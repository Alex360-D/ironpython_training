# -*- coding: utf-8 -*-

import clr
# import os.path
# project_dir = os.path.dirname(os.path.abspath(__file__))
# import sys
# sys.path.append(os.path.join(project_dir, "TestStack.White.0.13.3\\lib\\net40\\"))
# sys.path.append(os.path.join(project_dir, "Castle.Core.3.3.0\\lib\\net40-client\\"))
import sys
sys.path.append("C:\\Devel\\ironpython_training\\TestStack.White.0.13.3\\lib\\net40\\")
sys.path.append("C:\\Devel\\ironpython_training\\Castle.Core.3.3.0\\lib\\net40-client\\")
clr.AddReferenceByName('TestStack.White')

from TestStack.White import Application
from TestStack.White.InputDevices import Keyboard
from TestStack.White.WindowsAPI import KeyboardInput
from TestStack.White.UIItems.Finders import *

clr.AddReferenceByName('UIAutomationTypes, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35')
from System.Windows.Automation import *

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_application(self):
        application = Application.Launch("c:\\Devel\\ironpython_training\\App\\AddressBook\\AddressBook.exe")
        main_window = application.GetWindow("Free Address Book")
        return main_window

    def open_group_editor(self, main_window):
        main_window.Get(SearchCriteria.ByAutomationId("groupButton")).Click()
        modal = main_window.ModalWindow("Group editor")
        return modal

    def close_group_editor(self, modal):
        modal.Get(SearchCriteria.ByAutomationId("uxCloseAddressButton")).Click()

    def close_application(self, main_window):
        main_window.Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()

    def add_new_group(self, main_window, name):
        modal = self.open_group_editor(main_window)
        modal.Get(SearchCriteria.ByAutomationId("uxNewAddressButton")).Click()
        modal.Get(SearchCriteria.ByControlType(ControlType.Edit)).Enter(name)
        Keyboard.Instance.PressSpecialKey(KeyboardInput.SpecialKeys.RETURN)
        self.close_group_editor(modal)
        self.group_cache = None

    group_cache = None

    def get_group_list(self, main_window):
        if self.group_cache is None:
            modal = self.open_group_editor(main_window)
            self.group_cache = []
            tree = modal.Get(SearchCriteria.ByAutomationId("uxAddressTreeView"))
            root = tree.Nodes[0]
            self.group_cache = [node.Text for node in root.Nodes]
            self.close_group_editor(modal)
        return self.group_cache

    def open_delete_group(self, main_window):
        main_window.Get(SearchCriteria.ByAutomationId("groupButton")).Click()
        modal = main_window.ModalWindow("Group editor")
        return modal

    def del_group(self, main_window, index):
        modal_group = self.open_group_editor(main_window)
        tree = modal_group.Get(SearchCriteria.ByAutomationId("uxAddressTreeView"))
        root = tree.Nodes[0]
        root.Nodes[index].Select()
        modal_group.Get(SearchCriteria.ByAutomationId("uxDeleteAddressButton")).Click()
        modal_delete = modal_group.ModalWindow("Delete group")
        modal_delete.Get(SearchCriteria.ByAutomationId("uxOKAddressButton")).Click()
        self.close_group_editor(modal_group)
        self.group_cache = None