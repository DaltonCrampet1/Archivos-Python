class Tarjeta:
    def __init__(self, num, tit, venc, cvvs, credito):
        self.numero = num
        self.titular = tit
        self.fechavenc = venc
        self.cvv = cvvs
        self.limitcredito = credito


num1 = 1234567890123456
tit1 = "Adela Sanchez"
venc1 = "12/26"
cvvs1 = "123"
credito1 = 2000

num2 = 9876543210987654
tit2 = "Juan Oreste"
venc2 = "06/25"
cvvs2 = "456"
credito2 = 1500

tarjeta1 = Tarjeta(num1, tit1, venc1, cvvs1, credito1)
tarjeta2 = Tarjeta(num2, tit2, venc2, cvvs2, credito2)


class Pagar:
    def __str__(self):
        print("a")
