#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.3 on Sun Aug 12 10:23:49 2018
#

import wx
import pyembroidery
from wx.lib.embeddedimage import PyEmbeddedImage

makestitch_icon = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B'
    b'AACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAASwSURBVGhD1ZlLKLxfGMcf5J5bbNDE'
    b'ROR+CVkgkVuSXMJOZGGjJBY2VoqSjYWikJBQLsl9IcREpsYlC5cyKMJC4xaG83+fx/n9/uln'
    b'hmHM+/rU5JznnGne73ue5znPOYBJkOHhYQYAzNramnl6elIbPwEBAay5uZnPeovkhGg0Gnpo'
    b'tVrNLa88Pz+z9vZ2JpfLabyuro6PvCI5IZ2dnUwmk/He++zv75OYqKgobmHMXDBICicnJzg7'
    b'O+O99/Hx8cEFgPX1dSgqKiKbGaqhloQwMzODl5cX+vsROOfi4kKaQuLi4sDW1hbm5ua4RTel'
    b'paUgxI/gaBJFeEamUCh4Tzc4x97eXnrB/oe+vj4S8xFarZbmSdK1DAFjycLCAkTPWl1dXSCk'
    b'UQpa/Li6ukJhYSEsLS3xGfpZW1sDKysr8WJkdHSUXAI/NTU1bHFxkSmVStbb28syMjL+jtXX'
    b'1/NvvE9xcTETUrA4MdLY2EgPiaWIPoaGhpidnR3Nrays5Nb/ubu7o7GTkxPTC7m/v6cfv76+'
    b'5paPUalUzNvbm76XmprK5ufnqQLAflVVFc0xuZDa2loWExPDe4Zxfn7OCgoKmBBLzN3dnY2P'
    b'j/MRZvqslZycDJGRkdDU1MQtxsHkWQvf20+8O5MLCQoKgt3dXd4zIuhapmRsbIyC1NiIsrPj'
    b'xvf4+AiWlpbc8n1E2dnxPNHQ0MB7RoLWxcRg2jT2T4siBEEhAwMDvPd9RBPS2tpq1FURtYzH'
    b'oBdKDSgpKeGWV46Pj2FnZwdOT09BKGWgoqKCj+hGVCEzMzOQnp6Oy0J9fPCFhQUSmJKSQpcL'
    b'Dw8PkJWVReN6QSFigjVTTk4OW15eZh0dHezw8JDsgiDW09ND7c8g+glxdXUVtra2wNPTE4Rz'
    b'CNmE8h6enp7ogPVZRD0hCuU4uZNCoYC8vDyydXd3g7W1tUEiCFoXEcBDE5Yrf8BHwZMhHpK+'
    b'giiu1d/fD3K5HGJjY8mtNjY26B4rPz8fjo6OQCaT8Zmfx6RChKMpTE1Nkev4+vpSfNjY2EB8'
    b'fDx4eHhAW1sblJeX/81ihmAyIfjWt7e3wcHBAW5ubsDZ2RlCQkL+efsY8NPT0waL+XEhmH0m'
    b'Jibo/gnBO6i0tDRaCV2Eh4eTcEMe7UezFvq/ENTUxo3N398fsrOz9YpAVCoVlJWV0cbY0tLC'
    b'rfr5kRXBVRAqXHoQbLu4uNBObSibm5sQFhZGbXQ3XEldGF3I3t4elRaYhW5vb+lm3cvLi49+'
    b'jebmZqiurgZzc/PXm/d3MKqQyclJyky4CkLpAYmJiXzEOGCyCA4O5r23GEWIUB/R7oxpFUXg'
    b'lY+bmxsfNQ3fFjI7OwtXV1ckwM/PD6Kjo/mIafmyEPw/H9ZKeIGAvpuZmUkrIhZfEiKU3KBW'
    b'q6mNPhsaGkptMTFIiEajoTSo1WoppaamptIGJwU+LUSpVNLxE10pISGBaiMp8aEQDGKh3KY9'
    b'ITAwULRg/gi9Qg4ODuhfYI6OjpCUlESFnlTRKQRjAU9veGYICAjgVunyj5DLy0sYGRmha01c'
    b'hd/CGyErKyt05Z+bm0vu9JsgIahlcHCQduaIiAg+9LswE3ZohquAx83fC8B/QI+w8nkB9vAA'
    b'AAAASUVORK5CYII=')
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

MaKeStitchVersion = "0.2.0"
PMV_SCALE = 2.5
PMV_CURVE = 75


class StitchPanel(wx.Panel):
    def __init__(self, *args, **kwds):

        # begin wxGlade: StitchPanel.__init__
        kwds["style"] = kwds.get("style", 0) | wx.WANTS_CHARS
        wx.Panel.__init__(self, *args, **kwds)

        self.name_dict = pyembroidery.get_common_name_dictionary()
        self.emb_pattern = pyembroidery.EmbPattern()
        self.emb_pattern.stitch_abs(0, 0)
        self.name = None
        self.max_stitch = 0
        self.current_stitch = -1
        self.scale = 1
        self.translate_x = 0
        self.translate_y = 0
        self.buffer = 0.1
        self.grid = None
        self.text_grid = None
        self.clicked_position = None

        self.drag_point = None
        self.selected_point = 0

        self.__set_properties()
        self.__do_layout()

        # end wxGlade
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.on_erase)
        self.Bind(wx.EVT_MOTION, self.on_mouse_move)
        self.Bind(wx.EVT_KEY_DOWN, self.on_key_press)
        self.Bind(wx.EVT_LEFT_DOWN, self.on_mouse_down)
        self.Bind(wx.EVT_LEFT_UP, self.on_mouse_up)
        self.Bind(wx.EVT_LEFT_DCLICK, self.on_left_double_click)
        self.Bind(wx.EVT_MIDDLE_DCLICK, self.on_left_double_click)
        self.Bind(wx.EVT_RIGHT_DCLICK, self.on_right_double_click)
        self.Bind(wx.EVT_RIGHT_DOWN, self.on_right_mouse_down)
        self.Bind(wx.EVT_DROP_FILES, self.on_drop_file)

    def on_drop_file(self, event):
        for filename in event.GetFiles():
            self.load(str(filename))

    def on_mouse_move(self, event):
        if self.drag_point is None:
            return
        mod_stitch = self.emb_pattern.stitches[self.drag_point]
        position = self.scene_location_to_grid_position(event.GetPosition())
        mod_stitch[0] = position[0] * PMV_SCALE
        mod_stitch[1] = position[1] * PMV_SCALE
        self.update_drawing()

    def on_mouse_down(self, event):
        self.SetFocus()
        if self.emb_pattern is None:
            return
        position = event.GetPosition()
        nearest = self.get_nearest_point(position)
        if nearest[1] > 100:
            event.Skip()
            self.drag_point = None
            return
        best_index = nearest[0]
        self.drag_point = best_index
        self.selected_point = best_index

    def on_mouse_up(self, event):
        self.drag_point = None
        self.update_affines()
        self.update_drawing()

    def on_right_double_click(self, event):
        if self.selected_point is None:
            return
        stitches = self.emb_pattern.stitches
        stitch = stitches[self.selected_point]
        new_stitch = stitch[:]
        new_stitch2 = stitch[:]
        new_stitch3 = stitch[:]
        position = self.scene_location_to_grid_position(self.clicked_position)
        new_stitch[0] = position[0] * PMV_SCALE
        new_stitch[1] = position[1] * PMV_SCALE
        new_stitch3[0] = position[0] * PMV_SCALE
        new_stitch3[1] = position[1] * PMV_SCALE
        stitches.insert(self.selected_point + 1, new_stitch)
        stitches.insert(self.selected_point + 2, new_stitch2)
        stitches.insert(self.selected_point + 3, new_stitch3)
        self.selected_point += 3
        self.update_affines()
        self.update_drawing()

    def on_left_double_click(self, event):
        self.clicked_position = event.GetPosition()
        nearest = self.get_nearest_point(self.clicked_position)
        if nearest[0] is None:  # No nearest node. Must have no nodes.
            position = self.scene_location_to_grid_position(self.clicked_position)
            stitches = self.emb_pattern.stitches
            stitches.append([position[0]*PMV_SCALE, position[1]*PMV_SCALE, pyembroidery.STITCH])
            self.selected_point = 0
            self.update_affines()
            self.update_drawing()
            return

        if self.selected_point is None:
            return
        stitches = self.emb_pattern.stitches
        stitch = stitches[self.selected_point]
        new_stitch = stitch[:]
        position = self.scene_location_to_grid_position(self.clicked_position)
        new_stitch[0] = position[0]*PMV_SCALE
        new_stitch[1] = position[1]*PMV_SCALE
        stitches.insert(self.selected_point + 1, new_stitch)
        self.selected_point += 1
        self.update_affines()
        self.update_drawing()

    def on_right_mouse_down(self, event):
        self.clicked_position = event.GetPosition()
        nearest = self.get_nearest_point(self.clicked_position)
        if nearest[1] > 25:
            event.Skip()
            return
        menu = wx.Menu()
        menu_item = menu.Append(wx.ID_ANY, "Delete", "")
        self.Bind(wx.EVT_MENU, self.on_menu_delete, menu_item)
        menu_item = menu.Append(wx.ID_ANY, "Duplicate", "")
        self.Bind(wx.EVT_MENU, self.on_menu_duplicate, menu_item)
        self.PopupMenu(menu)
        menu.Destroy()

    def on_menu_delete(self, event):
        best_index = self.get_nearest_point(self.clicked_position)[0]
        stitches = self.emb_pattern.stitches
        del stitches[best_index]
        self.selected_point = None
        self.update_drawing()

    def on_menu_duplicate(self, event):
        best_index = self.get_nearest_point(self.clicked_position)[0]
        stitches = self.emb_pattern.stitches
        stitch = stitches[best_index]
        stitches.insert(best_index, stitch[:])
        self.selected_point = best_index
        self.update_drawing()

    def on_key_press(self, event):
        keycode = event.GetKeyCode()
        stitch_max = len(self.emb_pattern.stitches)
        if keycode in [68, wx.WXK_RIGHT, wx.WXK_NUMPAD6]:
            if self.selected_point is None:
                self.selected_point = 0
            else:
                self.selected_point += 1
            if self.selected_point >= stitch_max:
                self.selected_point = stitch_max - 1
            self.update_drawing()
        elif keycode in [65, wx.WXK_LEFT, wx.WXK_NUMPAD4]:
            if self.selected_point is None:
                self.selected_point = stitch_max - 1
            else:
                self.selected_point -= 1
            if self.selected_point < 0:
                self.selected_point = 0
            self.update_drawing()
        elif keycode in [127]:
            position = self.selected_point
            if position is None:
                return
            stitches = self.emb_pattern.stitches
            del stitches[position]
            stitch_max = len(self.emb_pattern.stitches)
            if self.selected_point >= stitch_max:
                self.selected_point = stitch_max - 1
            if stitch_max == 0:
                self.selected_point = None
            self.update_drawing()

    def load(self, filename):
        self.Update()
        self.emb_pattern = pyembroidery.read(filename)
        for pos, stitch in enumerate(self.emb_pattern.stitches):
            command = stitch[2]
            if command != pyembroidery.END:
                continue
            self.emb_pattern.stitches = self.emb_pattern.stitches[0:pos]
            break
        self.emb_pattern.get_as_command_blocks()
        self.name = filename
        self.selected_point = None
        self.drag_point = None
        self.update_affines()
        self.update_drawing()

    def update_affines(self):
        Size = self.ClientSize
        try:
            self.update_affine(Size[0], Size[1])
        except (AttributeError, TypeError):
            pass

    def update_affine(self, width, height):
        extends = self.emb_pattern.bounds()
        min_x = min(extends[0], 0)
        min_y = min(extends[1], -35)
        max_x = max(extends[2], 100)
        max_y = max(extends[3], 35)

        embroidery_width = (max_x - min_x) #+ (width * self.buffer)
        embroidery_height = (max_y - min_y) #+ (height * self.buffer)
        scale_x = float(width) / embroidery_width
        scale_y = float(height) / embroidery_height
        self.scale = min(scale_x, scale_y) * 2
        self.translate_x = -min_x + 3
        self.translate_y = -(min_y/2)
        self.grid = None
        self.text_grid = None

    def scene_location_to_grid_position(self, position):
        px = position[0]
        py = position[1]
        px /= self.scale
        py /= self.scale
        px -= self.translate_x
        py -= self.translate_y
        px -= py * py / PMV_CURVE
        px = round(px)
        py = round(py)
        return px, py

    def grid_position_to_scene_location(self, grid_x, grid_y):
        x = grid_x
        y = grid_y
        x += grid_y * grid_y / PMV_CURVE
        x += self.translate_x
        y += self.translate_y
        x *= self.scale
        y *= self.scale
        return x, y

    @staticmethod
    def distance_sq(p0, p1):
        dx = p0[0] - p1[0]
        dy = p0[1] - p1[1]
        dx *= dx
        dy *= dy
        return dx + dy

    def get_nearest_point(self, position):
        best_point = None
        best_index = None
        best_distance = float('-inf')
        for i, stitch in enumerate(self.emb_pattern.stitches):
            s_x, s_y = self.grid_position_to_scene_location(stitch[0]/PMV_SCALE, stitch[1]/PMV_SCALE)
            distance = self.distance_sq(position, (s_x, s_y))
            if best_point is None or distance < best_distance or (
                    distance == best_distance and self.selected_point == i):
                best_point = stitch
                best_distance = distance
                best_index = i
        return best_index, best_distance, best_point

    def __set_properties(self):
        # begin wxGlade: StitchPanel.__set_properties
        self.SetFocus()
        self.DragAcceptFiles(True)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: StitchPanel.__do_layout
        self.Layout()
        # end wxGlade

    def perform_draw_grid(self, dc):
        if self.grid is None:
            self.build_grid()
        for g in self.grid:
            dc.SetPen(wx.Pen(g[0]))
            dc.DrawLineList(g[1])
        for t in self.text_grid:
            font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD)
            dc.SetFont(font)
            w, h = dc.GetTextExtent(t[0])
            if t[3] == 0:
                dc.DrawText(t[0], wx.Point(t[1] - w, t[2]-h/2))
            elif t[3] == 1:
                dc.DrawText(t[0], wx.Point(t[1] - w / 2, t[2]-h))
            else:
                dc.DrawText(t[0], wx.Point(t[1] - w / 2, t[2]))

    def build_grid(self):
        text = []
        black_lines = []
        grey_lines = []
        magenta_lines = []
        black = False
        for j in range(-14, 14 + 1):
            black = not black
            x0, y0 = self.grid_position_to_scene_location(0, j)
            x1, y1 = self.grid_position_to_scene_location(100,j)
            text.append((str(j), x0, y0, 0))
            if j == 0:
                magenta_lines.append([x0, y0, x1, y1])
            else:
                if black:
                    black_lines.append([x0, y0, x1, y1])
                else:
                    grey_lines.append([x0, y0, x1, y1])
        black = False
        for j in range(-14, 14):
            for k in range(0, 100):
                black = not black
                x0, y0 = self.grid_position_to_scene_location(k, j)
                x1, y1 = self.grid_position_to_scene_location(k, j+1)
                if k % 5 == 0 and j == -14:
                    text.append((str(k), x0, y0, 1))
                if k % 5 == 0 and j == 13:
                    text.append((str(k), x1, y1, -1))
                if black:
                    black_lines.append([x0, y0, x1, y1])
                else:
                    grey_lines.append([x0, y0, x1, y1])
        self.grid = [((0xFF, 0, 0xFF), magenta_lines),
                     ((0x80, 0x80, 0x80), grey_lines),
                     ((0, 0, 0), black_lines)]
        self.text_grid = text

    def perform_draw(self, dc):
        dc.SetBackground(wx.Brush("White"))
        dc.Clear()
        self.perform_draw_grid(dc)
        if self.emb_pattern is None:
            return

        draw_data = []
        for color in self.emb_pattern.get_as_colorblocks():
            lines = []
            last_x = None
            last_y = None
            for i, stitch in enumerate(color[0]):
                current_x, current_y = self.grid_position_to_scene_location(stitch[0]/PMV_SCALE, stitch[1]/PMV_SCALE)
                if last_x is not None:
                    lines.append([last_x, last_y, current_x, current_y])
                last_x = current_x
                last_y = current_y
            draw_data.append(((0, 0, 0), lines))

        current_stitch = self.current_stitch
        # Here's the actual drawing code.

        if current_stitch == -1:
            for drawElements in draw_data:
                pen = wx.Pen(drawElements[0])
                pen.SetWidth(5)
                dc.SetPen(pen)
                dc.DrawLineList(drawElements[1])
        else:
            count = 0
            count_range = 0
            for drawElements in draw_data:
                pen = wx.Pen(drawElements[0])
                pen.SetWidth(5)
                dc.SetPen(pen)
                count_range += len(drawElements[1])
                if current_stitch < count_range:
                    dif = current_stitch - count
                    segments = drawElements[1]
                    subsegs = segments[:dif]
                    dc.DrawLineList(subsegs)
                    break
                else:
                    dc.DrawLineList(drawElements[1])
                count = count_range
        dc.SetBrush(wx.Brush("Blue"))
        dc.GetPen().SetWidth(1)
        for stitch in self.emb_pattern.stitches:
            current_x, current_y = self.grid_position_to_scene_location(stitch[0]/PMV_SCALE, stitch[1]/PMV_SCALE)
            dc.DrawCircle(current_x, current_y, 10)

        if self.selected_point is not None:
            font = wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD)
            dc.SetFont(font)
            mod_stitch = self.emb_pattern.stitches[self.selected_point]
            name = "%s %d (%g, %g)" % (self.name_dict[mod_stitch[2]],
                                       int(self.selected_point),
                                       float(mod_stitch[0]) / PMV_SCALE,
                                       float(mod_stitch[1]) / PMV_SCALE)
            dc.DrawText(name, 0, 0)
            dc.SetBrush(wx.Brush("Green"))
            m_x, m_y = self.grid_position_to_scene_location(mod_stitch[0]/PMV_SCALE, mod_stitch[1]/PMV_SCALE)
            dc.DrawCircle(m_x, m_y, 10)

    def on_paint(self, event):
        wx.BufferedPaintDC(self, self._Buffer)

    def on_size(self, event):
        # The Buffer init is done here, to make sure the buffer is always
        # the same size as the Window
        # Size  = self.GetClientSizeTuple()
        self.update_affines()
        # Make new offscreen bitmap: this bitmap will always have the
        # current drawing in it, so it can be used to save the image to
        # a file, or whatever.
        Size = self.ClientSize
        self._Buffer = wx.Bitmap(*Size)
        self.update_drawing()

    def on_erase(self, event):
        pass

    def update_drawing(self):
        dc = wx.MemoryDC()
        dc.SelectObject(self._Buffer)
        self.perform_draw(dc)
        del dc  # need to get rid of the MemoryDC before Update() is called.
        self.Refresh()
        self.Update()

    def OnDropFiles(self, x, y, filenames):
        """
        When files are dropped, write where they were dropped and then
        the file paths themselves
        """
        self.window.SetInsertionPointEnd()
        self.window.updateText("\n%d file(s) dropped at %d,%d:\n" %
                               (len(filenames), x, y))
        for filepath in filenames:
            self.window.updateText(filepath + '\n')


# end of class StitchPanel

class Stitcher(wx.Frame):
    def __init__(self, *args, **kwds):
        self.design = None
        # begin wxGlade: Stitcher.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((600, 400))
        self.stitch_panel = StitchPanel(self, wx.ID_ANY)

        self.Bind(wx.EVT_KEY_DOWN, self.stitch_panel.on_key_press)

        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        menu_import = wxglade_tmp_menu.Append(wx.ID_ANY, "Import", "")
        self.Bind(wx.EVT_MENU, self.on_menu_import, menu_import)

        menu_export = wxglade_tmp_menu.Append(wx.ID_ANY, "Export", "")
        self.Bind(wx.EVT_MENU, self.on_menu_export, menu_export)
        self.frame_menubar.Append(wxglade_tmp_menu, "File")
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Stitcher.__set_properties
        self.SetTitle("MK Stitch v%s" % MaKeStitchVersion)
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(makestitch_icon.GetBitmap())
        self.SetIcon(_icon)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Stitcher.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.stitch_panel, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def on_menu_import(self, event):
        files = ""
        for format in pyembroidery.supported_formats():
            try:
                if format["reader"] is not None and format["category"] == "stitch":
                    files += "*." + format["extension"] + ";"
            except KeyError:
                pass

        with wx.FileDialog(self, "Open Stitch", wildcard=files[:-1],
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind
            pathname = fileDialog.GetPath()
            self.stitch_panel.load(str(pathname))

    def on_menu_export(self, event):
        files = ""
        for format in pyembroidery.supported_formats():
            try:
                if format["writer"] is not None and format["category"] == "stitch":
                    files += format["description"] + "(*." + format["extension"] + ")|*." + format[
                        "extension"] + "|"
            except KeyError:
                pass

        with wx.FileDialog(self, "Save Stitch", wildcard=files[:-1],
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # save the current contents in the file
            pathname = fileDialog.GetPath()
            pyembroidery.write(self.stitch_panel.emb_pattern, str(pathname))


# end of class Stitcher

class MyApp(wx.App):
    def OnInit(self):
        self.stitch_frame = Stitcher(None, wx.ID_ANY, "")
        self.SetTopWindow(self.stitch_frame)
        self.stitch_frame.Show()
        return True


# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
