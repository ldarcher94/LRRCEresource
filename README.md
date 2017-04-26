# LRRCEresource

This repository contains files associated with the project: 
"Developing a Web-based Resource for the Classification, Annotation, and Sequence Retrieval 
of Small Leucine-rich Repeat Proteins and Proteoglycans"

Supervisor: Dr. Jordi Bella

To run the server and view the resource in a browser:
  1. Clone repository to local machine
  2. Open command line and navigate to root file of repository (File that contains manage.py)
  3. Run server with this command - $ python3 manage.py runserver
    (System should perform checks and identify 0 issues)
  4. Open browser, and in the address bar enter: localhost:8000/catalog/
    This is the homepage of the resource, and from here you should be able to navigate around 
    the site without the need to enter anything into the address bar
    
To see the structure of the database, go to localhost:8000/admin/
This will take you to a page constructed by Django, containing links to the different tables in
in the database and showing the information contained.
For a more detailed view of an entry (or to edit the information) click on individual entries.
