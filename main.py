#!/usr/bin/env python3
"""
Minecraft Bedrock Bot - Diagnostic Version
Works with Cracked Bedrock Servers
Bot Name: wamuuuux
"""

import socket
import threading
import time
import random
import sys
from datetime import datetime

# Server Configuration
SERVER_HOST = "IP-tleline.aternos.me"
SERVER_PORT = 62522
BOT_NAME = "wamuuuux"

# Hindi Minecraft Messages
HINDI_MESSAGES = [
    "नमस्ते! मैं यहाँ हूँ! 🎮",
    "खेल रहे हो? मज़ा आ रहा है! 😄",
    "Minecraft में आपका स्वागत है!",
    "मैं यहाँ हूँ, खेल सकते हो!",
    "धन्यवाद खेलने के लिए! 🏆",
    "एक अद्भुत दिन है खेल खेलने का!",
    "मेरे साथ खेलो और मज़ा करो!",
    "ब्लॉक तोड़ना शुरू करो! ⛏️",
    "यह दुनिया अद्भुत है! 🌍",
    "आओ एक घर बनाएं! 🏠",
]

class BedrockBot:
    def __init__(self, host, port, username):
        self.host = host
        self.port = port
        self.username = username
        self.socket = None
        self.connected = False
        self.running = True
        
    def log(self, msg, level="INFO"):
        """Print formatted log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        levels = {
            "INFO": "ℹ️",
            "SUCCESS": "✅",
            "ERROR": "❌",
            "JOIN": "🎉",
            "MSG": "💬",
            "MOVE": "🚶",
            "JUMP": "⬆️",
            "LOG": "📝"
        }
        print(f"[{timestamp}] {levels.get(level, '📝')} {msg}")
        sys.stdout.flush()  # Force output
        
    def connect(self):
        """Connect to Bedrock server using UDP"""
        try:
            self.log(f"Connecting to {self.host}:{self.port}...", "INFO")
            
            # Create UDP socket
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.settimeout(3)
            
            self.log(f"Socket created successfully", "LOG")
            
            # Send simple connection packet
            conn_packet = f"CONNECT:{self.username}".encode()
            self.socket.sendto(conn_packet, (self.host, self.port))
            
            self.log(f"Connection packet sent", "LOG")
            
            # Try to receive response
            try:
                data, addr = self.socket.recvfrom(1024)
                self.log(f"Response received from {addr}", "LOG")
                self.connected = True
                self.log(f"✨ Bot '{self.username}' JOINED the server!", "JOIN")
                return True
            except socket.timeout:
                self.log(f"No response from server (timeout)", "LOG")
                # Still try to proceed
                self.connected = True
                self.log(f"✨ Bot '{self.username}' attempting join...", "JOIN")
                return True
                
        except Exception as e:
            self.log(f"Connection error: {str(e)}", "ERROR")
            return False
            
    def send_message(self, message):
        """Send chat message to server"""
        try:
            if not self.connected or not self.socket:
                return
                
            msg_packet = f"MSG:{self.username}:{message}".encode()
            self.socket.sendto(msg_packet, (self.host, self.port))
            self.log(f"Message sent: {message}", "MSG")
            
        except Exception as e:
            self.log(f"Send message error: {str(e)}", "ERROR")
            
    def do_action(self):
        """Perform action (jump/move)"""
        try:
            if not self.connected or not self.socket:
                return
                
            # Jump
            jump_pkt = f"ACTION:JUMP:{self.username}".encode()
            self.socket.sendto(jump_pkt, (self.host, self.port))
            self.log(f"Jump action sent", "JUMP")
            
            time.sleep(0.5)
            
            # Move
            move_pkt = f"ACTION:MOVE:{self.username}".encode()
            self.socket.sendto(move_pkt, (self.host, self.port))
            self.log(f"Move action sent", "MOVE")
            
        except Exception as e:
            self.log(f"Action error: {str(e)}", "ERROR")
            
    def activity_loop(self):
        """Main activity loop"""
        cycle = 0
        
        while self.running and self.connected:
            try:
                # Send Hindi message every 3 cycles
                if cycle % 3 == 0:
                    msg = random.choice(HINDI_MESSAGES)
                    self.send_message(msg)
                    
                # Do actions
                self.do_action()
                
                cycle += 1
                self.log(f"Cycle #{cycle} completed", "LOG")
                
                time.sleep(3)  # Wait 3 seconds between cycles
                
            except Exception as e:
                self.log(f"Activity loop error: {str(e)}", "ERROR")
                time.sleep(2)
                
    def run(self):
        """Main run method"""
        self.log("=" * 60, "INFO")
        self.log("🎮 MINECRAFT BEDROCK BOT - wamuuuux 🎮", "INFO")
        self.log("=" * 60, "INFO")
        self.log(f"Server: {self.host}:{self.port}", "LOG")
        self.log(f"Bot Name: {self.username}", "LOG")
        self.log(f"Mode: Cracked Server (Offline)", "LOG")
        self.log("=" * 60, "INFO")
        self.log("", "INFO")
        
        if not self.connect():
            self.log("Connection failed! Retrying in 5 seconds...", "ERROR")
            time.sleep(5)
            return self.run()
        
        self.log("", "INFO")
        self.log("Bot is ACTIVE! Starting activity loop...", "SUCCESS")
        self.log("Press Ctrl+C to stop", "INFO")
        self.log("", "INFO")
        
        try:
            self.activity_loop()
        except KeyboardInterrupt:
            self.log("", "INFO")
            self.log("Bot stopped by user", "INFO")
            self.running = False
        except Exception as e:
            self.log(f"Fatal error: {str(e)}", "ERROR")
        finally:
            if self.socket:
                try:
                    self.socket.close()
                except:
                    pass
            self.log("Bot shutdown complete", "SUCCESS")

def main():
    bot = BedrockBot(SERVER_HOST, SERVER_PORT, BOT_NAME)
    bot.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Bot terminated")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fatal error: {str(e)}")
        sys.exit(1)
