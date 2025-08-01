qa_digital_forensics = [
    ("What is digital forensics?",
     "Digital forensics is the process of identifying, preserving, analyzing, and presenting digital evidence in a legally admissible manner."),
    
    ("What are the phases of digital forensics?",
     "The main phases are identification, preservation, analysis, documentation, and presentation."),
    
    ("What is chain of custody?",
     "Chain of custody refers to the documented process that records the control, transfer, analysis, and disposition of evidence."),
    
    ("Why is hashing important in digital forensics?",
     "Hashing ensures data integrity by generating a unique digital fingerprint that confirms the evidence hasn't been altered."),
    
    ("What is a write blocker?",
     "A write blocker is a device or software that prevents any write operations to a storage device during acquisition."),
    
    ("What is imaging in digital forensics?",
     "Imaging involves creating a bit-by-bit copy of a digital device to analyze without altering the original."),
    
    ("Name common file systems examined in forensics.",
     "Common file systems include FAT32, NTFS, exFAT, EXT4, and APFS."),
    
    ("What is volatile data?",
     "Volatile data is temporary and lost when a system is powered off, like RAM content and active network connections."),
    
    ("Define steganography.",
     "Steganography is the practice of hiding data within other non-secret files like images or videos."),
    
    ("How is steganography detected?",
     "It can be detected through steganalysis tools that inspect files for hidden content."),
    
    ("What is slack space?",
     "Slack space is unused space within a file cluster that may contain residual data."),
    
    ("What is metadata in forensics?",
     "Metadata refers to hidden data within files that records information such as file creation, modification, and access times."),
    
    ("What is live forensics?",
     "Live forensics involves collecting data from a running system, including RAM, network sessions, and open files."),
    
    ("What is network forensics?",
     "Network forensics is the analysis of network traffic to detect and investigate security incidents."),
    
    ("What is email forensics?",
     "Email forensics involves the recovery and analysis of email messages and headers to trace communication."),
    
    ("What is mobile forensics?",
     "Mobile forensics is the science of recovering digital evidence from mobile devices such as smartphones and tablets."),
    
    ("What is data carving?",
     "Data carving is the process of extracting files from unallocated or raw disk space without file system metadata."),
    
    ("What is file signature analysis?",
     "It verifies the file type by examining its binary pattern, regardless of its file extension."),
    
    ("What is timeline analysis in forensics?",
     "It reconstructs the sequence of events based on timestamps of files and logs."),
    
    ("What are digital artifacts?",
     "Artifacts are residual data left by applications or users, such as browser history, logs, or deleted files."),
    
    ("What is Windows Registry in forensics?",
     "The registry stores system and user configuration information that can reveal user activity."),
    
    ("What is the role of EnCase in digital forensics?",
     "EnCase is a commercial tool used for imaging, analyzing, and reporting digital evidence."),
    
    ("What is FTK?",
     "FTK (Forensic Toolkit) is a computer forensics software used to acquire, analyze, and index digital evidence."),
    
    ("What is an MD5 hash?",
     "MD5 is a cryptographic hash function that produces a 128-bit hash value, often used to verify file integrity."),
    
    ("What is a forensic image format?",
     "Common formats include E01 (EnCase), AFF, and raw DD. They store a copy of a digital drive for analysis."),
    
    ("What is triage in digital forensics?",
     "Triage refers to quickly assessing digital evidence to determine its importance and prioritize further analysis."),
    
    ("What is a keyword search in forensic tools?",
     "It helps locate specific terms in digital evidence like emails, documents, or chats."),
    
    ("What are log files?",
     "Log files record events and transactions on a system, which can provide evidence of user or system activity."),
    
    ("What is the purpose of volatility framework?",
     "Volatility is an open-source tool for analyzing RAM dumps to extract evidence from memory."),
    
    ("What is carving unallocated space?",
     "It refers to extracting files from disk areas not currently assigned to any active file."),
    
    ("What is bit-stream imaging?",
     "Bit-stream imaging creates an exact copy of a digital device including every bit, not just visible files."),
    
    ("What is a hex editor used for in forensics?",
     "It lets analysts view and edit binary files and raw disk sectors."),
    
    ("What are indicators of compromise (IOCs)?",
     "IOCs are forensic data like file hashes, IPs, and URLs used to identify malicious activity."),
    
    ("What is the importance of timestamps in forensics?",
     "Timestamps help create timelines and prove when data was created, modified, or accessed."),
    
    ("What are honeypots in digital forensics?",
     "Honeypots are decoy systems set up to attract attackers and study their behavior."),
    
    ("What is the role of cloud forensics?",
     "Cloud forensics involves collecting and analyzing data stored in cloud environments."),
    
    ("What is forensic readiness?",
     "Forensic readiness is the ability of an organization to prepare for potential investigations by preserving evidence proactively."),
    
    ("What is exif data?",
     "EXIF data is metadata stored in image files, revealing camera details, time, and possibly GPS location."),
    
    ("What is the difference between static and live acquisition?",
     "Static acquisition is done on a powered-off device. Live acquisition collects volatile data from a running system."),
    
    ("What is MAC time?",
     "MAC refers to Modified, Accessed, and Created timestamps of files."),
    
    ("What is a timeline anomaly?",
     "A timeline anomaly is an inconsistency in file timestamps that may suggest tampering."),
    
    ("What is system restore in forensics?",
     "System restore points can provide historical data about system configurations and installed programs."),
    
    ("What are browser artifacts?",
     "Browser artifacts include history, cache, cookies, and bookmarks that reveal user web activity."),
    
    ("What is registry key analysis?",
     "Registry key analysis uncovers program installations, user activity, and connected devices."),
    
    ("What is hashing collision?",
     "It’s when two different files produce the same hash, which can undermine evidence integrity."),
    
    ("What is event log analysis?",
     "Event logs track user actions and system events like logins, shutdowns, and errors."),
    
    ("What is drive wiping?",
     "Drive wiping is the process of securely erasing data so it cannot be recovered."),
    
    ("What is a master file table (MFT)?",
     "MFT is a database used by NTFS to track all files on the volume."),
    
    ("What is volatile vs non-volatile memory?",
     "Volatile memory (e.g., RAM) is temporary. Non-volatile memory (e.g., HDD) persists after power-off."),

    ("What is data remanence?",
     "Data remanence is the residual representation of data that remains even after attempts to erase or remove it."),

    ("What is disk cloning?",
     "Disk cloning creates an exact replica of a hard drive, including system files and partitions."),

    ("What is cross-drive analysis?",
     "It involves comparing data across multiple drives to detect similarities or shared data patterns."),

    ("What is an anomaly detection in forensics?",
     "It's the identification of unusual patterns in data that don't conform to expected behavior."),

    ("What is entropy analysis?",
     "Entropy analysis is used to detect compressed or encrypted data by analyzing randomness in file content."),

    ("What is the difference between logical and physical acquisition?",
     "Logical acquisition copies files and folders. Physical acquisition copies the entire drive bit-by-bit."),

    ("What are timestamps anti-forensics techniques?",
     "These include modifying, spoofing, or deleting timestamps to mislead investigators."),

    ("What is OSINT in digital investigations?",
     "Open-Source Intelligence (OSINT) uses publicly available data to aid investigations."),

    ("What are anti-forensics tools?",
     "These are tools designed to hide, alter, or destroy digital evidence."),

    ("What is email header analysis?",
     "It involves examining metadata in email headers to trace the source and path of an email."),

    ("What is the role of virtual machines in forensics?",
     "VMs are used for safe testing of malware or simulating environments for analysis."),

    ("What is a RAM dump?",
     "A RAM dump is a snapshot of volatile memory, capturing live data for analysis."),

    ("What is file system journaling?",
     "Journaling records changes before they are committed, which can help in recovery and analysis."),

    ("What is a forensic report?",
     "A forensic report documents findings, procedures, and conclusions in a legally acceptable format."),

    ("What is carving embedded files?",
     "Extracting files hidden within other files, such as ZIP files within documents."),

    ("What is an unallocated space?",
     "Disk space not currently used by files but may still contain remnants of deleted data."),

    ("What is the role of timestamps in email forensics?",
     "They help determine the timing and flow of email communication."),

    ("What is timeline reconstruction?",
     "Organizing digital events in chronological order to understand a sequence of actions."),

    ("What is exfiltration in forensics?",
     "Unauthorized transfer of data from a system, often detected through forensic analysis."),

    ("What is shellbag forensics?",
     "Analyzing shellbags can reveal folder access history in Windows systems."),

    ("What is the pagefile?",
     "A system file used as virtual memory that may contain sensitive data remnants."),

    ("What is swap space?",
     "Memory used by the OS when RAM is full; may hold forensic artifacts."),

    ("What are deleted file recovery techniques?",
     "Methods include carving, MFT analysis, and software like Recuva or FTK Imager."),

    ("What is SQLite forensics?",
     "Analyzing SQLite databases often used by browsers, apps, and mobile devices."),

    ("What is B-tree in file systems?",
     "A data structure used by file systems to manage indexing and quick search."),

    ("What is process hollowing?",
     "A technique where malware injects itself into a legitimate process, used to evade detection."),

    ("What is cloud acquisition?",
     "Collecting evidence directly from cloud storage like Google Drive or OneDrive."),

    ("What is the importance of file header analysis?",
     "It helps verify file type and detect tampering by comparing magic bytes to extensions."),

    ("What is journaling in EXT file systems?",
     "It records metadata changes, aiding recovery and forensic analysis."),

    ("What is the role of DNS logs in forensics?",
     "DNS logs can reveal domain lookups that indicate browsing or malware activity."),

    ("What is the difference between evidence and intelligence?",
     "Evidence is admissible in court; intelligence helps in decision-making but may not be admissible."),

    ("What is command line history analysis?",
     "Recovering command-line entries from history files like .bash_history for user activity insights."),

    ("What is password cracking in forensics?",
     "The process of recovering passwords using techniques like brute force or dictionary attacks."),

    ("What is shadow volume copy analysis?",
     "Examining Windows backups to recover previous versions of files."),

    ("What is hidden partition detection?",
     "Identifying disk partitions not normally visible or mounted by the OS."),

    ("What is registry hive?",
     "A registry file containing configuration data, user settings, and system info."),

    ("What is APFS?",
     "Apple File System (APFS) is used on modern Apple devices, requiring specialized forensic tools."),

    ("What is network traffic capture?",
     "Recording data packets on a network using tools like Wireshark for forensic analysis."),

    ("What is keyword hit analysis?",
     "Analyzing search results for specific keywords to locate relevant digital evidence."),

    ("What is volatile vs non-volatile artifacts?",
     "Volatile artifacts exist in memory; non-volatile ones reside on disk or storage devices."),

    ("What is an event correlation?",
     "Linking events across logs and systems to understand cause-effect relationships."),

    ("What are timestamps spoofing tools?",
     "Tools used to modify file creation or access times to mislead investigators."),

    ("What is container file forensics?",
     "Analyzing archives like ZIP or RAR files to uncover hidden or encrypted content."),

    ("What is print spool forensics?",
     "Examining temporary files created during printing to uncover document evidence."),

    ("What is screen scraping?",
     "Capturing screen output, which can be used as evidence in forensic investigation."),

    ("What is boot record analysis?",
     "Inspecting the Master Boot Record (MBR) or GUID Partition Table (GPT) for boot-related evidence."),

    ("What is forensic soundness?",
     "Maintaining evidence integrity through reproducible and validated processes."),

    ("What is a forensic image verification?",
     "Using hash comparison to confirm that a forensic image matches the original data."),

    ("What is the importance of timestamps in registry keys?",
     "They help track system and user activities like software installation or device usage."),

    ("What is registry key LastWrite time?",
     "It indicates when a registry key was last modified—useful in establishing timelines.")
]


