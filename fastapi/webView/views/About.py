# 声明：本代码仅供学习和研究目的使用。使用者应遵守以下原则：  
# 1. 不得用于任何商业用途。  
# 2. 使用时应遵守目标平台的使用条款和robots.txt规则。  
# 3. 不得进行大规模爬取或对平台造成运营干扰。  
# 4. 应合理控制请求频率，避免给目标平台带来不必要的负担。   
# 5. 不得用于任何非法或不当的用途。
#   
# 详细许可条款请参阅项目根目录下的LICENSE文件。  
# 使用本代码即表示您同意遵守上述原则和LICENSE中的所有条款。  

# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : About.py
# Time       ：2026.2.9 18:03
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com OR WorkerHMan@gmail.com
# version    ：python 3.9
# Description：
"""
from pywebio.output import popup, put_markdown, put_html, put_text, put_link, put_image
from webView.views.ViewsUtils import ViewsUtils

t = ViewsUtils().t


# 关于弹窗/About pop-up
def about_pop_window():
    with popup(t('更多信息', 'More Information')):
        put_html('<h3>👀{}</h3>'.format(t('访问记录', 'Visit Record')))
        put_image('https://views.whatilearened.today/views/github/evil0ctal/TikTokDownload_PyWebIO.svg',
                  title='访问记录')
        put_html('<hr>')
        put_html('<h3>⭐Github</h3>')
        put_markdown('[Douyin_TikTok_Download_API](https://github.com/Evil0ctal/Douyin_TikTok_Download_API)')
        put_html('<hr>')
        put_html('<h3>🎯{}</h3>'.format(t('反馈', 'Feedback')))
        put_markdown('{}：[issues](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/issues)'.format(
            t('Bug反馈', 'Bug Feedback')))
        put_html('<hr>')
        put_html('<h3>💖WeChat</h3>')
        put_markdown('WeChat：[Evil0ctal](https://mycyberpunk.com/)')
        put_html('<hr>')
