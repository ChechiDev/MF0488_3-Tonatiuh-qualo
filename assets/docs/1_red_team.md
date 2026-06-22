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

Establecemos conexión con la **VM** de **THM**..

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
└─$ nmap -sS -p- 10.129.157.89
Starting Nmap 7.95 ( https://nmap.org ) at 2026-06-22 07:01 EDT
Nmap scan report for 10.129.157.89
Host is up (0.038s latency).
Not shown: 65531 closed tcp ports (reset)
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
44053/tcp open  unknown
50000/tcp open  ibm-db2

Nmap done: 1 IP address (1 host up) scanned in 26.54 seconds
```

**Scan profundo**: Para detección de versiones y scripts:

```bash
┌──(kali㉿kali)-[~]
└─$ nmap -sC -sV -p- 10.129.157.89
Starting Nmap 7.95 ( https://nmap.org ) at 2026-06-22 07:02 EDT
Nmap scan report for 10.129.157.89
Host is up (0.038s latency).
Not shown: 65531 closed tcp ports (reset)
PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 fa:6d:30:2f:35:99:47:dc:85:98:63:9e:2f:05:6d:1c (RSA)
|   256 9c:51:ad:13:f5:f4:2d:86:31:2f:22:fe:8c:c7:b6:36 (ECDSA)
|_  256 28:cf:0c:59:67:96:3c:36:c3:3c:62:a1:e4:a2:93:88 (ED25519)
80/tcp    open  http     Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Maintenance
44053/tcp open  java-rmi Java RMI
50000/tcp open  http     Apache Tomcat (language: en)
| http-title: Log in to TeamCity &mdash; TeamCity
|_Requested resource was /login.html
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 48.81 seconds
```

Después de realizar el scan, podemos ver:

| Puerto | Estado | Servicio | Versión |
|--------|--------|----------|---------|
| 22     | open   | ssh      | OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 |
| 80     | open   | http     | Apache httpd 2.4.41 |
| 44053  | open   | java-rmi | Java RMI (comunicación interna TeamCity) |
| 50000  | open   | http     | Apache Tomcat  **TeamCity** |

- **Puerto 80**: Página estática de mantenimiento y sin contenido.
- **Puerto 50000**: Panel de login de **JetBrains TeamCity**.

Accedemos al puerto `50000` via `http`:

![task1-landing_teamcity](./assets/images/task1-landing_teamcity.png)

Versión identificada en **TeamCity 2023.11.3 (build 147512)**

### Identificación de vulnerabilidad

Investigamos las posibles CVE asociadas a **TeamCity 2023.11.3**. 

Se han identificado dos vulnerabilidades críticas publicadas en marzo de 2024:

| CVE | Tipo | CVSS | Descripción |
|-----|------|------|-------------|
| [CVE-2024-27198](https://www.incibe.es/en/incibe-cert/early-warning/vulnerabilities/cve-2024-27198) | Authentication Bypass | 9.8 | Acceso administrativo sin credenciales |
| [CVE-2024-27199](https://nvd.nist.gov/vuln/detail/cve-2024-27199) | Path Traversal | 7.3 | Acceso a rutas restringidas del servidor |

Ambas afectan a versiones anteriores a **2023.11.4**. Nuestro target (2023.11.3) es vulnerable.

Vector de ataque seleccionado: **CVE-2024-27198**: Permite control total sobre TeamCity sin autenticación.

