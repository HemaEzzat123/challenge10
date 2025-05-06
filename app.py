from flask import Flask, request, render_template_string
import subprocess  

app = Flask(__name__)


@app.route('/report')
def report():
    user_input = request.args.get('template', '')
    context = {
        'Popen': subprocess.Popen  
    }

    rendered = render_template_string(user_input, **context)
    return f"Report: {rendered}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

