class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел


class Stack:
    """
    Основной класс для стека
    """
    def __init__(self):
        self.end = None  # ссылка на конец стека

    def is_empty(self):
        """
        Проверка, пуст ли стек
        """
        return self.end is None

    def push(self, val):
        """
        Добавление элемента val в конец стека
        """
        new_node = Node(val) 
        if self.end is not None:
            new_node.pref = self.end
        self.end = new_node

    def pop(self):
        """
        Возвращение последнего элемента из стека с удалением его из стека
        """
        if self.is_empty():
            raise IndexError("Стек пуст")

        val = self.end.data
        self.end = self.end.pref
        return val

    def print(self):
        """
        Вывод на печать содержимого стека
        """
        if self.is_empty():
            print("Стек пуст")
            return

        current = self.end
        while current is not None:
            print(current.data, end=", " if current.pref is not None else "\n")
            current = current.pref

# Пример использования
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

stack.print()

print("Извлеченный элемент:", stack.pop())
stack.print()

stack.push(4)
stack.print()