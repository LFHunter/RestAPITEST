
FROM python:3.11

# 在容器內建立一個 /app 資料夾，並切換到該資料夾
WORKDIR /app

# 将应用代码复制到镜像中（根据需要修改）
COPY . /app/

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH=/app


LABEL maintainer="aaaa_email@example.com"

# 安裝 Python 依賴
COPY requirements.txt .
RUN python3 --version && pip3 --version
RUN pip3 install -r requirements.txt



# 默认命令（根据需要修改）
# CMD pytest --html=MarketstackAPITest_Proj/report.html MarketstackAPITest_Proj/Testcases/test_historical_api.py
CMD pytest --alluredir=reports MarketstackAPITest_Proj/Testcases/test_historical_api.py


