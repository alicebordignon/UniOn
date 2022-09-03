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

#5

'''
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX uo: <http://purl.org/ontology/UniOn#>
            SELECT (SUM(?CFUofEducation) as ?CFU)
            WHERE {
            ?DegreeProgramme a uo:BachelorDegree ;
                             uo:hasEducationalActivity ?EducationalActivity ;
                             rdfs:label "Storia" .
            ?EducationalActivity uo:hasSsd "M-STO/01" .
            ?EducationalActivity uo:hasCfu ?CFUofEducation .

            }
'''

#6
'''
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX uo: <http://purl.org/ontology/UniOn#>
            SELECT ?DepartmentLabel
            WHERE {
            ?DegreeProgramme uo:isManagedBy ?Department ;
                             rdfs:label "Digital humanities and digital knowledge" .

            OPTIONAL { ?Department rdfs:label ?DepartmentLabel }
            }
'''

#7
'''
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX uo: <http://purl.org/ontology/UniOn#>
            SELECT (COUNT(?EducationalActivity) as ?LaboratoryCount)
            WHERE {
            ?DegreeProgramme uo:hasEducationalActivity ?EducationalActivity ;
                            rdfs:label "Dams - discipline delle arti, della musica  e dello spettacolo" .
            ?EducationalActivity a uo:Laboratory .

            }
'''

#8
'''
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX uo: <http://purl.org/ontology/UniOn#>
            SELECT ?EducationalActivityLabel
            WHERE {
            ?DegreeProgramme uo:hasEducationalActivity ?EducationalActivity ;
                            rdfs:label "Dams - discipline delle arti, della musica  e dello spettacolo" .
            ?EducationalActivity a UniOn:Laboratory .

            OPTIONAL { ?EducationalActivity rdfs:label ?EducationalActivityLabel }

            }
'''
#9

'''
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX uo: <http://purl.org/ontology/UniOn#>
            SELECT ?DegreeProgrammeLabel
            WHERE {
            ?DegreeProgramme uo:hasDegreeClass ?DegreeClass .
            FILTER regex(?DegreeClass, "^LM-80", "i") .

            OPTIONAL { ?DegreeProgramme rdfs:label ?DegreeProgrammeLabel }

            }
'''

#10
'''
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX uo: <http://purl.org/ontology/UniOn#>
            SELECT ?CampusLabel ?PlaceOfTeachingLabel
            WHERE {
            ?DegreeProgramme uo:hasPlaceOfTeaching ?PlaceOfTeaching ;
                            uo:hasCampus ?Campus ;
                            rdfs:label "Conservazione e restauro dei beni culturali (abilitante ai sensi del d. lgs n. 42"

            OPTIONAL { ?Campus rdfs:label ?CampusLabel }
            OPTIONAL { ?PlaceOfTeaching rdfs:label ?PlaceOfTeachingLabel }

            }
'''

#11

'''
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX uo: <http://purl.org/ontology/UniOn#>
            SELECT ?DegreeProgrammeLabel
            WHERE {
            ?DegreeProgramme a uo:InternationalDegree .
            ?DegreeProgramme a uo:MasterDegree .

            OPTIONAL { ?DegreeProgramme rdfs:label ?DegreeProgrammeLabel }
            }
'''
