Preliminary Sentiment Analysis of Minecraft User Reviews

1.Project Overview

This project fulfills the requirements of the AI task description: "AI often begins with data insights." The goal was to perform a preliminary sentiment analysis on user-generated comments for a selected product.


2.Technical Implementation Details

2.1 No AI declararation

All data in comments.csv was collected from Metacritic (https://www.metacritic.com/game/minecraft/user-reviews/?platform=pc) ,and formatted by AI into CSV format.

No AIs have participated in any piece of code. All done by myself after query to AI about related knowledge.


2.2. Classification Thresholds

The compound score ranges from -1.0 to +1.0. We defined the following custom thresholds to classify the sentiment, as required by the assignment:

Compound Score Range,Classification

Score > 0.05           ,Positive

Score < −0.05          ,Negative

−0.05 ≤ Score ≤ 0.05      ,Neutral


2.3. Data Visualization

The results are presented visually using the matplotlib.pyplot library, generating two charts simultaneously:
A Pie Chart showing the percentage distribution of the three sentiment categories.
A Bar Chart showing the raw count of reviews per category.


3.How to Run the Code

3.1. Prerequisites

You need the following Python packages installed:

**pip install vaderSentiment pandas matplotlib**

3.3. Execution

Execute the main Python script from your terminal:

**python analyze.py**

This will:

Print the final Positive/Neutral/Negative counts to the console.

Open a window displaying the combined Pie and Bar charts.
