from flask import request, jsonify

def init_routes(app):
    @app.route('/recommend_videos', methods=['GET'])
    def recommend_videos():
        # Extract query parameters from the URL
        user_data = request.args.get('user_data')
        video_data = request.args.get('video_data')

        # Example response for testing
        response = {
            "user_data": user_data,
            "video_data": video_data,
            "message": "Successfully received the parameters"
        }

        return jsonify(response)
