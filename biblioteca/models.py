from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Libro(models.Model):
    GENEROS = [
        ('ficcion', 'Ficcion'),
        ('no_ficcion', 'No Ficcion'),
        ('fantasia', 'Fantasia'),
        ('ciencia', 'Ciencia'),
        ('historia', 'Historia'),
    ]
    
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    isbn = models.CharField(max_length=13, unique=True)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=20, choices=GENEROS)
    paginas = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo
    
class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateTimeField(unll=True, blank=True)
    devuelto = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.libro.titulo} - {self.usuario.username}"