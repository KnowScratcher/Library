from barcode import Code128
from barcode.writer import ImageWriter

for i in range(1, 10000):
    number = "ADD%04d" %i
    my_code = Code128(number, writer=ImageWriter())
    my_code.save("barcode/codes/ADD%04d" %i)