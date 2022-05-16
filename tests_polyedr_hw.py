from common.r3 import R3
from polyedr_hw import Polyedr
from common.tk_drawer import TkDrawer as tk


class TestPolyedr_hw:

    def test_1(self):
        tk1 = tk()
        ccc = Polyedr("data/ccc.geom")
        ccc.draw(tk1)
        tk1.close()
        assert 30 * ccc.c * 0.99 < ccc.sum < 30 * ccc.c * 1.01

    def test_3(self):
        tk3 = tk()
        polyedr = Polyedr("data/cube.geom")
        polyedr.draw(tk3)
        tk3.close()
        assert 9 * polyedr.c * 0.99 < polyedr.sum < 9 * polyedr.c * 1.01

    def test_5(self):
        tk5 = tk()
        polyedr = Polyedr("data/box.geom")
        polyedr.draw(tk5)
        tk5.close()
        assert 10 * polyedr.c * 0.99 < polyedr.sum < 10 * polyedr.c * 1.01

    def test_7(self):
        tk7 = tk()
        polyedr = Polyedr("data/pyramid_top.geom")
        polyedr.draw(tk7)
        tk7.close()
        # так как результат посчитан в геогебре
        # с округлением до 2 знаков после запятой
        assert 29.02 * polyedr.c * 0.99 < polyedr.sum < 29.02 * polyedr.c * 1.01

    def test_9(self):
        tk9 = tk()
        polyedr = Polyedr("data/pyramid_bottom.geom")
        polyedr.draw(tk9)
        tk9.close()
        # так как результат посчитан в геогебре
        # с округлением до 2 знаков после запятой
        assert 11.18 * polyedr.c * 0.99 < polyedr.sum < 11.18 * polyedr.c * 1.01

    def test_10(self):
        tk10 = tk()
        polyedr = Polyedr("data/pyramid_in_cube.geom")
        polyedr.draw(tk10)
        tk10.close()
        # так как результат посчитан в геогебре
        # с округлением до 2 знаков после запятой
        assert 18.13 * polyedr.c * 0.99 < polyedr.sum < 18.13 * polyedr.c * 1.01
