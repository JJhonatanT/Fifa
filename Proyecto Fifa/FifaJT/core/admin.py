from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from . models import Team, Player, PlayerPosition, Coach



@admin.register(Team)
class TeamAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display= ('name_team', 'Bandera', 'Escudo')
    list_display_links= ('name_team',)
    search_fields= ('name_team',) 

    class TeamResource(resources.ModelResource):
        class Meta:
            model = Team
            fields = ('name_team')
            export_order = ('name_team')

@admin.register(Player)
class PlayerAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display= ('first_name', 'last_name', 'FotoJugador', 'date_of_birth')
    list_display_links= ('first_name',)
    search_fields= ('first_name',)  

    class PlayerResource(resources.ModelResource):
        class Meta:
            model = Player
            fields = ('first_name')
            export_order = ('first_name')

@admin.register(PlayerPosition)
class PlayerPositionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display= ('name', 'description')
    list_display_links= ('name',)
    search_fields= ('name',)  

    class PlayerPositionResource(resources.ModelResource):
        class Meta:
            model = PlayerPosition
            fields = ('name')
            export_order = ('name')


@admin.register(Coach)
class CoachAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display= ('first_name', 'last_name', 'date_of_birth', 'nationality', 'role')
    list_display_links= ('role', 'nationality',)
    search_fields= ('role', 'first_name',)  

    class CoachResource(resources.ModelResource):
        class Meta:
            model = Coach
            fields = ('first_name')
            export_order = ('first_name')