import pdfplumber

dict = {'(cid:211)': 'У', '(cid:210)': 'Т', '´': 'В', '¯': 'Е', '—': 'Р', '˘': 'Ж', '˜': 'Д', '˝': 'Н', '˛': 'О',
        'ˇ': 'П', '(cid:240)': 'р', '(cid:238)': 'о', '(cid:229)': 'е', 'Œ': 'к', '(cid:242)': 'т', '(cid:239)': 'п',
        '(cid:243)': 'у', '(cid:247)': 'ч', 'Æ': 'б', '(cid:237)': 'н', 'Ø': 'й', '(cid:224)': 'а', '(cid:192)': 'А',
        '.': '.', '(cid:226)': 'в', '1': '1', '5': '5', 'Ł': 'и', '(cid:254)': 'ю', '(cid:255)': 'я', '2': '2',
        '0': '0', '3': '3', 'ª': 'г', 'ˆ': 'Г', '(cid:204)': 'М', '(cid:228)': 'д', 'æ': 'с', '(cid:246)': 'ц',
        'º': 'л', ':': ':', '(cid:236)': 'м', '(cid:190)': '«', 'ß': 'ы', '(cid:244)': 'ф', '(cid:231)': 'з', '¿': '»',
        ',': ',', '9': '9', '¨': 'И', '(cid:252)': 'ь', 'ı': 'х', '˚': 'К', '4': '4', '(cid:221)': 'Э',
        '(cid:253)': 'э', '6': '6', '`': 'Б', '-': '-', 'ł': 'ш', '(cid:212)': 'Ф', '(cid:216)': 'Ш', '(cid:22)': '—',
        '(': '(', ')': ')', '(cid:209)': 'С', '(cid:219)': 'Ы', '(cid:213)': 'Х', '(cid:215)': 'Ч', '…': 'ё', '˙': 'З',
        'ø': 'щ', '¸': 'Л', '(cid:230)': 'ж', '7': '7', '8': '8', '(cid:214)': 'Ц', 'h': 'h', 't': 't', 'p': 'p',
        '/': '/', 'w': 'w', 'u': 'u', 'm': 'm', 'n': 'n', 'o': 'o', 'v': 'v', 'r': 'r', '(cid:223)': 'Я',
        '(cid:222)': 'Ю', 'C': 'С', '*': '*', '(cid:21)': '–', 'I': 'I', ';': ';', 'V': 'V', 'a': 'a', 'b': 'b',
        'c': 'c', '̸': '!', '=': '=', '[': '[', ']': ']', '?': '?', 'x': 'x', '+': '+', '∗': '*', '(cid:220)': 'Ь',
        '−': '−', 'A': 'A', 'd': 'd', 'e': 'e', '·': '·', 'B': 'B', '≥': '≥', 'O': 'О', '(cid:24)': '~',
        '(cid:159)': '§', 'N': 'N', '(cid:0)': '-'}
with pdfplumber.open("Аналитическая_геометрия_Задавальник.pdf") as pdf:
    pages = [page.extract_text() for page in pdf.pages]
text = '\n'.join(pages)
index = 0
word = []
all_words = []
all_words_copy = []
while index <= len(text) - 1:
    if text[index] == " " or text[index] == "\n":
        index += 1
        all_words.append(word)
        word = []
    else:
        if index < len(text) - 5:
            if text[index] == '(' and text[index + 1:index + 5] == 'cid:':
                slice = text[index:index + 5]
                index_slice = index + 5
                while text[index_slice] != ')':
                    slice += text[index_slice]
                    index_slice += 1
                slice += ')'
                index += len(slice) - 1
            else:
                slice = text[index]
        else:
            slice = text[index]
        index += 1
        word.append(slice)
flag = True
all_words_copy = [[j for j in i] for i in all_words]
for i in range(len(all_words)):
    for j in range(len(all_words[i])):
        if all_words[i][j] in dict:
            all_words[i][j] = dict[all_words[i][j]]
for i in range(0, len(all_words)):
    flag = False
    print(all_words[i])
    for j in range(len(all_words[i])):
        if not all_words_copy[i][j] in dict:
            flag = True
    if flag is True:
        string = input()
    else:
        continue
    for j in range(len(all_words[i])):
        if not all_words_copy[i][j] in dict:
            dict[all_words_copy[i][j]] = string[j]
            all_words[i][j] = dict[all_words[i][j]]
    for i in range(len(all_words)):
        for j in range(len(all_words[i])):
            if all_words[i][j] in dict:
                all_words[i][j] = dict[all_words[i][j]]
    print(dict)
for i in range(len(all_words)):
    all_words[i] = "".join(all_words[i])
print(all_words)
dict_of_tasks = {}
current = 0
index = 0
all = 0
while index < len(all_words) - 2:
    if all_words[index + 1] == 'неделя':
        if all_words[index] == '1':
            all += 1
            dict_of_tasks[str(all) + ' задание'] = {}
        dict_of_tasks[str(all) + ' задание'][all_words[index] + ' ' + all_words[index + 1]] = []
        current = all_words[index]
        index += 3
    elif all_words[index + 2][:2] == 'ЗА' or all_words[index + 2][:2] == 'Со' or all_words[index] == '*':
        current = 0
        index += 1
    else:
        if current != 0:
            if all_words[index][-1] in (';', '.'):
                all_words[index] = all_words[index][:-1]
            if all_words[index] != 'C:':
                if all_words[index][0] not in '0123456789Т' or ((all_words[index - 1][0] not in '0123456789Т') and all_words[index - 1] != 'С:'):
                    dict_of_tasks[str(all) + ' задание'][current + ' неделя'][-1] += ' ' + all_words[index]
                else:
                    if all_words[index].count(';') > 0:
                        dict_of_tasks[str(all) + ' задание'][current + ' неделя'].extend(all_words[index].split(';'))
                    else:
                        dict_of_tasks[str(all) + ' задание'][current + ' неделя'].append(all_words[index])
        index += 1
print(dict_of_tasks)
