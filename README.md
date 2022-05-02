# Первое ревью

### Клонирование репозитория с помощью ssh
В терминале запускайте следующую команду
> git clone git@github.com:humooo/Python_first_review.git

можно заметить, что появилась папка Python_first_review, наберите эти команды
> cd Python_first_review\
> ./build.sh

дальнейшие работы также делайте в том же терминале для каждого случая(ниже приведены примеры и скрины для них)

### Шифрование шифра Цезаря:
>  PYTHONPATH=src python3 encryptor.py encode --cipher caesar --key {number} [--input-file examples/input.txt] [--output-file examples/output.txt] \
> \
Зашифровать входное сообщение с помощью ключа
![](IMG/1.png)


### Дешифрование шифра Цезаря:
>  PYTHONPATH=src python3 encryptor.py decode --cipher caesar --key {number} [--input-file examples/input.txt] [--output-file examples/output.txt] \
> \
Расшифровать входное сообщение, зная ключ, с которым оно было зашифровано
![](IMG/2.png)


### Шифрование шифра Виженера:
>  PYTHONPATH=src python3 encryptor.py encode --cipher vigenere --key {word} [--input-file examples/input.txt] [--output-file examples/output.txt] \
> \
Зашифровать входное сообщение с помощью ключа
![](IMG/3.png)


### Дешифрование шифра Виженера:
>  PYTHONPATH=src python3 encryptor.py decode --cipher vigenere --key {word} [--input-file examples/input.txt] [--output-file examples/output.txt] \
> \
Расшифровать входное сообщение, зная ключ, с которым оно было зашифровано
![](IMG/4.png)


### Шифрование шифра Вернама:
>  PYTHONPATH=src python3 encryptor.py encode --cipher vernam --key {examples/text_key.txt} [--input-file examples/input.txt] [--output-file examples/output.txt] \
> \
Зашифровать входное сообщение с помощью ключа
![](IMG/5.png)


### Дешифрование шифра Вернама:
>  PYTHONPATH=src python3 encryptor.py decode --cipher vernam --key {examples/text_key.txt} [--input-file examples/input.txt] [--output-file examples/output.txt] \
> \
Расшифровать входное сообщение, зная ключ, с которым оно было зашифровано
![](IMG/6.png)

### Построить языковую модель для взлома:

> PYTHONPATH=src python3 encryptor.py train  --text-file examples/text.txt --model-file examples/model.txt \
> \
> Проанализировать большой текст(текст Шекспира) и построить языковую модель


### Взлом шифра Цезаря методами частотного анализа:

> PYTHONPATH=src python3 encryptor.py hack [--input-file examples/input.txt] [--output-file examples/output.txt] --model-file examples/model.txt \
> \
> Рассшифровать текст
![](IMG/7.png)


### Взлом шифра Виженера с помощью индексов совпадений:
> PYTHONPATH=src python3 encryptor.py hack_vigenere [--input-file examples/input.txt] [--output-file examples/output.txt] --model-file examples/model.txt \
> \
> Рассшифровать текст
![](IMG/8.png)

### Стеганография:
> PYTHONPATH=src python3 stegano.py stegano_encode  --start-img {start.png|start.bmp} --encoded-img {encoded.png|encoded.bmp} [--input-file examples/input.txt] \
> \
Шифрование
![](IMG/9.png)
Можно заметить, что фотографии практически ничем не отличаются 


> PYTHONPATH=src python3 stegano.py stegano_encode --encoded-img {encoded.png|encoded.bmp} [--output-file examples/output.txt] \
> \
Расшифрование
![](IMG/10.png)