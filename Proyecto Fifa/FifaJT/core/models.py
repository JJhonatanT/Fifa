from django.db import models
from datetime import datetime
from django.utils.html import format_html

class Team(models.Model):
    name_team = models.CharField(max_length=100, verbose_name="NombreEquipo")
    flag_image = models.ImageField(upload_to='media', null=True, blank=True)
    team_shield = models.ImageField(upload_to='media', null=True, blank=True)

    def Bandera(self):
        return format_html('<img src={} width="100" /> ', self.flag_image.url)
    
    def Escudo(self):
        return format_html('<img src={} width="100" /> ', self.team_shield.url)
    
    def __str__(self):
        return self.name_team

    class Meta:
        verbose_name = "Equippo"
        verbose_name_plural = "Equipos"
        db_table = "equipo"
        ordering = ['id']

class Player(models.Model):

    IS_TITULAR_CHOICES = [
    ('SI', 'Sí'),
    ('NO', 'No'),
    ]
    first_name = models.CharField(max_length=50, verbose_name="Nombre")
    last_name = models.CharField(max_length=50, verbose_name="Apellido")
    player_photo = models.ImageField(upload_to='media', null=True, blank=True)
    date_of_birth = models.DateField(verbose_name="Fecha Nacimiento")
    position = models.CharField(max_length=50, verbose_name="Posicion")
    jersey_number = models.PositiveIntegerField(verbose_name="Numero Camisa")
    starter = models.CharField(max_length=2, choices=IS_TITULAR_CHOICES, default='NO', verbose_name="Es Titular")
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='players', verbose_name="Team")

    def FotoJugador(self):
        return format_html('<img src={} width="100" /> ', self.player_photo.url)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"
        db_table = "jugador"
        ordering = ['id']
        
class PlayerPosition(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripcion")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Posicion Jugador"
        verbose_name_plural = "Posicion Jugadores"
        db_table = "posicion_jugador"
        ordering = ['id']
        


class Coach(models.Model):
    TECHNICAL = 'tecnico'
    ASSISTANT = 'asistente'
    MEDICAL = 'medico'
    CONDITIONING = 'preparador'

    ROLE = [
        (TECHNICAL, 'Tecnico'),
        (ASSISTANT, 'Asistente'),
        (MEDICAL, 'Medico'),
        (CONDITIONING, 'Preparador'),
    ]

    FOOTBALL_COUNTRIES = [
        ('BRA', 'Brasil'),
        ('ARG', 'Argentina'),
        ('GER', 'Alemania'),
        ('ITA', 'Italia'),
        ('FRA', 'Francia'),
        ('ESP', 'España'),
        ('ENG', 'Inglaterra'),
        ('POR', 'Portugal'),
        ('NED', 'Países Bajos'),
        ('URU', 'Uruguay'),
        ('COL', 'Colombia'),
    ]
    
    FOOTBALL_NATIONALITIES = [
        ('BRA', 'Brasil'),
        ('ARG', 'Argentina'),
        ('GER', 'Alemania'),
        ('ITA', 'Italia'),
        ('FRA', 'Francia'),
        ('ESP', 'España'),
        ('ENG', 'Inglaterra'),
        ('POR', 'Portugal'),
        ('NED', 'Países Bajos'),
        ('URU', 'Uruguay'),

]

    first_name = models.CharField(max_length=50, verbose_name="Nombre")
    last_name = models.CharField(max_length=50, verbose_name="Apellido")
    date_of_birth = models.DateField(verbose_name="FechaNacimiento")
    nationality = models.CharField(max_length=3, choices=FOOTBALL_COUNTRIES, verbose_name="Nacionalidad")
    role = models.CharField(max_length=20, choices=ROLE, verbose_name="Rol")
    equipo = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='coaches', verbose_name="Team")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Tecnico"
        verbose_name_plural = "Tecnicos"
        db_table = "tecnico"
        ordering = ['id']
