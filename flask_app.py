from flask import Flask, request, jsonify
# from comment_classifer import *
# from toxicResponse import ToxicResponse
from Sentiment_Response import SentimentResponse
from sentiment_analysis import *

app = Flask(__name__)


# run_with_ngrok(app)

# @app.route('/comment_classifier', methods=['POST'])
# def process_list():
#     try:
#         # Get the list from the request
#         data = request.json
#         input_list = data.get('comments')
#
#         # Perform operations on the list (for example, reverse it)
#         output_list = classify(input_list).tolist()
#         print(output_list)
#         out = []
#         for i in range(len(input_list)):
#             out.append(ToxicResponse(input_list[i], *output_list[i]).__dict__)
#
#         print(out)
#         # Return the processed list
#         return jsonify({'classes': out})
#     except Exception as e:
#         return jsonify({'error': str(e)})
#

@app.route('/sentiment_analysis', methods=['POST'])
def sentiment():
    try:
        data = request.json
        input_list = data.get('messages')

        # Perform operations on the list (for example, reverse it)
        output_list = sentiment_analysis(input_list)
        out = []
        for i in range(len(input_list)):
            out.append(SentimentResponse(input_list[i], **output_list[i]).__dict__)

        print(out)
        # Return the processed list
        return jsonify({'classes': out})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run()
