from picographics import PicoGraphics, DISPLAY_TUFTY_2040
from jpegdec import JPEG

display = PicoGraphics(display=DISPLAY_TUFTY_2040)
j = JPEG(display)

j.open_file("r8.jpg")
j.decode()
display.update()