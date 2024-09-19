# Postmortem: Web Stack Outage on September 19th, 2024

## Issue Summary
- **Duration:** September 19th, 2024, 10:30 AM to 12:00 PM (UTC)
- **Impact:** Web service was down for 1 hour and 30 minutes, affecting 75% of users. Users experienced 502 Bad Gateway errors and were unable to access the site.
- **Root Cause:** Expired SSL certificate on backend servers caused failed connections between the load balancer (HA-Proxy) and the backend servers.

---

## Timeline

- **10:30 AM:** Monitoring detected a spike in 502 errors.
- **10:32 AM:** PagerDuty alerted internal teams about the issue.
- **10:40 AM:** Nginx on web servers was suspected; attempted restart, but the issue persisted.
- **11:00 AM:** Backend services and databases were checked with no issues found.
- **11:10 AM:** Investigation of HA-Proxy performance started due to suspected high load; ruled out as the cause.
- **11:30 AM:** HA-Proxy logs showed SSL/TLS errors indicating connection failures to backend servers.
- **11:35 AM:** The expired SSL certificate was discovered as the root cause.
- **11:45 AM:** Escalated to security and operations teams to renew the certificates.
- **12:00 PM:** SSL certificates were renewed, and service was restored.

---

## Root Cause and Resolution

The outage occurred due to an expired SSL certificate on the backend servers (web-01 and web-02). The HA-Proxy load balancer was unable to establish secure connections to these servers, resulting in 502 Bad Gateway errors for users.

To resolve the issue, the expired SSL certificates were renewed and redeployed across both backend servers, allowing secure connections to be re-established and restoring normal service.

---

## Corrective and Preventative Measures

### Areas for Improvement:
1. **SSL Certificate Monitoring:**
   - Implement automated SSL certificate expiration monitoring.
   - Set up alerts when certificates are close to expiring (30 days in advance).

2. **Automated SSL Certificate Renewal:**
   - Configure automatic SSL certificate renewal using services like Let’s Encrypt.
   - Automate the process of updating and deploying certificates across all servers.

3. **Improved Load Balancer Error Detection:**
   - Enhance monitoring to detect SSL/TLS errors from HA-Proxy earlier.
   - Set up detailed alerts for all load balancer errors (502, 503, etc.).

4. **Documentation and Incident Playbooks:**
   - Update incident response playbooks to include steps for SSL troubleshooting.
   - Provide team-wide training on SSL/TLS and certificate management.

---

## Action Items

1. **Install SSL monitoring tool** (e.g., Certbot) on all web servers.
2. **Configure SSL expiration alerts** in our monitoring systems (e.g., Prometheus).
3. **Automate SSL certificate renewal** using Let’s Encrypt.
4. **Deploy automated SSL updates** in staging and production environments.
5. **Improve HA-Proxy logging** to capture SSL handshake errors explicitly.
6. **Revise incident response playbook** to include SSL troubleshooting steps.
7. **Conduct a post-incident team training** on SSL/TLS and certificate management.

---
