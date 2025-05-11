from flask import Flask, jsonify, request
from task import predict_rank

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

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5002)
