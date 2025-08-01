qa_scada_ot = [
    # --- Introduction ---
    ("What is SCADA?",
     "SCADA (Supervisory Control and Data Acquisition) is a system used to monitor and control industrial processes like manufacturing, power generation, water treatment, etc., using sensors, PLCs, and HMI interfaces."),

    ("What is OT (Operational Technology)?",
     "Operational Technology refers to hardware and software that detects or causes changes through direct monitoring and control of physical devices, processes, and events in industrial environments."),

    ("How is OT different from IT?",
     "IT deals with data (e.g., business systems), while OT controls physical processes. OT focuses on availability and safety, and often runs legacy systems with real-time requirements."),

    ("What industries use SCADA systems?",
     "SCADA is widely used in utilities (electricity, water), oil and gas, manufacturing, transportation, building automation, and critical infrastructure sectors."),

    ("Why is SCADA/OT security important?",
     "Because SCADA/OT systems control critical infrastructure, a cyberattack could disrupt services, damage equipment, or endanger lives. Ensuring security prevents downtime and sabotage."),

    # --- Components ---
    ("What are the key components of a SCADA system?",
     "Key components include: RTUs (Remote Terminal Units), PLCs (Programmable Logic Controllers), HMI (Human-Machine Interface), SCADA servers, and communication networks."),

    ("What is an HMI?",
     "An HMI (Human-Machine Interface) is a graphical interface that allows operators to interact with and monitor SCADA systems in real-time."),

    ("What is a PLC?",
     "A Programmable Logic Controller (PLC) is a rugged industrial computer used to automate and control electromechanical processes."),

    ("What is a RTU?",
     "An RTU (Remote Terminal Unit) is a microprocessor-controlled device that interfaces with sensors and actuators and communicates with the central SCADA server."),

    ("What communication protocols are used in SCADA systems?",
     "Common protocols include Modbus, DNP3, IEC 60870-5-104, OPC, BACnet, and PROFIBUS."),

    # --- Threats & Vulnerabilities ---
    ("What are common threats to SCADA systems?",
     "Common threats include malware, unauthorized access, phishing, physical tampering, man-in-the-middle attacks, and protocol-level vulnerabilities."),

    ("What is a man-in-the-middle attack in SCADA?",
     "It's when an attacker intercepts and possibly alters communications between two legitimate SCADA components without their knowledge."),

    ("What is Stuxnet and why is it significant?",
     "Stuxnet was a sophisticated worm discovered in 2010 that targeted Siemens PLCs. It was the first known malware to physically sabotage industrial equipment."),

    ("Why are SCADA systems often more vulnerable than IT systems?",
     "They often run legacy, unpatched systems; lack encryption; prioritize availability over security; and may lack physical and network isolation."),

    ("What is a zero-day vulnerability?",
     "A zero-day is a previously unknown vulnerability for which no patch exists, making it highly exploitable if discovered by attackers."),

    # --- Security Controls ---
    ("How can SCADA systems be protected?",
     "Best practices include network segmentation, firewalls, intrusion detection systems, access control, patch management, and security training."),

    ("What is network segmentation?",
     "It involves dividing a network into smaller segments to limit the spread of malware or unauthorized access across systems."),

    ("What is a DMZ in OT networks?",
     "A DMZ (Demilitarized Zone) isolates OT from IT networks, allowing controlled access to external services while protecting critical systems."),

    ("What is role-based access control (RBAC)?",
     "RBAC assigns system access permissions based on user roles, reducing the chance of unauthorized actions by limiting access to what's necessary."),

    ("What is the principle of least privilege?",
     "It means giving users only the permissions they need to perform their tasks, minimizing risk of misuse or compromise."),

    # --- Standards and Frameworks ---
    ("What is ISA/IEC 62443?",
     "ISA/IEC 62443 is a globally recognized cybersecurity standard specifically for industrial automation and control systems, including SCADA and OT."),

    ("What is NIST SP 800-82?",
     "It's a NIST guideline for securing Industrial Control Systems (ICS), including risk management, access control, and system monitoring."),

    ("What is the Purdue Model?",
     "The Purdue Model is a reference architecture for industrial control systems, organizing assets into zones/layers (Level 0–5) for structured security and data flow control."),

    ("What is a risk assessment in OT security?",
     "A risk assessment evaluates threats, vulnerabilities, and impacts to determine the most critical risks to prioritize for mitigation."),

    ("What is asset inventory in OT?",
     "Asset inventory is the process of identifying and cataloging all devices in the OT environment, which is crucial for vulnerability management and monitoring."),

    # --- Incident Response & Monitoring ---
    ("What is incident response in OT environments?",
     "It includes preparation, detection, containment, eradication, and recovery actions tailored to minimize impact of cyber events on physical processes."),

    ("Why is logging important in OT security?",
     "Logs help detect anomalies, trace incidents, and ensure compliance by recording user actions, system events, and network traffic."),

    ("What is anomaly detection in SCADA?",
     "Anomaly detection monitors for unusual behavior (e.g., unusual traffic or device behavior) which may indicate security breaches or system faults."),

    ("What is a honeypot in OT?",
     "A honeypot is a decoy system designed to lure attackers and study their behavior without risking actual systems."),

    ("What is the role of SIEM in OT security?",
     "A SIEM (Security Information and Event Management) aggregates and analyzes security data from various sources, helping detect and respond to threats in real time."),

    # --- Physical & Wireless Security ---
    ("Why is physical security important in SCADA?",
     "Because physical access to PLCs or network equipment can allow tampering, sabotage, or direct injection of malware into systems."),

    ("What are air-gapped networks?",
     "Air-gapped networks are physically isolated from external networks (like the internet), providing strong protection from remote attacks."),

    ("Is Wi-Fi safe in SCADA environments?",
     "Generally not recommended due to vulnerability to eavesdropping and jamming. If used, it must be heavily secured with encryption and authentication."),

    ("What is USB-based malware?",
     "Malware introduced via infected USB drives, often a threat in air-gapped or physically isolated systems lacking network defenses."),

    ("How can removable media be secured?",
     "Use of antivirus scans, write protections, usage policies, and disabling USB ports where unnecessary can reduce the threat."),

    # --- Case Studies & Real Attacks ---
    ("What was the Ukraine power grid attack?",
     "In 2015, attackers used malware (BlackEnergy) to remotely disable circuit breakers, causing massive blackouts—highlighting OT system vulnerabilities."),

    ("What was the Triton malware?",
     "Triton (or Trisis) targeted safety instrumented systems in an industrial facility, aiming to disrupt or cause physical damage, posing a life-threatening risk."),

    ("What is the Colonial Pipeline incident?",
     "In 2021, a ransomware attack on the Colonial Pipeline disrupted fuel distribution in the US. While IT was targeted, OT systems were shut down preemptively."),

    ("What is Havex malware?",
     "Havex is a remote access Trojan used to target ICS/SCADA systems through supply chain attacks and OPC protocol scanning."),

    ("What is Industroyer?",
     "Industroyer (CrashOverride) is malware designed to interact with industrial control protocols directly to disrupt electric power grids."),

    # --- OT Security Best Practices ---
    ("Why is patching difficult in SCADA systems?",
     "Because many SCADA systems run 24/7, unplanned downtime is unacceptable, and vendors may not support modern updates on legacy systems."),

    ("What is the role of vendor management?",
     "Vendors often install or maintain SCADA components; secure access control and audit trails are crucial to prevent supply chain risks."),

    ("What is whitelisting in SCADA environments?",
     "Whitelisting allows only approved software or devices to run or connect, helping prevent unauthorized access or malware execution."),

    ("Why is network traffic monitoring important?",
     "It detects anomalies, protocol abuse, and malicious activity early. Baselines help distinguish normal from abnormal behavior."),

    ("What is OT cybersecurity training?",
     "Regular training ensures staff can recognize phishing, follow security procedures, and respond to incidents effectively, reducing human error."),

    # --- Future Trends ---
    ("What is IT/OT convergence?",
     "It's the integration of IT and OT systems for improved efficiency and analytics, but it introduces new cybersecurity challenges due to differing priorities."),

    ("What is the role of AI in SCADA security?",
     "AI can analyze massive logs and detect anomalies faster than manual methods, improving detection of sophisticated threats."),

    ("What is predictive maintenance?",
     "Using data analytics and machine learning to anticipate equipment failures before they occur, reducing downtime in SCADA-controlled environments."),

    ("What is IEC 61850?",
     "A communication protocol for electrical substations allowing automation and standardized messaging in SCADA systems."),

    ("What is OT zero-trust architecture?",
     "A security model where no user or device is trusted by default—even inside the network. Access is verified continuously using strict policies.")
]
