from queue import Queue

class Buffer:
    def __init__(self, size):
        self.queue = Queue(maxsize=size)

    def put(self, item):
        self.queue.put(item)

    def get(self):
        return self.queue.get()

    def is_full(self):
        return self.queue.full()

    def is_empty(self):
        return self.queue.empty()

    def size(self):
        return self.queue.qsize()