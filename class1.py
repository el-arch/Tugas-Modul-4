
class kelas:
    def __init__(self, x, y, z, pil):
        if(x == 1):
            print("-" * 40)
            print("Anda memilih jaket", y[pil-1], "dengan harga Rp.", z[pil-1])
            print("-" * 40)
        else:
            return 0

    def hasil(self, y, a, b, c, pil1, pil):
        if(y == 2):    
            print("-" * 40)
            print("Anda memilih jaket", a[pil-1], ", ukuran", b[pil1-1], "dengan harga Rp.", c[pil-1])
            print("-" * 40)
        else:
            return 0
