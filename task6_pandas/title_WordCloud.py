
import pandas as pd
import jieba
import jieba.analyse
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt

# 词云来自上次爬取看雪精华帖的文章标题
def get_titles(file):
    df = pd.read_csv(file)
    titles = df['title']
    # print(list(titles))
    return list(titles)

def get_keywords(fromWhere,howMany):
    # 第一个参数：从哪里选取关键词
    # 第二个参数：选取几个关键词
    keywords = jieba.analyse.extract_tags(fromWhere,topK=howMany,withWeight=True)
    # withWeight参数：是否记录关键词的权重
    df = pd.DataFrame(keywords,columns=['keyword','weight'])
    # 生成两列的DataFrame就结构即一个矩阵
    return df

def generate_cloud(frequencies):
    wordcloud = WordCloud(
    'simfang.ttf', # 字体路径：OTF或TTF
    width=1900,
    height=1000,
    background_color='white',
    stopwords=STOPWORDS).generate_from_frequencies(frequencies) # from words or frequencies
    fig = plt.figure(figsize=(12,9))
    plt.imshow(wordcloud) # 将数据显示为图片
    plt.axis('off') # 不显示坐标轴
    plt.tight_layout(pad=0) # tight_layout调整子图的参数，pad相当于css中padding
    plt.show()

if __name__ == '__main__':
    titles = get_titles('essence.csv')
    jieba.analyse.set_stop_words(r'excludeWords.txt')
    df = pd.DataFrame(columns=['keyword','weight'])
    for title in titles:
        title_keyword = get_keywords(title,3)
        df = df.append(title_keyword)
    # print(df)
    grouped = df.groupby('keyword').sum()
    keywords = grouped.sort_values('weight',ascending=False)
    # print(keywords)
    top_300 = keywords[0:300]
    generate_cloud(top_300.weight.to_dict())