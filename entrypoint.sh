#!/bin/sh

# 调试信息
echo "=== 网易云音乐解析器启动 ==="
echo "当前用户: $(whoami)"
echo "当前目录: $(pwd)"
echo "Python版本: $(python3 --version)"

# 如果设置了NETEASE_COOKIE环境变量，则写入到cookie.txt文件作为备份
if [ -n "$NETEASE_COOKIE" ]; then
    echo "检测到NETEASE_COOKIE环境变量，写入cookie.txt作为备份..."
    echo "$NETEASE_COOKIE" > /app/cookie.txt
    echo "Cookie已写入文件"
else
    echo "未检测到NETEASE_COOKIE环境变量，将使用现有的cookie.txt文件"
    if [ -f "/app/cookie.txt" ]; then
        echo "找到现有的cookie.txt文件"
    else
        echo "警告: 未找到cookie.txt文件且未设置NETEASE_COOKIE环境变量"
    fi
fi

# 启动应用
echo "启动应用..."
echo "参数: --level ${LEVEL:-lossless} --mode ${MODE:-api} --url ${URL:-''}"
python3 main.py --level "${LEVEL:-lossless}" --mode "${MODE:-api}" --url "${URL:-''}"
