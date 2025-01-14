# ColorChat - Git-Backed Messaging Application

A secure, Git-backed chat application with cryptographic message signing and verification, featuring a beautiful space-themed UI.

## Features

- Real-time messaging with cryptographic signatures
- Git-based message storage for transparency and auditability
- Optional GitHub synchronization
- Message verification using RSA signatures
- Dark mode support
- Space-themed UI with twinkling stars and constellations
- Rainbow message borders
- Responsive design for mobile and desktop

## Quick Start (Local Development)

1. Clone the repository:
```bash
git clone https://github.com/yourusername/colorchat.git
cd colorchat
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your configuration:
```bash
SIGN_MESSAGES=true
MESSAGE_VERIFICATION=true
ENVIRONMENT=development
```

4. Run the server:
```bash
python3 server.py
```

5. Open http://localhost:8000 in your browser

## Deployment

### Heroku Deployment

1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

2. Create a new Heroku app:
```bash
heroku create your-colorchat-app
```

3. Set environment variables:
```bash
heroku config:set SIGN_MESSAGES=true
heroku config:set MESSAGE_VERIFICATION=true
heroku config:set ENVIRONMENT=production
```

4. Deploy to Heroku:
```bash
git push heroku main
```

### Manual Server Deployment

1. Clone the repository on your server:
```bash
git clone https://github.com/yourusername/colorchat.git
cd colorchat
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
export SIGN_MESSAGES=true
export MESSAGE_VERIFICATION=true
export ENVIRONMENT=production
export PORT=80  # or your preferred port
```

4. Run with a production server (e.g., using gunicorn):
```bash
gunicorn server:app --bind 0.0.0.0:$PORT
```

## Configuration

Environment variables:

- `PORT`: Server port (default: 8000)
- `ENVIRONMENT`: 'development' or 'production'
- `COLORCHAT_STORAGE`: Storage backend ('git' or 'sqlite', default: sqlite)
- `SIGN_MESSAGES`: Enable message signing (true/false)
- `MESSAGE_VERIFICATION`: Enable signature verification (true/false)
- `KEYS_DIR`: Directory for key storage
- `SYNC_TO_GITHUB`: Enable GitHub sync (true/false)
- `GITHUB_TOKEN`: GitHub personal access token
- `GITHUB_REPO`: GitHub repository for sync

## Project Structure

```
colorchat/
├── server.py           # Main server file
├── key_manager.py      # RSA key management
├── static/            
│   ├── css/           # Stylesheets
│   └── js/            # Client-side scripts
├── templates/         
│   └── index.html     # Main page template
└── storage/           # Storage backends
```

## Logging

ColorChat includes a comprehensive logging system with multiple debug levels:

1. ERROR - Critical errors that need immediate attention
2. WARNING - Important events that are not errors
3. INFO - General information about system operation
4. DEBUG - Detailed information for debugging

To enable debug logging:

```bash
export COLORCHAT_DEBUG=true
```

Or on Windows:

```cmd
set COLORCHAT_DEBUG=true
```

## Troubleshooting

Common issues and solutions:

1. Check the logs in the console output
2. Enable console debug output temporarily using the `COLORCHAT_DEBUG` environment variable
3. Verify your configuration in `.env`
4. Check file permissions for the keys directory

## License

MIT License - See LICENSE file for details
