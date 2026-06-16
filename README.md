# situ-devops-03 Лаб 3.
Проект демонстрирует базовый observability-стек с метриками и дашбордом.

## Stack
- Flask — веб-приложение со счетчиком посещений
- Redis — хранение состояния (counter)
- Prometheus — сбор метрик
- Grafana — визуализация метрик
- Docker Compose — оркестрация сервисов

## Сервисы
- Flask App	http://localhost:5000
- Prometheus	http://localhost:9090
- Grafana	http://localhost:3000

## Запуск проекта
```
git clone https://github.com/sergeylobaev/situ-devops-06.git
cd situ-devops-06
docker compose up -d --build
```

Визуализация счетчика посещений в Grafana
<img width="1314" height="732" alt="image" src="https://github.com/user-attachments/assets/276301bc-fd82-4dc3-9b89-bf12f0cd4575" />
