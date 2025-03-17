class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # ссылка на предыдущий узел


class Queue:
    """
    Основной класс для очереди
    """
    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None    # ссылка на конец очереди

    def is_empty(self):
        """
        Проверка, пуста ли очередь
        """
        return self.start is None

    def push(self, val):
        """
        Добавление элемента val в конец очереди
        """
        new_node = Node(val)
        if self.end is not None:
            self.end.nref = new_node
            new_node.pref = self.end
        self.end = new_node

        if self.start is None:
            self.start = new_node

    def pop(self):
        """
        Возвращение элемента из начала очереди с удалением его из очереди
        """
        if self.is_empty():
            raise IndexError("Очередь пуста")

        val = self.start.data 
        self.start = self.start.nref 

        if self.start is not None:
            self.start.pref = None
        else:
            self.end = None

        return val

    def insert(self, n, val):
        """
        Вставка элемента val между элементами с номерами n-1 и n
        """
        if n < 0:
            raise IndexError("Некорректный индекс")

        new_node = Node(val)

        if n == 0:
            new_node.nref = self.start
            if self.start is not None:
                self.start.pref = new_node
            self.start = new_node
            if self.end is None:
                self.end = new_node
            return

        current = self.start
        index = 0

        while current is not None and index < n - 1:
            current = current.nref
            index += 1

        if current is None:
            raise IndexError("Индекс выходит за пределы очереди")

        new_node.nref = current.nref
        new_node.pref = current
        if current.nref is not None:
            current.nref.pref = new_node
        current.nref = new_node

        if new_node.nref is None:
            self.end = new_node

    def print(self):
        """
        Вывод на печать содержимого очереди
        """
        if self.is_empty():
            print("Очередь пуста")
            return

        current = self.start
        while current is not None:
            print(current.data, end=", " if current.nref is not None else "\n")
            current = current.nref


# Пример использования
queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)

queue.print()

print("Извлеченный элемент:", queue.pop())
queue.print()

queue.insert(1, 4)
queue.print()

queue.push(5)
queue.print()