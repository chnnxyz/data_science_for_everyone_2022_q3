# Tarea: tres problemas tipicos de entrevista

Todos los problemas aqui marcados deben ser declarados dentro de funciones 

## FizzBuzz
Dado un entero `n`, para cada `i < n` regresa un string y guardalo en un array con las siguientes condiciones

- `answer[i] == "FizzBuzz"` si `i` es divisible entre 3 y 5.
- `answer[i] == "Fizz"` si `i` es divisible entre 3.
- `answer[i] == "Buzz"` if `i` is divisible by 5.
- `answer[i] == i` (como string) si no se cumple ninguna condición

Tip: investiga el operador "modulo" `%`

## Contador de palabras

Para el string:
```
pepe pecas pica papas con un pico pica papas pepe pecas
```

Generar una funcion cuyo resultado permita saber cuantas veces se repite cada palabra.

Tip: investiga el método String.split()

## Verificador de palíndromos

Un palíndromo es una frase que, ignorando espacios, se lee igual al derecho y al revés (sin importar espacios ni capitalización)

Generar una función que tome un string y regrese True si es palíndromo y False si no.

Ej:
```python
>>> palindrome_checker('Anita Lava La Tina')
True
>>> palindrome_checker('Doctor Psiquiatra')
False
```
Tips:
- Investiga el método `String.split()`
- Investiga el método `List.join()`
- Investiga el método `String.replace()`
- Recuerda como lidiar con capitalización.