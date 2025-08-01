# topics/network_security.py

qa_network_security = [
    ("What is the CIA Triad in cybersecurity?",
     "CIA stands for Confidentiality (data privacy), Integrity (data accuracy), and Availability (timely access)."),

    ("Explain the difference between authentication, authorization, and accounting (AAA).",
     "Authentication verifies identity, Authorization grants access rights, Accounting logs user activities."),

    ("What are common types of cyber attacks?",
     "Examples include phishing, malware, ransomware, DoS/DDoS, Man-in-the-Middle, SQL injection, and social engineering."),

    ("What is a firewall and how does it protect a network?",
     "A firewall filters incoming/outgoing traffic based on security rules to block unauthorized access."),

    ("What is the difference between symmetric and asymmetric encryption?",
     "Symmetric encryption uses one key for encryption/decryption; asymmetric uses a public-private key pair."),

    ("Describe public key infrastructure (PKI).",
     "PKI is a system for managing digital certificates and public-key encryption to secure communications."),

    ("What is SSL/TLS and why is it important?",
     "SSL/TLS protocols secure data transmitted over networks by encrypting traffic, used in HTTPS."),

    ("What are intrusion detection systems (IDS) and intrusion prevention systems (IPS)?",
     "IDS monitors network traffic for suspicious activity; IPS actively blocks or prevents attacks."),

    ("Explain the concept of a VPN and how it enhances security.",
     "VPN creates an encrypted tunnel between the user and the network, hiding traffic from attackers."),

    ("What is multi-factor authentication (MFA)?",
     "MFA requires two or more verification methods (e.g., password + fingerprint) to increase security."),

    ("Define malware and types of malware.",
     "Malware is malicious software including viruses, worms, trojans, ransomware, spyware, and adware."),

    ("What is social engineering in cybersecurity?",
     "Manipulating people into revealing confidential info or performing actions compromising security."),

    ("Describe phishing attacks and how to defend against them.",
     "Phishing tricks users into giving sensitive info via fake emails or websites; defense includes user training and email filtering."),

    ("What is a zero-day vulnerability?",
     "A software security flaw unknown to the vendor and unpatched, exploitable by attackers."),

    ("Explain the role of a Security Information and Event Management (SIEM) system.",
     "SIEM collects and analyzes security data from multiple sources to detect and respond to threats."),

    ("What is ransomware and how does it work?",
     "Ransomware encrypts victim’s files and demands payment for decryption keys."),

    ("Explain the difference between white hat, black hat, and grey hat hackers.",
     "White hats test systems ethically, black hats hack maliciously, grey hats operate between legal/illegal boundaries."),

    ("What is a botnet?",
     "A network of infected devices controlled by an attacker to perform coordinated attacks like DDoS."),

    ("What is the principle of least privilege?",
     "Users are given the minimum levels of access necessary to perform their jobs."),

    ("Explain the difference between vulnerability assessment and penetration testing.",
     "Vulnerability assessment identifies weaknesses; penetration testing exploits vulnerabilities to assess real risk."),

    ("What are some common cybersecurity frameworks and standards?",
     "Examples: NIST Cybersecurity Framework, ISO 27001, CIS Controls, PCI-DSS."),

    ("What is patch management and why is it important?",
     "Regularly updating software to fix security vulnerabilities and bugs to prevent exploits."),

    ("Define DNS spoofing and how it can be mitigated.",
     "Attackers alter DNS responses to redirect users to malicious sites; mitigated via DNSSEC and secure DNS."),

    ("What is data encryption at rest and in transit?",
     "Encryption at rest protects stored data; encryption in transit protects data moving across networks."),

    ("Explain what a man-in-the-middle (MITM) attack is.",
     "An attacker secretly intercepts and possibly alters communication between two parties."),

    ("What is a brute force attack?",
     "Attempting all possible password combinations until the correct one is found."),

    ("Describe the concept of defense in depth.",
     "Using multiple layers of security controls to protect information assets."),

    ("What is port scanning and why might attackers use it?",
     "Scanning target systems to discover open ports/services for potential exploitation."),

    ("Explain the use of honeypots in cybersecurity.",
     "Decoy systems set up to attract attackers, helping detect and analyze threats."),

    ("What is phishing simulation?",
     "A training tool where fake phishing emails test employee readiness to detect phishing."),

    ("What are botnets used for in cyber attacks?",
     "Launching DDoS attacks, sending spam, stealing data, or spreading malware."),

    ("Explain keylogging and how it threatens security.",
     "Software or hardware that records keystrokes to capture sensitive info like passwords."),

    ("What is social engineering prevention?",
     "Security awareness training, strong policies, and verification processes to reduce manipulation risk."),

    ("What is a denial-of-service (DoS) attack?",
     "An attack that overwhelms a system’s resources to make it unavailable to users."),

    ("What is network segmentation and why is it important?",
     "Dividing a network into segments to contain breaches and limit access."),

    ("Explain what endpoint security is.",
     "Protecting devices like laptops, mobiles, and desktops from cyber threats."),

    ("What is two-factor authentication (2FA)?",
     "A security process that requires two separate forms of identification."),

    ("Describe what a security policy is.",
     "A formal document outlining security rules, responsibilities, and procedures."),

    ("What are digital certificates?",
     "Electronic documents that use PKI to associate public keys with entities."),

    ("What is a brute force protection mechanism?",
     "Techniques like account lockout or CAPTCHA to block repeated login attempts."),

    # Q41 to Q100

    ("What is a security audit?",
     "A systematic evaluation of an organization's information system's security measures and compliance."),

    ("Explain the concept of risk management in cybersecurity.",
     "Identifying, assessing, and prioritizing risks to minimize, monitor, and control their impact."),

    ("What is a vulnerability scanner?",
     "A tool that scans systems to detect security weaknesses or vulnerabilities."),

    ("What is the difference between a virus and a worm?",
     "A virus attaches to files and needs user action; a worm is self-replicating and spreads automatically."),

    ("Explain what a Trojan horse is in malware context.",
     "Malicious software disguised as legitimate to trick users into installing it."),

    ("What is spear phishing?",
     "Targeted phishing attacks aimed at specific individuals or organizations."),

    ("What is a security incident?",
     "An event that compromises the confidentiality, integrity, or availability of information."),

    ("Explain the role of encryption algorithms like AES and RSA.",
     "AES is symmetric encryption for fast data encryption; RSA is asymmetric for secure key exchange."),

    ("What is a rootkit?",
     "Malicious software designed to hide its presence and allow continued privileged access."),

    ("Describe the concept of sandboxing.",
     "Isolating running programs to prevent them from affecting the host system."),

    ("What is a digital signature?",
     "An electronic signature that verifies authenticity and integrity of digital messages/documents."),

    ("Explain the difference between hashing and encryption.",
     "Hashing is one-way data transformation; encryption is reversible with the correct key."),

    ("What is a firewall DMZ?",
     "Demilitarized Zone - a subnetwork that exposes external services to the internet while protecting internal networks."),

    ("What are botnets and how are they controlled?",
     "Networks of infected devices controlled by command and control servers for malicious purposes."),

    ("Explain the importance of patch management.",
     "Regularly updating software to fix vulnerabilities and prevent exploits."),

    ("What is a mantrap in physical security?",
     "A small room with two interlocking doors used to control access to secure areas."),

    ("What is spear phishing and how does it differ from phishing?",
     "Spear phishing targets specific individuals, while phishing is more general and broad."),

    ("What are the main functions of a SIEM system?",
     "Collects logs, analyzes security events, alerts on suspicious activity, and helps with compliance."),

    ("What is an Advanced Persistent Threat (APT)?",
     "A prolonged and targeted cyberattack where intruders maintain access over time."),

    ("Explain the use of MAC address filtering.",
     "Restricts network access to devices with authorized MAC addresses."),

    ("What is a wireless intrusion detection system (WIDS)?",
     "A system that monitors wireless networks for unauthorized access or attacks."),

    ("What is social engineering and common attack methods?",
     "Manipulating people into giving confidential info; methods include phishing, baiting, pretexting."),

    ("Define data exfiltration.",
     "Unauthorized transfer of data from a system to an external destination."),

    ("What is network sniffing?",
     "Intercepting and logging network traffic to analyze data packets."),

    ("What is the principle of defense in depth?",
     "Using multiple security layers to protect assets in case one fails."),

    ("Explain the importance of strong password policies.",
     "Enforces complex passwords to reduce risk of unauthorized access."),

    ("What is the difference between IDS and IPS?",
     "IDS detects and alerts; IPS detects and actively blocks threats."),

    ("What are the primary goals of information security?",
     "Confidentiality, Integrity, Availability, Authentication, Non-repudiation."),

    ("Describe the role of network access control (NAC).",
     "Enforces security policies for devices accessing the network."),

    ("What is the difference between black box and white box penetration testing?",
     "Black box tests without knowledge of system internals; white box tests with full knowledge."),

    ("What are the most common types of firewalls?",
     "Packet-filtering, Stateful inspection, Proxy firewalls, Next-generation firewalls."),

    ("What is ransomware and typical attack vectors?",
     "Malware encrypting data, demanding ransom; often spread via phishing or exploit kits."),

    ("Explain phishing awareness training.",
     "Educates users to recognize and avoid phishing attempts."),

    ("What is a brute force attack and how can it be prevented?",
     "Trying all possible passwords; prevention includes lockouts and MFA."),

    ("What is two-factor authentication (2FA)?",
     "Using two different authentication methods to verify user identity."),

    ("What is a man-in-the-middle attack and how to prevent it?",
     "Intercepting communication between two parties; prevented by encryption and authentication."),

    ("Explain the difference between HTTP and HTTPS.",
     "HTTPS is HTTP over TLS/SSL, providing encrypted communication."),

    ("What is the purpose of a VPN?",
     "To create a secure encrypted tunnel over a public network."),

    ("What is a DMZ in networking?",
     "A separate network that exposes external-facing services while isolating internal networks."),

    ("What is a port scan?",
     "Probing a system for open ports to find potential entry points."),

    ("Explain session hijacking.",
     "Taking over a user’s active session to gain unauthorized access."),

    ("What is cross-site scripting (XSS)?",
     "An attack injecting malicious scripts into trusted websites."),

    ("What is SQL injection?",
     "Injecting malicious SQL statements to manipulate databases."),

    ("What is a zero-day exploit?",
     "An attack exploiting a previously unknown vulnerability."),

    ("Describe malware types: virus, worm, trojan, ransomware.",
     "Virus attaches to files; worm self-replicates; trojan disguises as legit; ransomware encrypts files."),

    ("What is a honeypot in cybersecurity?",
     "A decoy system to attract and analyze attacker behavior."),

    ("What is the difference between threat, vulnerability, and risk?",
     "Threat: potential harm; Vulnerability: weakness; Risk: likelihood of exploitation."),

    ("Explain the concept of endpoint security.",
     "Protecting devices that connect to the network, such as laptops and mobiles."),

    ("What is social engineering?",
     "Manipulating individuals into divulging confidential info."),

    ("What is a brute force attack?",
     "Attempting every possible password combination to gain access."),

    ("What is multi-factor authentication?",
     "Using two or more authentication methods for verifying identity."),

    ("What is the role of encryption in cybersecurity?",
     "Protecting data confidentiality during storage and transmission."),

    ("Explain the concept of least privilege.",
     "Users only get access necessary to perform their roles."),

    ("What are common cyberattack vectors?",
     "Phishing, malware, insider threats, social engineering, software vulnerabilities."),

    ("What is the difference between a virus and a worm?",
     "Viruses require user action; worms self-propagate without user intervention."),

    ("Explain the difference between IDS and IPS.",
     "IDS detects attacks; IPS detects and blocks attacks."),

    ("What is penetration testing?",
     "Simulated attack to identify vulnerabilities before real attackers do."),

    ("What is data loss prevention (DLP)?",
     "Systems that prevent unauthorized data transfer or leakage."),

    ("What is a firewall rule?",
     "A defined policy that allows or blocks specific traffic based on criteria."),

    ("What is network segmentation?",
     "Dividing a network into smaller parts to improve security and performance."),

    ("What is the purpose of a security policy?",
     "To define organizational security goals and responsibilities."),

    ("What is phishing?",
     "Fraudulent attempt to obtain sensitive information by pretending to be trustworthy."),

    ("What is cryptography?",
     "The science of securing information through encryption and related techniques."),

    ("What is two-step verification?",
     "An authentication process that uses two different methods to verify identity."),

    ("What is a digital certificate?",
     "An electronic document used to prove ownership of a public key."),

    ("What is a keylogger?",
     "Software or hardware that records keystrokes to steal sensitive data."),

    ("What is a worm?",
     "Malware that replicates itself to spread to other computers."),

    ("What is malware?",
     "Any software designed to cause damage or unauthorized access."),

    ("What is ransomware?",
     "Malware that encrypts data and demands payment for decryption keys."),

    ("What is a botnet?",
     "A network of compromised devices used for malicious activities."),

    ("What is the difference between black hat and white hat hackers?",
     "Black hats attack maliciously; white hats test systems for security."),

    ("What is a security breach?",
     "An incident where unauthorized access to data or systems occurs."),

    ("What is patch management?",
     "Process of updating software to fix security vulnerabilities."),

    ("What is social engineering?",
     "Manipulating people to divulge confidential information."),

    ("What is a firewall?",
     "A device or software that blocks unauthorized access to a network."),

    ("What is a Trojan horse?",
     "Malware disguised as legitimate software."),

    ("What is an exploit?",
     "A piece of software or code that takes advantage of a vulnerability."),

    ("What is multi-factor authentication?",
     "A security system requiring multiple methods of authentication."),

    ("What is a security audit?",
     "An assessment to evaluate security policies and controls."),

    ("What is a zero-day attack?",
     "An attack exploiting an unknown vulnerability."),

    ("What is penetration testing?",
     "Testing a system by simulating an attack to find vulnerabilities."),

    ("What is a honeypot?",
     "A decoy system set up to detect and analyze attackers."),

    ("What is an insider threat?",
     "Security risk posed by people within the organization."),

    ("What is a security policy?",
     "A set of rules defining how to protect information."),

    ("What is phishing?",
     "Fraudulent attempt to acquire sensitive info by pretending to be trustworthy."),

    ("What is data encryption?",
     "Process of converting data into unreadable form to prevent unauthorized access."),

    ("What is a denial-of-service (DoS) attack?",
     "Attack that makes a service unavailable by overwhelming it with traffic."),

    ("What is the principle of least privilege?",
     "Granting users the minimum access necessary to perform their jobs.")
]
