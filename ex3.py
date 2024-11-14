class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor 
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor 
        else:
            print("Saldo insuficiente")
    def saldao(self):
        print(f"saldo: {self.__saldo}")

c = ContaBancaria("Fabio", 500)
c.depositar(60)
c.sacar(30)
c.saldao()
c.sacar(70)
