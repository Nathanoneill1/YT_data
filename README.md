# Video Database Dashboard

A YouTube Studio-inspired dashboard built with Python Flask backend and React frontend.

## Features

- Dark theme matching YouTube Studio design
- Sidebar navigation with Dashboard and Baseline Tracker
- Video Database section with sample video cards
- Responsive design
- Channel analytics display

## Setup Instructions

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask application:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

- `app.py` - Flask backend with API routes
- `templates/index.html` - Main HTML template with React components
- `static/styles.css` - CSS styling for the dark theme
- `requirements.txt` - Python dependencies

## API Endpoints

- `GET /` - Main dashboard page
- `GET /api/dashboard` - Dashboard analytics data
- `GET /api/video-database` - Video database data

## Technologies Used

- **Backend**: Python Flask
- **Frontend**: React (via CDN), HTML, CSS
- **Styling**: Custom CSS with YouTube Studio-inspired dark theme
