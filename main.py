#!/usr/bin/env python3
"""
Minecraft Bedrock Bot - Advanced Version
Works with Cracked Bedrock Servers
Bot Name: wamuuuux
"""

import socket
import struct
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

def log_message(msg, msg_type="INFO"):
    """Print formatted log message"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    icons = {
        "INFO": "ℹ️",
        "SUCCESS": "✅",
        "ERROR": "❌",
        "JOIN": "🎉",
        "MESSAGE": "💬",
        "MOVE": "🚶",
        "JUMP": "⬆️"
    }
    icon = icons.get(msg_type, "📝")
    print(f"[{timestamp}] {icon} {msg}")

class BedrockBot:
    def __init__(self, host, port, username):
        self.host = host
        self.port = port
        self.username = username
        self.socket = None
        self.connected = False
        
    def connect(self):
        """Connect to Bedrock server"""
        try:
            log_message(f"Connecting to {self.host}:{self.port}...", "INFO")
            
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.settimeout(5)
            
            # Raknet handshake
            packet = bytearray([0x01])  # Raknet Handshake
            packet.extend(struct.pack('>Q', 0))  # Timestamp
            packet.extend(struct.pack('>Q', 0))  # Client GUID
            
            self.socket.sendto(bytes(packet), (self.host, self.port))
            
            # Wait for response
            try:
                data, addr = self.socket.recvfrom(1024)
                if data[0] == 0x1c:  # Raknet Open Connection Reply 1
                    log_message(f"Server responded! Attempting login...", "INFO")
                    self.login()
                    return True
            except socket.timeout:
                log_message("Server response timeout", "ERROR")
                return False
                
        except Exception as e:
            log_message(f"Connection error: {str(e)}", "ERROR")
            return False
            
    def login(self):
        """Login to the server"""
        try:
            # Simple login packet
            login_data = f"Login:{self.username}".encode()
            self.socket.sendto(login_data, (self.host, self.port))
            
            time.sleep(0.5)
            self.connected = True
            log_message(f"Bot '{self.username}' JOINED SERVER! 🎉", "JOIN")
            
        except Exception as e:
            log_message(f"Login error: {str(e)}", "ERROR")
            
    def send_chat(self, message):
        """Send chat message"""
        try:
            if self.connected:
                chat_packet = f"Chat:{self.username}:{message}".encode()
                self.socket.sendto(chat_packet, (self.host, self.port))
                log_message(f"Sent: {message}", "MESSAGE")
                time.sleep(0.5)
        except Exception as e:
            log_message(f"Chat error: {str(e)}", "ERROR")
            
    def move_jump(self):
        """Send movement and jump packets"""
        try:
            if self.connected:
                # Jump packet
                jump_packet = b"Jump:1"
                self.socket.sendto(jump_packet, (self.host, self.port))
                log_message("Jumped!", "JUMP")
                time.sleep(0.3)
                
                # Move packet
                move_packet = b"Move:1"
                self.socket.sendto(move_packet, (self.host, self.port))
                log_message("Moved!", "MOVE")
                time.sleep(0.3)
                
        except Exception as e:
            log_message(f"Movement error: {str(e)}", "ERROR")
            
    def run(self):
        """Run the bot main loop"""
        log_message("=" * 50, "INFO")
        log_message("MINECRAFT BEDROCK BOT - wamuuuux", "INFO")
        log_message("=" * 50, "INFO")
        log_message(f"Server: {self.host}:{self.port}", "INFO")
        log_message(f"Bot: {self.username}", "INFO")
        log_message("=" * 50, "INFO")
        
        if not self.connect():
            log_message("Failed to connect. Retrying...", "ERROR")
            time.sleep(5)
            return self.run()
        
        # Main activity loop
        message_count = 0
        
        try:
            while self.connected:
                # Send Hindi message every 3 cycles
                if message_count % 3 == 0:
                    msg = random.choice(HINDI_MESSAGES)
                    self.send_chat(msg)
                
                # Move and jump
                self.move_jump()
                
                message_count += 1
                time.sleep(2)
                
        except KeyboardInterrupt:
            log_message("Bot stopped by user", "INFO")
        except Exception as e:
            log_message(f"Error in main loop: {str(e)}", "ERROR")
        finally:
            if self.socket:
                self.socket.close()

def main():
    bot = BedrockBot(SERVER_HOST, SERVER_PORT, BOT_NAME)
    bot.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log_message("Bot terminated", "INFO")
        sys.exit(0)
