from flask import Flask, request, jsonify
import db
import db_sql_lite

app = Flask(__name__)
db_sql_lite.load_data()


@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'


@app.route('/students_db', methods=['POST'])
def find_std_ids():
    ids = request.get_json().get('ids')
    res = db.first_student_by_ids(ids)
    result = [std.to_dict() for std in res.values()]
    return jsonify(result)


@app.route('/students_db_lite', methods=['POST'])
def find_std_by_id_lite():
    return jsonify(db_sql_lite.students_by_ids(request.get_json().get('ids')))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
