import board
import busio
import serial_lcd_kit

uart = busio.UART(board.TX, board.RX, baudrate=9600)
lcd = serial_lcd_kit.SerialLCDKit(uart)

lcd.clear_display()
lcd.write("Hello, world!")