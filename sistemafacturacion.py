import datetime

class Mayorista:
    def __init__(self, nombre, razon_social):
        self.m_nombre = nombre
        self.m_razon_social = razon_social
        self.m_facturas = []

    def add_factura(self, factura):
        self.m_facturas.append(factura)

    def sumallfacturas(self):
        total = 0
        for factura in self.m_facturas:
            total += factura.m_total
        return total
    
    def mostrar_resultados(self):
        print(f"Nombre de la empresa: {self.m_nombre} - IVA: {self.m_razon_social}")
        for factura in self.m_facturas:
            factura.mostrar_resultados()
        print(f"Total de todas las facturas: {self.sumallfacturas()}")

class Factura:
    def __int__(self, nro_factura, fecha, cliente):
        self.m_nro_factura = nro_factura
        self.m_fecha = fecha
        self.m_cliente = cliente
        self.m_elementos = []
        self.m_total = self.calcular_total()

    def calcular_total(self):
        total = 0
        for elemento in self.m_elementos:
            total += elemento[1]
        return total
    
    def mostrar_resultados(self):
        print(f"Factura nro: {self.m_nro_factura}")
        print(f"Cliente: {self.m_cliente.m_nombre}")
        print(f"Fecha: {self.m_fecha.strftime('%d/%m/%Y')}")
        print(f"Total: {self.m_total}")
        cont = 1
        for elemento in self.m_elementos:
            print(f"Detalle {cont}: {elemento[0]} Total Item: {elemento[1]}")
            cont += 1
    



class Cliente:
    def __init__(self, nombre, razon_social, cuil):
        self.m_nombre = nombre
        self.m_razon_social = razon_social
        self.m_cuil = cuil

# Cargar mayoristas
mayorista1 = Mayorista("Mayorista S.A", "Monotributo")
mayorista2 = Mayorista("Kilgelman S.A", "Responsable Inscripto")

# Cargar clientes
cliente1 = Cliente("Cliente 1", "Monotributista", 12456780)
cliente2 = Cliente("Cliente 2", "Consumidor Final", 43928621)

# Cargar facturas
factura1 = Factura(1000, datetime.date.today(), cliente1)
factura2 = Factura(1001, datetime.date.today(), cliente2)
# Contenido de las facturas
elemento1 = ("Porcelanato 45x45 100 unid.", 600)
elemento2 = ("Grifería FV 6 piezas 1 unid.", 400)
factura1.m_elementos.append(elemento1)
factura1.m_elementos.append(elemento2)

elemento3 = ("4 resmas A4 45 grms.", 700)
elemento4 = ("Papel fotografico x20u.", 500)
factura2.m_elementos.append(elemento3)
factura2.m_elementos.append(elemento4)

mayorista1.add_factura(factura1)
mayorista1.add_factura(factura2)
    