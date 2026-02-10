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
# File       : start.py
# Time       ：2026.2.9 15:55
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com OR WorkerHMan@gmail.com
# version    ：python 3.9
# Description：
"""
import os
import sys
path = os.path.dirname(os.path.abspath(__file__))
sys.path += [
    path,
]
os.chdir(path)

from main import Host_IP, Host_Port
import uvicorn

if __name__ == '__main__':
    uvicorn.run('main:app', host=Host_IP, port=Host_Port, reload=True, log_level="info")