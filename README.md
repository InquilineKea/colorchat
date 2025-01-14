# ColorChat - Git-Backed Messaging Application

A secure, Git-backed chat application with cryptographic message signing and verification.

## Features

- Real-time messaging with cryptographic signatures
- Git-based message storage for transparency and auditability
- Optional GitHub synchronization
- Message verification using RSA signatures
- Dark mode support
- Responsive design for mobile and desktop

## Quick Start

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
```

4. Run the server:
```bash
python3 server.py
```

5. Open http://localhost:8000 in your browser

## Configuration

Environment variables:

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

## Deployment

ColorChat supports multiple deployment options:

1. Local development server (default)
2. Production server with WSGI
3. Docker container

See `doc/DEPLOYMENT.md` for detailed instructions.

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
