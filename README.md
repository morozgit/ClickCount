# ClickCount

Делает короткую ссылку и считает количество переходов по ней

## Установка 

### Установка python
   
#### Для Linux 
```
sudo apt-get install python3
```
#### Для Mac OC
```
brew install python3
```
## Репозиторий
Клонируйте репозиторий в удобную папку

## Окружение

### Библиотеки

В терминале перейдите в папку с репозиторием

Установите библиотеки с помощью команды
```python 
pip3 install -r requirements.txt
```

### Переменные окружения 
#### Получение токена

* Зарегистрируйтесь на [сайте](https://app.bitly.com/Bn55hH2ctPw/bitlinks/3pg5ZpS/details) и получите токен. Для простоты получения, регистрируйтесь через e-mail.

#### Запись токена
```python
echo BITLY_TOKEN=ваш токен > .env
```
## Запуск 

Передайте в виде аргумента вашу ссылку
```python
python3 main.py ваша ссылка
```
Если передать полную ссылку, то результатом будет короткая. 

Если передать короткую ссылку, то результатом будет число кликов по ней. 