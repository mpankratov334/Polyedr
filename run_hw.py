#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from polyedr_hw import Polyedr


tk = TkDrawer()
try:
    for name in ["ccc", "cube", "box", "pyramid_top",
                 "pyramid_bottom", "pyramid_in_cube", "king", "cow"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        Polyedr(f"data/{name}.geom").draw(tk)
        delta_time = time() - start_time
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        input("Hit 'Return' to continue -> ")
except(EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
