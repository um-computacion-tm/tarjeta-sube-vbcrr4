class NoHaySaldoException(Exception):
    pass
class UsuarioDesactivadoException(Exception):
    pass
class EstadoNoExistenteException(Exception):
    pass

PRIMARIO = 'primario'
SECUNDARIO = 'secundario'
UNIVERSITARIO = 'universitario'
JUBILADO = 'jubilado'
PRECIO_TICKET = 70
DESACTIVADO = 'desactivado'
ACTIVADO = 'activado'

DESCUENTOS = {
    PRIMARIO: 50,
    SECUNDARIO: 40,
    UNIVERSITARIO: 30,
    JUBILADO: 25,
}

class Sube():
    def __init__(self):
        self.saldo = 0
        self.estado = 'activado'
        self.grupo_beneficiario = None
    
    def cambiar_estado(self,nuevoEstado):
        if nuevoEstado not in [ACTIVADO, DESACTIVADO]:
            raise EstadoNoExistenteException

        self.estado = nuevoEstado

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario in DESCUENTOS:
            descuento_porcentaje = DESCUENTOS[self.grupo_beneficiario]
            precio_con_descuento = PRECIO_TICKET * (1 - descuento_porcentaje / 100)
            return precio_con_descuento
        else:
            return PRECIO_TICKET
        
    def pagar_pasaje(self):
        precioticket = self.obtener_precio_ticket()
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException("El usuario está desactivado")
        if self.saldo < precioticket:
            raise NoHaySaldoException("No hay saldo suficiente")
        self.saldo -= precioticket

if __name__ == '__:main__':
    pass