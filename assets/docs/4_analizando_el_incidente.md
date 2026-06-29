# 4. Analizando el incidente

<p align="center">
  <img src="./assets/images/analizando.png" alt="analizando" width="400">
</p>

## El cambio de rol: De vuelta al SOC

La fase de emulación de adversarios (Red Team) ha concluido. Ahora sabes exactamente lo frágil que es el servidor de Black Mamba porque tú mismo lograste vulnerarlo. Es hora de quitarte el sombrero negro, ponerte el "sombrero azul" y sentarte en tu consola de analista en Tonatiuh qualo.

## Tu Misión: Triage Inicial y Caza de Amenazas

Para esta primera fase de respuesta a incidentes, el cliente nos ha dado acceso a su instancia de Splunk, donde se centralizan todos los registros (logs) del servidor. Sabemos que hubo una filtración de datos en la Dark Web, pero no sabemos ni cuándo ni cómo empezó el ataque real. Tu objetivo aquí es hacer saltar la primera alarma y encontrar al "Paciente Cero".

---

## Análisis

Nos conectamos a `splunk` vía: `http://10.128.176.37:8000/` 

1. ¿Cómo se llama el host que se está analizando?

Realizamos una primera búsqueda total de todos los registros dentro de `splunk´

![splunk-hostname](./assets/images/splunk-hostname.png)

Vemos que el hostname es `brains`

2. ¿Cuántos `sourcetype` de los logs se están analizando?

Para contar cuantos `sourcetype` tenemos, filtramos con: `index=* | stats count by sourcetype`

![splunk-sourcetype_count](./assets/images/splunk-sourcetype_count.png)

Como se ve en la imagen tenemos `3 sourcetype`

3. ¿Cuántos eventos generó el `sourcetype` que más eventos tiene?

Aprovechando la imagen anterior, vemos que el máximo de eventos que generó el `sourcetype` son: `3.816`

4. ¿En que año se generaron más eventos?

Para filtrar por logs por el año utilizaremos el método **strftime**: `index=* | eval year=strftime(_time, "%Y") | stats count by year`

Una vez tenemos filtado por año, usamos el método **count** para contar cuantos eventos existen.

![splunk-year_count](./assets/images/splunk-year_count.png)

Vamos que el año con más eventos totales es: `2024`

5. ¿Cuantos eventos se generaron en ese año?

Aprovechando la misma imagen y filtro, vamos que los eventos totales para el año **2024** es: `4.109`
