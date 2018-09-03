# MaKe-stitch
wxWidget stitch creator making pmv stitch files from scratch.

Requires pyembroidery

`pip install pyembroidery`

Requires wxPython:

`pip install wxPython`

---

* MaKe-stitch.py GUI - for making .pmv stitch files (or other ones, but there aren't any other ones).
   * ![make-stitch](https://user-images.githubusercontent.com/3302478/44017845-9e4cb12e-9e8e-11e8-9849-f9b9ba75d516.png)
   * See tutorial video: https://youtu.be/HCiFgb9-JHQ
   * Left Double-Click inserts a stitch.
   * Middle Double-Click inserts a stitch. Note: Since Left Click selects a node, double clicking a node selects then inserts at that exact location which duplicates the node. Using middle click means it will allow double-backing on nodes without selecting them.
   * Right Double-Click inserts a triple stitch.
   * Left Click selects nodes.
   * Right-click: on nodes, opens popup menu (delete, duplicate).
   * Drag-and-Move selected nodes to new locations.
   * (In Windows) Drag-and-drop files to open them (other OS's when wxPython supports with the bind I used).
   * Keyboard Commands:
      * Delete button deletes selected node.
      * Right Arrow or 'd' moves to the next node in the list.
      * Left Arrow or 'a' moves to the next node in the list. ('a' & 'd' are WASD keys).
