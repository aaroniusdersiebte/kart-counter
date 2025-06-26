#!/usr/bin/env python3
"""
Mario Kart Challenge - HTTP Bridge Server
Ermöglicht Kommunikation zwischen Control Panel und OBS Display
"""

import json
import http.server
import socketserver
import os
from urllib.parse import urlparse, parse_qs
import webbrowser
import threading
import time

PORT = 8080
GAMESTATE_FILE = "gamestate.json"

def get_default_gamestate():
    """Get default game state"""
    return {
        "completedPositions": [],
        "jokers": 3,
        "gameStatus": "running",
        "lastAchievement": None,
        "timestamp": int(time.time() * 1000)
    }

class ChallengeHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/api/gamestate':
            self.send_gamestate()
        elif parsed_path.path == '/api/status':
            self.send_status()
        else:
            # Serve static files
            super().do_GET()
    
    def do_POST(self):
        """Handle POST requests"""
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/api/gamestate':
            self.update_gamestate()
        elif parsed_path.path == '/api/reset':
            self.reset_gamestate()
        else:
            self.send_error(404)
    
    def send_gamestate(self):
        """Send current game state as JSON"""
        try:
            if os.path.exists(GAMESTATE_FILE):
                with open(GAMESTATE_FILE, 'r', encoding='utf-8') as f:
                    gamestate = json.load(f)
            else:
                gamestate = get_default_gamestate()
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(json.dumps(gamestate).encode('utf-8'))
            
        except Exception as e:
            print(f"Error sending gamestate: {e}")
            self.send_error(500)
    
    def update_gamestate(self):
        """Update game state from POST data"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            new_gamestate = json.loads(post_data.decode('utf-8'))
            
            # Add timestamp
            new_gamestate['timestamp'] = int(time.time() * 1000)
            
            # Save to file
            with open(GAMESTATE_FILE, 'w', encoding='utf-8') as f:
                json.dump(new_gamestate, f, indent=2, ensure_ascii=False)
            
            print(f"📝 Game state updated: Plätze={len(new_gamestate.get('completedPositions', []))}, Joker={new_gamestate.get('jokers', 0)}, Status={new_gamestate.get('gameStatus', 'unknown')}")
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(json.dumps({"status": "success"}).encode('utf-8'))
            
        except Exception as e:
            print(f"Error updating gamestate: {e}")
            self.send_error(500)
    
    def reset_gamestate(self):
        """Reset game state to default"""
        try:
            default_state = get_default_gamestate()
            
            with open(GAMESTATE_FILE, 'w', encoding='utf-8') as f:
                json.dump(default_state, f, indent=2, ensure_ascii=False)
            
            print("🔄 Game state reset to default")
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(json.dumps({"status": "reset"}).encode('utf-8'))
            
        except Exception as e:
            print(f"Error resetting gamestate: {e}")
            self.send_error(500)
    
    def send_status(self):
        """Send server status"""
        status = {
            "server": "Mario Kart Challenge Bridge",
            "version": "1.0",
            "port": PORT,
            "time": int(time.time() * 1000),
            "gamestate_exists": os.path.exists(GAMESTATE_FILE)
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        self.wfile.write(json.dumps(status).encode('utf-8'))
    
    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def log_message(self, format, *args):
        """Override to reduce spam in console"""
        # Only log important messages
        if 'api/' in args[1] if len(args) > 1 else False:
            print(f"🌐 {args[1]} - {args[0]}")

def start_server():
    """Start the HTTP server"""
    Handler = ChallengeHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🏁 Mario Kart Challenge Bridge Server gestartet!")
        print(f"📡 Server läuft auf: http://localhost:{PORT}")
        print(f"🎮 Control Panel: http://localhost:{PORT}/control-v3.html")
        print(f"📺 OBS Display: http://localhost:{PORT}/obs-v3.html")
        print("\n💡 Tipps:")
        print("   - Lass diesen Server während des Streams laufen")
        print("   - Öffne das Control Panel in deinem Browser")
        print("   - Nutze die OBS URL in deiner Browser Source")
        print("\n❌ Zum Beenden: Strg+C drücken\n")
        
        # Initialize gamestate file if it doesn't exist
        if not os.path.exists(GAMESTATE_FILE):
            default_state = get_default_gamestate()
            with open(GAMESTATE_FILE, 'w', encoding='utf-8') as f:
                json.dump(default_state, f, indent=2, ensure_ascii=False)
            print(f"✅ Gamestate-Datei erstellt: {GAMESTATE_FILE}")
        else:
            print(f"📂 Gamestate-Datei gefunden: {GAMESTATE_FILE}")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server wird beendet...")
            httpd.shutdown()

def check_python_version():
    """Check if Python version is compatible"""
    import sys
    if sys.version_info < (3, 6):
        print("❌ Python 3.6 oder höher erforderlich!")
        print(f"   Aktuelle Version: {sys.version}")
        input("Drücke Enter zum Beenden...")
        return False
    return True

if __name__ == "__main__":
    # Check Python version
    if not check_python_version():
        exit(1)
    
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    print(f"📁 Arbeitsverzeichnis: {script_dir}")
    
    print("🎮 Mario Kart Challenge HTTP Bridge")
    print("=====================================")
    
    # Check if port is available
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', PORT))
    sock.close()
    
    if result == 0:
        print(f"❌ Port {PORT} ist bereits belegt!")
        print("   Beende andere Anwendungen oder ändere den PORT in diesem Script.")
        input("Drücke Enter zum Beenden...")
    else:
        try:
            start_server()
        except Exception as e:
            print(f"❌ Fehler beim Starten des Servers: {e}")
            input("Drücke Enter zum Beenden...")
