import string


russian_alphabeth = 'йцукенгшщзхъфывапролджэячсмитьбюё'
russian_alphabeth += 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
arabian_alphabeth = 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي'
symbols = {0: ',', 1: '.', 2: '?', 3: '!', 4: ' '}
symbols_ = {',': 0, '.': 1, '?': 2, '!': 3, ' ': 4}
len_russian_alphabeth = len(russian_alphabeth) // 2
len_arabian_alphabeth = len(arabian_alphabeth)
len_symbols = len(symbols)
len_english_alphabeth = 26
ord_first_arabian_symbol = 1575
