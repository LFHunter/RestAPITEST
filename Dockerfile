
# 使用官方的 Ubuntu 基础镜像
FROM ubuntu:22.04

# 在容器內建立一個 /app 資料夾，並切換到該資料夾
WORKDIR /app

# 将应用代码复制到镜像中（根据需要修改）
COPY . /app/

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH=/app

# 设置维护者信息（可选）
LABEL maintainer="your_email@example.com"

# 更新系统并安装必要的工具 ,不同 RUN 指令彼此是獨立的環境，工作路徑不會自動沿用
RUN apt-get update && \
    apt-get install -y software-properties-common curl && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.12 python3.12-venv  && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 设置 Python3.12 为默认的 python3 和 pip ,優先序給 1
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1 && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12

# 验证 Python 和 Pip 版本（可选）
RUN python3 --version && pip3 --version

RUN pip3 install --no-cache-dir -r requirements.txt



# 默认命令（根据需要修改）
CMD pytest --html=MarketstackAPITest_Proj/report.html MarketstackAPITest_Proj/Testcases/test_historical_api.py

