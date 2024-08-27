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
import threading
import time
from playwright.sync_api import sync_playwright

app = Flask(__name__)
CORS(app)

# Path to the cookies file
cookie_file_path = os.path.join(os.getcwd(), 'cookies.txt')

def save_cookies_as_netscape(cookies, file_path):
    with open(file_path, 'w') as f:
        f.write("# Netscape HTTP Cookie File\n")
        f.write("# http://curl.haxx.se/rfc/cookie_spec.html\n")
        f.write("# This is a generated file!  Do not edit.\n")
        for cookie in cookies:
            domain = cookie.get('domain', '')
            flag = 'TRUE' if cookie.get('httpOnly', False) else 'FALSE'
            path = cookie.get('path', '/')
            secure = 'TRUE' if cookie.get('secure', False) else 'FALSE'
            expires = int(cookie.get('expires', 0))
            name = cookie.get('name', '')
            value = cookie.get('value', '')
            print(domain)
            print(flag)
            print(path)
            print(secure)
            print(expires)
            print(name)
            print(value)
            # Ensure cookie fields are present and formatted properly
            if all([domain, name]):
                f.write(f"{domain}\t{flag}\t{path}\t{secure}\t{expires}\t{name}\t{value}\n")

def refresh_cookies():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            page.goto('https://www.youtube.com')
            page.wait_for_timeout(10000)
            cookies = context.cookies()
            save_cookies_as_netscape(cookies, cookie_file_path)
            browser.close()
            print("Cookies refreshed and saved successfully.")
    except Exception as e:
        print("Failed to refresh cookies:", str(e))

def start_cookie_refresh(interval=600):
    while True:
        refresh_cookies()
        time.sleep(interval)

@app.route("/", methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the API"}), 200

@app.route("/get_video_info", methods=['GET'])
def get_video_info():
    video_url = request.args.get("video_url")
    if video_url is None:
        return jsonify({"message": "Video URL is required"}), 400

    try:
        if not os.path.exists(cookie_file_path):
            refresh_cookies()

        ydl_opts = {
            'format': 'best',
            'verbose': True,
            'cookiefile': cookie_file_path,
            'nocheckcertificate': True,
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
        if "cookies" in error_message.lower():
            refresh_cookies()
            return jsonify({'error': 'Cookies expired or invalid, refreshing...'}), 403
        return jsonify({'error': error_message}), 404
    except yt_dlp.utils.DownloadError as e:
        error_message = str(e)
        print(error_message)
        return jsonify({'error': error_message}), 404
    except Exception as e:
        error_message = str(e)
        print("Unexpected error occurred:", error_message)
        return jsonify({'error': 'An unexpected error occurred', 'details': error_message}), 500

# Start the cookie refresh thread
threading.Thread(target=start_cookie_refresh, daemon=True).start()


