from django.contrib import admin
from django.urls import path, include
from .views import home, ingresos,costos,gastos_operacionales, agregar_cliente, ingresos_editar, gastos_operacionales_editar, costos_editar

urlpatterns = [
    path('home/', home,name='home'),
    path('ingresos/',ingresos,name='ingresos'),
    path('costos/',costos,name='costos'),
    path('gastos_operacionales/',gastos_operacionales,name='gastos_operacionales'),
    path('agregar_cliente/',agregar_cliente,name='agregar_cliente'),
    path('ingresos_editar/',ingresos_editar,name='ingresos_editar'),
    path('gastos_operacionales_editar/',gastos_operacionales_editar,name='gastos_operacionales_editar'),
    path('costos_editar',costos_editar,name='costos_editar')

]
