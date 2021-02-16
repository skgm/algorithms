"""
Закодируйте любую строку по алгоритму Хаффмана.
"""


from collections import Counter

arr = 'abracadabra'


class Haffman:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def __str__(self):
        return f'{self.left}-{self.right}'


def get_list_of_freq(data):
    count = Counter()
    for item in data:
        count[item] += 1
    freq_dict = count.most_common()
    return freq_dict


def check(data):
    if len(data) == 1:
        cnt = data[0][1]
        return '0' * cnt
    else:
        return False


def tree(data):
    while len(data) > 1:
        key, value = data.pop()
        key_2, value_2 = data.pop()
        node = Haffman(key, key_2)
        data.append((node, value + value_2))
        data.sort(key=lambda x: x[1], reverse=True)
    return data


def code_tree(node, left=True, string=''):
    if type(node) is str:
        return {node: string}
    (left, right) = node.children()
    code_dict = {}
    code_dict.update(code_tree(left, True, string + '0'))
    code_dict.update(code_tree(right, False, string + '1'))
    return code_dict


if arr:
    common_char = get_list_of_freq(arr)
    checking = check(common_char)
    if not checking:
        d = tree(common_char)
        huff_code = code_tree(d[0][0])
        print(' Char\t |\t Huffman code ')
        print('----------------------')
        for k, v in huff_code.items():
            print(f'\t{k}\t -\t {v}')
        code = ''
        for i in arr:
            for k, v in huff_code.items():
                if k == i:
                    code += v
                    break
        print(f'Строка {arr} в закодированном виде: {code}')
    else:
        print(f'Строка {arr} в закодированном виде: {checking}')
else:
    print(f'Пустая строка')
