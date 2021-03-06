# Sparkfun Enabled LCD Kit API

_CMD_BACKLIGHT = 0x80
_CMD_BAUD_RATE = 0x81
_CMD_SPECIAL_COMMAND = 0xFE
_SPEC_CMD_CLEAR = 0x01
_SPEC_CMD_MOVE_CURSOR_RIGHT_ONE = 0x14
_SPEC_CMD_MOVE_CURSOR_LEFT_ONE = 0x10
_SPEC_CMD_SCROLL_RIGHT = 0x1C
_SPEC_CMD_SCROLL_LEFT = 0x18
_SPEC_CMD_TURN_OFF = 0x08
_SPEC_CMD_TURN_ON = 0x0C
_SPEC_CMD_UNDERLINE_ON = 0x0E
_SPEC_CMD_UNDERLINE_OFF = 0x0C
_SPEC_CMD_BLINKING_BOX_ON = 0x0D
_SPEC_CMD_BLINKING_BOX_OFF = 0x0C
_SPEC_CMD_SET_CURSOR_POSITION = 0x80
_SPEC_CMD_TOGGLE_SPLASH = 0x1E

class SerialLCDKit:
  def __init__(self, uart):
    self._uart = uart

  def command(self, buf):
    self._uart.write(buf)

  def special_command(self, cmd):
    self.command(bytes([_CMD_SPECIAL_COMMAND, cmd]))

  def set_baud_rate(self, rate):
    self.command(bytes([_CMD_BAUD_RATE, rate]))

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

  def disable_underline(self):
    self.special_command(_SPEC_CMD_UNDERLINE_OFF)

class BaudRate:
  BAUD_RATE_300 = 300
  BAUD_RATE_1200 = 1200
  BAUD_RATE_2400 = 2400
  BAUD_RATE_4800 = 4800
  BAUD_RATE_9600 = 9600
  BAUD_RATE_14400 = 14400
  BAUD_RATE_19200 = 19200
  BAUD_RATE_38400 = 38400
  BAUD_RATE_57600 = 57600
  BAUD_RATE_115200 = 115200