import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .metodos.Capitulo_1 import biseccion, regla_falsa, punto_fijo, newton, secante, raices_multiples
from .metodos.Graficas import graficar_intervalos, graficar_punto_fijo, graficar_newton, graficar_secante, \
    graficar_raices_multiples, graficar_polinomio, graficar_tramos_lineal

from .metodos.Capitulo_2 import jacobi, gauss_seidel, sor
from .metodos.Capitulo_3 import vandermonde, newton_interpolante, lagrange, spline_lineal


def index(request):
    return render(request, 'index.html')


def capitulo_1(request):
    # Generador de menus:
    metodos = [
        {'id': 'biseccion', 'nombre': 'Bisección'},
        {'id': 'regla_falsa', 'nombre': 'Regla Falsa'},
        {'id': 'punto_fijo', 'nombre': 'Punto Fijo'},
        {'id': 'newton', 'nombre': 'Newton'},
        {'id': 'secante', 'nombre': 'Secante'},
        {'id': 'raices_multiples', 'nombre': 'Raíces Múltiples'},
    ]

    return render(request, 'capitulo_1.html', context={'metodos': metodos})


def extraer_parametros_comunes(request):
    funcion = request.POST.get('funcion')
    tolerancia = float(request.POST.get('tolerancia'))
    max_iter = int(request.POST.get('max_iter'))
    return funcion, tolerancia, max_iter


@csrf_exempt
def metodos_capitulo_1(request):
    metodo = request.POST.get('metodo')
    funcion = request.POST.get('funcion')
    tolerancia = float(request.POST.get('tolerancia'))
    max_iter = int(request.POST.get('max_iter'))
    try:
        tabla = None
        if metodo == "biseccion":
            a = float(request.POST.get('a'))
            b = float(request.POST.get('b'))
            tabla = biseccion(funcion, a, b, tolerancia, max_iter)
        elif metodo == "regla_falsa":
            a = float(request.POST.get('a'))
            b = float(request.POST.get('b'))
            tabla = regla_falsa(funcion, a, b, tolerancia, max_iter)
        elif metodo == "punto_fijo":
            funcion_g = request.POST.get('funcion_g')
            x_0 = float(request.POST.get('x_0'))
            tabla = punto_fijo(funcion, funcion_g, x_0, tolerancia, max_iter)
        elif metodo == "newton":
            x_0 = float(request.POST.get('x_0'))
            tabla = newton(funcion, x_0, tolerancia, max_iter)
        elif metodo == "secante":
            x_0 = float(request.POST.get('x_0'))
            x_1 = float(request.POST.get('x_1'))
            tabla = secante(funcion, x_0, x_1, tolerancia, max_iter)
        elif metodo == "raices_multiples":
            x_0 = float(request.POST.get('x_0'))
            tabla = raices_multiples(funcion, x_0, tolerancia, max_iter)
        return JsonResponse({'tabla': tabla})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
def informe_capitulo_1(request):
    funcion = request.POST.get('funcion')
    tolerancia = float(request.POST.get('tolerancia'))
    max_iter = int(request.POST.get('max_iter'))

    a = float(request.POST.get('a'))
    b = float(request.POST.get('b'))
    x_0 = float(request.POST.get('x_0'))
    x_1 = float(request.POST.get('x_1'))
    funcion_g = request.POST.get('funcion_g')

    tabla1 = biseccion(funcion, a, b, tolerancia, max_iter)
    tabla2 = regla_falsa(funcion, a, b, tolerancia, max_iter)
    tabla3 = punto_fijo(funcion, funcion_g, x_0, tolerancia, max_iter)
    tabla4 = newton(funcion, x_0, tolerancia, max_iter)
    tabla5 = secante(funcion, x_0, x_1, tolerancia, max_iter)
    tabla6 = raices_multiples(funcion, x_0, tolerancia, max_iter)

    tablas = [tabla1, tabla2, tabla3, tabla4, tabla5, tabla6]

    # Buscamos el mejor
    metodos = ["Biseccion", "Regla Falsa", "Punto Fijo", "Newton", "Secante", "Raices Multiples"]
    errores = []
    for tabla_indice in range(len(tablas)):
        ultimo = tablas[tabla_indice][-1]
        errores.append({tabla_indice: ultimo["error"]})

    menor = min(errores, key=lambda diccionario: list(diccionario.values()))
    menor_indice = list(menor.keys())[0]
    return JsonResponse({'tabla': tablas, 'mejor': metodos[menor_indice], 'valor': menor[menor_indice]})


def capitulo_2(request):
    metodos = [
        {'id': 'jacobi', 'nombre': 'Jacobi'},
        {'id': 'gauss_seidel', 'nombre': 'Gauss-Seidel'},
        {'id': 'sor', 'nombre': 'SOR'},
    ]
    return render(request, 'capitulo_2.html', context={'metodos': metodos})


@csrf_exempt
def metodos_capitulo_2(request):
    tabla = None
    radio_espectral = None

    metodo = request.POST.get('metodo')
    matriz = request.POST.get('matriz_A')
    vector = request.POST.get('vector_B')
    x_0 = request.POST.get('vector_inicial')
    tolerancia = float(request.POST.get('tolerancia'))
    max_iter = int(request.POST.get('max_iter'))

    if metodo == "jacobi":
        tabla, radio_espectral = jacobi(matriz, vector, x_0, tolerancia, max_iter)
    elif metodo == "gauss_seidel":
        tabla, radio_espectral = gauss_seidel(matriz, vector, x_0, tolerancia, max_iter)
    elif metodo == "sor":
        relajacion = float(request.POST.get('relajacion'))
        tabla, radio_espectral = sor(matriz, vector, x_0, relajacion, tolerancia, max_iter)

    return JsonResponse({'tabla': tabla, 'radio': radio_espectral})


@csrf_exempt
def informe_capitulo_2(request):
    matriz = request.POST.get('matriz_A')
    vector = request.POST.get('vector_B')
    x_0 = request.POST.get('vector_inicial')
    relajacion = float(request.POST.get('relajacion'))
    tolerancia = float(request.POST.get('tolerancia'))
    max_iter = int(request.POST.get('max_iter'))

    tabla1, radio_espectral1 = jacobi(matriz, vector, x_0, tolerancia, max_iter)
    tabla2, radio_espectral2 = gauss_seidel(matriz, vector, x_0, tolerancia, max_iter)
    tabla3, radio_espectral3 = sor(matriz, vector, x_0, relajacion, tolerancia, max_iter)

    tablas = [tabla1, tabla2, tabla3]
    radios = [radio_espectral1, radio_espectral2, radio_espectral3]

    # Buscamos el mejor
    metodos = ["Jacobi", "Gauss-Seidel", "SOR"]
    errores = []

    for tabla_indice in range(len(tablas)):
        if len(tablas[tabla_indice]) > 0:
            ultimo = tablas[tabla_indice][-1]
            errores.append({tabla_indice: ultimo["error"]})

    if len(errores) > 0:
        menor = min(errores, key=lambda diccionario: list(diccionario.values()))
        menor_indice = list(menor.keys())[0]
        return JsonResponse(
            {'tabla': tablas, 'radio': radios, 'mejor': metodos[menor_indice], 'valor': menor[menor_indice]})
    else:
        return JsonResponse({'tabla': tablas, 'radio': radios, 'mejor': 'Ninguno', 'valor': 100})


def capitulo_3(request):
    metodos = [
        {'id': 'vandermonde', 'nombre': 'Vandermonde'},
        {'id': 'newton_interpolante', 'nombre': 'Newton Interpolante'},
        {'id': 'lagrange', 'nombre': 'Lagrange'},
        {'id': 'spline_lineal', 'nombre': 'Spline Lineal'},
        {'id': 'spline_cubico', 'nombre': 'Spline Cúbico'},
    ]
    return render(request, 'capitulo_3.html', context={'metodos': metodos})


@csrf_exempt
def metodos_capitulo_3(request):
    metodo = request.POST.get('metodo')
    x_str = request.POST.get('punto_x')
    y_str = request.POST.get('punto_y')

    if metodo == "vandermonde":
        polinomio = vandermonde(x_str, y_str)
        return JsonResponse({'polinomio': polinomio})

    if metodo == "newton_interpolante":
        polinomio, expandido = newton_interpolante(x_str, y_str)
        return JsonResponse({'polinomio': polinomio, 'expandido': expandido})

    elif metodo == "lagrange":
        polinomio, expandido = lagrange(x_str, y_str)
        return JsonResponse({'polinomio': polinomio, 'expandido': expandido})

    elif metodo == "spline_lineal":
        tramos, polinomios = spline_lineal(x_str, y_str)
        return JsonResponse({'tramos': tramos, 'polinomios': polinomios})

    return None


@csrf_exempt
def informe_capitulo_3(request):
    matriz = request.POST.get('matriz_A')
    vector = request.POST.get('vector_B')
    x_0 = request.POST.get('vector_inicial')
    relajacion = float(request.POST.get('relajacion'))
    tolerancia = float(request.POST.get('tolerancia'))
    max_iter = int(request.POST.get('max_iter'))

    tabla1, radio_espectral1 = jacobi(matriz, vector, x_0, tolerancia, max_iter)
    tabla2, radio_espectral2 = gauss_seidel(matriz, vector, x_0, tolerancia, max_iter)
    tabla3, radio_espectral3 = sor(matriz, vector, x_0, relajacion, tolerancia, max_iter)

    tablas = [tabla1, tabla2, tabla3]
    radios = [radio_espectral1, radio_espectral2, radio_espectral3]

    # Buscamos el mejor
    metodos = ["Jacobi", "Gauss-Seidel", "SOR"]
    errores = []

    for tabla_indice in range(len(tablas)):
        if len(tablas[tabla_indice]) > 0:
            ultimo = tablas[tabla_indice][-1]
            errores.append({tabla_indice: ultimo["error"]})

    if len(errores) > 0:
        menor = min(errores, key=lambda diccionario: list(diccionario.values()))
        menor_indice = list(menor.keys())[0]
        return JsonResponse(
            {'tabla': tablas, 'radio': radios, 'mejor': metodos[menor_indice], 'valor': menor[menor_indice]})
    else:
        return JsonResponse({'tabla': tablas, 'radio': radios, 'mejor': 'Ninguno', 'valor': 100})


@csrf_exempt
def graficar_view(request):
    metodo = request.POST.get('metodo')
    funcion = request.POST.get('funcion')  # función por defecto
    try:
        if metodo == "biseccion" or metodo == "regla_falsa":
            a = float(request.POST.get('a'))
            b = float(request.POST.get('b'))
            x_m = float(request.POST.get('x_m'))
            imagen = graficar_intervalos(funcion, a, b, x_m)
            return HttpResponse(imagen, content_type='image/png')

        elif metodo == "punto_fijo":
            funcion_g = request.POST.get('funcion_g')
            x_n = float(request.POST.get('x_n'))
            imagen = graficar_punto_fijo(funcion, funcion_g, x_n)
            return HttpResponse(imagen, content_type='image/png')

        elif metodo == "newton":
            x_n = float(request.POST.get('x_n'))
            imagen = graficar_newton(funcion, x_n)
            return HttpResponse(imagen, content_type='image/png')

        elif metodo == "secante":
            x_n = float(request.POST.get('x_n'))
            imagen = graficar_secante(funcion, x_n)
            return HttpResponse(imagen, content_type='image/png')

        elif metodo == "raices_multiples":
            x_n = float(request.POST.get('x_n'))
            imagen = graficar_raices_multiples(funcion, x_n)
            return HttpResponse(imagen, content_type='image/png')
    except Exception as e:
        return HttpResponse(f'Error al graficar: {e}', content_type='text/plain')

    return None


@csrf_exempt
def graficar_view_3(request):
    metodo = request.POST.get('metodo')

    polinomio = request.POST.get('polinomio')
    x_str = request.POST.get('punto_x')
    y_str = request.POST.get('punto_y')
    try:
        if metodo == "vandermonde" or metodo == "newton_interpolante" or metodo == "lagrange":
            imagen = graficar_polinomio(polinomio, x_str, y_str, titulo=metodo)
            return HttpResponse(imagen, content_type='image/png')
        if metodo == "spline_lineal":
            tramos = request.POST.get('tramos')
            imagen = graficar_tramos_lineal(tramos, x_str, titulo=metodo)
            return HttpResponse(imagen, content_type='image/png')

    except Exception as e:
        return HttpResponse(f'Error al graficar: {e}', content_type='text/plain')

    return None
