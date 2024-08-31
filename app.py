
import yt_dlp
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_method():
    return "Welcome To My Python Api"

@app.route('/get_video_info', methods=['GET'])
def get_video_info():
    video_url = request.args.get('video_url')  # Using .get() to avoid KeyError if 'video_url' is missing
    if not video_url:
        return jsonify({'error': 'Missing video_url parameter'}), 400
    
    # Options for yt-dlp to handle subtitles and provide verbose output
    ydl_opts = {
        'format': 'best',  # Change this if needed
        '--verbose': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            
            # Check if there are available formats
            if not info.get('formats'):
                return jsonify({'error': 'No formats available for this video'}), 404
            
            # Return all available information, including formats and subtitles
            return jsonify(info), 200
    except yt_dlp.utils.ExtractorError as e:
        error_message = str(e)
        print(error_message)
        return jsonify({'error': error_message}), 404
    except yt_dlp.utils.DownloadError as e:
        error_message = str(e)
        print(error_message)
        return jsonify({'error': error_message}), 404
    except Exception as e:
        print(e)
        return jsonify({'error': 'An unexpected error occurred'}), 500
