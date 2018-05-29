"""
Manager process wraps an web API over all the modules.

"""

from flask import Flask

app = Flask(__name__)


@app.route("/train")
def train():
    return " training module"

@app.route("/testing")
def test():
    return " <H1>testing module</H1>"

if __name__ == "__main__":
    import _pickle as pickle

    import pprint

    data = [{'a': 'A', 'b': 2, 'c': 3.0}]

    pickle.dump(data, open("pickled_obj.sav", "wb"))
    loder=pickle.load(open("pickled_obj.sav", "rb"))
    print(loder)
