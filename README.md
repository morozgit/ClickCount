# Делает короткую ссылки и считает количество переходов по ней
## Для запуска скрипта 

1. ### Установите python
   
    #### Для Linux введите в терминале
    ```
    sudo apt-get install python3
    ```
    #### Для Mac OC
    ```
    brew install python3
    ```
2. ### Клонируйте репозиторий

3. ### Зарегистрируйтесь на [сайте](https://app.bitly.com/Bn55hH2ctPw/bitlinks/3pg5ZpS/details) и получите токен. 
    #### Для простоты получения, регистрируйтесь через e-mail.

4. ### В терминале перейдите в папку с репозиторием
5. ### Установите библиотеки с помощью команды
    ```python 
    pip3 install -r requirements.txt
    ```

1. ### С помощью команды запишите свой токен в файл
    ```python
    echo BITLY_TOKEN=ваш токен > .env
    ```
1. ### Запустите скрипт и передайте в виде аргумента вашу ссылку
    ```python
    python3 main.py ваша ссылка
    ```
    #### Если передать полную ссылку, то результатом будет короткая. 

    #### Если передать короткую ссылку, то результатом будет число кликов по ней. 