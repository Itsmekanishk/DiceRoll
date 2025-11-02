from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll', methods=['POST'])
def roll_dice():
    num_dice = int(request.form.get('num_dice', 1))
    
    # Roll the dice - generate random numbers between 1 and 6
    results = [random.randint(1, 6) for _ in range(num_dice)]
    total = sum(results)
    
    return jsonify({
        'results': results,
        'total': total,
        'num_dice': num_dice
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
