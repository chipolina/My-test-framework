FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

# Download Allure CLI
RUN wget -O /usr/bin/allure https://github.com/allure-framework/allure2/releases/download/2.15.0/allure-2.15.0.zip \
    && unzip /usr/bin/allure -d /usr/bin/ \
    && chmod +x /usr/bin/allure/bin/allure \
    && rm /usr/bin/allure

CMD ["bash"]
