from flask import Flask, request
from datetime import datetime
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/time')
def get_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f'The current time is: {current_time}'

# Vulnerable Route
@app.route('/list')
def list_dir():
    dir_to_list = request.args.get('dir', '')  # Get directory from user input
    command = f'ls {dir_to_list}'  # Construct command with user input
    result = subprocess.check_output(command, shell=True)  # Execute command
    return result.decode()

if __name__ == '__main__':
    app.run()
