# UI Automation Testing Framework

## Описание

Этот проект содержит автоматизированные UI-тесты для веб-приложения Saucedemo (https://www.saucedemo.com/). Написан на Python с использованием паттерна Page Object Model для поддержки и масштабируемости.

## Технологии и инструменты

- Python
- Pytest
- Selenium WebDriver
- Allure
- Docker
- GitHub Actions

## Инструкция по запуску

### Предварительные требования:
- Python 3.11+
- Браузер Chrome или Firefox (драйверы установятся автоматически)

### Быстрый старт:

1. Установите зависимости
   pip install -r requirements.txt

3. (Опционально) Настройте браузер в файле src/data/config.json:
   {
     "browser": "chrome"
   }
   Доступные варианты: chrome, firefox

4. Запустите тесты
   
   Без отчета:
   pytest
   
   С отчетом Allure:
   pytest -n auto --alluredir=./allure-results

5. Откройте Allure-отчет
   allure serve allure-results

## Запуск через Docker

docker-compose up --build

## Примеры тестов

Проект покрывает следующий функционал:

- Авторизация (позитивные и негативные сценарии)
- Добавление товаров в корзину
- Удаление товаров из корзины
- Оформление заказа
