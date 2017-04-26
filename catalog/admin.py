from django.contrib import admin

from .models import Organism, Gene, Link

#admin.site.register(Organism)
#admin.site.register(Gene)
#admin.site.register(Link)

@admin.register(Organism)
class OrganismAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'taxonomic_group')
    
@admin.register(Gene)
class GeneAdmin(admin.ModelAdmin):
    list_display = ('title', 'class_field', 'organism')
    list_filter = ('class_field', 'organism')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('link_accession', 'gene', 'link_type', 'primary')

# Register your models here.