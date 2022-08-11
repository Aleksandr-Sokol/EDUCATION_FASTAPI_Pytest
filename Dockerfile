# образ на основе которого создаём контейнер
FROM python:3.9.5-alpine

# рабочая директория внутри проекта
WORKDIR /app

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# копируем содержимое текущей папки в контейнер
# COPY ./consumer/ ./config.py ./schema.py .
COPY . .
# CMD [ "python", "run.py" ]
CMD [ "pytest"]


#FROM python:3
## Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
#ENV PYTHONUNBUFFERED 1
## Устанавливает рабочий каталог контейнера — "app"
#WORKDIR /app
## Копирует все файлы из нашего локального проекта в контейнер
#ADD . /app
## Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
#RUN pip install -r requirements.txt