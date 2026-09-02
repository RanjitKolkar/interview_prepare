"""
Cloud Security & DevSecOps Interview Preparation Questions & Answers
Format: (Question, Crisp Answer with Key Characteristics and Example)
"""

qa_cloud_devsecops = [
    (
        "What is the Cloud Shared Responsibility Model?",
        "**Direct Answer:** The Shared Responsibility Model is a cloud security framework dictating that the cloud service provider (CSP) is responsible for the security *of* the cloud (physical data centers, host hardware, virtualization), while the customer is responsible for security *in* the cloud (data, IAM, network configs, operating system updates depending on service model).\n\n"
        "**Key Characteristics:**\n"
        "• IaaS: Customer manages OS, runtime, middleware, data, and firewall rules; CSP manages hypervisor and hardware.\n"
        "• PaaS: CSP manages OS and runtime; customer manages application code and data configurations.\n"
        "• SaaS: CSP manages everything except customer data access, user identities, and credential policies.\n\n"
        "**Example:** If an AWS EC2 Linux instance is compromised due to an unpatched OpenSSL vulnerability or open port 22, the customer is accountable; if AWS hardware fails or physical servers are breached, AWS is accountable."
    ),
    (
        "What is the Principle of Least Privilege (PoLP) in Cloud IAM?",
        "**Direct Answer:** The Principle of Least Privilege requires granting identities (users, groups, roles, service accounts) only the minimum set of permissions necessary to perform their required tasks, for the shortest required duration.\n\n"
        "**Key Characteristics:**\n"
        "• Avoids wildcards (`*`) in IAM policy actions (`s3:*`, `iam:*`) and resource definitions.\n"
        "• Leverages temporary credential tokens via role assumption (STS) instead of long-lived access keys.\n"
        "• Periodically audited using IAM Access Analyzers to prune unused historical permissions.\n\n"
        "**Example:** Granting an automated microservice read-only access to a single designated S3 bucket prefix (`s3:GetObject` on `bucket/reports/*`) rather than full tenant-wide S3 administrator privileges."
    ),
    (
        "How do you secure an AWS S3 bucket against public data leaks?",
        "**Direct Answer:** S3 buckets are secured by enabling Account-level 'Block Public Access', enforcing strict bucket policies, encrypting data at rest and in transit, and enabling continuous audit logging.\n\n"
        "**Key Characteristics:**\n"
        "• S3 Block Public Access enabled at both account and bucket level to override permissive ACLs.\n"
        "• Bucket policy enforcing HTTPS-only transport (`aws:SecureTransport: true`).\n"
        "• Server-side encryption via AWS KMS customer-managed keys (SSE-KMS).\n"
        "• Versioning and Object Lock enabled to safeguard against ransomware deletion.\n\n"
        "**Example:** Deploying an AWS Config rule `s3-bucket-public-read-prohibited` that automatically detaches public read ACLs whenever a developer misconfigures a storage bucket."
    ),
    (
        "What is DevSecOps and how does 'Shift-Left' security work?",
        "**Direct Answer:** DevSecOps integrates automated security practices and controls seamlessly into every stage of the DevOps CI/CD pipeline, and 'Shift-Left' means identifying and remediating vulnerabilities early in development rather than post-deployment.\n\n"
        "**Key Characteristics:**\n"
        "• Automated security gating: linting, secret detection, SAST, SCA, and DAST inside CI pipelines.\n"
        "• Pre-commit hooks to block hardcoded API keys and credentials before Git commits.\n"
        "• Reduces remediation cost by up to 80% compared to fixing vulnerabilities discovered in production.\n\n"
        "**Example:** A GitHub Actions pipeline automatically runs Gitleaks and Trivy; if a developer accidentally commits a private SSH key or introduces a CVE with CVSS > 8.0 in `package.json`, the pull request build immediately fails."
    ),
    (
        "What is the difference between SAST, DAST, and SCA?",
        "**Direct Answer:** SAST analyzes source code without executing it (white-box); DAST tests running applications from the outside (black-box); and SCA scans third-party open-source dependencies and libraries for known Common Vulnerabilities and Exposures (CVEs).\n\n"
        "**Key Characteristics:**\n"
        "• SAST (Static Application Security Testing): fast, points to exact source file and line number; high false-positive rate.\n"
        "• DAST (Dynamic Application Security Testing): tests live environments against SQLi, XSS, and authentication bypass; cannot locate exact code lines.\n"
        "• SCA (Software Composition Analysis): generates Software Bill of Materials (SBOM) and tracks license compliance (GPL/MIT).\n\n"
        "**Example:** SAST (SonarQube) catches insecure `eval()` calls in source code; SCA (Snyk) alerts that a logging library is vulnerable to Log4j; DAST (OWASP ZAP) catches missing HTTP security headers on the staging web endpoint."
    ),
    (
        "What is Container Security and how do you harden Docker images?",
        "**Direct Answer:** Container security encompasses protecting the container runtime, base image, host kernel, and cluster orchestration by running minimal, non-root images with immutable filesystems and scanned dependencies.\n\n"
        "**Key Characteristics:**\n"
        "• Use minimal base images (Alpine, Distroless, or scratch) to shrink attack surface.\n"
        "• Never run container processes as root (`USER nonroot`).\n"
        "• Enable read-only root filesystems and drop all non-essential Linux capabilities (`--cap-drop=ALL`).\n"
        "• Multi-stage Docker builds to prevent build-time tools (compilers, git) from entering production images.\n\n"
        "**Example:** In a Python microservice Dockerfile: using `python:3.11-slim`, creating a dedicated user `appuser`, copying only wheels from a builder stage, and specifying `USER 10001`."
    ),
    (
        "What is Kubernetes RBAC and how does it prevent cluster takeover?",
        "**Direct Answer:** Kubernetes Role-Based Access Control (RBAC) regulates user and service account access to cluster resources (Pods, Secrets, Nodes) by binding Roles/ClusterRoles containing discrete API verbs (get, list, create) to Subjects.\n\n"
        "**Key Characteristics:**\n"
        "• Namespace-scoped (`Role`, `RoleBinding`) vs. Cluster-wide (`ClusterRole`, `ClusterRoleBinding`).\n"
        "• Prevent granting wildcard verbs (`*`) or sensitive permissions like `create pods/exec` or access to `secrets`.\n"
        "• Default service accounts should have token automounting disabled (`automountServiceAccountToken: false`).\n\n"
        "**Example:** A monitoring daemon like Prometheus is granted a `ClusterRole` restricted strictly to `get`, `list`, and `watch` metrics endpoints, explicitly denying read access to database `Secrets`."
    ),
    (
        "What is Infrastructure as Code (IaC) Security and how do tools like tfsec/Checkov help?",
        "**Direct Answer:** IaC Security is the practice of scanning declarative infrastructure definitions (Terraform, CloudFormation, Ansible) for security misconfigurations, insecure defaults, and compliance violations before cloud resources are provisioned.\n\n"
        "**Key Characteristics:**\n"
        "• Catches misconfigurations (unencrypted disks, open security groups, wildcard IAM) directly in pull requests.\n"
        "• Eliminates manual compliance auditing and drift between declared state and cloud reality.\n"
        "• Integrates with policy-as-code engines like Open Policy Agent (OPA) / Rego.\n\n"
        "**Example:** A developer creates a Terraform script with `ingress { cidr_blocks = [\"0.0.0.0/0\"] }` for port 3389 (RDP); Checkov blocks the commit with an error rule `CKV_AWS_24: Ensure no security groups allow ingress from 0.0.0.0/0 to port 3389`."
    ),
    (
        "What is the difference between CloudTrail, CloudWatch, and AWS GuardDuty?",
        "**Direct Answer:** CloudTrail logs API calls and account governance actions ('who did what and when'); CloudWatch monitors performance metrics, system logs, and triggers operational alarms; GuardDuty uses machine learning and threat intelligence for intelligent threat detection.\n\n"
        "**Key Characteristics:**\n"
        "• CloudTrail: Audit trail for compliance, forensic analysis, and governance.\n"
        "• CloudWatch: CPU utilization, disk metrics, application logs, and auto-scaling alarms.\n"
        "• GuardDuty: Anomaly detection analyzing VPC Flow Logs, DNS logs, and CloudTrail management events without agents.\n\n"
        "**Example:** GuardDuty alerts SOC analysts that an EC2 instance is querying known Tor exit nodes and mining cryptocurrency; analysts look up CloudTrail to identify which compromised IAM key created the instance."
    ),
    (
        "What is Zero Trust Architecture (ZTA) in cloud environments?",
        "**Direct Answer:** Zero Trust is a security paradigm rooted in the principle of 'Never Trust, Always Verify', requiring continuous identity authentication, authorization, and cryptographic validation for every access request, regardless of whether the requester is inside or outside the network boundary.\n\n"
        "**Key Characteristics:**\n"
        "• Micro-segmentation eliminates flat internal networks and blocks lateral attacker movement.\n"
        "• Continuous contextual verification (user identity, device health, geolocation, risk score).\n"
        "• Assumes the perimeter has already been breached (Assume Breach mindset).\n\n"
        "**Example:** Instead of giving employees open network VPN access, a Zero Trust Network Access (ZTNA) proxy validates device compliance, MFA tokens, and role permissions individually for each internal dashboard."
    )
]
