



from src.nlp.util import * ; import src.nlp.util as util
from src.nlp.pipeline import pipeline, state_dict
from src.nlp.classifiers import classifiers

import flask
app = flask.Flask(__name__)


@app.route('/get-relevance-classifiers')
def get_relevance_classifiers():
    names = sorted(list(classifiers.keys()))
    resp = flask.Response(response=json.dumps(names), status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
@app.route('/get-relevance')
def get_relevance():
    text = flask.request.args.get('text')
    classifier = flask.request.args.get('classifier')
    metadata = json.loads(flask.request.args.get('metadata'))

    ans = classifiers[classifier](text, metadata)
    resp = flask.Response(response=json.dumps(ans), status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/get-entities')
def get_entities():
    text = flask.request.args.get('text')
    doc = pipeline(text)
    ents = [
        (ent.lemma_, ent.start, ent.label_)
        for ent in doc.ents
    ]
    for i in range(len(ents)):
        lemma,start,label = ents[i]
        if not label in ['GPE', 'LOC']:
            continue
        if lemma.lower() in state_dict:
            ents.append((state_dict[lemma.lower()], start, 'STATE'))
            continue
        toks = [l.lower() for l in lemma.split(' ')]
        for tok in toks:
            if tok in state_dict:
                ents.append((state_dict[tok], start, 'STATE'))
                # print((state_dict[tok], start, 'STATE'))

    resp = flask.Response(response=json.dumps(ents), status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/get-lemma')
def get_lemma():
    text = flask.request.args.get('text')
    doc = pipeline(text)
    lemmas = [token.lemma_ for token in doc]

    resp = flask.Response(response=json.dumps(lemmas), status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/convert-state-abbreviation')
def convert_state_abbreviation():
    text = flask.request.args.get('queries')
    ans = [
        q if q.lower() not in state_dict else state_dict[q.lower()]
        for q in json.loads(text)
    ]

    resp = flask.Response(response=json.dumps(ans), status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=9001, use_reloader=False)
