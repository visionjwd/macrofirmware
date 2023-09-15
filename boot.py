import board
from digitalio import DigitalInOut, Direction, Pull

print ("Boot Up")

row = DigitalInOut(board.D7)
col = DigitalInOut(board.D6)

row.direction = Direction.INPUT
col.direction = Direction.OUTPUT
