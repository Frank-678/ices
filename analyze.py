# Import libraries used in 'main' function
from csv import DictReader
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialization of global variables
pos = 0
neu = 0
neg = 0


def main():
    # Create variable tailored to analyze
    analyzer = SentimentIntensityAnalyzer()
    
    # Read csv
    with open('comments.csv', 'r') as file:
        reader = DictReader(file)
        for row in reader:
            # Analyze each sample    
            analyzer_score = analyzer.polarity_scores(row['Review_Text'])
            classify_sentiment(analyzer_score['compound'])
    
    #  Summarize in the form of words and charts
    print("Summary:",f"positive : {pos}",f"neutral : {neu}",f"negtive : {neg}", sep = '\n')
    print_chart()


def classify_sentiment(score):
    
    global pos, neu, neg

    if score < -0.5:
        neg += 1
    elif score > 0.5:
        pos += 1
    else:
        neu += 1


def print_chart():
    import matplotlib.pyplot as plt

    labels = ['positive', 'neutral', 'negtive']
    sizes = [pos, neu, neg]

    plt.figure(figsize = (16, 12))

    plt.subplot(8, 12, 1)
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Pie Chart Example')

    plt.subplot(8, 12, 2)
    plt.bar(labels, sizes)
    plt.title('Bar Chart Example')
    plt.xlabel('Categories')
    plt.ylabel('Values')

    plt.show()


if __name__ == '__main__':
    main()