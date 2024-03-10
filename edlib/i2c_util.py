import board

def board_i2c():
    # Create I2C bus as normal
    print()
    try:
        i2c = board.I2C()  # uses board.SCL and board.SDA
        print("Using I2C")
    except Exception:
        try:
            i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
            print("Using STEMMA")
        except Exception:
            print("Unable to locate I2C interface - is anything connected?")
            exit(1)
    return i2c

