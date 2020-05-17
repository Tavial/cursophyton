
import re
"""
    Definimos la clase validador
"""

class Validador():
    def __init__(self):
        self.patron_no_vacio = "(^$)|(\s+$)"  # que no esté vacío o haya espacios en blanco
        self.patron_num_real = "^\d+((\.|,)\d+)?$"
        self.patron_num_entero = "^[0-9]+$"
        self.patron_nombre = "^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$"
        self.patron_email ="^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$"

    def noVacio(self, texto_a_validar):
        valida = re.compile(self.patron_no_vacio)
        resultado_validacion = valida.match(texto_a_validar)

        if resultado_validacion:
            return False
        else:
            return True

    def numReal(self, texto_a_validar):
        valida = re.compile(self.patron_num_real)
        resultado_validacion = valida.match(texto_a_validar)

        if resultado_validacion:
            return True
        else:
            return False

    def numEntero(self, texto_a_validar):
        valida = re.compile(self.patron_num_entero)
        resultado_validacion = valida.match(texto_a_validar)

        if resultado_validacion:
            return True
        else:
            return False

    def nombreApellidos (self, texto_a_validar):
        valida = re.compile(self.patron_nombre)
        resultado_validacion = valida.match(texto_a_validar)

        if resultado_validacion:
            return True
        else:
            return False

    def email (self, texto_a_validar):
        valida = re.compile(self.patron_email)
        resultado_validacion = valida.match(texto_a_validar)
        if resultado_validacion:
            return True
        else:
            return False
