import board
import terminalio
import displayio
from analogio import AnalogIn
from fourwire import FourWire
from adafruit_display_text import label
from adafruit_st7789 import ST7789
from adafruit_ms8607 import MS8607
i2c = board.I2C()
pht = MS8607(i2c)
import time
border = 20
fontscale = 2
bg_color = 0xFFFFF
fg_color = 0xAA0068
txt_color = 0xFFFF00
displayio_release_displays()
spi = board.SPI()
tft_cs = board.D2
tft_dc = board.D3
dbus = FourWire(spi, command = tft_dc, chip_select = tft_cs)
display = ST7789(dbus, rotation = 270, width = 240, height = 135, rowstart = 40, colstart = 53)
splash = displayio.Group()
Display_Root_Group = splash
color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = bg_color
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader = color_palette, x = 0, y = 0)
splash.append(bg_sprite)
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.polygon import Polygon

tmp = AnalogIn(board.AD)

try:
  from fourwire import FourWire
except ImportError:
  from displayio import FourWire
from adafruit_display_text import label
from adafruit_st7789 import ST7789
border = 20
fontscale = 2
bg_color = 0xFFFFF
fg_color = 0xAA0068
txt_color = 0xFFFF00
displayio_release_displays()
spi = board.SPI()
tft_cs = board.D2
tft_dc = board.D3
dbus = FourWire(spi, command = tft_dc, chip_select = tft_cs)
display = ST7789(dbus, rotation = 270, width = 240, height = 135, rowstart = 40, colstart = 53)
splash = displayio.Group()
Display_Root_Group = splash
inner_bitmap = displayio.Bitmap(display.width - border * 2, display.height - border*2, 1)
inner_palette = fg_color
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader = inner_palette, x = border, y = border)
splash.append(inner_sprite)

def display_text(text):
  text_area = label.Label(teminalio.FONT, text = txt, color = txt_color)
  text_width = text_area.boundingbox[2] * fontscale
  text_group = displayio.Group(scale = fontscale, x = display.width // 2 - text_width // 2, y = display.width // 2,)
  text_group.append(text_area)
  splash.append(text_group)
  time.sleep(3.0)
  splash.remove(text_group)

while True:
  pressure = pht.pressure
  print(pressure)
  display_text(str(pressure) + "hPa")
  
  
