class OffsetPrinter:
    def __init__(self):
        self.offset = 0
    def __enter__(self):
        self.offset += 1
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.offset -= 1
    def print(self, msg):
        offsets =''.join(['\t' for _ in range(self.offset)])
        print(offsets + msg)

printer = OffsetPrinter()

printer.print('N1')
with printer:
    printer.print('N2')
    with printer:
        printer.print('N3')
    printer.print('N2')
printer.print('N1')