import os
from typing import Dict, Optional

class CookieManager:
    def __init__(self, cookie_file: Optional[str] = None):
        if cookie_file is None:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            cookie_file = os.path.join(script_dir, 'cookie.txt')
        self.cookie_file: str = cookie_file

    def read_cookie(self) -> str:
        # 优先从环境变量读取cookie
        env_cookie = os.getenv('NETEASE_COOKIE')
        if env_cookie:
            print("使用环境变量中的cookie配置")
            return env_cookie.strip()
        
        # 如果环境变量不存在，则从文件读取（向后兼容）
        try:
            with open(self.cookie_file, 'r', encoding='utf-8') as f:
                print(f"使用文件 {self.cookie_file} 中的cookie配置")
                return f.read().strip()
        except FileNotFoundError:
            print(f"警告: 未找到cookie文件 {self.cookie_file}，且未设置环境变量 NETEASE_COOKIE")
            return ""
        except Exception as e:
            print(f"读取cookie文件时出错: {e}")
            return ""

    @staticmethod
    def parse_cookie(text: str) -> Dict[str, str]:
        if not text:
            return {}
        cookie_ = [item.strip().split('=', 1) for item in text.strip().split(';') if item.strip()]
        cookie_ = {k.strip(): v.strip() for k, v in cookie_ if len([k, v]) == 2}
        return cookie_
