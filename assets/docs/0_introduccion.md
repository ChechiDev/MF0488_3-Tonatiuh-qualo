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
