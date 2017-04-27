from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Organism, Gene, Link

def index(request):
    """
    View function for homepage of site
    """
    
    # Render the HTML template index.html
    
    return render(
        request,
        'index.html',
    )
    
    
class OrganismListView(generic.ListView):

    model = Organism
    context_object_name = 'organism_list'
    template_name = 'gene_list'
    


class OrganismDetailView(generic.DetailView):
    
    model = Organism
    context_object_name = 'org_details'
    template_name = 'catalog/org_details.html'


class PrimaryLinkView(generic.ListView):
    
    model = Link
    context_object_name = 'prim_links'
    template_name = 'catalog/org_details.html'
    
    