from flask import Flask, render_template, request

app = Flask(__name__)

# Function to perform operations
def calculate(operation, num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        if operation == 'add':
            return num1 + num2
        elif operation == 'subtract':
            return num1 - num2
        elif operation == 'multiply':
            return num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return "Error! Division by zero."
            return num1 / num2
        elif operation == 'modulus':
            return num1 % num2
        elif operation == 'power':
            return num1 ** num2
        else:
            return "Invalid operation."
    except ValueError:
        return "Invalid input."

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        operation = request.form.get("operation")
        result = calculate(operation, num1, num2)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
