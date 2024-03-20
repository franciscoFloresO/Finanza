from django.db import models
#from django.contrib.auth.models import AbstractUser

# Create your models here.
class Pais(models.Model):
    id_pais=models.AutoField(primary_key=True)
    pais_nombre=models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.pais_nombre
    

class Division(models.Model):
    id_division=models.AutoField(primary_key=True)
    division_nombre=models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.division_nombre
    
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    cliente_nombre = models.CharField(max_length=50, unique=True, default='')  
    cliente_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='pais_cliente', blank=True)  
    cliente_division = models.ForeignKey(Division, on_delete=models.CASCADE, blank=True)  
    cliente_ceco = models.CharField(max_length=50, null=True, blank=True, unique=True, default='')  

    def __str__(self):
        return self.cliente_nombre
    
class Ingreso(models.Model):
    id_ingreso = models.AutoField(primary_key=True)
    ingreso_pais = models.CharField(max_length=50)
    ingreso_ceco = models.CharField(max_length=50)
    ingreso_cliente = models.CharField(max_length=100)  
    ingreso_division = models.CharField(max_length=100) 
    ingreso_mes = models.CharField(max_length=10)
    ingreso_anno = models.CharField(max_length=4)
    ingreso_real = models.CharField(max_length=10, null=True, blank=True)  
    ingreso_forecast = models.CharField(max_length=10, null=True, blank=True) 

    def __str__(self):
        return str(self.id_ingreso)



class Costo(models.Model):
    id_costo=models.AutoField(primary_key=True)
    costo_pais=models.CharField(max_length=50)
    costo_ceco=models.CharField(max_length=50)
    costo_cliente=models.CharField(max_length=100)
    costo_division=models.CharField(max_length=100)
    costo_mes=models.CharField(max_length=10)
    costo_anno=models.CharField(max_length=4)
    costo_real=models.CharField(max_length=10, null=True, blank=True)
    costo_forecast=models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.id_costo)
    
class Gasto_Operacional(models.Model):
    id_gas_op=models.AutoField(primary_key=True)
    gas_op_pais=models.CharField(max_length=50)
    gas_op_ceco=models.CharField(max_length=50)
    gas_op_cliente=models.CharField(max_length=100)
    gas_op_division=models.CharField(max_length=100)
    gas_op_mes=models.CharField(max_length=10)
    gas_op_anno=models.CharField(max_length=4)
    gas_op_real=models.CharField(max_length=10, null=True, blank=True)
    gas_op_forecast=models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.id_gas_op)    
    

# class Usuario(AbstractUser):
#     usuario = models.EmailField(max_length=30)
#     pais = models.ForeignKey(Pais, on_delete=models.CASCADE, blank=True) 
#     division = models.ForeignKey(Division, on_delete=models.CASCADE, blank=True) 

#     def __str__(self):
#         return self.username