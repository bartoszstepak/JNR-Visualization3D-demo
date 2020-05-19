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
    generated_points = points.get_joint_numerical_range(500)

    # points = Points()
    # generated_points = points.get_joint_numerical_range(1500)
    return Response(dumps(generated_points), mimetype='text/json')


def main():
    app.run(port=8800)


if __name__ == '__main__':
    main()
