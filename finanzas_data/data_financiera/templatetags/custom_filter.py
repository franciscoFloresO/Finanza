from django import template
from data_financiera.models import Ingreso  # Asegúrate de importar tu modelo Ingreso

register = template.Library()

@register.filter(name='get_by_cliente')
def get_by_cliente(ingresos, cliente_nombre):
    return ingresos.filter(ingreso_cliente=cliente_nombre)