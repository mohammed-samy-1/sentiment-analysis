from flask import Flask, request, jsonify

from Sentiment_Response import SentimentResponse
from transformers import pipeline

app = Flask(__name__)
pipline = pipeline("sentiment-analysis")


def sentiment_analysis(comments: list):
    out = pipline.predict(comments)
    return out

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
