import collections

class Solution:
    def racecar(self, target: int) -> int:
        queue = collections.deque([(0, 0, 1)])  # (moves, position, speed)
        visited = set()

        while queue:
            moves, position, speed = queue.popleft()

            if position == target:
                return moves 

            if (position, speed) in visited:
                continue
            else:
                visited.add((position, speed))

                # Move forward
                queue.append((moves + 1, position + speed, speed * 2))

                # Reverse direction if overshooting
                if (position + speed > target and speed > 0) or (position + speed < target and speed < 0):
                    reverse_speed = -1 if speed > 0 else 1
                    queue.append((moves + 1, position, reverse_speed))

# Test the function
solution = Solution()
result = solution.racecar(6)
print(f"Minimum moves to reach target 6: {result}")
