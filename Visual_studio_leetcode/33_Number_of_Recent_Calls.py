class RecentCounter:
    def __init__(self):
        self.records = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.records.append(t)
        while self.records[self.start] < t - 3000:
            self.start += 1
        return len(self.records) - self.start


# Simulating input execution
operations = ["RecentCounter", "ping", "ping", "ping", "ping"]
arguments = [[], [1], [100], [3001], [3002]]

result = []
obj = None  # Placeholder for RecentCounter instance

for op, arg in zip(operations, arguments):
    if op == "RecentCounter":
        obj = RecentCounter()  # Create an instance
        result.append(None)  # Append None for constructor
    elif op == "ping":
        output = obj.ping(arg[0])  # Call ping() with argument
        result.append(output)

print(result)  # Expected Output: [None, 1, 2, 3, 3]


# time complexity per call is O(1) amortized.
# the space complexity is effectively O(1).
