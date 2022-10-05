import time
from micropython import const

# Sparkfun Enabled LCD Kit API

_CMD_BACKLIGHT = const(0x80)
_CMD_BAUD_RATE = const(0x81)
_CMD_SPECIAL_COMMAND = const(0xFE)
_SPEC_CMD_CLEAR = const(0x01)
_SPEC_CMD_20_COLUMNS = const(0x03)
_SPEC_CMD_16_COLUMNS = const(0x04)
_SPEC_CMD_4_LINES = const(0x05)
_SPEC_CMD_2_LINES = const(0x06)
_SPEC_CMD_MOVE_CURSOR_RIGHT_ONE = const(0x14)
_SPEC_CMD_MOVE_CURSOR_LEFT_ONE = const(0x10)
_SPEC_CMD_SCROLL_RIGHT = const(0x1C)
_SPEC_CMD_SCROLL_LEFT = const(0x18)
_SPEC_CMD_TURN_OFF = const(0x08)
_SPEC_CMD_TURN_ON = const(0x0C)
_SPEC_CMD_UNDERLINE_ON = const(0x0E)
_SPEC_CMD_UNDERLINE_OFF = const(0x0C)
_SPEC_CMD_BLINKING_BOX_ON = const(0x0D)
_SPEC_CMD_BLINKING_BOX_OFF = const(0x0C)
_SPEC_CMD_SET_CURSOR_POSITION = const(0x80)
_SPEC_CMD_TOGGLE_SPLASH = const(0x1E)
_CHAR_CMD_CARRIAGE_RETURN = const(0X0D)
_CHAR_CMD_LINE_FEED = const(0x0A)
_CHAR_CMD_TAB = const(0x09)
_CHAR_CMD_BACKSPACE = const(0x08)

class SerialLCDKit:
  def __init__(self, uart):
    self._uart = uart

  def command(self, buf):
    self._uart.write(buf)

  def special_command(self, cmd):
    self.command(bytes([_CMD_SPECIAL_COMMAND, cmd]))
  
  def char_command(self, cmd):
    self.command(bytes([cmd]))

  def set_baud_rate(self, baud, show_new_rate=True):
    # update the LCD itself, changing the current baud rate and updating the EEPROM
    self.command(bytes([_CMD_BAUD_RATE, baud[1]]))
    # sleep briefly so the command has time to get sent over slow UART connections
    time.sleep(1)
    # update the UART so we can keep talking to the LCD
    self._uart.baudrate = baud[0]

    # update the display to show the new baud rate
    self.clear_display()
    if show_new_rate:
      self.write(f"Using {baud[0]} BPS")

  def write(self, str):
    self.command(bytes(str, "ascii"))

  def clear_display(self):
    self.special_command(_SPEC_CMD_CLEAR)

  def toggle_splash(self):
    self.special_command(_SPEC_CMD_TOGGLE_SPLASH)

  def set_backlight(self, level):
    self.command(bytes([_CMD_BACKLIGHT, level]))
  
  def enable(self):
    self.special_command( _SPEC_CMD_TURN_ON)

  def disable(self):
    self.special_command(_SPEC_CMD_TURN_OFF)

  def set_cursor_at(self, pos):
    self.command(bytes([_CMD_SPECIAL_COMMAND, _SPEC_CMD_SET_CURSOR_POSITION, pos]))

  def right(self):
    self.special_command(_SPEC_CMD_MOVE_CURSOR_RIGHT_ONE)

  def left(self):
    self.special_command(_SPEC_CMD_MOVE_CURSOR_LEFT_ONE)

  def scroll_right(self):
    self.special_command(_SPEC_CMD_SCROLL_RIGHT)

  def scroll_left(self):
    self.special_command(_SPEC_CMD_SCROLL_LEFT)

  def enable_blink(self):
    self.special_command(_SPEC_CMD_BLINKING_BOX_ON)

  def disable_blink(self):
    self.special_command(_SPEC_CMD_BLINKING_BOX_OFF)

  def enable_underline(self):
    self.special_command(_SPEC_CMD_UNDERLINE_ON)

  def set_display_20_columns(self):
    self.special_command(_SPEC_CMD_20_COLUMNS)

  def set_display_16_columns(self):
    self.special_command(_SPEC_CMD_16_COLUMNS)

  def set_display_4_lines(self):
    self.special_command(_SPEC_CMD_4_LINES)

  def set_display_2_lines(self):
    self.special_command(_SPEC_CMD_2_LINES)

  def disable_underline(self):
    self.special_command(_SPEC_CMD_UNDERLINE_OFF)

  def carriage_return(self):
    self.char_command(_CHAR_CMD_CARRIAGE_RETURN)

  def line_feed(self):
    self.char_command(_CHAR_CMD_LINE_FEED)

  def tab(self):
    self.char_command(_CHAR_CMD_TAB)

  def backspace(self):
    self.char_command(_CHAR_CMD_BACKSPACE)
    
class BaudRate:
  # the first value of each tuple is the bit rate (used to set the UART),
  # the second is the value expected by the serial backpack to use that bit rate
  BAUD_RATE_300 = (300, 0)
  BAUD_RATE_1200 = (1200, 1)
  BAUD_RATE_2400 = (2400, 2)
  BAUD_RATE_4800 = (4800, 3)
  BAUD_RATE_9600 = (9600, 4)
  BAUD_RATE_14400 = (14400, 5)
  BAUD_RATE_19200 = (19200, 6)
  BAUD_RATE_28800 = (28800, 7)
  BAUD_RATE_38400 = (38400, 8)
  BAUD_RATE_57600 = (57600, 9)
  BAUD_RATE_115200 = (115200, 10)