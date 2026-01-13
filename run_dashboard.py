#!/usr/bin/env python3
"""
Simple HTTP Server for E-Commerce Dashboard
Run this script to launch the dashboard in your browser
"""

import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

def main():
    """Start the dashboard server"""
    
    print("🚀 E-Commerce Sales Analysis Dashboard")
    print("=" * 50)
    
    # Change to the project directory
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    
    # Server configuration
    PORT = 8000
    
    # Create a custom handler to serve files
    class DashboardHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            super().end_headers()
    
    try:
        with socketserver.TCPServer(("", PORT), DashboardHandler) as httpd:
            print(f"📊 Dashboard is running at: http://localhost:{PORT}")
            print(f"🌐 Open your browser and navigate to: http://localhost:{PORT}/dashboard.html")
            print("\n📋 Dashboard Features:")
            print("   ✅ Key Business Metrics")
            print("   ✅ Interactive Charts")
            print("   ✅ Top Performers Analysis")
            print("   ✅ Business Insights")
            print("   ✅ Download Links")
            print("\n🔄 Server is running... Press Ctrl+C to stop")
            
            # Auto-open browser
            webbrowser.open(f'http://localhost:{PORT}/dashboard.html')
            
            # Start server
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n👋 Dashboard server stopped. Thank you!")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {PORT} is already in use. Please try a different port.")
            print(f"💡 You can manually open: http://localhost:{PORT}/dashboard.html")
        else:
            print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    main()
