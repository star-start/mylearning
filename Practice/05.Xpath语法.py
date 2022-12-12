from lxml import etree

# 获取html
html = open('test.html', 'r', encoding='utf-8').read()
# print(html)
# 解析方法有两个：etree.HTML和etree.parse
# 针对字符串的解析使用etree.HTML
html_ele = etree.HTML(html)
print(html_ele)  # <Element html at 0x2304f3ae0c0>
# 读取html文件使用etree.parse，参数1为路径，参数2是解析器
# html_ele = etree.parse('./test.html', etree.HTMLParser())
# print(html_ele)  # <lxml.etree._ElementTree object at 0x000002420A3D9140>

# 获取所有图片的src
srcs = html_ele.xpath('//img/@src')
print(srcs)  # 因为获取的是src的值，所以获取的是字符串的列表
# 获取img标签本身
imgs = html_ele.xpath('//img')
# html中的标签在这里也是Element对象
print(imgs)  # [<Element img at 0x276ecfac0c0>, <Element img at 0x276ecfac100>]

# 获取歌曲信息的ul的所有li标签
lis = html_ele.xpath('//body/ul/li')
print(lis)  # [<Element li at 0x207ee62c400>, <Element li at 0x207ee62c440>, <Element li at 0x207ee62c480>]
for li in lis:  # Element对象本身就可以继续使用xpath
    # name = li.xpath('text()')[0]  # 获取歌手名
    name = li.xpath('./text()')[0]  # 获取歌手名
    print("歌手：" + name)
    music = li.xpath('span/text()')[0]  # 获取歌名
    print("歌曲：" + music)

    # 将两个一起获取
    # name_music = li.xpath('//text()')  # 这里相当于面对整个html进行匹配
    # print(li.xpath('/html'))  # [<Element html at 0x1eaebd78500>]
    name_music = li.xpath('.//text()')  # 如果要使用//或者 / ，一定要使用 . 表示从当前位置出发
    print(name_music)