from json import dumps
from points import Points
from flask import Flask, Response
from flask_cors import CORS

import helper
import qwe


app = Flask('server')

CORS(app)

cors =  CORS(app, resources={
    r"/*": {
        "origins" : "*"
    }
})


@app.route('/', methods=['GET'])
def get_points():
    matrix = [
        [
            [0, 1],
            [1, 0]
        ],
        [
            [0, complex(0, -1)],
            [complex(0, 1), 0]
        ],
        [
            [1, 0],
            [0, -1]
        ]
    ]

    points = Points(matrix, 2)
    generated_points = points.get_joint_numerical_range(1000)
    qwe.qwe(generated_points)
    qwe.qwe(helper.get_fibonacci_sphere_as_vectors(500))

    return Response(dumps(generated_points), mimetype='text/json')


def main():
    app.run(port=2323)


if __name__ == '__main__':
    main()