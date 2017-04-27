from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()
   
@register.filter
def filter_by_taxonomy(Organism, taxonomic_group):
    return Organism.filter(taxonomic_group=taxonomic_group)

