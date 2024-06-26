import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def put(self, priority, item):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def get(self):
        return heapq.heappop(self._queue)[::2]

    def empty(self):
        return len(self._queue) == 0
