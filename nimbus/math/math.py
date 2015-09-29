

def interpolate(g1, g2, g, d1, d2):
    d = d1 + (d2 - d1) * ((g - g1) / (g2 - g1))
    return d


def interpolate_from_table(value, table, g_col, d_col,
                           extrapolate_min=False, extrapolate_max=False):
    min_tuple = table[0]
    max_tuple = table[-1]
    if min_tuple[g_col] < value < max_tuple[g_col]:
        index = next(i for i, v in enumerate(table) if (v[g_col] > value))
        g1 = table[index - 1][g_col]
        g2 = table[index][g_col]
        g = value
        d1 = table[index - 1][d_col]
        d2 = table[index][d_col]
        interpolated_value = interpolate(g1, g2, g, d1, d2)
    elif value <= min_tuple[g_col]:
        interpolated_value = min_tuple[d_col]
    else:
        interpolated_value = max_tuple[d_col]
    return interpolated_value


def goal_seek(function, bound1, bound2, goal, max_iterations, tolerance):
    a = bound1
    b = bound2
    if min(function(a), function(b)) < goal < max(function(a), function(b)):
        for i in range(max_iterations):
            c = (a + b) / 2.0
            solve_a = function(a)
            y_a = (solve_a / goal) - 1.0
            solve_c = function(c)
            y_c = (solve_c / goal) - 1.0
            if abs(b - a) / 2.0 < tolerance:  # Solution Found
                return c
            elif y_a * y_c < 0.0:
                b = c
            else:
                a = c  # New Interval
    return
