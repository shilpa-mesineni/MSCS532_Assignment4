class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority  # Lower value means higher priority in min-heap
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __repr__(self):
        return f"(Task ID: {self.task_id}, Priority: {self.priority})"


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        # Add new task at the end of the heap
        self.heap.append(task)
        # Fix the heap property from bottom up
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # Replace the root (min) with the last element
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        # Fix the heap property from top down
        self._heapify_down(0)
        return root

    def decrease_key(self, task_index, new_priority):
        if task_index < 0 or task_index >= len(self.heap):
            return

        # Set new priority and heapify up to maintain heap property
        self.heap[task_index].priority = new_priority
        self._heapify_up(task_index)

    def is_empty(self):
        return len(self.heap) == 0

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index].priority < self.heap[parent_index].priority:
            # Swap if the current node's priority is higher (lower value means higher priority)
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        # Check if left child exists and is smaller
        if left_child < len(self.heap) and self.heap[left_child].priority < self.heap[smallest].priority:
            smallest = left_child

        # Check if right child exists and is smaller
        if right_child < len(self.heap) and self.heap[right_child].priority < self.heap[smallest].priority:
            smallest = right_child

        # If the smallest is not the current node, swap and continue heapifying
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

# Test Case: Create tasks and perform operations on the heap
if __name__ == "__main__":
    # Create a MinHeap instance
    heap = MinHeap()

    # Create some Task instances with task_id, priority, arrival_time, deadline
    task1 = Task(1, 10, "10:00 AM", "12:00 PM")
    task2 = Task(2, 5, "10:30 AM", "12:30 PM")
    task3 = Task(3, 15, "11:00 AM", "01:00 PM")
    task4 = Task(4, 3, "11:30 AM", "01:30 PM")
    task5 = Task(5, 7, "12:00 PM", "02:00 PM")

    # Insert tasks into the heap
    print("Inserting tasks into the heap:")
    heap.insert(task1)
    heap.insert(task2)
    heap.insert(task3)
    heap.insert(task4)
    heap.insert(task5)

    print("Heap after insertion:")
    print(heap.heap)

    # Extract min (lowest priority task) from the heap
    print("\nExtracted Task:", heap.extract_min())

    # Decrease the priority of task3 (task with ID 3)
    print("\nDecreasing priority of Task 3 to 1:")
    heap.decrease_key(2, 1)  # Task 3 now has the highest priority

    print("Heap after decreasing priority of Task 3:")
    print(heap.heap)

    # Extract min again (task3 should be the new minimum)
    print("\nExtracted Task:", heap.extract_min())

    # Check if the heap is empty
    print("\nIs heap empty?", heap.is_empty())

    # Final heap state
    print("Final heap state:")
    print(heap.heap)
