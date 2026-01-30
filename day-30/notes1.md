# Arcade 1 — Cloud Networking, Kubernetes Deployments & Docker Fundamentals

Today I completed the second Arcade of google cloud skill, which consisted of three hands-on labs covering **VPC networking**, **Kubernetes deployment strategies**, and **Docker container fundamentals**. The focus was on understanding how modern cloud-native systems are built, deployed, and managed in production environments.

---

## Lab 1 — VPC Networks, Firewalls & VM Connectivity

In this lab, I explored how **Virtual Private Cloud (VPC) networks** work in Google Cloud and how they provide isolated, secure networking environments inside the cloud.

### Key Concepts Learned

- **VPC Networks**
  - VPCs are isolated private networking domains.
  - Auto mode VPCs create subnets automatically in all regions.
  - Custom mode VPCs give full control over subnet creation and IP ranges.

- **Subnets & CIDR Planning**
  - Subnets are regional.
  - Non-overlapping CIDR ranges are mandatory, especially for multi-interface VMs.

- **Firewall Rules**
  - Ingress firewall rules control traffic to VM instances.
  - ICMP, SSH, and RDP access must be explicitly allowed.
  - Firewall rules apply at the network level, not per VM.

- **VM Instances & Networking**
  - VM instances inherit firewall rules from their VPC.
  - External IP connectivity is controlled by firewall rules.
  - Internal IP connectivity works only within the same VPC by default.

### Connectivity Observations

- External IPs are reachable across VPCs if firewall rules allow.
- Internal IPs are reachable **only within the same VPC**, even across regions.
- VPCs are isolated by design unless connected via peering or VPN.

### Multi-Network Interface VM

- A single VM can have multiple network interfaces (NICs).
- Each NIC connects the VM directly to a different VPC.
- Each interface receives its own internal IP and routing rules.
- Only the **primary interface** gets the default route unless policy routing is configured.

This lab clarified how cloud networking isolation, routing, and security are enforced in real-world systems.

---

## Lab 2 — Kubernetes Deployments & Release Strategies

This lab focused on **Kubernetes deployments** and how production systems safely roll out changes without downtime.

### Core Kubernetes Concepts

- **Deployments**
  - Manage replica sets and pod lifecycles.
  - Allow declarative updates and rollbacks.
  - Automatically maintain desired replica counts.

- **Services**
  - Expose deployments internally or externally.
  - Route traffic to matching pods using label selectors.

- **Scaling**
  - Horizontal scaling by increasing or decreasing replicas.
  - Scaling is independent of application code.

### Deployment Strategies Learned

- **Rolling Updates**
  - Gradually replace old pods with new ones.
  - Zero downtime updates.
  - Ability to pause, resume, and roll back updates.

- **Canary Deployments**
  - Deploy a small percentage of traffic to a new version.
  - Useful for testing new versions in production safely.
  - Both old and new versions serve traffic simultaneously.

- **Blue-Green Deployments**
  - Maintain two separate environments (blue = old, green = new).
  - Traffic switches instantly from old to new version.
  - Very fast rollback by switching service selectors.

This lab demonstrated how Kubernetes enables **safe, controlled, and observable application releases**.

---

## Lab 3 — Docker Containers & Image Lifecycle

This lab introduced **Docker** and the full lifecycle of containerized applications.

### Docker Fundamentals

- Containers package applications with all dependencies.
- Containers are lightweight compared to virtual machines.
- Images are immutable, versioned artifacts.

### Image Creation & Execution

- Dockerfiles define how images are built.
- Images are composed of layers.
- Containers are runtime instances of images.
- Port mapping allows access to containerized services.

### Debugging Containers

- Logs can be inspected for runtime issues.
- Containers can be entered interactively using exec.
- Container metadata can be inspected for networking and configuration details.

### Artifact Registry & Image Portability

- Images can be pushed to private registries.
- Authentication is required for secure registries.
- Images can be pulled and run on any machine with Docker installed.
- Demonstrates true portability of containerized applications.

This lab reinforced the idea that **containers are the foundation of modern cloud-native platforms** and integrate seamlessly with Kubernetes.

---

## Overall Takeaways from Arcade 1

- Cloud networking relies on strong isolation and explicit configuration.
- Kubernetes provides powerful abstractions for scaling and deployment safety.
- Docker enables consistent application packaging across environments.
- Modern DevOps workflows depend on automation, repeatability, and declarative configuration.

This arcade strengthened my understanding of **infrastructure, orchestration, and containerization**, forming a strong base for advanced cloud and DevOps workflows.
