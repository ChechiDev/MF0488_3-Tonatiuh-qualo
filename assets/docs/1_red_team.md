# Red Team

Para atrapar a un cibercriminal, primero debes entender cómo opera. La dirección de **Nebula Inc.** ha firmado las Reglas de Enfrentamiento (RoE) y ha autorizado a nuestro equipo en **Tonatiuh** qualo para realizar una prueba de explotación activa y ofensiva contra su servidor de producción.

Durante esta fase, dejarás temporalmente tu puesto en el **SOC**, te pondrás el "sombrero negro" y actuarás como el atacante. Vamos a recrear la intrusión para descubrir de primera mano las debilidades estructurales del sistema.

![red_team_flow](./assets/images/red_team_flow.svg)

## Objetivo Final

El propósito de esta fase no es solo "hackear por hackear". El objetivo real es comprender la cadena del ataque para que, cuando pases a la fase defensiva (Blue Team), sepas exactamente qué estás buscando.

### Regla de Oro del Red Team:

Un atacante silencioso no deja notas, pero un buen auditor documenta cada paso.

**Anota todos los comandos que ejecutes, los exploits que utilices y toma capturas de pantalla de tus accesos**. Necesitarás esta información técnica (tu WriteUp) como evidencia vital para redactar tu Informe Final de Auditoría.

*¡Prepara tu terminal, despliega tus herramientas ofensivas y que comience la intrusión!*

---

## Red Team

Establecemos conexión con la **VM** de **THM**, que en este caso nos da la **IP** `10.130.185.84`

Comprobamos conexión:

```bash
┌──(kali㉿kali)-[~]
└─$ ping -c 4 10.130.185.84                     
PING 10.130.185.84 (10.130.185.84) 56(84) bytes of data.
64 bytes from 10.130.185.84: icmp_seq=1 ttl=62 time=39.2 ms
64 bytes from 10.130.185.84: icmp_seq=2 ttl=62 time=31.8 ms
64 bytes from 10.130.185.84: icmp_seq=3 ttl=62 time=32.6 ms
64 bytes from 10.130.185.84: icmp_seq=4 ttl=62 time=31.8 ms

--- 10.130.185.84 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 31.775/33.830/39.177/3.102 ms
```

Realizamos un scan con `Nmap` para ver qué servicios y puertos estan abiertos.

```bash
┌──(kali㉿kali)-[~]
└─$ nmap -sS -p- 10.130.185.84
Starting Nmap 7.95 ( https://nmap.org ) at 2026-06-22 04:55 EDT
Nmap scan report for 10.130.185.84
Host is up (0.036s latency).
Not shown: 65531 closed tcp ports (reset)
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
46229/tcp open  unknown
50000/tcp open  ibm-db2

Nmap done: 1 IP address (1 host up) scanned in 33.70 seconds
```

Después de realizar el scan, podemos ver que los puertos `22, 80, 46229 y 50000` están abiertos


