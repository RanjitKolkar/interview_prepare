"""
Active Directory & Identity Security (IAM/PAM) Interview Preparation Questions & Answers
Format: (Question, Crisp Answer with Key Characteristics and Example)
"""

qa_identity_ad = [
    (
        "How does Active Directory Kerberos Authentication work (TGT vs. ST)?",
        "**Direct Answer:** Kerberos is a ticket-based symmetric key authentication protocol where a user authenticates to the Key Distribution Center (KDC / Domain Controller) to receive a Ticket Granting Ticket (TGT), which is subsequently presented to request Service Tickets (ST / TGS) for accessing specific network services without resending credentials.\n\n"
        "**Key Characteristics:**\n"
        "• AS-REQ / AS-REP: User encrypts timestamp with their password hash; KDC verifies and returns a TGT encrypted with the domain `krbtgt` account hash.\n"
        "• TGS-REQ / TGS-REP: User presents TGT to KDC to request access to a Service Principal Name (SPN); KDC returns a Service Ticket encrypted with that service account's password hash.\n"
        "• AP-REQ: User presents the Service Ticket directly to the target application server to gain access.\n\n"
        "**Example:** A user logs into Windows workstation; the LSASS process handles Kerberos ticket requests behind the scenes, allowing seamless single sign-on access to file shares (`cifs/fileserver.corp.local`) using cached Service Tickets."
    ),
    (
        "What is a Kerberoasting attack and how do defenders detect and mitigate it?",
        "**Direct Answer:** Kerberoasting is a post-exploitation attack where an authenticated domain user requests Kerberos Service Tickets (TGS) for service accounts with registered Service Principal Names (SPNs), extracts the tickets from local memory, and cracks their password hashes offline using dictionary/brute-force tools.\n\n"
        "**Key Characteristics:**\n"
        "• Requires zero administrative privileges—any valid domain user account can request a service ticket for any registered SPN.\n"
        "• Performed entirely offline: the target service server is never contacted, generating zero authentication failure logs on the target.\n"
        "• Detection: Monitor Windows Event ID 4769 (Kerberos ticket requested) with RC4 encryption type (`0x17`) requested by standard user accounts.\n"
        "• Mitigation: Use Group Managed Service Accounts (gMSA) with 120-character random passwords that cannot be brute-forced, or AES-256 encryption.\n\n"
        "**Example:** An attacker with domain user access runs `GetUserSPNs.ps1`, receives a Kerberos ticket for `MSSQLSvc/sql.corp.local`, exports the hash to hashcat (mode 13100), and cracks the weak password `Password123!` in under 3 minutes."
    ),
    (
        "What is AS-REP Roasting and what specific account misconfiguration enables it?",
        "**Direct Answer:** AS-REP Roasting is an attack targeting Active Directory accounts that have the 'Do not require Kerberos preauthentication' attribute enabled (`DONT_REQ_PREAUTH`), allowing an attacker to request an AS-REP ticket without knowing the user's password and crack the returned encrypted timestamp offline.\n\n"
        "**Key Characteristics:**\n"
        "• Pre-authentication normally forces the client to prove knowledge of the password before the KDC issues an AS-REP.\n"
        "• If disabled, anyone on the network can send an AS-REQ for that username and receive an AS-REP containing data encrypted with the user's password hash.\n"
        "• Does not require elevated privileges and can be executed anonymously or with low-privileged credentials.\n"
        "• Mitigated by ensuring pre-authentication is enforced on all domain accounts via Group Policy auditing.\n\n"
        "**Example:** An attacker queries LDAP for `userAccountControl:1.2.840.113556.1.4.803:=4194304` and discovers a contractor account with pre-auth disabled; they immediately pull the AS-REP blob using Rubeus and crack the hash offline."
    ),
    (
        "What is a Golden Ticket attack vs. a Silver Ticket attack in Active Directory?",
        "**Direct Answer:** A Golden Ticket is a forged Ticket Granting Ticket (TGT) created using the compromised `krbtgt` account NTLM hash, granting permanent unrestricted domain admin access across the entire Active Directory forest; a Silver Ticket is a forged Service Ticket (TGS) created using a specific service account's password hash, granting access only to that specific service.\n\n"
        "**Key Characteristics:**\n"
        "• Golden Ticket: Forged with `krbtgt` hash; grants access to *any* service on the domain; circumvents smart-card and MFA requirements; KDC is never contacted.\n"
        "• Silver Ticket: Forged with service account hash (e.g. `cifs`, `http`, `mssql`); scoped strictly to that targeted service; Domain Controller is never contacted.\n"
        "• Remediation of Golden Ticket requires resetting the `krbtgt` password **twice** with a 10-hour replication interval to invalidate all existing forged tickets.\n\n"
        "**Example:** After compromising a Domain Controller, an attacker dumps the `krbtgt` NTLM hash using Mimikatz and generates a Golden Ticket valid for 10 years, ensuring persistent domain takeover even if all user passwords are reset."
    ),
    (
        "What is a DCSync attack and what specific Active Directory rights are abused?",
        "**Direct Answer:** DCSync is an attack where an adversary uses Mimikatz to simulate the behavior of an authentic Domain Controller using the Directory Replication Service Remote Protocol (MS-DRSR), requesting replication of password hashes (including `krbtgt` and Administrator) from an active DC without running code on the DC itself.\n\n"
        "**Key Characteristics:**\n"
        "• Requires two specific extended rights on the Domain root: 'Replicating Directory Changes' and 'Replicating Directory Changes All'.\n"
        "• Does not require logging into or dropping malware on the physical Domain Controller host.\n"
        "• Detected via Windows Event ID 4662 (Access to an object with replication access masks `1131f6aa-9c07-11d1-f79f-00c04fc2dcd2`) initiated by non-machine accounts.\n\n"
        "**Example:** An attacker compromises an account assigned to the 'Domain Sync Administrators' group and runs `lsadump::dcsync /domain:corp.local /user:Administrator` in Mimikatz, receiving the clear NTLM hash of the Enterprise Admin instantly."
    ),
    (
        "What is Pass-the-Hash (PtH) and how does Administrative Tiering mitigate it?",
        "**Direct Answer:** Pass-the-Hash is an attack where an adversary uses an extracted NTLM hash directly to authenticate against remote services via NTLM without needing to decrypt or crack the cleartext password; Administrative Tiering mitigates it by strictly isolating administrative credentials so that high-privilege credentials never log into lower-tier hosts.\n\n"
        "**Key Characteristics:**\n"
        "• NTLM protocol authenticates clients using the password hash directly as the cryptographic proof.\n"
        "• When an administrator logs into a compromised workstation via RDP or PsExec, their LSASS process caches the hash in memory.\n"
        "• Tiering Architecture: Tier 0 (Domain Controllers, Identity), Tier 1 (Enterprise Servers), Tier 2 (User Workstations); Tier 0 accounts are cryptographically and policy-blocked from logging into Tier 1 or Tier 2 machines.\n\n"
        "**Example:** A Domain Admin logs into a standard marketing workstation to troubleshoot a printer; an attacker with local admin dumps LSASS using ProcDump, steals the Domain Admin's NTLM hash, and executes `psexec` against the primary Domain Controller."
    ),
    (
        "What is BloodHound and how is Graph Theory utilized for Active Directory defense?",
        "**Direct Answer:** BloodHound is an Active Directory mapping and reconnaissance tool that uses graph theory and Neo4j databases to reveal hidden, unintended relationship chains and shortest privilege escalation paths to Domain Admin.\n\n"
        "**Key Characteristics:**\n"
        "• Ingests AD objects via SharpHound collector (Users, Groups, Computers, ACLs, Active Sessions, GPOs).\n"
        "• Maps relationships such as `GenericAll`, `WriteDacl`, `MemberOf`, `AdminTo`, and `CanRDP`.\n"
        "• Enables blue teams to identify and prune critical choke points and toxic permission combinations that grant standard users unexpected control over Tier-0 assets.\n\n"
        "**Example:** BloodHound maps that User A is in Group B, Group B has `WriteDacl` on Group C, and Group C can reset the password of a Domain Admin; by revoking that single `WriteDacl` ACL, defenders sever the entire attack chain."
    ),
    (
        "What is FIDO2 / WebAuthn and why is it considered Phishing-Resistant MFA?",
        "**Direct Answer:** FIDO2 / WebAuthn is an authentication standard based on public-key cryptography where the private key is held securely in hardware (e.g. YubiKey, TPM) and cryptographic authentication challenges are mathematically bound to the browser's verified Origin domain, making proxy-based phishing technically impossible.\n\n"
        "**Key Characteristics:**\n"
        "• Phishing-resistant: Even if an attacker proxies the login page (via Evilginx / AitM), the browser signs the challenge with the attacker's fake domain in the client data, which fails verification on the genuine service.\n"
        "• Eliminates shared secrets (passwords and SMS/OTP codes that can be intercepted or relayed).\n"
        "• Supported natively across modern operating systems, mobile devices (Passkeys), and web browsers.\n\n"
        "**Example:** A user is targeted by an Adversary-in-the-Middle (AitM) phishing site `login.microsofft-verify.com`; the user inserts their FIDO2 security key; the browser binds the cryptographic signature to `microsofft-verify.com`, which the legitimate Microsoft server immediately rejects."
    )
]
