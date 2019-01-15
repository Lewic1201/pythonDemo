'''
Created on 2018-12-17

@author: li_panfeng
'''


class BinaryTree:
    def __init__(self, rootObj):
        self.root = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            print('The leftChild is not None.You can not insert')

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            print('The rightChild is not None.You can not insert')


class BinaryTreeList():
    def biTree(self, data, left, right):
        return [data, left, right]

    def is_empty_BiTree(self, bitree):
        return bitree == []

    def root(self, bitree):
        return bitree[0]

    def leftch(self, bitree):
        return bitree[1]

    def rightch(self, bitree):
        return bitree[2]

    def set_root(self, bitree, data):
        bitree[0] = data

    def set_leftch(self, bitree, left):
        bitree[1] = left

    def set_rightch(self, bitree, right):
        bitree[2] = right


if __name__ == '__main__':
    r = BinaryTree('a')
    print('root:', r.root, ';', 'leftChild:', r.leftChild, ';', 'rightChild:', r.rightChild)
    r.insertLeft('b')
    print('root:', r.root, ';', 'leftChild:', r.leftChild, ';', 'rightChild:', r.rightChild)
    print('root:', r.root, ';', 'leftChild.root:', r.leftChild.root, ';', 'rightChild:', r.rightChild)
