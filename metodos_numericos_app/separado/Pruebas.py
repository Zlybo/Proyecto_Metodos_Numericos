def error_truncamiento(x_vals, y_vals):
    # Diferencias divididas de orden 3
    def diferencia_dividida_orden3(xs, ys):
        f01 = (ys[1] - ys[0]) / (xs[1] - xs[0])
        f12 = (ys[2] - ys[1]) / (xs[2] - xs[1])
        f23 = (ys[3] - ys[2]) / (xs[3] - xs[2])
        f012 = (f12 - f01) / (xs[2] - xs[0])
        f123 = (f23 - f12) / (xs[3] - xs[1])
        f0123 = (f123 - f012) / (xs[3] - xs[0])
        return f0123

    f123 = diferencia_dividida_orden3(x_vals, y_vals)

    producto = 1
    for xi in x_vals[:-1]:
        producto *= (x_vals[-1] - xi)

    return f123 * producto


# Datos con el nuevo punto agregado
x_vals = [3.0000, 3.6667, 4.3333, 5.0000]
y_vals = [6.7472, 10.7997, 15.8063, 21.7486]

error = error_truncamiento(x_vals, y_vals)
print(f"Error de truncamiento Rn = {error:.4f}")
