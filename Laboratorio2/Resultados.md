# Resultados del Laboratorio 2

Para este ejemplo utilice los threading y multiprocessing. En realidad, la que se deberia usar es threading o asyncio ya que es un problema de I/O porque se debe consultar la base de datos del API. A continuacion se presentan los resultados. 

## Resultado Threading

El resultado de threading fue mu parecido al multiprocessing y me dio lo siguiente:

150 users check in 2.8377041816711426 seconds

Pero como mencione este metodo es el mas recomendable.

## Resultado Multiprocessing

El resultado de multiprocessing es el siguiente:

150 users check in 2.7220447063446045 second

Es muy parecido a Threading con una leve mejoria.