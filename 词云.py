import jieba
from jieba.analyse import extract_tags
from scipy.misc import imread
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt

import imageio



def generater(**kwargs):
    content_name = kwargs['content_name']
    # content_path = './{}.txt'.format(content_name)
    content_path = 'finall.txt'
    top_k = kwargs['top_k']
    bg_name = kwargs['bg_name']
    color = kwargs['color']
    font_type = kwargs['font_type']

    with open('result1.txt',encoding='utf-8') as f:
        content = f.read()
    '''
    根据TF/IDF提取topK个关键词
    '''
    tags = extract_tags(sentence=content, topK=top_k)
    # tags = ['不见','万里','何处','不得','明月','琵琶','不知','故人','春风','长安','将军','青山','昨夜','无人']
    '''
    得到关键词的词频
    '''
    # 全模式
    words = [word for word in jieba.cut(content, cut_all=True)]
    words_freq = {}
    for tag in tags:
        freq = words.count(tag)
        words_freq[tag] = freq
    '''
    设置背景
    scipy.misc imread()：返回的是 numpy.ndarray 也即 numpy 下的多维数组对象
    '''
    bg_path = './{}.png'.format(bg_name)
    bg_img = imageio.imread(bg_path)
    font_path = './{}.ttf'.format(font_type)
    word_cloud = WordCloud(font_path=font_path,  # 设置字体
                           background_color=color,  # 背景颜色
                           max_words=top_k,  # 词云显示的最多词数
                           max_font_size=100,  # 字体最大
                           mask=bg_img,  # 背景图
                           )
    word_cloud.generate_from_frequencies(words_freq)
    # # 改变字体颜色
    # img_colors = ImageColorGenerator(bg_img)
    # # 字体颜色为背景图片的颜色
    # word_cloud.recolor(color_func=img_colors)

    # 显示图片
    plt.imshow(word_cloud)
    plt.axis('off')  # 不显示坐标轴
    plt.show()

    # 保存图片
    word_cloud_img = 'china1_word_cloud.png'
    word_cloud.to_file(word_cloud_img)


if __name__ == '__main__':
      generater(content_name='xjp',
                color='white',
                top_k=51,
                bg_name='china',  # 默认png
                font_type='wryh')
