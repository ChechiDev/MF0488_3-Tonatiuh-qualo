# Introducción

Trabajas como Analista de Ciberseguridad (Respuesta a Incidentes) en el Centro de Operaciones de Seguridad (SOC) de Tonatiuh qualo, un Proveedor de Servicios de Seguridad Gestionados (MSSP) de primer nivel. Tu equipo se encarga de monitorizar, detectar y responder a las ciberamenazas que acechan a la infraestructura de sus clientes.

![ir_lifecycle](./assets/images/ir_lifecycle.svg)

Esta mañana, tu gerente de incidentes te ha asignado un ticket de máxima prioridad. El departamento de IT de uno de sus clientes principales ha enviado una solicitud urgente de investigación tras detectar anomalías en uno de sus servidores críticos.

<div style="border-left: 3px solid #444444; padding-left: 12px;">

**De**: Dpto. de IT - Operaciones de Infraestructura

**Para**: SOC Incident Response - Tonatiuh qualo

**Asunto**: URGENTE - Archivos sospechosos y posible Ransomware en Servidor

*Equipo de Tonatiuh qualo*,

*Necesitamos su asistencia inmediata. Nuestro servicio de monitorización externa acaba de notificarnos que múltiples archivos confidenciales, pertenecientes a los directorios de usuarios de nuestro servidor principal, han sido publicados y exfiltrados en un foro de la Dark Web.*

*Actualmente, el servidor en cuestión está encendido y parece funcionar correctamente en cuanto a rendimiento operativo, lo que nos indica que la intrusión original pasó completamente desapercibida en su momento.*

*Nos preocupa enormemente que la amenaza inicial haya dejado puertas traseras y siga activa dentro de nuestra red. Necesitamos que realicen un análisis forense exhaustivo de los registros históricos del sistema en Splunk para determinar exactamente cómo lograron entrar, qué ocurrió y cerrar cualquier brecha persistente.*

</div>

## Misión Analista

Tu gerente te ha proporcionado acceso al SIEM corporativo (Splunk), donde ya se han ingerido todos los logs del servidor afectado (Sysmon, eventos de seguridad de Windows y tráfico de red).

Dado que el daño en los archivos ya es visible, nos encontramos en un escenario claro de post-explotación. Tu labor como analista forense es examinar el servidor e identificar las huellas del atacante.

Tus objetivos para este laboratorio son:

- **Analizar** los eventos en Splunk para reconstruir la línea de tiempo del incidente.
- **Identificar el malware**: Descubrir qué proceso o binario fue el responsable de modificar las extensiones de los archivos.
- **Rastrear las acciones post-explotación**: Determinar qué comandos ejecutó el atacante una vez dentro del sistema y si logró establecer algún mecanismo de persistencia.
- Elaborar el Informe de Hallazgos: Redactar un reporte técnico claro detallando el vector de ataque y las recomendaciones de mitigación para el cliente.

---

### URL Defang

```bash
hxxps[://]tryhackme[.]com/jr/25FOAP7810195046037_Tonatiuh_qualo_mf0488
```


---

## Contenido
- [Red Team](#red-team)

---

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

```bash
┌──(kali㉿kali)-[~]
└─$ nmap -sC -sV -p 22,80,46229,50000 10.129.157.89
Starting Nmap 7.95 ( https://nmap.org ) at 2026-06-22 06:34 EDT
Nmap scan report for 10.129.157.89
Host is up (0.037s latency).

PORT      STATE  SERVICE VERSION
22/tcp    open   ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 fa:6d:30:2f:35:99:47:dc:85:98:63:9e:2f:05:6d:1c (RSA)
|   256 9c:51:ad:13:f5:f4:2d:86:31:2f:22:fe:8c:c7:b6:36 (ECDSA)
|_  256 28:cf:0c:59:67:96:3c:36:c3:3c:62:a1:e4:a2:93:88 (ED25519)
80/tcp    open   http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Maintenance
|_http-server-header: Apache/2.4.41 (Ubuntu)
46229/tcp closed unknown
50000/tcp open   http    Apache Tomcat (language: en)
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: TeamCity Maintenance &mdash; TeamCity
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.36 seconds
```

Después de realizar el scan, podemos ver que los puertos `22, 80, 46229 y 50000` están abiertos

Accedemos al puerto `50000` via `http` y nos encontramos con un formulario de acceso de usuario.

![task1-landing_teamcity](./assets/images/task1-landing_teamcity.png)




---

