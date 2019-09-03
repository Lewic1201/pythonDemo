#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ! python3
"""
@author: Lewic
@file: script
@time: 2019/6/20 8:58
@desc:
"""

import win32ui
import win32api
from win32con import *
from pywin.mfc import window


class MyWnd(window.Wnd):
    def __init__(self):
        window.Wnd.__init__(self, win32ui.CreateWnd())
        self._obj_.CreateWindowEx(WS_EX_CLIENTEDGE, \
                                  win32ui.RegisterWndClass(0, 0, COLOR_WINDOW + 1), \
                                  'Lipanfeng', WS_OVERLAPPEDWINDOW, \
                                  (10, 10, 800, 500), None, 0, None)
        self.HookMessage(self.OnRClick, WM_RBUTTONDOWN)

    def OnClose(self):
        self.EndModalLoop(0)

    def OnRClick(self, param):
        submenu = win32ui.CreatePopupMenu()
        submenu.AppendMenu(MF_STRING, 1054, 'Copy')
        submenu.AppendMenu(MF_STRING, 1055, 'Paste')
        submenu.AppendMenu(MF_STRING, 1056, None)
        submenu.AppendMenu(MF_STRING, 1057, 'Cut')
        flag = TPM_LEFTALIGN | TPM_LEFTBUTTON | TPM_RIGHTBUTTON
        submenu.TrackPopupMenu(param[5], flag, self)


w = MyWnd()
w.ShowWindow()
w.UpdateWindow()
w.RunModalLoop(1)
