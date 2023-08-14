FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

# Download Allure CLI
RUN wget -O /tmp/allure.zip https://github.com/allure-framework/allure2/releases/download/2.15.0/allure-2.15.0.zip \
    && unzip /tmp/allure.zip -d /usr/bin/ \
    && chmod +x /usr/bin/allure/bin/allure \
    && rm /tmp/allure.zip

CMD ["bash"]
