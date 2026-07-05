import pyxel

pyxel.init(160, 120, title="Custom Font")
pyxel.load("my_resource.pyxres")

font10 = pyxel.Font("assets/umplus_j10r.bdf")  # BDF doesn't use font size
font12 = pyxel.Font("assets/PixelMplus12-Regular.ttf", 12)

pyxel.cls(1)
pyxel.blt(0, 0, 1, 0, 0, 128, 128)

pyxel.text(4, 8, "日本語で表示", 8, font10)
pyxel.text(4, 88, "気軽に楽しく", 7, font12)
pyxel.text(4, 103, "プログラミング！", 7, font12)

pyxel.show()