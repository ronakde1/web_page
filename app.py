from flask import Flask, render_template

app = Flask(__name__)

# Example data — in a real app, you could pull from a database or API
articles = [
    {
        "title": "Tech Giants Announce New AI Initiative",
        "image": "https://picsum.photos/400/250?random=2",
        "summary": "Several leading tech companies unveiled plans for a collaborative AI research project..."
    },
    {
        "title": "Sports: Championship Finals Set to Begin",
        "image": "https://picsum.photos/400/250?random=3",
        "summary": "The stage is set for one of the most anticipated sports finals in recent memory..."
    },
    {
        "title": "World Leaders Meet for Climate Summit",
        "image": "https://picsum.photos/400/250?random=4",
        "summary": "Global leaders convened today to discuss the next phase of environmental policy..."
    },
    {
        "title": "Innovation: Breakthrough in Renewable Energy",
        "image": "https://picsum.photos/400/250?random=5",
        "summary": "Scientists report a major advancement that could revolutionize sustainable power..."
    }
]

@app.route('/')
def home():
    featured_article = {
        "title": "Breaking: Major Developments in Global Markets",
        "image": "https://picsum.photos/900/400?random=1",
        "summary": "The global stock market saw dramatic changes today as analysts weigh the impacts of ongoing economic shifts..."
    }
    return render_template("index.html", featured=featured_article, articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
