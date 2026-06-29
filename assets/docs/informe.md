# Informe Final Auditoría de Seguridad

## 1.1 Datos del Proyecto

| Campo | Detalle |
| :--- | :--- |
| **Empresa Auditora** | Tonatiuh Qualo (Servicios de Seguridad Gestionados |
| **Cliente** | Nebula Inc. |
| **Proyecto** | Auditoría integral - Operación Eclipse |
| **Fecha Emisión** | 01/07/2026 |
| **Auditor Jefe** | Sergi Pérez |
| **Clasificación** | <span style="color:orange; font-size:14px; font-weight:bold">CONFIDENCIAL</span> |

## 1.2 Resumen Ejecutivo

Tras la investigación realizada por el equipo de respuesta de incidentes **Tonatiuh Qualo**, la postura de seguridad de **Nebula Inc.** se clasifica como <span style="color:red; font-size:12px; font-weight:bold">CRÍTICA</span>.

Se ha confirmado que, un atacante externo accedió al servidor de producción sin credenciales, escaló privilegios al máximo nivel e instaló mecanismos de acceso persistente, sin que los sistemas internos de la organización generasen alguna alerta.

Se han identificado **4 hallazgos de riesgo** <span style="color:red; font-size:12px; font-weight:bold">CRÍTICO</span> a partir del análisis de 4100 eventos en el **SIEM (Splunk)**. El ataque ha sido reconstruido en su totalidad, desde el vector de entrada inicial hasta la exfiltración de datos confirmado.

De no actuar ante estos hallazgos, **Nebula Inc.** se expone a un impacto combinado sobre tres ámbitos: 

- **Financiero**: Posibles sanciones de *RGPD* sobre la facturación anual.
- **Legal**: Responsabilidad civil frente a clientes cuyos datos han sido comprometidos.
- **Reputacional**: Los archivos exfiltrados ya han sido publicados en foros de la `Dark web`

Estos 3 riesgos, se retroalimentan entre sí y requieren de actuación inmediata por parte de la dirección.

## 1.3 Alcance y Metodología

### Sistemas evaluados:

| Sistema | Descripción |
| :--- | :--- |
| **Servidor de Producción** | OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 |
| **SIEM Splunk** | Plataforma centralizada de logs del cliente |

### Maros normativos aplicados:

| Marco | Aplicación |
| :--- | :--- |
| **MAGERIT v3** | Análisis y Gestión de risgos |
| **ISO 27001** | Referencia de controles de seguridad de la información |
| **NIS** | Marco europeo de ciberseguridad |

### Herramientas empleadas:

| Herramienta | Uso |
| :--- | :--- |
| **Splunk Enterprise** | Thread Hunting, correlación de enventos |
| **Nmap** | Reconocimiento activo de ataque (puertos, servicios y versiones) |
| **Metasploit/Meterpeter** | Emulación del vector de ataque original |

## 1.4 Hallazgo

### Hallazgo 1: Aplicación crítica expuesta a Internet sin actualizaciones

**Nivel de Riesgo**: <span style="color:red; font-size:16px; font-weight:bold">CRÍTICO</span> **(CVSS 9.8)**

El servidor de producción utiliza una versión obsoleta de la plataforma *JetBrains TeamCity*, accesible directamente desde internet. Esta versión contiene un fallo de seguridad conocido **(CVE-2024-27198)** que permite acceder como administrador sin necesidad de usuario y password. El fabricante publicó la corrección en marzo de 2024 pero en el momento del incidente (julio 2024) aún no se había aplicado.

**Condición (Lo que es)**: Cualquier persona desde internet puede acceder a TeamCity y aprovechando el fallo de seguridad, tomar el control completo del servidor. Esto ha sido verificado durante la simulación del ataque.

**Criterio (Lo que debería ser)**: Las normas de seguridad de la información (ISO27001), establecen que las correcciones de seguridad críticas deben aplicarse en un plazo razonable, especialmente en sistemas accesibles desde el exterior. Un fallo de esta gravedad no debería estar sin resolver durante mucho tiempo.

**Causa (Por qué ocurre)**: No existe un proceso establecido para revisar y aplicar actualizaciones de seguridad de forma periódica. El equipo de IT no contaba con alertas que avisaran de nuevos fallos publicados por los fabricantes.

**Consecuencia e Impacto**: Este ha sido el vector de entrada del atacante. A partir de aquí ha podido ejecutar acciones en el servidor, crear cuentas con privilegios y avanzar hasta la extracción de datos confidenciales.

### Plan de accion:

1. **Contención inmediata**: Actualizar **TeamCity** a la ultima versión. Restringir el acceso a la plataforma exclusivamente desde la red interna o a través de conexión **VPN**
2. **Acción definitva**: Establecer un proceso de revisión mensual de actualizaciones de seguridad e incoporar herramientas que alerten automáticamente cuando un sistema presente fallos conocidos. Documentar todo el proceso de revisión.

### Hallazgo-2: Privilegios de administración excesivos en cuenta de servicio

**Nivel de Riesgo**: <span style="color:red; font-size:16px; font-weight:bold">CRÍTICO</span>

La cuenta de usuario del sistema operativo bajo la que se ejecuta **TeamCity** `(ubuntu)` tiene permisos para realizar cualquier acción como administrador `(root)` sin necesidad de introducir el password. Esto significa que cualquier atacante que consiga acceso al servidor con este usuario, obtiene automáticamente el control absoluto del sistema operativo sin ningún obstáculo adicional.

**Condición (Lo que es)**: La configuración del sistema permite al usuario `ubuntu` ejecutar cualquier comando con privilegios máximos sin autenticación adicional `(NOPASSWD: ALL)`. Durante la simulación del ataque, se confirmó que ha bastado un solo comando para pasar de usuario limitado a administrador total del servidor.

**Criterio (Lo que debería ser)**: El principio de mínimo privilegio (ISO 27001) establece que cada cuenta debe tener únicamente los permisos estrictamente necesarios para su función. Una cuenta de servicio jamás debería tener permisos ilimitados de administración, y mucho menos sin requerir contraseña.

**Causa (Por qué ocurre)**: Configuración por defecto que no fue revisada ni restringida tras el despliegue del servidor. La ausencia de auditorías periódicas de permisos ha permitido que esta configuración pase desapercibida.

**Consecuencia e Impacto**: El atacante aprovechó esta configuración para escalar de un acceso limitado al control total del servidor en cuestión de segundos. Esto le permitió acceder a todos los archivos del sistema, instalar software malicioso y crear mecanismos de persistencia sin restricción alguna.

### Plan de acción:

1. **Contención inmediata**: Eliminar los permisos `NOPASSWD: ALL` de la cuenta `ubuntu`. Restringir sus privilegios exclusivamente a los comandos necesarios para operar **TeamCity**.
2. **Acción definitiva**: Implantar una política de mínimo privilegio en todos los servidores. Realizar auditorías trimestrales o mensuales de los permisos de las cuentas del sistema y registrar toda elevación de privilegios en el **SIEM** para su monitorización.

---
