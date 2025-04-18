# VoiceInk-Sesame Voice Assistant: Technical PRD

## Overview
This project aims to create an integrated voice assistant system leveraging VoiceInk for voice capture and transcription on macOS with Sesame TTS for high-quality speech synthesis on an Ubuntu server with GPU acceleration. By separating the voice recognition and speech synthesis components across devices, we optimize for each platform's strengths: macOS for user interaction and Ubuntu's GPU capabilities (RTX 3090 GPU and 128GB RAM) for text-to-speech processing. This hybrid system will provide a seamless voice interaction experience, with wake word detection, natural-sounding responses, and minimal latency.

## Core Features

### 1. Mac-Based Voice Recognition with VoiceInk
- **What it does**: Captures and transcribes voice input through VoiceInk on macOS
- **Why it's important**: Provides accurate, low-latency speech recognition with native macOS integration
- **How it works**: Utilizes VoiceInk's local whisper.cpp-based transcription with trigger word detection

### 2. AI Provider Integration
- **What it does**: Routes transcribed queries to AI services like Google's Gemini API
- **Why it's important**: Enables intelligent responses to user queries without developing custom NLP
- **How it works**: Uses VoiceInk's built-in AI provider integration with configurable trigger words

### 3. High-Quality Speech Synthesis with Sesame
- **What it does**: Converts AI-generated text responses into natural-sounding speech
- **Why it's important**: Creates a more engaging and accessible user experience
- **How it works**: Leverages Sesame's CSM-1B model running on Ubuntu's GPU for faster processing

### 4. Cross-Device Communication
- **What it does**: Establishes reliable communication between macOS client and Ubuntu server
- **Why it's important**: Enables distributed processing while maintaining a seamless experience
- **How it works**: Implements a RESTful API with appropriate error handling and recovery mechanisms

### 5. Voice Customization
- **What it does**: Provides multiple voice options and allows for voice cloning
- **Why it's important**: Creates a personalized experience and accommodates user preferences
- **How it works**: Utilizes Sesame's voice cloning capabilities with custom voice profiles

### 6. Continuous and On-Demand Listening Modes
- **What it does**: Offers both always-listening (wake word) and manual activation modes
- **Why it's important**: Provides flexibility for different usage scenarios and privacy preferences
- **How it works**: Implements wake word detection in VoiceInk and keyboard shortcut activation

## User Experience

### User Personas

1. **Developer Devon**
   - Uses macOS for development work
   - Wants hands-free access to AI assistance while coding
   - Needs clear, natural-sounding voice responses for complex queries

2. **Content Creator Casey**
   - Creates multimedia content on macOS
   - Needs reliable voice transcription and high-quality speech output
   - Values customizable voices for different projects

### Key User Flows

1. **Manual Activation Flow**
   - Press Ctrl+Q to begin voice capture
   - Speak query including trigger word (e.g., "Gemini, what is...")
   - Release Ctrl+Q to end capture
   - System processes query and speaks response

2. **Wake Word Activation Flow**
   - System continuously listens for wake word
   - User speaks wake word followed by query
   - System processes query and speaks response
   - Conversation continues until timeout or dismissal

3. **Voice Customization Flow**
   - Access web interface on Ubuntu server
   - Upload voice sample or select from existing voices
   - Configure voice parameters
   - Set as default or save for future use

### UI/UX Considerations

- Minimal visual interface, focusing on voice interaction
- Clear audio cues for system states (listening, processing, responding)
- Simple configuration interface for voice and trigger word settings
- Seamless integration with existing macOS workflows

## Technical Architecture

### System Components

1. **Mac Client (VoiceInk)**
   - VoiceInk application for voice capture and transcription
   - Python script for clipboard monitoring and request forwarding
   - Local configuration and cache
   - Status indicators and audio feedback

2. **Ubuntu Server (Sesame TTS)**
   - Docker container with Sesame TTS
   - RESTful API service for text-to-speech requests
   - Voice profile management system
   - Web interface for configuration (optional)

3. **Cross-Device Communication Layer**
   - HTTP/REST protocol for text-to-speech requests
   - Audio streaming for response playback
   - Secure communication with authentication
   - Error handling and retry mechanisms

4. **AI Integration Layer**
   - VoiceInk's built-in AI provider integration
   - Google Gemini API client
   - Query formatting and response parsing
   - Context management for conversational interactions

### Data Models

1. **Voice Request**
   ```json
   {
     "text": "string",
     "voice": "string",
     "speed": "float",
     "response_format": "string"
   }
   ```

2. **Voice Response**
   ```json
   {
     "audio": "binary",
     "format": "string",
     "duration": "float",
     "text": "string"
   }
   ```

3. **Voice Profile**
   ```json
   {
     "id": "string",
     "name": "string",
     "description": "string",
     "created_at": "datetime",
     "sample_count": "integer",
     "audio_duration": "float"
   }
   ```

4. **System Configuration**
   ```json
   {
     "trigger_word": "string",
     "default_voice": "string",
     "listening_mode": "string",
     "server_url": "string",
     "api_keys": {
       "gemini": "string"
     },
     "audio_settings": {
       "volume": "float",
       "speed": "float"
     }
   }
   ```

### APIs and Integrations

1. **Sesame TTS API Endpoints**
   - `POST /v1/audio/speech` - Generate speech from text
   - `GET /v1/audio/voices` - List available voices
   - `GET /v1/audio/models` - List available models
   - `POST /v1/voice-cloning/clone` - Clone a new voice
   - `GET /v1/voice-cloning/voices` - List cloned voices

2. **VoiceInk Integration**
   - Configuration for trigger word
   - AI provider settings for Gemini
   - Clipboard access for response capture
   - Keyboard shortcut configuration

3. **Google Gemini API**
   - Text query submission
   - Response retrieval and parsing
   - API key management
   - Error handling and retry logic

### Infrastructure Requirements

1. **Hardware**
   - Mac client (any modern macOS system)
   - Ubuntu server with RTX 3090 GPU and 128GB RAM
   - Reliable network connection between devices

2. **Software**
   - macOS 14+ with VoiceInk installed
   - Ubuntu 22.04+ with Docker and NVIDIA Container Toolkit
   - Python 3.10+ for client scripts
   - CUDA 11.7+ for GPU acceleration

3. **Network**
   - Open port 8000 on Ubuntu server
   - Local network connectivity or VPN for remote operation
   - Optional SSL/TLS for secure communication

## Development Roadmap

### Phase 1: Foundation Setup
1. **Sesame TTS Docker Deployment**
   - Set up Docker environment on Ubuntu
   - Configure NVIDIA Container Toolkit
   - Deploy Sesame TTS container
   - Test basic TTS functionality

2. **VoiceInk Configuration**
   - Install and configure VoiceInk on macOS
   - Set up trigger word detection
   - Configure Gemini API integration
   - Test basic transcription and AI response

3. **Basic Communication Layer**
   - Create simple Mac client script for clipboard monitoring
   - Implement basic HTTP requests to Sesame TTS
   - Set up audio playback mechanism on Mac
   - Test end-to-end communication

### Phase 2: Core Functionality
1. **Enhanced TTS Integration**
   - Implement voice selection mechanism
   - Add speech parameter controls (speed, pitch)
   - Optimize audio quality and latency
   - Set up error handling and recovery

2. **Conversation Management**
   - Implement context handling for multi-turn conversations
   - Add conversation history tracking
   - Create timeout and interruption handling
   - Improve natural flow of interactions

3. **Voice Profile Management**
   - Create voice cloning interface
   - Implement voice storage and selection
   - Add voice preview functionality
   - Set up default voice configuration

### Phase 3: User Experience Refinement
1. **Audio Feedback System**
   - Add audible cues for system states
   - Implement interruption detection
   - Create natural transition sounds
   - Optimize response timing

2. **Configuration Interface**
   - Create settings management for Mac client
   - Implement web interface for Sesame configuration
   - Add user preference storage
   - Create backup and restore functionality

3. **Performance Optimization**
   - Optimize network communication
   - Implement caching for frequent responses
   - Reduce end-to-end latency
   - Minimize resource usage

### Phase 4: Advanced Features
1. **Continuous Listening Mode**
   - Implement efficient background listening on Mac
   - Add wake word detection sensitivity controls
   - Create privacy-focused listening modes
   - Optimize battery usage

2. **Multi-Modal Interaction**
   - Add text input fallback option
   - Implement visual feedback components
   - Create notification system for responses
   - Add gesture controls (optional)

3. **Extended AI Capabilities**
   - Implement multiple AI provider options
   - Add specialized response formatting
   - Create domain-specific optimizations
   - Implement personalization features

## Logical Dependency Chain

1. **Foundation Components (Start Here)**
   - Sesame TTS Docker container on Ubuntu
   - VoiceInk configuration on macOS
   - Basic network connectivity
   - Simple clipboard monitoring

2. **Core Integration Layer**
   - Text-to-speech request handling
   - Audio playback implementation
   - Error handling and recovery
   - Configuration management

3. **User Experience Layer**
   - Voice customization
   - Conversational context
   - Response quality optimization
   - Feedback mechanisms

4. **Advanced Capabilities (Final Stage)**
   - Continuous listening mode
   - Multi-modal interactions
   - Extended AI integrations
   - Performance optimizations

## Risks and Mitigations

### Technical Challenges
1. **Cross-Device Networking Issues**
   - Risk: Network instability affects voice assistant reliability
   - Mitigation: Implement robust error handling, local caching, and reconnection logic

2. **GPU Compatibility**
   - Risk: CUDA version incompatibility with Sesame TTS
   - Mitigation: Test specific container configurations before deployment, create fallback CPU mode

3. **Audio Quality Issues**
   - Risk: Audio streaming introduces artifacts or delay
   - Mitigation: Optimize audio formats, implement buffer management, consider local caching

### Integration Challenges
1. **VoiceInk Limitations**
   - Risk: Limited access to VoiceInk's internal functionality
   - Mitigation: Use clipboard monitoring and configuration options, prepare for future updates

2. **AI Provider Changes**
   - Risk: Gemini API changes affect integration
   - Mitigation: Create abstraction layer for AI providers, implement version checking

3. **OS Updates Impact**
   - Risk: macOS updates affect VoiceInk or scripting capabilities
   - Mitigation: Test on beta OS versions, maintain compatibility layer

### Resource Constraints
1. **Mac Performance Impact**
   - Risk: Continuous monitoring affects system performance
   - Mitigation: Optimize polling intervals, implement efficient resource usage

2. **Server Load Handling**
   - Risk: Multiple requests overload TTS server
   - Mitigation: Implement request queuing, load balancing, and prioritization

3. **Network Bandwidth**
   - Risk: Limited bandwidth affects audio quality
   - Mitigation: Implement adaptive quality, compression options, and caching

## Appendix

### Installation Instructions

```bash
# Ubuntu Server Setup

# 1. Install Docker and NVIDIA Container Toolkit
sudo apt-get update
sudo apt-get install -y docker.io docker-compose curl

# Install NVIDIA Container Toolkit
curl -s -L https://nvidia.github.io/nvidia-container-runtime/gpgkey | \
  sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-container-runtime/$distribution/nvidia-container-runtime.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-runtime.list
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker

# 2. Create project directory
mkdir -p ~/voice-assistant/sesame-tts
cd ~/voice-assistant/sesame-tts

# 3. Create .env file
cat > .env << EOF
HF_TOKEN=your_hugging_face_token_here
EOF

# 4. Create docker-compose.yml
cat > docker-compose.yml << 'EOF'
version: '3'

services:
  sesame-tts:
    image: phildougherty/sesame_csm_openai:latest
    container_name: sesame-tts
    ports:
      - "8000:8000"
    volumes:
      - ./data:/app/data
      - ./.env:/app/.env
    environment:
      - HF_TOKEN=${HF_TOKEN}
      - CSM_DEVICE_MAP=auto
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
    restart: unless-stopped
EOF

# 5. Start the container
docker-compose up -d

# Mac Client Setup

# 1. Install required Python packages
pip3 install requests pyperclip pygame

# 2. Create client script
cat > voice_bridge.py << 'EOF'
#!/usr/bin/env python3
"""
VoiceInk to Sesame TTS Bridge
Monitors clipboard for text from VoiceInk and sends it to Sesame for TTS.
"""

import time
import requests
import re
import subprocess
import argparse
import os
import pyperclip

# Configuration
SESAME_API_URL = "http://your-ubuntu-ip:8000/v1/audio/speech"
SESAME_VOICE = "alloy"  # Options: alloy, echo, fable, onyx, nova, shimmer
POLLING_INTERVAL = 0.5  # seconds
TRIGGER_WORD = "Gemini"

# Function definitions
def play_audio(audio_data):
    """Play audio using macOS afplay"""
    temp_file = "/tmp/tts_response.mp3"
    with open(temp_file, "wb") as f:
        f.write(audio_data)
    subprocess.run(["afplay", temp_file])

def text_to_speech(text, voice=SESAME_VOICE):
    """Convert text to speech using Sesame TTS API"""
    try:
        payload = {
            "model": "csm-1b",
            "input": text,
            "voice": voice,
            "response_format": "mp3"
        }
        response = requests.post(SESAME_API_URL, json=payload)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Error from TTS server: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Error connecting to TTS server: {e}")
        return None

def contains_trigger_word(text):
    """Check if text contains the trigger word"""
    return TRIGGER_WORD.lower() in text.lower()

def extract_query(text):
    """Extract the actual query part after the trigger word"""
    match = re.search(TRIGGER_WORD, text, re.IGNORECASE)
    if match:
        return text[match.end():].strip()
    return text

def monitor_clipboard():
    """Monitor clipboard for text changes and process when trigger word is found"""
    last_clipboard = ""
    print(f"Monitoring clipboard for text containing '{TRIGGER_WORD}'...")
    
    while True:
        current_clipboard = pyperclip.paste()
        
        if current_clipboard != last_clipboard and current_clipboard:
            if contains_trigger_word(current_clipboard):
                print(f"Trigger word found: {current_clipboard}")
                query = extract_query(current_clipboard)
                if query:
                    print(f"Processing query: {query}")
                    
                    # Wait for VoiceInk to process and update clipboard
                    time.sleep(2)
                    
                    # Get the response (should be in clipboard now)
                    response_text = pyperclip.paste()
                    
                    # If response is different from the query
                    if response_text != current_clipboard:
                        print(f"Response: {response_text}")
                        
                        # Convert to speech
                        audio_data = text_to_speech(response_text)
                        if audio_data:
                            play_audio(audio_data)
            
            last_clipboard = current_clipboard
        
        time.sleep(POLLING_INTERVAL)

# Main function
def main():
    parser = argparse.ArgumentParser(description='VoiceInk to Sesame TTS Bridge')
    parser.add_argument('--server', type=str, default=SESAME_API_URL, 
                        help='Sesame TTS server URL')
    parser.add_argument('--voice', type=str, default=SESAME_VOICE, 
                        help='Voice to use (alloy, echo, fable, onyx, nova, shimmer)')
    parser.add_argument('--trigger', type=str, default=TRIGGER_WORD, 
                        help='Trigger word to listen for')
    
    args = parser.parse_args()
    
    global SESAME_API_URL, SESAME_VOICE, TRIGGER_WORD
    SESAME_API_URL = args.server
    SESAME_VOICE = args.voice
    TRIGGER_WORD = args.trigger
    
    print(f"Starting Voice Assistant Bridge")
    print(f"TTS Server: {SESAME_API_URL}")
    print(f"Voice: {SESAME_VOICE}")
    print(f"Trigger Word: {TRIGGER_WORD}")
    
    # Start monitoring clipboard
    monitor_clipboard()

if __name__ == "__main__":
    main()
EOF

# 3. Make the script executable
chmod +x voice_bridge.py

# 4. Configure VoiceInk
echo "Configure VoiceInk with trigger word '${TRIGGER_WORD}' and set up API keys"

# 5. Run the client
echo "Start the bridge with: ./voice_bridge.py --server http://your-ubuntu-ip:8000/v1/audio/speech"
```

### Mac Client Script Implementation Details

The Mac client script functions as follows:

1. **Clipboard Monitoring**:
   - Continuously polls the clipboard for changes
   - Detects when VoiceInk has added transcribed text
   - Identifies trigger words in the transcribed text

2. **Query Processing**:
   - Extracts the actual query from the transcribed text
   - Waits for VoiceInk to process the query with Gemini
   - Detects when the response is placed in the clipboard

3. **TTS Request Handling**:
   - Sends the response text to Sesame TTS API
   - Receives audio data from the server
   - Plays the audio through the Mac's speakers

4. **Error Handling**:
   - Manages connection issues with the TTS server
   - Handles audio playback failures
   - Provides useful error messages and recovery options

### Voice Cloning Guide

To create a customized voice using Sesame's voice cloning:

1. **Record a clear voice sample** (2-3 minutes of speech)
2. **Access the Sesame web interface** at http://your-ubuntu-ip:8000/voice-cloning
3. **Upload your voice sample** and provide a name
4. **Optionally provide a transcript** of the audio for better results
5. **Clone the voice** using the web interface
6. **Test the voice** with sample text to verify quality
7. **Update the Mac client** to use the new voice ID

### Technical Specifications

#### Hardware Requirements
- **Mac Client**: Any Mac running macOS 14+
- **Ubuntu Server**: System with RTX 3090 GPU, 128GB RAM
- **Network**: Local network connectivity with at least 10Mbps bandwidth

#### Performance Metrics
- **Voice Recognition Latency**: 1-3 seconds (dependent on VoiceInk)
- **AI Processing Time**: 1-5 seconds (dependent on Gemini)
- **TTS Generation Time**: 0.5-2 seconds for typical responses
- **End-to-End Latency**: 2.5-10 seconds total response time

#### Resource Utilization
- **Mac CPU Usage**: 5-10% during active monitoring
- **Ubuntu GPU Memory**: ~8GB VRAM for Sesame TTS model
- **Network Usage**: ~100KB per request, ~1MB per response
