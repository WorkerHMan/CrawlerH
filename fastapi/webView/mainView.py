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
# File       : mainView.py
# Time       ：2026.2.9 18:03
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com OR WorkerHMan@gmail.com
# version    ：python 3.9
# Description：
"""
import os
import yaml

from pywebio import session, config as pywebio_config
from pywebio.input import *
from pywebio.output import *

from webView.views.About import *
from webView.views.Document import *

# 读取上级再上级目录的配置文件
config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.yaml')
with open(config_path, 'r', encoding='utf-8') as file:
    _config = yaml.safe_load(file)

pywebio_config(theme=_config['Web']['PyWebIO_Theme'],
               title=_config['Web']['Tab_Title'],
               description=_config['Web']['Description'],
               js_file=[
                   # 整一个看板娘，二次元浓度++
                   _config['Web']['Live2D_JS'] if _config['Web']['Live2D_Enable'] else None,
               ])

class MainView:
    def __init__(self):
        self.utils = ViewsUtils()

    # 主界面/Main view
    def main_view(self):
        # 左侧导航栏/Left navbar
        with use_scope('main'):
            # 设置favicon/Set favicon
            favicon_url = _config['Web']['Favicon']
            session.run_js(f"""
                            $('head').append('<link rel="icon" type="image/png" href="{favicon_url}">')
                            """)
            # 修改footer/Remove footer
            session.run_js("""$('footer').remove()""")
            # 设置不允许referrer/Set no referrer
            session.run_js("""$('head').append('<meta name=referrer content=no-referrer>');""")
            # 设置标题/Set title
            title = self.utils.t("TikTok/抖音无水印在线解析下载",
                                 "Douyin/TikTok online parsing and download without watermark")
            put_html(f"""
                    <div align="center">
                    <a href="/" alt="logo" ><img src="{favicon_url}" width="100"/></a>
                    <h1 align="center">{title}</h1>
                    </div>
                    """)
            # 设置导航栏/Navbar
            put_row(
                [
                    put_button(self.utils.t("开放接口", 'Open API'),
                               onclick=lambda: api_document_pop_window(), link_style=True, small=True),
                    put_button(self.utils.t("关于", 'About'),
                               onclick=lambda: about_pop_window(), link_style=True, small=True),
                ])

            # 设置功能选择/Function selection
            options = [
                # Index: 0
                self.utils.t('🔍批量解析视频', '🔍Batch Parse Video'),
                # Index: 1
                self.utils.t('🔍解析用户主页视频', '🔍Parse User Homepage Video'),
                # Index: 2
                self.utils.t('🥚小彩蛋', '🥚Easter Egg'),
            ]
            select_options = select(
                self.utils.t('请在这里选择一个你想要的功能吧 ~', 'Please select a function you want here ~'),
                required=True,
                options=options,
                help_text=self.utils.t('📎选上面的选项然后点击提交', '📎Select the options above and click Submit')
            )
            # 根据输入运行不同的函数
            if select_options == options[0]:
                put_markdown(self.utils.t('暂未开放，敬请期待~', 'Not yet open, please look forward to it~'))
            elif select_options == options[1]:
                put_markdown(self.utils.t('暂未开放，敬请期待~', 'Not yet open, please look forward to it~'))
            elif select_options == options[2]:
                put_markdown(self.utils.t('暂未开放，敬请期待~', 'Not yet open, please look forward to it~'))