# MaKe-stitch

MaKe stitch is an open source stitch creator software that creates, reopens, edits and saves .pmv stitch files. These are common used in a series of brother sewing machines with customizable stitches. Other formats are currently unknown.

wxWidget stitch creator making pmv stitch files from scratch.

You can download a compiled copy of MaKe-stitch for windows in Releases.

https://github.com/EmbroidePy/MaKe-stitch/releases

Python
---

Requires pyembroidery

`pip install pyembroidery`

Requires wxPython:

`pip install wxPython`

Instructions
---
* MaKe-stitch.py GUI - for making .pmv stitch files (or other ones, but there aren't any other ones).
   * ![mkstitch](https://user-images.githubusercontent.com/3302478/99155566-e4644780-266d-11eb-9234-244d25132cee.png)
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

Thanks
---

* Mark Kressin.
* PlantLily.
