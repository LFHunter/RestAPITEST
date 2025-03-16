
FROM python:3.10

# 在容器內建立一個 /app 資料夾，並切換到該資料夾
WORKDIR /app


# # 安裝 Java（Allure 需要 Java）
# RUN apt-get update && apt-get install -y openjdk-11-jre wget unzip

# # 安裝 Allure
# RUN wget -O allure.zip https://github.com/allure-framework/allure2/releases/latest/download/allure-2.33.0.zip && \
#     unzip allure.zip -d /opt/allure && \
#     rm allure.zip && \
#     ln -s  /opt/allure/allure-2.33.0/bin/allure /usr/local/bin/allure


# 将应用代码复制到镜像中（根据需要修改）
COPY . /app/
RUN ls -l /app/

ENV DEBIAN_FRONTEND=noninteractive



LABEL maintainer="aaaa_email@example.com"

# 安裝 Python 依賴
COPY requirements.txt .
RUN python3 --version && pip3 --version
RUN pip3 install -r requirements.txt



# 默认命令（根据需要修改）
# CMD pytest --html=MarketstackAPITest_Proj/report.html MarketstackAPITest_Proj/Testcases/test_historical_api.py
ENV PYTHONPATH=/app
CMD ls /app && echo 'test123' && pwd && ls -l && pytest --alluredir=reports MarketstackAPITest_Proj/Testcases/test_historical_api.py


