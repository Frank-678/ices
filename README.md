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

​4. 遇到的挑战与解决方法 (Challenges Encountered and Solutions)

​4.1. 最大的挑战：从零开始探索多领域的交叉技术
​本项目最大的挑战在于，任务要求本身跨越了多个我之前从未接触过的技术领域。从数据获取到最终的可视化，每一步都是一个全新的学习过程：

​API 调用： 首次尝试理解什么是 API、如何进行 HTTP 请求、处理 API Key 以及解析 JSON 响应。
​文本情感分析 (NLP)： 首次接触“情感分析”这一概念，需要理解如何将非结构化的文本（用户评论）转换为结构化的数据（情感分数）。

​Python 库的选型： 面对海量的 Python 库，需要自行调研、评估并选择合适（且符合方案 B 要求）的工具（如 vaderSentiment）。

​数据可视化： 首次学习使用 matplotlib 库，理解 Figure, Subplot, Axes 的概念，并将抽象的数据（计数）转换为直观的图表（饼图和柱状图）。

​因此，本项目的所有具体技术挑战，都是在克服这一“陡峭学习曲线”的背景下完成的。

​4.2. 方案选择的变更：从 API (方案A) 到本地库 (方案B)

​最初的挑战 (API 调用)：

​作为对 API 领域的初次探索，我尝试了方案 A。
​我首先尝试了 DeepSeek 的 API，随后又转向了百度千帆平台。

​遇到的困难： 两个平台的示例代码都假设使用者已有 API 基础。在缺乏“API 调用机理”知识的情况下，我无法清晰理解其工作流程（如请求构造、参数传递和响应解析），导致项目在第一步就陷入了停滞。

​解决方案 (转向方案B)：

​为了在有限时间内完成任务核心，我决定采用方案 B (使用现成库)。这个方案绕过了复杂的网络和认证问题，让我能把学习重点聚焦在“情感分析”和“数据处理”这两个核心任务上。

​4.3. 库的选型：适配英文评论

​挑战 (SnowNLP 的局限性)：

​方案 B 建议使用 SnowNLP，但该库主要面向中文情感分析。本项目收集的数据（来自 Metacritic）是英文评论。

​解决方案 (VADER 库)：

​通过调研，我找到了一个完美符合需求的库：vaderSentiment。

​VADER 是一个基于词典和规则的分析器，专门为英文（尤其是社交媒体文本）设计。它不依赖机器学习，完美符合方案 B 的要求，并且能高效地处理英文评论。

​4.4. 代码实现中的具体技术难题

​挑战 1：理解 VADER 库的返回值 (TypeError)

​问题： analyzer.polarity_scores() 返回的到底是什么？我最初错误地认为它返回一个单一的分数，并尝试将 analyzer_score (一个 dict 字典) 直接与浮点数进行比较。

​解决： 通过调试和阅读文档，我确认了 analyzer_score 是一个包含 neg, neu, pos, compound 四个键的字典。正确的做法是仅提取其 compound 键（一个 float 浮点数）进行比较。

​挑战 2：全局变量 (Global Variables) 的作用域

​问题： 为了统计 pos, neu, neg 的数量，我最初将它们定义为全局变量。但在 classify_sentiment 函数内部尝试 neg += 1 时，Python 抛出了 UnboundLocalError。

​解决 (方案一)： 在函数内部使用 global pos, neu, neg 关键字，明确声明意图是修改全局变量。

​解决 (方案二 - 升级)： 认识到使用 global 会使数据流变得混乱。因此，我重构了代码：在 main() 函数中初始化一个 counts 字典，并将其作为参数传递给 classify_sentiment 和 print_chart 函数。这实现了代码的封装，使程序更健壮。

​挑战 3：选择合适的分类逻辑 (if/else vs match/case)

​问题： 在 classify_sentiment 中，需要根据 score 的范围（大于 0.05，小于 -0.05）来进行判断。

​解决： 我研究了 match/case 语法，发现它并不直接支持不等式比较。因此，我确定传统的 if/elif/else 结构是处理数值范围判断时最清晰、最正确的选择。

​挑战 4：在同一窗口中绘制多个图表 (Subplot)

​问题： 希望同时提供“比例”（适合饼图）和“绝对数量”（适合柱状图）两种视角。

​解决： 使用了 matplotlib 的子图 (Subplot) 功能。通过 plt.subplot(1, 2, 1) 和 plt.subplot(1, 2, 2)，将画布分割为 1 行 2 列的网格，在一个窗口中并排展示了两个关联的图表。

​挑战 5：格式化控制台的总结输出 (sep='\n')

​问题： 希望将最终的三个计数器分行打印，而不是挤在一行。

​解决： 利用了 print() 函数的 sep='\n' 参数。通过将所有要打印的项作为独立参数（用逗号分隔）传入，print 自动在每个参数之间插入换行符，代码更简洁且易读。
