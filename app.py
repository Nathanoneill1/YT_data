from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/dashboard')
def get_dashboard_data():
    return jsonify({
        'current_subscribers': 0,
        'views_last_28_days': 0,
        'watch_time_hours': 0.0,
        'top_videos_views': 0
    })

@app.route('/api/video-database')
def get_video_database():
    return jsonify({
        'videos': [
            {'id': 1, 'title': 'Sample Video 1', 'views': 150, 'duration': '5:30'},
            {'id': 2, 'title': 'Sample Video 2', 'views': 89, 'duration': '3:45'},
            {'id': 3, 'title': 'Sample Video 3', 'views': 234, 'duration': '7:12'}
        ]
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
