from flask import Flask, request, jsonify
import tweepy

app = Flask(__name__)

# Twitter API anahtarları (bunları kendi aldığınız anahtarlarla değiştirin)
API_KEY = "Eo6B0jHAoISpdhyEnS3UVr6WU"
API_SECRET_KEY = "BbTuRh8nhXeR1qEdl9NZDsh2ywtP6W29dcSY0yVLdCKwQ2kZey"
ACCESS_TOKEN = "1464165640390991872-h8dglYf65oR9LAjvdUji3qGH9SmtEz"
ACCESS_TOKEN_SECRET = "9CnNNBXaLuEtiIE3cjIxLwHM9V2BVbrO6TmIutkcyH6jg"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAADAqwgEAAAAA2je68KmMcZYPXIwKdf2roZ8b3mQ%3DZEyCDoIvEMKb0Ml11wkhSF4beAoz2gZxzt6uw8g4FpgTOA4VpG"

# Twitter API bağlantısı
client = tweepy.Client(bearer_token=BEARER_TOKEN)

@app.route('/api/getTweets', methods=['POST'])
def get_tweets():
    data = request.json
    search_term = data.get('searchTerm')
    like_limit = int(data.get('likeLimit'))
    tweet_count = int(data.get('tweetCount'))

    response = client.search_recent_tweets(
        query=search_term,
        max_results=tweet_count,
        tweet_fields=["author_id", "created_at", "public_metrics"]
    )

    tweets_data = []
    if response.data:
        for tweet in response.data:
            likes = tweet.public_metrics['like_count']
            if likes >= like_limit:
                tweets_data.append({'text': tweet.text, 'likes': likes})

    return jsonify(tweets_data)

if __name__ == '__main__':
    app.run(debug=True)
