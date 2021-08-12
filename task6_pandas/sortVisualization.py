
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.arrays import integer
from pandas.core.arrays.sparse import dtype
import textwrap 

def sort(file):
    # df是dataFrame的简称
    # 设置dtype是因为sort_values函数必须按数值排序，而essence.csv文件中eyeNum这一列类型是object
    df = pd.read_csv(file,dtype={'eyeNum':int})

    df_title_eye = df.loc[:,['title','eyeNum']]
    # print(df_title_eye)
    # 本次是统计浏览数前20的文章，故不需求和sum，直接排序
    sort_title_eye = df_title_eye.sort_values(by='eyeNum',ascending=False)
    # print(sort_title_eye)

    top_20_articles = sort_title_eye[0:20]
    # print(top_20_articles)

    for i in range(20):
        # textwrap给文章标题换行，因为有的标题太长，无法全部显示
        top_20_articles.iat[i, 0] = textwrap.fill(top_20_articles.iat[i, 0],20)
    # print(top_20_articles)
    return top_20_articles

def visualize(df):
    # 设置字体，解决中文乱码问题
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # 下面三个分别是设置画布大小，设置y轴标签字体大小，设置y轴标签倾斜角度
    # 原因均为标题太长了！！！！！！！！！
    # 经多次调整，效果仍然差强人意，日后看看是否有其他办法。
    plt.figure(figsize=(16,16))
    plt.tick_params(axis='y',labelsize=7)
    plt.yticks(rotation=10)

    # 设置横纵坐标分别是什么
    plt.barh(df['title'],df['eyeNum'])
    # 翻转y轴，即将浏览数最多的放在最上面
    plt.gca().invert_yaxis()
    plt.show()
if __name__ == '__main__':
    df = sort('essence.csv')
    visualize(df)
