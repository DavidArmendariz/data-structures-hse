def calc_rain_water(h):
    n = len(h)
    stack = []
    result = 0
    for i in range(n):
        while len(stack) != 0 and h[stack[-1]] < h[i]:
            last_height = h[stack.pop()]
            if len(stack) == 0:
                break
            left_to_right_boundary_distance = i - stack[-1] - 1
            min_height = min(h[stack[-1]], h[i]) - last_height
            result += left_to_right_boundary_distance * min_height
        stack.append(i)
    return result
