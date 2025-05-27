from flask import Flask, jsonify, request
from task import predict_rank
from get_range import predict_rank_range

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid input, no JSON data provided."}), 400

    try:
        easy_questions = data['easy']
        medium_questions = data['medium']
        hard_questions = data['hard']
        student_marks = data['marks']
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

    result = predict_rank(student_marks, easy_questions, medium_questions, hard_questions)
    return jsonify({"predicted_rank": result})

@app.route('/get-rank-range', methods=['POST'])
def get_rank_range():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input, no JSON data provided."}), 400

    try:
        marks = data['marks']
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400

    result = predict_rank_range(marks)
    if(len(result) == 2):
        return jsonify({"min_rank": result[0], "max_rank": result[1]})
    else:
        return jsonify({"max_rank": result})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5002)