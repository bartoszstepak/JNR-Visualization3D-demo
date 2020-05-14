from json import dumps
from points import Points
from flask import Flask, Response
from flask_cors import CORS


app = Flask('server')

CORS(app)

cors =  CORS(app, resources={
    r"/*": {
        "origins" : "*"
    }
})


@app.route('/', methods=['GET'])
def get_points():
    points = Points()
    generated_points = points.get_joint_numerical_range(10000);
    return Response(dumps(generated_points), mimetype='text/json')


def main():
    app.run(port=8800)


if __name__ == '__main__':
    main()
