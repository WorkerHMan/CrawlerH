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
# File       : ViewsUtils.py
# Time       ：2026.2.9 18:58
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com OR WorkerHMan@gmail.com
# version    ：python 3.9
# Description：
"""
import re

from pywebio.output import get_scope, clear
from pywebio.session import info as session_info


class ViewsUtils:

    # 自动检测语言返回翻译/Auto detect language to return translation
    @staticmethod
    def t(zh: str, en: str) -> str:
        return zh if 'zh' in session_info.user_language else en

    # 清除前一个scope/Clear the previous scope
    @staticmethod
    def clear_previous_scope():
        _scope = get_scope(-1)
        clear(_scope)

    # 解析抖音分享口令中的链接并返回列表/Parse the link in the Douyin share command and return a list
    @staticmethod
    def find_url(string: str) -> list:
        url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
        return url