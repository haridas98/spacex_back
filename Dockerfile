   # Используйте официальный образ Python в качестве базового образа
   FROM python:3.11

   # Установите рабочую директорию в контейнере
   WORKDIR /fullx

   # Скопируйте requirements.txt в контейнер
   COPY requirements.txt .

   # Установите зависимости
   RUN pip install --no-cache-dir -r requirements.txt

   # Скопируйте все файлы вашего приложения в контейнер
   COPY . .

   # Указать команду, которая будет запускаться при старте контейнера
   CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
