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

    if "xvideos.com" in video_url:
        video_url=video_url.replace('www.','mobile-')
    print("Video Link: ", video_url)
    
    ydl_opts = {'format':'best','--verbose': True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
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

if __name__ == '__main__':
    app.run(debug=True)
