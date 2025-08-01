qa_basic_networks = [
    ("Explain the OSI Model and each of its 7 layers with examples.",
     "The OSI model has 7 layers: Physical (hardware transmission like cables, hubs), "
     "Data Link (MAC addressing, error detection, switches), Network (IP routing via routers), "
     "Transport (TCP/UDP for data delivery), Session (manages communication sessions), "
     "Presentation (encryption, data formatting), and Application (network services like HTTP, FTP)."),

    ("Describe TCP/IP architecture and contrast it with OSI.",
     "TCP/IP has 4 layers: Link, Internet, Transport, Application. "
     "It is practical and widely used. OSI has 7 theoretical layers. "
     "TCP/IP combines some OSI layers (e.g., Link = Physical + Data Link)."),

    ("Functions of routers, switches, hubs, and gateways.",
     "Routers connect different networks and route packets. Switches connect devices in a LAN using MAC addresses. "
     "Hubs broadcast incoming packets to all ports. Gateways translate between different protocols."),

    ("Understand IPv4 vs IPv6 – header structure and benefits.",
     "IPv4 uses 32-bit addresses (~4.3 billion addresses). IPv6 uses 128-bit addresses, providing a vastly larger address space, "
     "simplified headers, and improved security features."),

    ("What are DNS, DHCP, NAT and how do they work in a network?",
     "DNS translates domain names into IP addresses. DHCP dynamically assigns IP addresses to devices. "
     "NAT translates private IP addresses to public IPs for internet access."),

    ("What is a MAC address and its significance?",
     "MAC address is a unique hardware identifier assigned to network interfaces, used for communication within a LAN at the Data Link layer."),

    ("Explain the difference between TCP and UDP.",
     "TCP is connection-oriented and reliable, ensuring ordered delivery and error checking. "
     "UDP is connectionless, faster, but unreliable, used for streaming and real-time applications."),

    ("What is subnetting and why is it used?",
     "Subnetting divides a large network into smaller sub-networks to improve routing efficiency and enhance security and management."),

    ("Explain the purpose of ARP.",
     "Address Resolution Protocol (ARP) translates IP addresses to MAC addresses within a local network."),

    ("Define broadcast and multicast addressing.",
     "Broadcast sends data to all devices in a subnet. Multicast sends data to a specific group of devices."),

    ("What is a firewall and its types?",
     "A firewall filters network traffic based on rules. Types include packet-filtering, stateful, proxy, and next-generation firewalls."),

    ("Explain VLAN and its benefits.",
     "Virtual LANs segment a physical network into logical networks to improve security and reduce broadcast traffic."),

    ("What is a proxy server and how does it work?",
     "A proxy server acts as an intermediary between clients and servers, providing caching, content filtering, and anonymity."),

    ("Describe the concept of encapsulation in networking.",
     "Encapsulation wraps data with protocol headers at each layer of the OSI or TCP/IP model as it travels through the network stack."),

    ("What is the difference between unicast, broadcast, and multicast?",
     "Unicast is one-to-one communication, broadcast is one-to-all, multicast is one-to-many specific receivers."),

    ("Explain how data flows from one device to another over the internet.",
     "Data is broken into packets and routed through multiple devices like switches and routers using IP addresses until it reaches the destination."),

    ("What is the role of DHCP in IP address assignment?",
     "DHCP automatically assigns IP addresses to devices joining a network to simplify configuration."),

    ("Define latency and bandwidth in networking.",
     "Latency is the delay before data transfer begins; bandwidth is the maximum rate of data transfer over a network."),

    ("What is the difference between static and dynamic IP addressing?",
     "Static IPs are manually assigned and remain constant. Dynamic IPs are assigned by DHCP and can change over time."),

    ("Explain the use of ports in TCP/IP.",
     "Ports identify specific processes or services on a device, allowing multiple network services to run simultaneously."),

    ("What is the difference between a public IP and a private IP address?",
     "Public IP addresses are routable on the internet, while private IP addresses are used inside local networks and are not routable externally."),

    ("What is NAT and why is it important?",
     "Network Address Translation (NAT) allows multiple devices on a private network to share a single public IP address for internet access."),

    ("What is a subnet mask and its purpose?",
     "A subnet mask determines which portion of an IP address refers to the network and which part refers to the host."),

    ("Explain the term 'collision domain'.",
     "A collision domain is a network segment where packet collisions can occur, typical in hubs but reduced in switches."),

    ("What is the difference between a collision domain and a broadcast domain?",
     "Collision domain is where data collisions happen; broadcast domain is where broadcast packets are propagated."),

    ("What protocols are used at the Transport layer?",
     "Main protocols are TCP (Transmission Control Protocol) and UDP (User Datagram Protocol)."),

    ("What is the purpose of ICMP?",
     "Internet Control Message Protocol (ICMP) is used for diagnostic and error messages, like ping and traceroute."),

    ("What is ARP spoofing?",
     "ARP spoofing is a network attack where a malicious actor sends fake ARP messages to associate their MAC with another IP address."),

    ("Explain the differences between half-duplex and full-duplex communication.",
     "Half-duplex allows data transmission in one direction at a time; full-duplex allows simultaneous two-way data transmission."),

    ("What is the purpose of the 'Three-way handshake' in TCP?",
     "It establishes a reliable connection using SYN, SYN-ACK, and ACK packets between client and server."),

    ("What is MTU and why is it important?",
     "Maximum Transmission Unit (MTU) is the largest size of a packet or frame that can be sent in a single network transaction."),

    ("Explain what a DNS server does.",
     "DNS servers translate human-friendly domain names into IP addresses usable by devices."),

    ("What is the function of a load balancer?",
     "Load balancers distribute network traffic across multiple servers to optimize resource use and prevent overload."),

    ("Describe what a VPN is and how it works.",
     "Virtual Private Network (VPN) encrypts and tunnels traffic over public networks, providing secure remote access."),

    ("What is port forwarding?",
     "Port forwarding redirects traffic from one port on a network device to another device/port, often used in routers."),

    ("What is a broadcast storm?",
     "A broadcast storm is excessive broadcasting that saturates a network and causes degradation or failure."),

    ("Explain the concept of a default gateway.",
     "A default gateway routes traffic from a local network to other networks or the internet."),

    ("What is the difference between TCP and UDP checksum?",
     "TCP checksum ensures error-free delivery with acknowledgment, UDP checksum is optional and simpler."),

    ("What is an IP address?",
     "An IP address is a unique numerical label assigned to each device on a network to identify and locate it."),

    ("What are the main classes of IPv4 addresses?",
     "Classes A, B, C, D (multicast), and E (experimental), distinguished by leading bits and range."),

    ("Explain what DHCP lease time means.",
     "DHCP lease time is how long a dynamically assigned IP address is valid before renewal is needed."),

    ("What is SNMP used for?",
     "Simple Network Management Protocol (SNMP) monitors and manages network devices."),

    ("Describe the differences between TCP congestion control algorithms.",
     "Algorithms like Tahoe, Reno, and Vegas manage how TCP reduces data transmission during network congestion."),

    ("What is a MAC address table?",
     "It is maintained by switches to map MAC addresses to specific ports for efficient forwarding."),

    ("Explain CSMA/CD.",
     "Carrier Sense Multiple Access with Collision Detection is a protocol for network devices to detect collisions and retransmit."),

    ("What is the function of the Network layer?",
     "Routing packets between networks and logical addressing with IP."),

    ("What is a DHCP relay agent?",
     "It forwards DHCP requests between clients and servers when they are on different subnets."),

    ("Describe the main difference between IPv4 and IPv6 headers.",
     "IPv6 headers are simplified with fixed size and include features like flow labeling and better security support."),

    ("What is tunneling in networking?",
     "Tunneling encapsulates one network protocol inside another to securely send data across incompatible networks."),

    ("Explain the term 'link-local address'.",
     "A link-local address is an IP address valid only within a local subnet, automatically assigned for communication within a link."),

    ("What is a wireless access point (WAP)?",
     "A device that allows wireless devices to connect to a wired network using Wi-Fi."),

    ("What is the difference between simplex, half-duplex, and full-duplex communication?",
     "Simplex is one-way only, half-duplex is two-way but one direction at a time, full-duplex is two-way simultaneously."),

    ("What is the primary purpose of DHCP?",
     "To automatically assign IP addresses and network configuration to devices."),

    ("What is a MAC address spoofing attack?",
     "An attacker falsifies a MAC address to bypass security or impersonate another device."),

    ("What is a broadcast domain?",
     "A network segment where a broadcast packet is forwarded to all devices."),

    ("What is a VLAN tag?",
     "An identifier added to Ethernet frames to indicate the VLAN they belong to."),

    ("What is QoS in networking?",
     "Quality of Service prioritizes certain types of traffic to ensure reliable performance."),

    ("Explain what a subnet mask 255.255.255.0 means.",
     "The first 3 octets are the network portion; the last octet identifies hosts."),

    ("What is a routing table?",
     "A database in routers containing routes to various network destinations."),

    ("What is a default route?",
     "A route used when no specific route for a destination exists, usually points to the gateway."),

    ("Describe what happens during ARP request and reply.",
     "Request broadcasts to find MAC for an IP; reply sends the MAC address back."),

    ("What is a multicast address?",
     "An IP address used to deliver packets to a group of interested receivers."),

    ("What is a TCP segment?",
     "A TCP segment is a piece of data with a TCP header used for transmission."),

    ("What is the maximum size of an IPv4 packet?",
     "65,535 bytes including header and data."),

    ("What is a network protocol?",
     "A set of rules governing data exchange between devices."),

    ("What is the difference between half-open and full-open TCP connections?",
     "Half-open occurs when handshake is incomplete; full-open means connection is established."),

    ("What is DHCP snooping?",
     "A security feature to prevent rogue DHCP servers from assigning IP addresses."),

    ("What is the role of DNS cache?",
     "To store recently resolved domain names to speed up future queries."),

    ("What is ICMP used for?",
     "Network diagnostic tools like ping and traceroute use ICMP to send control messages."),

    ("What is port scanning?",
     "A technique to find open ports on a target system, often used by attackers."),

    ("Explain the difference between flooding and broadcasting.",
     "Flooding sends packets to all switch ports except source; broadcasting sends to all devices in the broadcast domain."),

    ("What is a VPN concentrator?",
     "A device that manages VPN connections and tunnels."),

    ("What is a packet sniffer?",
     "A tool that captures and analyzes network traffic."),

    ("What is network latency?",
     "The time taken for a packet to travel from source to destination."),

    ("Explain the difference between unshielded twisted pair (UTP) and shielded twisted pair (STP) cables.",
     "STP has shielding to reduce electromagnetic interference, UTP does not."),

    ("What is the main use of fiber optic cables in networking?",
     "To provide high-speed data transmission over long distances with low loss."),

    ("What is a broadcast address in IPv4?",
     "An address where all host bits are set to 1, used to send packets to all devices in a subnet."),

    ("What is a default gateway used for?",
     "To forward packets destined outside the local network."),

    ("What is DHCP reservation?",
     "Mapping a specific IP address to a device's MAC address to always assign the same IP."),

    ("Explain the use of the ping command.",
     "To check connectivity between devices by sending ICMP echo requests."),

    ("What is the difference between wired and wireless networks?",
     "Wired networks use physical cables; wireless networks use radio waves for communication."),

    ("What is a DMZ in networking?",
     "A Demilitarized Zone is a separate network segment that hosts public-facing services, isolated for security."),

    ("What is the purpose of a packet filter firewall?",
     "To inspect packets and allow or block based on rules like IP addresses and ports."),

    ("What is a Stateful firewall?",
     "A firewall that tracks the state of active connections and makes decisions based on connection state."),

    ("What is the difference between IPv4 public and private addresses?",
     "Public addresses are routable on the internet; private addresses are used within internal networks."),

    ("Explain what an IP address classless inter-domain routing (CIDR) is.",
     "CIDR allows flexible IP address allocation by using variable-length subnet masks."),

    ("What is the use of the traceroute command?",
     "To identify the path packets take to reach a destination by listing routers along the way."),

    ("What is a broadcast storm and how can it be prevented?",
     "Excessive broadcast traffic that can overwhelm a network; prevented by using switches and VLANs."),

    ("Explain the term 'port number'.",
     "A 16-bit number used to identify specific processes/services in TCP/UDP communication."),

    ("What is the maximum number of hosts on a /24 subnet?",
     "254 hosts (2^8 - 2, accounting for network and broadcast addresses)."),

    ("What is the use of the MAC address in network communication?",
     "To uniquely identify devices on a local network at the Data Link layer."),

    ("Explain what an IP address is and its version types.",
     "An IP address is a unique identifier for devices on a network. IPv4 is 32-bit, IPv6 is 128-bit."),

    ("What is a network switch and how does it differ from a hub?",
     "A switch forwards data only to the destination port using MAC addresses, whereas a hub broadcasts to all ports."),

    ("What is a TCP three-way handshake?",
     "The process of SYN, SYN-ACK, and ACK messages to establish a TCP connection."),

    ("What is DHCP and how does it work?",
     "Dynamic Host Configuration Protocol automatically assigns IPs and network settings to devices."),

    ("What is the function of the Transport layer in the OSI model?",
     "Provides end-to-end communication, error correction, and flow control."),

    ("What is IP fragmentation?",
     "Breaking a packet into smaller pieces to pass through a network with smaller MTU."),

    ("What is a MAC address and how is it formatted?",
     "A 48-bit address assigned to network interfaces, usually formatted as six groups of two hexadecimal digits."),
]