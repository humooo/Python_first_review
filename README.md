# Первое ревью

## Объязательная часть
#### Шифрование:
>  PYTHONPATH=src python3 encryptor.py encode --cipher {caesar|vigenere|vernam} --key {<'number'>|<'word'>} [--input-file input.txt] [--output-file out.txt] \
> \
Зашифровать входное сообщение с помощью ключа


#### Дешифрование:
>  PYTHONPATH=src python3 encryptor.py decode --cipher {caesar|vigenere|vernam} --key {<'number'>|<'word'>} [--input-file input.txt] [--output-file out.txt] \
> \
Расшифровать входное сообщение, зная шифр и ключ, с которым оно было зашифровано


#### Взлом шифра Цезаря методами частотного анализа:
> PYTHONPATH=src python3 encryptor.py train  --text-file {text.txt} --model-file{model} \
> \
> Проанализировать большой текст(текст Шекспира) и построить языковую модель

> PYTHONPATH=src python3 encryptor.py hack [--input-file input.txt] [--output-file output.txt] --model-file{model} \
> \
> Рассшифровать текст

## Бонусная часть
#### Взлом шифра виженера с помощью индексов совпадений:
> PYTHONPATH=src python3 encryptor.py train  --text-file {text.txt} --model-file{model} \
> \
> Проанализировать большой текст(текст Шекспира) и построить языковую модель

> PYTHONPATH=src python3 encryptor.py hack_vigenere [--input-file input.txt] [--output-file output.txt] --model-file{model} \
> \
> Рассшифровать текст