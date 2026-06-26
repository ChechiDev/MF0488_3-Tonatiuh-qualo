# Detección del incidente

<p align="center">
  <img src="./assets/images/analizando.png" alt="analizando" width="400">
</p>

## Reconstruyendo la Kill Chain

¡Buen trabajo en la detección inicial! Ya tenemos nuestras primeras piezas de evidencia y sabemos qué binarios e IPs estuvieron involucrados. Sin embargo, un hash o una IP aislada no le sirven al CEO de Black Mamba. Necesitamos la historia completa.

## Tu Misión: Análisis Profundo y Línea de Tiempo

En esta tarea, tu objetivo es realizar la correlación de eventos. Debes rastrear los pasos del atacante desde ese primer indicio hasta la exfiltración final y la toma de control del sistema operativo. Vamos a reconstruir la Kill Chain (Cadena de Ataque).

---

## Detección

1. ¿Cómo se llama el usuario que se creó durante la explotación?

Realizamos una primera búsqueda sobre los eventos en `splunk` para buscar el user: `index=* *new user*`

<p align="center">
  <img src="./assets/images/splunk-id12.png" alt="splunk-id12" width="600">
</p>

Vemos que los eventos mostrados, muestran que hay dos usuarios sospechosos (id=11 y id=12) que se crean a sí mismos, lo cual es el comportamiento exacto del exploit `CVE-2024-27198`, algo curioso.

Pero con la anterior búsqueda, no hemos obtenido aún el nombre del usuario creado. Ahora buscaremos por usuarios nuevos creados: `index=* *new user*`

<p align="center">
  <img src="./assets/images/splunk-eviluser.png" alt="eviluser" width="600">
</p>

Hemos encontrado el usuario creado: `eviluser`

2. ¿Cuándo se creó el usuario?

Accedemos a la información del evento:

<p align="center">
  <img src="./assets/images/splunk-event_created.png" alt="splunk-event_created" width="600">
</p>

Extraemos la fecha de cuando se creó: `Jul  4 22:32:37` 

3. ¿Cuál es su `punct`?



4. ¿Qué tipo de shell se creó?



5. ¿Cuál es el nombre del paquete malicioso instalado en el servidor?



6. ¿Cuál es la versión del paquete?



7. ¿A qué hora se emepzó a instalar el paquete?



8. ¿Cuál es el nombre del plugin que se instaló?



9. ¿Cuál es el source del evento del plugin?



10. ¿Desde que IP entró el atacante?



11. ¿Cuál es la Public Key por la que accedió el atacante?
