from django import template


register = template.Library()
   
@register.filter
def filter_by_taxonomy(Organism, taxonomic_group):
    return Organism.filter(taxonomic_group=taxonomic_group)

