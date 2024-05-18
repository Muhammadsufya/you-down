from flask import Flask, request, send_file, jsonify
from pytube import YouTube
import os
import uuid

app = Flask(__name__)

def download_video(url, resolution):
    yt = YouTube(url)
    stream = yt.streams.filter(res=resolution, file_extension='mp4').first()
    if not stream:
        return None
    file_path = stream.download(filename=f"{uuid.uuid4()}.mp4")
    return file_path

def download_audio(url):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    if not stream:
        return None
    file_path = stream.download(filename=f"{uuid.uuid4()}.mp3")
    return file_path

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    url = data.get('url')
    format_type = data.get('format')
    resolution = data.get('resolution')

    if format_type == 'video':
        file_path = download_video(url, resolution)
    elif format_type == 'audio':
        file_path = download_audio(url)
    else:
        return jsonify({'error': 'Invalid format type'}), 400

    if not file_path:
        return jsonify({'error': 'Failed to download'}), 500

    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
