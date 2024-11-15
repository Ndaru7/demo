class Orang:
    
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        
    def halo(self):
        print(self.nama, self.umur)
        
class Siswa(Orang):
    def __init__(self, nama, umur, nisn):
        super().__init__(nama, umur)
        self.nisn = nisn
        
    def info(self):
        print(f"nama: {self.nama}\numur: {self.umur}\nnisn: {self.nisn}")
        
daru = Siswa("Daru", 20, 8080)
daru.info()