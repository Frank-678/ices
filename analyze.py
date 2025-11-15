# Perform sentiment analysis on user comments on Minecraft
from csv import DictReader
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize global variables
pos = 0
neu = 0
neg = 0


def main():
    # Create analyzer object
    analyzer = SentimentIntensityAnalyzer()
    
    # Read csv
    with open('comments.csv', 'r') as file:
        reader = DictReader(file)
        for row in reader:
            # Analyze each sample    
            analyzer_score = analyzer.polarity_scores(row['Review_Text']) # 注：返回的变量是字典，key分别是pos, neu, neg（相对权重比例）和compound（整体分数-1 ~ +1）
            classify_sentiment(analyzer_score['compound'])
    
    #  Summarize in the form of words and charts
    print("Summary:",f"positive : {pos}",f"neutral : {neu}",f"negative : {neg}", sep = '\n') # 注：sep指的不是 '+'（字符串连接符）而是','
    print_chart()


# Classify
def classify_sentiment(score):
    # State global variables
    global pos, neu, neg  # 注解易错：Python中修改全局变量必须global声明，而读取不需要。

    # Justify sentiment intensity
    if score < -0.05:
        neg += 1
    elif score > 0.05:
        pos += 1
    else:
        neu += 1 # 注：这里用match-case可能会麻烦（case不能是不等号）


# Print pie and bar charts
def print_chart():
    import matplotlib.pyplot as plt

    labels = ['positive', 'neutral', 'negative']
    sizes = [pos, neu, neg]

    # Create a window 
    plt.figure(figsize = (16, 9))

    # Generate pie chart on the left
    plt.subplot(1, 2, 1)  # 注：这里前两个参数表示把figure用几行几列分隔开
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Pie Chart')

    # Generate bar chart on the right
    plt.subplot(1, 2, 2)
    plt.bar(labels, sizes)
    plt.title('Bar Chart')
    plt.xlabel('Categories')
    plt.ylabel('Values')

    # Show graphs
    plt.show()


# Execute
if __name__ == '__main__':
    main()