# import yt_dlp
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# app = Flask(__name__)
# CORS(app)
# @app.route('/', methods=['GET'])
# def get_method():
#     return "Welcome To My Python Api"

# @app.route('/get_video_info', methods=['GET'])
# def get_video_info():
#     video_url = request.args.get('video_url')  # Using .get() to avoid KeyError if 'video_url' is missing
#     if not video_url:
#         return jsonify({'error': 'Missing video_url parameter'}), 400
    
#     # ydl_opts = {
#     # # 'format': 'best',
#     # # 'verbose': True,
#     # # 'headers': {
#     # #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
#     # #     'Referer': 'https://www.youtube.com/',
#     # #     'Accept-Encoding': 'gzip, deflate, br',
#     # #     'Connection': 'keep-alive'
#     # #     }
#     # }
#     ydl_opts = {
#         'force_generic_extractor': True,
#         '--verbose':True,
#         'cookiefile': 'cookies.txt',  # Path to your cookies file
#         'format': 'best',
#         'nocheckcertificate': True,
#         'quiet': True,
#         'http_headers': {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
#             'Accept-Language': 'en-US,en;q=0.5'
#         },
#         'extractor_retries': 3,  # Retry 3 times in case of extractor issues
#         'sleep_interval': 2,  # Sleep for a few seconds between requests
#         'throttled_rate': '1M'  # Throttle download rate to avoid triggering anti-bot measures
#     }


#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(video_url, download=False)
#             return jsonify(info), 200
#     except yt_dlp.utils.ExtractorError as e:
#         error_message = str(e)
#         print(error_message)
#         return jsonify({'error': error_message}), 404
#     except yt_dlp.utils.DownloadError as e:
#         error_message = str(e)
#         print(error_message)
#         return jsonify({'error': error_message}), 404
#     except Exception as e:
#         print(e)
#         return jsonify({'error': 'An unexpected error occurred'}), 500

# # import yt_dlp
# # from flask import Flask, request, jsonify
# # from flask_cors import CORS

# # app = Flask(__name__)
# # CORS(app)

# # @app.route('/', methods=['GET'])
# # def get_method():
# #     return "Welcome To My Python Api"

# # @app.route('/get_video_info', methods=['GET'])
# # def get_video_info():
# #     video_url = request.args.get('video_url')  # Using .get() to avoid KeyError if 'video_url' is missing
# #     if not video_url:
# #         return jsonify({'error': 'Missing video_url parameter'}), 400
    
# #     # Options for yt-dlp to handle subtitles and provide verbose output
# #     ydl_opts = {
# #         'format': 'best',  # Change this if needed
# #         '--verbose': True,
# #         'skip_download': True,  # Do not download the video
# #         'writesubtitles': True,  # Write subtitles if available
# #         'subtitleslangs': ['en', 'all'],
# #         'noplaylist': True,
# #         'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
# #     }

# #     try:
# #         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
# #             info = ydl.extract_info(video_url, download=False)
            
# #             # Check if there are available formats
# #             if not info.get('formats'):
# #                 return jsonify({'error': 'No formats available for this video'}), 404
            
# #             # Return all available information, including formats and subtitles
# #             return jsonify(info), 200
# #     except yt_dlp.utils.ExtractorError as e:
# #         error_message = str(e)
# #         print(error_message)
# #         return jsonify({'error': error_message}), 404
# #     except yt_dlp.utils.DownloadError as e:
# #         error_message = str(e)
# #         print(error_message)
# #         return jsonify({'error': error_message}), 404
# #     except Exception as e:
# #         print(e)
# #         return jsonify({'error': 'An unexpected error occurred'}), 500


# # import yt_dlp
# # from flask import Flask, request, jsonify
# # from flask_cors import CORS

# # app = Flask(__name__)
# # CORS(app)

# # @app.route('/', methods=['GET'])
# # def get_method():
# #     return "Welcome To My Python Api"

# # @app.route('/get_video_info', methods=['GET'])
# # def get_video_info():
# #     video_url = request.args.get('video_url')
# #     if not video_url:
# #         return jsonify({'error': 'Missing video_url parameter'}), 400
    
# #     # Adjusted options for yt-dlp
# #     ydl_opts = {
# #         '--verbose': True,
# #         'cookiefile': 'cookies.txt',
# #         'format': 'best',
# #         'skip_download': True,
# #         'writesubtitles': True,
# #         'subtitleslangs': ['en', 'all'],
# #         'noplaylist': True,
# #         'http_headers': {  # Set custom HTTP headers
# #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
# #             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# #             'Accept-Language': 'en-us,en;q=0.5',
# #             'Sec-Fetch-Mode': 'navigate'
# #         },
# #     }

# #     try:
# #         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
# #             info = ydl.extract_info(video_url, download=False)
            
# #             if not info.get('formats'):
# #                 return jsonify({'error': 'No formats available for this video'}), 404
            
# #             return jsonify(info), 200
# #     except yt_dlp.utils.ExtractorError as e:
# #         error_message = str(e)
# #         print(error_message)
# #         return jsonify({'error': error_message}), 404
# #     except yt_dlp.utils.DownloadError as e:
# #         error_message = str(e)
# #         print(error_message)
# #         return jsonify({'error': error_message}), 404
# #     except Exception as e:
# #         print(e)
# #         return jsonify({'error': 'An unexpected error occurred'}), 500


# from flask import Flask, jsonify, request
# from flask_cors import CORS
# import yt_dlp

# app = Flask(__name__)

# CORS(app)

# @app.route("/", methods=['GET'])
# def home():
#     return jsonify({"message": "Welcome to the API"}), 200

# @app.route("/get_video_info", methods=['GET'])
# def get_video_info():
#     video_url = request.args.get("video_url")
#     if video_url is None:
#         return jsonify({"message": "Video URL is required"}), 400
    
#     try:
#         ydl_opts = {
#             'format': 'best',
#             'verbose':True,
#             'cookiefile': 'cookies.txt',
#             'nocheckcertificate': True,  # Ignore SSL certificate errors
#         }
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(video_url, download=False)
#             return jsonify(info), 200

#     except yt_dlp.utils.ExtractorError as e:
#         error_message = str(e)
#         print(error_message)
#         return jsonify({'error': error_message}), 404
#     except yt_dlp.utils.DownloadError as e:
#         error_message = str(e)
#         print(error_message)
#         return jsonify({'error': error_message}), 404
#     except Exception as e:
#         print(e)
#         return jsonify({'error': 'An unexpected error occurred'}), 500

# from flask import Flask, jsonify, request
# from flask_cors import CORS
# import yt_dlp

# app = Flask(__name__)

# CORS(app)

# @app.route("/", methods=['GET'])
# def home():
#     return jsonify({"message": "Welcome to the API"}), 200

# @app.route("/get_video_info", methods=['GET'])
# def get_video_info():
#     video_url = request.args.get("video_url")
#     if video_url is None:
#         return jsonify({"message": "Video URL is required"}), 400
    
#     try:
#         # Corrected usage of cookiesfrombrowser
#         ydl_opts = {
#             'format': 'best',
#             'verbose': True,
#             'cookiesfrombrowser': ('chrome',),  # Correct format
#             'nocheckcertificate': True,
#             'http_headers': {
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
#                 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#                 'Accept-Language': 'en-us,en;q=0.5',
#                 'Sec-Fetch-Mode': 'navigate',
#             }
#         }
        
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(video_url, download=False)
#             return jsonify(info), 200

#     except yt_dlp.utils.ExtractorError as e:
#         error_message = str(e)
#         print(error_message)
#         return jsonify({'error': error_message}), 404
#     except yt_dlp.utils.DownloadError as e:
#         error_message = str(e)
#         print(error_message)
#         return jsonify({'error': error_message}), 404
#     except Exception as e:
#         print(e)
#         return jsonify({'error': 'An unexpected error occurred'}), 500



from flask import Flask, jsonify, request
from flask_cors import CORS
import yt_dlp
import os
import json
import traceback
import threading
import time
from playwright.sync_api import sync_playwright

app = Flask(__name__)
CORS(app)

# Path to the cookies file
cookie_file_path = os.path.join(os.getcwd(), 'cookies.txt')

# Function to refresh cookies using Playwright
def refresh_cookies():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)  # Set headless=True for server environments
            context = browser.new_context()
            page = context.new_page()

            # Open YouTube and perform the login process
            page.goto('https://www.youtube.com')
            page.wait_for_timeout(10000)  # Adjust timeout as needed to perform login manually

            # Save cookies to a file
            cookies = context.cookies()
            with open(cookie_file_path, 'w') as f:
                json.dump(cookies, f)

            browser.close()
            print("Cookies refreshed successfully.")
    except Exception as e:
        print("Failed to refresh cookies:", str(e))
        print(traceback.format_exc())

# Function to periodically refresh cookies
def start_cookie_refresh(interval=600):  # Interval set to 600 seconds (10 minutes)
    while True:
        refresh_cookies()
        time.sleep(interval)

# Start the cookie refresh thread outside of the __main__ block
threading.Thread(target=start_cookie_refresh, daemon=True).start()

@app.route("/", methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the API"}), 200

@app.route("/get_video_info", methods=['GET'])
def get_video_info():
    video_url = request.args.get("video_url")
    if video_url is None:
        return jsonify({"message": "Video URL is required"}), 400

    try:
        # Check if the cookie file exists and is valid
        if not os.path.exists(cookie_file_path):
            refresh_cookies()  # Refresh cookies if file is not found

        ydl_opts = {
            'format': 'best',
            'verbose': True,
            'cookiefile': cookie_file_path,  # Use dynamic cookie file
            'nocheckcertificate': True,      # Ignore SSL certificate errors
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-us,en;q=0.5',
                'Sec-Fetch-Mode': 'navigate',
            }
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            return jsonify(info), 200

    except yt_dlp.utils.ExtractorError as e:
        error_message = str(e)
        print(error_message)
        # If a cookie-related error is detected, attempt to refresh cookies
        if "cookies" in error_message.lower():
            refresh_cookies()  # Refresh cookies dynamically upon error
            return jsonify({'error': 'Cookies expired or invalid, refreshing...'}), 403
        return jsonify({'error': error_message}), 404
    except yt_dlp.utils.DownloadError as e:
        error_message = str(e)
        print(error_message)
        return jsonify({'error': error_message}), 404
    except Exception as e:
        error_message = str(e)
        print("Unexpected error occurred:", error_message)
        print(traceback.format_exc())
        return jsonify({'error': 'An unexpected error occurred', 'details': error_message}), 500
