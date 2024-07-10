from flask import Flask, request, render_template, jsonify
from commands import CommandProcessor

app = Flask(__name__)
processor = CommandProcessor()

@app.route('/')
def home():
    return render_template('index.html', commands='', output='')

@app.route('/run', methods=['POST'])
def run():
    commands = request.form['commands']
    command_list = commands.split('\n')
    output = []
    for command in command_list:
        command = command.strip()
        if command:
            result = processor.process(command)
            if result is not None:
                output.append(result)

    return render_template('index.html', commands=commands, output='\n'.join(output))

@app.route('/process', methods=['POST'])
def process_command():
    data = request.get_json()
    command = data.get('command')
    if not command:
        return jsonify({"error": "No command provided"}), 400

    result = processor.process(command)
    if result and "Error" not in result:
        return jsonify({"result": result})
    else:
        return jsonify({"error": result}), 400

if __name__ == '__main__':
    app.run(debug=True)
