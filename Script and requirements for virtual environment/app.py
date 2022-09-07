from flask import Flask, render_template, request, jsonify
from owlready2 import *

app = Flask(__name__)
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))


@app.route("/")
def home_page():
    return "API for SPARQL queries"


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
