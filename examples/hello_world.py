import board
# import busio if board.UART() is not available
#import busio
import serial_lcd_kit

lcd = serial_lcd_kit.SerialLCDKit(board.UART())

# if the above doesn't work, or if you need to use a secondary UART, use busio
#uart = busio.UART(board.TX, board.RX, baudrate=9600)
#lcd = serial_lcd_kit.SerialLCDKit(uart)

lcd.clear_display()
lcd.write("Hello, world!")