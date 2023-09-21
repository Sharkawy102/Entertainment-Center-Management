from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global variables to track the start time and rental status for each unit
unit_start_times = [None] * 6
unit_busy_statuses = [False] * 6

@app.route('/')
def index():
    return render_template('index.html', unit_start_times=unit_start_times, unit_busy_statuses=unit_busy_statuses)

@app.route('/start_rent/<int:unit_id>')
def start_rent(unit_id):
    if not unit_busy_statuses[unit_id]:
        # Add logic here to start the rental process (e.g., set start time, update status)
        unit_busy_statuses[unit_id] = True
    return redirect(url_for('index'))

@app.route('/stop_rent/<int:unit_id>')
def stop_rent(unit_id):
    if unit_busy_statuses[unit_id]:
        # Add logic here to stop the rental process (e.g., set stop time, update status)
        unit_busy_statuses[unit_id] = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
