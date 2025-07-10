import numpy as np
from PIL import Image

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def generate_fractal(width, height, x_min, x_max, y_min, y_max, max_iter):
    img = Image.new('RGB', (width, height), 'black')
    pixels = img.load()

    for x in range(width):
        for y in range(height):
            # Convert pixel coordinate to complex number
            real = x_min + (x / width) * (x_max - x_min)
            imag = y_min + (y / height) * (y_max - y_min)
            c = complex(real, imag)

            m = mandelbrot(c, max_iter)
            color = 255 - int(m * 255 / max_iter)
            pixels[x, y] = (color, color, color)

    img.save('fractal.png')

if __name__ == '__main__':
    # You can play with these values to change the zoom and detail
    generate_fractal(800, 600, -2.0, 1.0, -1.5, 1.5, 256)
