from flask import Flask, request, send_file
from flask_cors import CORS # Cần cài: pip install flask-cors
import asyncio
import edge_tts
import io

app = Flask(__name__)
CORS(app) # Cho phép Web gọi API này

async def get_voice_data(text):
    # Sử dụng giọng Mỹ en-US-AvaNeural
    communicate = edge_tts.Communicate(text, "en-US-AvaNeural")
    data = b""
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            data += chunk["data"]
    return data

@app.route('/speak')
def speak():
    text = request.args.get('text', '')
    if not text:
        return "No text provided", 400
    
    # Chạy xử lý TTS
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        audio_data = loop.run_until_complete(get_voice_data(text))
        return send_file(io.BytesIO(audio_data), mimetype="audio/mpeg")
    except Exception as e:
        print(f"Error in TTS: {e}")
        return str(e), 500

if __name__ == '__main__':
    print("TTS Server đang chạy tại http://localhost:5000")
    app.run(port=5000)
