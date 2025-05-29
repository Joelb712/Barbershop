from django.db import models

# Create your models here.
class Producto(models.Model):
    idproducto=models.AutoField(primary_key=True, auto_created=True, editable=False)
    nombre=models.CharField(max_length=100)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    descripcion=models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table='Productos'
