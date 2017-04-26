from django.db import models
from django.urls import reverse # Used to generate urls by reversing the url patterns

class Organism(models.Model):
    """
    Model to define the organisms table, which contains only an id field and organism name.
    
    Primary key - ID field autocreated
    Name - Organism name
    Taxonomic group - Broad taxonomic group that organism belongs to (i.e. Mammal, Urochordates)
    """
    
    name = models.CharField(max_length=50)
    taxonomic_group = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular organism instance
        """
        return reverse('organism', kwargs={'pk': self.pk})

    
class Gene(models.Model):
    """
    Model to define the genes table
    
    Primary key - ID field autocreated
    Foreign key - organism (links to organism table)
    Title - Short title of gene (i.e. KERA_HUMAN)
    Name - List of names (as seen on site)
    Existence - State of protein existence (i.e. Evidence at transcript level)
    LRRCE seq - ONLY sequence of LRRCE motif
    UniProt seq - Sequence from UniProt
    NCBI seq    -     "     "   NCBI
    Genbank seq -     "     "   Genbank
    Class field - Class of protein (i.e. Asporin - class I, Lumican - class IIa)
    """
    
    organism = models.ForeignKey(Organism, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    existence = models.CharField(db_column='Protein Existence', max_length=255)
    lrrce_seq = models.CharField(db_column='LRRCE sequence', max_length=255)
    uniprot_seq = models.TextField(blank=True)
    ncbi_seq = models.TextField(blank=True)
    genbank_seq = models.TextField(blank=True)
    genscan_pred_seq = models.TextField(blank=True, db_column='Genscan Prediction')
    ensembl_seq = models.TextField(blank=True)
    class_field = models.CharField(max_length=5)
    
    def __str__(self):
        return self.title
    
    """   
    def get_fasta_length(sequence):
    
        seq_string = sequence.split('\n', 1)[1] # split string on first newline char only to separate header from seq
    
        seq_formatted = seq_string.replace('\n', '') # remove newline chars
        fasta_length = len(seq_formatted) # find length
    
        return fasta_length
    """
        
    
class Link(models.Model):
    """
    Model to define links table
    
    Primary key - ID field autocreated
    Foreign key - gene (links to gene table)
                - organism (links to organism table)
    Link accession  - Accession code of link (i.e. P01938)
    Link type - UniProt, NCBI, ENSEMBL etc.
    Address - url of link
    Primary - Boolean field, designates primary or other link (True or False respectively)
    """
    
    link_accession = models.CharField(max_length=50)
    gene = models.ForeignKey(Gene, on_delete=models.CASCADE)
    organism = models.ForeignKey(Organism, on_delete=models.CASCADE)
    link_type = models.CharField(max_length=50)
    address = models.TextField()
    primary = models.BooleanField(default=False)
    
    def __str__(self):
        return self.link_accession