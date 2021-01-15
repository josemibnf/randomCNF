
from flask import Flask, jsonify, send_file
import randomCNF
import io

if __name__ == "__main__":

    app = Flask(__name__)

    @app.route('/')
    def get():
        return send_file(
            io.BytesIO(randomCNF.ok().SerializeToString()),
            as_attachment=True,
            attachment_filename='abc.abc',
            mimetype='attachment/x-protobuf'
        )

    app.run(host='0.0.0.0', port=8000)