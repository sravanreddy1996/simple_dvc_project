import flask
import os
import yaml
import joblib
import numpy as np

from src.get_data import read_params

params_path = "params.yaml"
webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = flask.Flask(__name__, static_folder=static_dir, template_folder=template_dir)


def predict(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    prediction = model.predict(data)
    print(prediction)
    return prediction[0]


def api_response(request):
    try:
        data = np.array([list(request.json.values())])
        response = predict(data)
        response = {"response": response}
        return response
    except Exception as e:
        print(e)
        error = {"error": "Something went wrong!! Try again"}
        return error

@app.route("/", methods=["GET", "POST"])
def index():
    if flask.request.method == "GET":
        # flask will get this template from templates directory added to flask app while creating it.
        return flask.render_template("index.html")
    elif flask.request.method == "POST":
        try:
            if flask.request.form:
                print("#########################")
                print(flask.request.form)
                data = dict(flask.request.form).values()
                data = [list(map(float, data))]
                response = predict(data)
                return flask.render_template("index.html", response=response)
            elif flask.request.json:
                print("#########################")
                print(flask.request.json)
                response = api_response(flask.request)
                return flask.jsonify(response)

        except Exception as e:
            print(e)
            error = {"error": "Something went wrong!! Try again"}
            return flask.render_template("404.html", error=error)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
