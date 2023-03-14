class Contador:
    contador = 0 # Atributo de classe

    # Método de classe (não precisa de self)
    @classmethod
    def incrementar(cls):
        cls.contador += 1
        return cls.contador
    
    @classmethod
    def decrementar(cls):
        cls.contador -= 1
        return cls.contador
    
    @staticmethod
    def resetar():
        Contador.contador = 0
        return Contador.contador
    
c1 = Contador()
print(c1.incrementar())
# Instâncias ainda podem acessar métodos da classe

# Dá até sem instancia
print(Contador.incrementar())
print(Contador.resetar())