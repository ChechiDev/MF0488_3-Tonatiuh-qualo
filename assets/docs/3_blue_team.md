# 3. Blue Team

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

---

<div style="border-left: 3px solid #444444; padding-left: 12px;">

[TIP]

```bash
Credentials

Only needed if you are using your own machine.

Username: splunk
 
Password: analyst123
 
IP address: MACHINE_IP
 
Connection via: http://MACHINE_IP:8000
```

<div>

