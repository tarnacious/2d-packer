# draw lines, a rounded-rectangle and a circle on a wx.PaintDC() surface
# tested with Python24 and wxPython26     vegaseat      06mar2007
# Works with Python2.5 on OSX bcl 28Nov2008

import wx
import sys


class MyFrame(wx.Frame):
    """a frame with a panel"""
    def __init__(self, parent=None, id=-1, title=None):
        lines = sys.stdin.readlines()
        self.boxes = []
        for line in lines:
            split = line.split(" ")
            self.boxes.append((int(split[0]), int(split[1]), int(split[2]), int(split[3])))
        wx.Frame.__init__(self, parent, id, title)
        self.panel = wx.Panel(self, size=(350, 200))
        self.panel.Bind(wx.EVT_PAINT, self.on_paint)
        self.Fit()

    def on_paint(self, event):
        scale = 5
        # establish the painting surface
        dc = wx.PaintDC(self.panel)
        dc.SetPen(wx.Pen('blue', 4))
        rect = wx.Rect(0, 0, 100 * scale, 100 * scale)
        dc.DrawRoundedRectangleRect(rect, 2)
        dc.SetPen(wx.Pen('red', 1))
        dc.SetBrush(wx.Brush('#c56c00'))
        # draw a red rounded-rectangle
        for box in self.boxes:
            rect = wx.Rect(box[0] * scale, box[1] * scale, box[2] * scale, box[3] * scale)
            dc.DrawRoundedRectangleRect(rect, 2)


# test it ...
app = wx.PySimpleApp()
frame1 = MyFrame(title='Box Pack')
frame1.Center()
frame1.Show()
app.MainLoop()
