## Ejercicio 1: 

[Solución](hw2/audio.py)


## Ejercicio 2: 

[Solución](hw2/frequency.py)


## Ejercicio 3: 

[Solución](hw2/generator.py)


## Ejercicio 4

Analizar si el sistema es:

* Estático o dinámico
* Lineal o no lineal
* Invariante o variante en el tiempo
* Causal o no causal
* Estable o inestable

a. $y(n) = \cos[x(n)]$

* Estático: solo depende de la muestra presente.
* No lineal.

Debe soportar superposición:

A nivel de entrada: $x(n) = a_1x_1(n)+a_2x_2(n)$

$$
y(n) = \cos[a_1x_1(n)+a_2x_2(n)]
$$

A nivel de salida: $y(n) = a_1y_1(n) +a_2y_2(n)$

$$
y(n) = a_1y_1(n) +a_2y_2(n) \\
y(n) = a_1\cos[x_1(n)] + a_2\cos[x_2(n)]
$$

No son iguales, por lo tanto NO ES LINEAL.

* Invariante en el tiempo: invariante

Debe soportar desplazos en la entrada:

$$
y(n, k) = \cos[x(n-k)]
$$

Y en la salida:

$$
y(n-k) = \cos[x(n-k)]
$$

Son iguales, por lo tanto es INVARIANTE.

* Causal: Es causal, dado que solo depende de muestras actuales
* Estable: Es estable, dado que la función $\cos[\cdot] \to [-1, 1] \in \mathbb{R}$

b. $y(n) = x(n) cos(\omega_0 n)$

* Estático: solo depende de la muestra presente.
* Lineal

A nivel de entrada: $x(n) = a_1x_1(n)+a_2x_2(n)$

$$
y(n) = [a_1x_1(n)+a_2x_2(n)]\cos(\omega_0 n)
$$

A nivel de salida: $y(n) = a_1y_1(n) +a_2y_2(n)$

$$
y(n) = a_1y_1(n) +a_2y_2(n) \\
y(n) = a_1x_1(n)\cos(\omega_0 n) + a_2x_2(n)\cos(\omega_0 n) \\
y(n) = [a_1x_1(n)+a_2x_2(n)]\cos(\omega_0 n) \\
$$

No son iguales, por lo tanto ES LINEAL.

* Invariante en el tiempo

Debe soportar desplazos en la entrada:

$$
y(n, k) = x(n-k)\cos[\omega_0 n]
$$

Y en la salida:

$$
y(n-k) = x(n-k)\cos[\omega_0 (n - k)]
$$

No son iguales, por lo tanto es VARIANTE.

* Causal: Es causal, dado que solo depende de muestras actuales
* Estable

Seleccionando la entrada $x(n)=Au(n)$, para $A \in \mathbb{R}$ constante:

$$
y(n) = Au(n)\cos(\omega_0 n)
$$

la salida estará definida entre: $-A \le y(n) \le A$.

c. $y(n) = \text{Round}[x(n)]$

* Estático: solo depende de la muestra presente.
* No lineal

A nivel de entrada: $x(n) = a_1x_1(n)+a_2x_2(n)$

$$
y(n) = \text{Round}[a_1x_1(n)+a_2x_2(n)]
$$

A nivel de salida: $y(n) = a_1y_1(n) +a_2y_2(n)$

$$
y(n) = a_1y_1(n) +a_2y_2(n) \\
y(n) = \text{Round}[a_1x_1(n)] + \text{Round}[a_2x_2(n)]
$$

No son iguales, por lo tanto, NO ES LINEAL.

* Invariante en el tiempo

Debe soportar desplazos en la entrada:

$$
y(n, k) = \text{Round}[x(n-k)]
$$

Y en la salida:

$$
y(n-k) = \text{Round}[x(n-k)]
$$

Son iguales, por lo tanto, es INVARIANTE.

* Causal: Es causal, dado que solo depende de muestras actuales
* Estable: el operador ROUND solo extrae la parte entera. Para un escalón, estaría definido por $\text{ROUND}[A]$, donde $A$ es una constante real.

d. $y(n) = x(2n)$

* Estático: solo depende de la muestra presente.
* Lineal

A nivel de entrada: $x(n) = a_1x_1(n)+a_2x_2(n)$

$$
y(n) = a_1x_1(2n)+a_2x_2(2n)
$$

A nivel de salida: $y(n) = a_1y_1(n) +a_2y_2(n)$

$$
y(n) = a_1y_1(n) +a_2y_2(n) \\
y(n) = a_1x_1(2n) +a_2x_2(2n)
$$

No son iguales, por lo tanto ES LINEAL.

* Invariante en el tiempo

Debe soportar desplazos en la entrada:

$$
y(n, k) = x(2n-k)
$$

Y en la salida:

$$
y(n-k) = x(2(n-k))
$$

No son iguales, por lo tanto es VARIANTE.

* Causal: Es causal, dado que solo depende de muestras actuales
* Estable
