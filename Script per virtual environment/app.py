from flask import Flask, render_template, request, jsonify
from owlready2 import *

app = Flask(__name__)
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))


@app.route("/")
def home_page():
    return "lorenza"


@app.route("/free_query", methods=['POST'])
def recipes_information():
    if request.method == 'POST':
        data = f"""{request.data.decode("utf-8")}"""

        go = get_ontology("./UniOn.owl").load()
        print(data)

        a = str(list(default_world.sparql(data)))

        print(a)

        return jsonify({"response": a})




if __name__ == "__main__":
    app.run()

#1

'''
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX uo: <http://purl.org/ontology/UniOn#>
            SELECT ?DegreeProgrammeLabel (COUNT(?DegreeProgrammeLabel) as ?DegreeCount)
            WHERE {
            ?DegreeProgramme uo:isDeliveredBy ?ItalianUniversity ;
                            uo:hasAcademicField ?AcademicField .
            ?ItalianUniversity rdfs:label "University of Bologna" .
            ?AcademicField rdfs:label "Studi umanistici" .

            OPTIONAL { ?DegreeProgramme rdfs:label ?DegreeProgrammeLabel}
            }
            GROUP BY ?DegreeProgrammeLabel
            ORDER BY DESC(?DegreeCount)
'''

#2
'''
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX uo: <http://purl.org/ontology/UniOn#>
            SELECT DISTINCT ?UniversityLabel
            WHERE {
            ?DegreeProgramme uo:isDeliveredBy ?University .
            ?DegreeProgramme rdfs:label "Filosofia" .

            OPTIONAL { ?University rdfs:label ?UniversityLabel}
            }
'''


#3
'''
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX uo: <http://purl.org/ontology/UniOn#>
            SELECT ?AccessTypeLabel
            WHERE {
            ?DegreeProgramme uo:hasAccessType ?AccessType .
            ?DegreeProgramme rdfs:label "Semiotica" .

            OPTIONAL { ?AccessType rdfs:label ?AccessTypeLabel}
            }
'''

#4

'''
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX uo: <http://purl.org/ontology/UniOn#>
            SELECT ?EducationalActivityLabel
            WHERE {
            ?DegreeProgramme uo:hasEducationalActivity ?EducationalActivity ;
                            rdfs:label "Storia" .

            OPTIONAL { ?EducationalActivity rdfs:label ?EducationalActivityLabel}
            }
'''

#5 DA CAMBIARE QUERY IN: quale corso di studi e quanti cfu mi da in tale ssd 

'''
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX uo: <http://purl.org/ontology/UniOn#>
            SELECT ?DegreeProgrammeLabel (SUM(?CFUofEducation) as ?CFU)
            WHERE {
            ?DegreeProgramme a <http://purl.org/ontology/UniOn#BachelorDegree> ;
                             uo:hasEducationalActivity ?EducationalActivity ;
                             rdfs:label "Storia" .
            ?EducationalActivity uo:hasSsd "M-STO/01" .
            ?EducationalActivity uo:hasCfu ?CFUofEducation .

            OPTIONAL { ?DegreeProgramme rdfs:label ?DegreeProgrammeLabel}
            }
'''
