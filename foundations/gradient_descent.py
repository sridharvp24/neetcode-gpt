class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> int | float:
        x = float(init)
        for _ in range(iterations):
            x = x - learning_rate * (2 * x)
        return int(x) if iterations == 0 and isinstance(init, int) else round(x, 5)