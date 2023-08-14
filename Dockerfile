FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

RUN apk update && \
    apk add --no-cache openjdk11 maven git && \
    git clone https://github.com/allure-framework/allure2.git && \
    cd allure2 && \
    mvn clean package && \
    mv ./target/allure-* /usr/bin/allure && \
    chmod +x /usr/bin/allure && \
    apk del git maven

CMD ["bash"]
