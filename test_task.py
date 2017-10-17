from rdflib import Graph
from rdflib import URIRef, Literal
from rdflib.namespace import RDF, FOAF
from rdflib import Namespace
import os

n = Namespace("people/")

path = os.path.dirname(os.path.realpath("test_task.py"))

g = Graph()

g.add( (URIRef(n.bob), RDF.type, FOAF.Person) )
g.add( (URIRef(n.alice), RDF.type, FOAF.Person) )
g.add( (URIRef(n.john), RDF.type, FOAF.Person) )
g.add( (URIRef(n.mike), RDF.type, FOAF.Person) )

g.add( (URIRef(n.bob), FOAF.name, Literal('Bob')) )
g.add( (URIRef(n.alice), FOAF.name, Literal('Alice')) )
g.add( (URIRef(n.john), FOAF.name, Literal('John')) )
g.add( (URIRef(n.mike), FOAF.name, Literal('Mike')) )


g.add( (URIRef(n.bob), FOAF.knows, URIRef(n.alice)) )
g.add( (URIRef(n.bob), FOAF.knows, URIRef(n.john)) )
g.add( (URIRef(n.alice), FOAF.knows, URIRef(n.bob)) )
g.add( (URIRef(n.alice), FOAF.knows, URIRef(n.Mike)) )
g.add( (URIRef(n.john), FOAF.knows, URIRef(n.bob)) )
g.add( (URIRef(n.mike), FOAF.knows, URIRef(n.alice)) )


g.serialize(destination = path + "\\output.foaf", format='turtle')


qres = g.query(
    """SELECT (count(*) as ?count)
    WHERE {
       ?s ?p ?o .
    }""")


for row in qres:
    print(row)