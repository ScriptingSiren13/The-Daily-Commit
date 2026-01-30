# Arcade — Secure Networking, IAM & GKE Autopilot (Conceptual Notes)

Today I completed an arcade consisting of three Google Cloud labs focused on **secure networking**, **access control**, and **managed Kubernetes deployments**. These labs strengthened my understanding of how cloud infrastructure is secured, managed, and operated at scale in real-world environments.

---

## Lab 1 — High-Throughput VPN Between Cloud & On-Prem Networks

This lab focused on building a **secure, encrypted VPN connection** between two isolated networks: a cloud VPC and a simulated on-premises VPC.

### Core Concepts Learned

- **Virtual Private Networks (VPNs)**
  - VPNs provide secure communication over public internet using encryption.
  - Google Cloud uses **IPsec VPN tunnels** to encrypt traffic between networks.
  - VPNs are commonly used to connect cloud infrastructure with on-prem systems or other clouds.

- **Cloud vs On-Prem Network Simulation**
  - Two separate VPCs were created to simulate real-world hybrid networking.
  - Each VPC had its own IP range, firewall rules, and subnet structure.
  - This mirrors real enterprise environments where networks must remain isolated but securely connected.

- **VPN Gateways & Tunnels**
  - VPN gateways act as secure endpoints for encrypted communication.
  - Tunnels are established between gateways using shared secrets and IKE (Internet Key Exchange).
  - Traffic is routed explicitly through VPN tunnels using custom routes.

- **Routing Over VPN**
  - Routes determine which traffic flows through the tunnel.
  - Without routes, traffic never enters the VPN even if the tunnel exists.
  - Proper routing is critical for secure inter-network communication.

- **Performance & Throughput Testing**
  - Secure networking is not just about encryption but also performance.
  - Throughput testing helps verify that VPNs can handle production traffic.
  - This highlighted the balance between security and performance in cloud networking.

### Key Takeaway

This lab demonstrated how **secure hybrid connectivity** is built in practice and how encryption, routing, and performance all work together to enable reliable enterprise networking.

---

## Lab 2 — Identity & Access Management (IAM)

This lab focused on **who can do what** inside a Google Cloud project and how permissions are granted and revoked.

### Core Concepts Learned

- **IAM Fundamentals**
  - IAM controls access to Google Cloud resources.
  - Permissions are assigned via roles, not directly to users.
  - IAM is centralized and applies consistently across services.

- **Project-Level Roles**
  - **Owner**: Full control, including billing and IAM management.
  - **Editor**: Can modify resources but cannot manage IAM or billing.
  - **Viewer**: Read-only access to resources.
  - These roles apply across the entire project.

- **Principle of Least Privilege**
  - Users should only receive permissions they actually need.
  - Removing unnecessary permissions improves security.
  - IAM allows fine-grained access instead of all-or-nothing permissions.

- **Service-Specific Roles**
  - Users can be granted access to a single service without project-wide access.
  - Example: Granting Cloud Storage read access without project visibility.
  - This enables safer collaboration and controlled sharing.

- **Permission Propagation**
  - IAM changes are not always instant.
  - Permission updates take time to propagate across systems.
  - This is important to understand when debugging access issues.

### Key Takeaway

This lab made it clear that **security in the cloud is identity-driven**, and proper IAM design is essential to prevent accidental or malicious misuse of resources.

---

## Lab 3 — Deploying Applications with GKE Autopilot

This lab introduced **Google Kubernetes Engine (GKE) Autopilot**, a fully managed Kubernetes mode.

### Core Concepts Learned

- **Kubernetes Abstraction**
  - Kubernetes manages containers, scaling, and availability.
  - Developers define desired state; Kubernetes enforces it.
  - Clusters traditionally require node management and tuning.

- **GKE Autopilot**
  - Autopilot removes the need to manage nodes manually.
  - Google automatically provisions, scales, and secures infrastructure.
  - Developers focus only on applications, not cluster operations.

- **Containerized Application Deployment**
  - Applications are packaged as containers.
  - Containers are deployed using Kubernetes manifests.
  - Services expose applications to users via load balancers.

- **Automated Build & Deploy Pipelines**
  - Build, push, and deploy steps can be automated.
  - Artifact Registry stores container images securely.
  - Deployment workflows are repeatable and consistent.

- **Testing & Cleanup**
  - Applications can be tested via public endpoints.
  - Clean teardown of resources prevents waste and misconfiguration.
  - Resource lifecycle management is part of production readiness.

### Key Takeaway

This lab highlighted how **modern cloud platforms reduce operational complexity**, allowing developers to deploy scalable applications without worrying about infrastructure management.

---

## Overall Learnings from This Arcade

- Secure networking requires encryption, routing, and performance validation.
- IAM is the backbone of cloud security and access control.
- Kubernetes abstracts infrastructure, while Autopilot removes operational overhead.
- Cloud-native systems prioritize automation, security, and scalability.

This arcade strengthened my understanding of **enterprise-grade cloud architecture**, covering networking, security, and container orchestration fundamentals.
