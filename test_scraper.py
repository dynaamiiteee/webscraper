import requests
from bs4 import BeautifulSoup
import time
#this import is for sentiment analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Initialize the VADER sentiment intensity analyzer
analyzer = SentimentIntensityAnalyzer()

# negative example
# https://www.fool.com/investing/2025/03/01/why-navitas-stock-plummeted-today/
# positive example
# https://www.fool.com/investing/2025/05/24/rare-signal-for-sp-500-15th-time-75-years-stocks/
# neutral example
# https://www.fool.com/investing/2025/05/23/warren-buffetts-warning-why-stock-market-crash/

url = input("Enter the URL of the article: ")

time.sleep(1)  # Sleep to avoid overwhelming the server
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')


# Find the article content
paragraphs = soup.find_all('p')


# Exclude paragraphs inside header and footer
header = soup.find('header')
footer = soup.find('footer')
# Function to check if a tag is inside the header or footer
def is_in_header_or_footer(tag):
    parent = tag.parent
    while parent:
        if parent == header or parent == footer:
            return True
        parent = parent.parent
    return False
# Filter out paragraphs that are inside the header or footer
paragraphs = [p for p in paragraphs if not is_in_header_or_footer(p)]


# variables to combine the total sentiment of all paragraphs
sentiment_total = 0
sentiment_paragraph_count = 0


# Loop through each paragraph and analyze sentiment
for paragraph in paragraphs:
    text = paragraph.get_text()
    parent_classes = paragraph.parent.get('class') or []
    if not text or len(text) < 175: 
        continue  # Skip short or empty paragraphs
    elif not any('article' in c for c in parent_classes):
        continue  # Skip if parent element does not have 'article' in its class
    else:
        sentiment = analyzer.polarity_scores(text)
        print(f"Text: {text}")
        print(f"Sentiment: {sentiment}")
        # Determine the overall sentiment based on the compound score
        sentiment_total += sentiment['compound']
        sentiment_paragraph_count += 1
        if sentiment['compound'] >= 0.05:
            print("  Overall Sentiment: Positive")
        elif sentiment['compound'] <= -0.05:
            print("  Overall Sentiment: Negative")
        else:
            print("  Overall Sentiment: Neutral")
        print("-" * 30)
        time.sleep(0.25)  # Sleep to avoid overwhelming the server


# Determine the overall sentiment of the article
print(f"Total Sentiment Score: {sentiment_total / sentiment_paragraph_count}")
if sentiment_total/ sentiment_paragraph_count >= 0.05:
    overall_sentiment = "Positive"
elif sentiment_total/ sentiment_paragraph_count <= -0.05:
    overall_sentiment = "Negative"
else:
    overall_sentiment = "Neutral"
print(f"Overall Sentiment of the Article: {overall_sentiment}")

# Save the results to a file
with open('sentiment_results.txt', 'w') as f:
    f.write(f"Total Sentiment Score: {sentiment_total / sentiment_paragraph_count}\n")
    f.write(f"Overall Sentiment of the Article: {overall_sentiment}\n")
    f.write("\nDetailed Sentiment Analysis:\n")
    for paragraph in paragraphs:
        text = paragraph.get_text()
        if text and len(text) >= 175:
            sentiment = analyzer.polarity_scores(text)
            f.write(f"Text: {text}\n")
            f.write(f"Sentiment: {sentiment}\n")
            f.write("-" * 30 + "\n")