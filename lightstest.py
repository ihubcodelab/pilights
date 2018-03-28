# author - Sam Baskin - @sambskn 
# Based off example code from Adafruit tutorial
import time

from neopixel import *

# LED strip configuration:
LED_COUNT   = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


#key functions to use when using these LED's
#numPixels() - returns number of pixels in the strip, helpful when looping through them all
#setPixelColor(pos, color) OR (pos,red, blue, green), sets color at a certain pixel, 
# can use a 24bit color value (first 8 bits are the red value and so on) 
# or you can just pass values between 0 and 255 for the RGB individually
# show() has to be called after changing color values for changes to take effect

#function here taken from neopixel library examples
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


#main loop
if __name__ == '__main__':
    #Check for arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', action='store_true', help='run a test of the current setup')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the strip (gotta do this first)
    strip.begin()

    print('Press Ctrl-C to quit')

    try:
        #acutal main loop begins here
        while True:
            print('lights yo')
    except KeyboardInterrupt:
        #turn off all lights on program close
        colorWipe(strip, Color(0,0,0), 10)
