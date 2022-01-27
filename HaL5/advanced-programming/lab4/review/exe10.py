#!/usr/bin/env python

'''
Viết chương trình xây dựng từ điển dạng cây tiền tố, tạo các lớp, xây dựng các
phương thức hợp lý để chương trình có các chức năng như:
    - Thêm 1 từ vào từ điển
    - Xóa 1 từ khỏi từ điển
    - Đếm số từ trong từ điển
    - Tìm kiếm một từ trong từ điển
    - In ra các từ có trong từ điển
    - In ra các từ có tiền tố p (p là tham số)
'''

class Node:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = Node('')

    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = Node(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True
        node.count += 1
