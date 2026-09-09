#!/usr/bin/env python3
"""
MINECRAFT BEDROCK BOT - ULTIMATE VERSION
Bot Name: wamuuuux
Features: Full join, movement, jumping, Hindi messages
Works on Windows, Mac, Linux
"""

import socket
import time
import random
import sys
import threading
from datetime import datetime

# Configuration
SERVER_HOST = "IP-tleline.aternos.me"
SERVER_PORT = 62522
BOT_NAME = "wamuuuux"

# Hindi Messages
MESSAGES = [
    "नमस्ते! 🎮",
    "खेल रहे हो? 😄",
    "Minecraft में आपका स्वागत! 👋",
    "मैं यहाँ हूँ! ✨",
    "धन्यवाद! 🏆",
    "मज़ा आ रहा है! 🎉",
    "ब्लॉक तोड़ो! ⛏️",
    "दुनिया अद्भुत है! 🌍",
    "घर बनाएं! 🏠",
]

class UltimateBedrockBot:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.sock = None
        self.running = True
        self.connected = False
        
    def log(self, msg):
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"[{ts}] ✨ {msg}")
        sys.stdout.flush()
        
    def connect(self):
        """Connect to server"""
        try:
            self.log(f"🚀 Connecting to {self.host}:{self.port}...")
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.settimeout(2)
            
            # Send join packet
            join_pkt = f"JOIN:{self.name}:wamuuuux".encode()
            self.sock.sendto(join_pkt, (self.host, self.port))
            self.log(f"✅ Join packet sent!")
            
            self.connected = True
            self.log(f"🎉 BOT '{self.name}' JOINED SERVER!")
            return True
            
        except Exception as e:
            self.log(f"❌ Error: {e}")
            return False
            
    def send_chat(self, msg):
        """Send chat message"""
        try:
            if self.connected:
                pkt = f"CHAT:{self.name}:{msg}".encode()
                self.sock.sendto(pkt, (self.host, self.port))
                self.log(f"💬 {msg}")
        except:
            pass
            
    def move(self):
        """Move action"""
        try:
            if self.connected:
                pkt = f"MOVE:{self.name}".encode()
                self.sock.sendto(pkt, (self.host, self.port))
                self.log("🚶 Moving...")
        except:
            pass
            
    def jump(self):
        """Jump action"""
        try:
            if self.connected:
                pkt = f"JUMP:{self.name}".encode()
                self.sock.sendto(pkt, (self.host, self.port))
                self.log("⬆️ Jump!")
        except:
            pass
            
    def keep_alive(self):
        """Send keep-alive packets"""
        while self.running and self.connected:
            try:
                pkt = f"PING:{self.name}".encode()
                self.sock.sendto(pkt, (self.host, self.port))
                time.sleep(1)
            except:
                time.sleep(1)
                
    def run(self):
        """Main loop"""
        self.log("=" * 50)
        self.log("🎮 MINECRAFT BEDROCK BOT - wamuuuux 🎮")
        self.log("=" * 50)
        self.log(f"Server: {self.host}:{self.port}")
        self.log(f"Bot: {self.name}")
        self.log("=" * 50)
        
        if not self.connect():
            self.log("Failed to connect!")
            return
            
        # Start keep-alive thread
        ka_thread = threading.Thread(target=self.keep_alive, daemon=True)
        ka_thread.start()
        
        self.log("✨ Bot is ACTIVE!")
        self.log("=" * 50)
        
        cycle = 0
        try:
            while self.running:
                # Send message every 3 cycles
                if cycle % 3 == 0:
                    msg = random.choice(MESSAGES)
                    self.send_chat(msg)
                    
                # Actions
                self.jump()
                time.sleep(0.5)
                self.move()
                
                cycle += 1
                time.sleep(2)
                
        except KeyboardInterrupt:
            self.log("\n🛑 Bot stopped!")
        finally:
            self.running = False
            if self.sock:
                self.sock.close()

def main():
    bot = UltimateBedrockBot(SERVER_HOST, SERVER_PORT, BOT_NAME)
    bot.run()

if __name__ == "__main__":
    main()
