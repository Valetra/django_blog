# Указывает Docker использовать официальный образ python 3 с dockerhub в качестве базового образа
FROM python:3.12.0a6-alpine3.17
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1
ENV LIBRARY_PATH=/lib:/usr/lib
# Устанавливает рабочий каталог контейнера — "app"
WORKDIR /app
# Копирует все файлы из нашего локального проекта в контейнер
ADD . /app
# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
RUN apk add build-base jpeg-dev zlib-dev
RUN pip install -r requirements.txt
RUN python manage.py migrate