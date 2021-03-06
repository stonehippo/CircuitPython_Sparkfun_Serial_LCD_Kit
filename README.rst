Introduction
============

This driver is for the `Sparkfun Serial LCD Kit <https://www.sparkfun.com/products/10097>`_. It provides and API for the full set of `byte-based commands that control the backpack <https://github.com/jimblom/Serial-LCD-Kit/wiki/Serial-Enabled-LCD-Kit-Datasheet>`_.

Dependencies
============

This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

The ``SerialLCDKit`` class sends text and special command bytes to the backup controller via a UART.

.. code-block:: python

  import board
  import busio
  import serial_lcd_kit

  uart = busio.UART(board.TX, board.RX, baudrate=9600)
  lcd = serial_lcd_kit.SerialLCDKit(uart)

  lcd.write("Hello, world!")

The ``BaudRate`` class defines constants for valid baud rates to set on the serial interface for the backpack controller

.. code-block:: python

  import board
  import busio
  import serial_lcd_kit

  uart = busio.UART(board.TX, board.RX, baudrate=9600)
  lcd = serial_lcd_kit.SerialLCDKit(uart)

  # set the new baud rate to 115,200 bps, which will be stored in EEPROM
  lcd.set_baud_rate(serial_lcd_kit.BaudRate.BAUD_RATE_115200)

  # adjust the baudrate on the UART to match
  lcd._uart.baudrate = 115200


