"""
Blockchain & Cryptography Interview Preparation Questions & Answers
Format: (Question, Crisp Answer with Key Characteristics and Example)
"""

qa_blockchain_crypto = [
    (
        "What is Blockchain and what are its core architectural components?",
        "**Direct Answer:** Blockchain is a decentralized, cryptographically secured distributed ledger that records ordered transactions across a peer-to-peer network, achieving data immutability and transparency through consensus algorithms without a central authority.\n\n"
        "**Key Characteristics:**\n"
        "• Distributed Ledger: Every full node maintains an identical synchronized copy of the transaction history.\n"
        "• Cryptographic Chaining: Each block contains the SHA-256 cryptographic hash of the previous block header, making historical tampering mathematically detectable.\n"
        "• Smart Contracts: Self-executing code stored on-chain that automatically enforces contractual agreements when predefined conditions are met.\n\n"
        "**Example:** In Bitcoin, transactions are batched into blocks mined roughly every 10 minutes; altering a transaction from 5 years ago would require recomputing the Proof of Work for all subsequent blocks across 51% of global network hash power."
    ),
    (
        "What is the difference between Symmetric and Asymmetric Cryptography?",
        "**Direct Answer:** Symmetric Cryptography uses a single shared secret key for both encryption and decryption (fast, high throughput for bulk data), while Asymmetric Cryptography uses a mathematically linked key pair—a Public Key for encryption and a Private Key for decryption (secure key exchange and digital signatures).\n\n"
        "**Key Characteristics:**\n"
        "• Symmetric algorithms: AES-256, ChaCha20, 3DES; primary challenge is the secure out-of-band key distribution problem.\n"
        "• Asymmetric algorithms: RSA, ECC (Elliptic Curve Cryptography), Ed25519; computationally intensive, used for handshakes and signatures.\n"
        "• Hybrid Cryptography: Asymmetric cryptography negotiates a temporary symmetric session key (e.g. TLS handshake), which then encrypts the bulk payload.\n\n"
        "**Example:** In an HTTPS connection, the browser uses RSA or ECDHE to securely exchange a symmetric AES-256 session key, which then encrypts all subsequent web page requests."
    ),
    (
        "How do Cryptographic Hash Functions work and what makes them secure?",
        "**Direct Answer:** A Cryptographic Hash Function is a deterministic one-way mathematical algorithm that transforms an arbitrary-length input into a unique, fixed-length digest, satisfying pre-image resistance, second pre-image resistance, and collision resistance.\n\n"
        "**Key Characteristics:**\n"
        "• Pre-image resistance (One-way): Infeasible to calculate input $m$ given hash $h = H(m)$.\n"
        "• Second pre-image resistance (Weak collision): Infeasible to find another input $m' \\ne m$ such that $H(m) = H(m')$.\n"
        "• Collision resistance (Strong collision): Infeasible to find any two arbitrary inputs $(m_1, m_2)$ such that $H(m_1) = H(m_2)$.\n"
        "• Avalanche Effect: Altering a single bit in the input radically alters at least 50% of the output digest bits.\n\n"
        "**Example:** Downloading a Linux ISO image and verifying its SHA-256 hash confirms the ISO was not corrupted in transit or backdoor-injected by a compromised mirror."
    ),
    (
        "What is a Digital Signature and how does it guarantee Non-Repudiation?",
        "**Direct Answer:** A Digital Signature is a cryptographic mechanism where a sender hashes a message and encrypts the hash using their private key, allowing anyone possessing the sender's public key to verify the message's authenticity, integrity, and author identity (non-repudiation).\n\n"
        "**Key Characteristics:**\n"
        "• Authentication: Proves the signature could only have been created by the holder of the corresponding private key.\n"
        "• Integrity: Any alteration of the signed document causes the recomputed hash to mismatch the decrypted signature hash.\n"
        "• Non-repudiation: The signer cannot deny having signed the message, as the private key is held exclusively by them.\n\n"
        "**Example:** When Alice sends 1.5 BTC to Bob, her Bitcoin wallet signs the transaction with her private key; the network verifies the signature against her public address before committing the ledger transfer."
    ),
    (
        "What is Proof of Work (PoW) vs. Proof of Stake (PoS) consensus?",
        "**Direct Answer:** Proof of Work achieves network consensus by requiring miners to expend physical computational energy solving mathematical puzzles (finding a nonce that produces a block hash below a target difficulty), while Proof of Stake selects validators proportionally to the economic tokens they have locked (staked) as collateral.\n\n"
        "**Key Characteristics:**\n"
        "• PoW: Capital expenditure on ASICs and electricity; high security against Sybil attacks; massive energy footprint.\n"
        "• PoS: Validators are penalized (slashed) for proposing invalid blocks or double-signing; cuts energy consumption by >99.9%.\n"
        "• Finality: PoW relies on probabilistic finality (e.g. 6 block confirmations); PoS frameworks (like Casper) provide deterministic epoch finality.\n\n"
        "**Example:** Bitcoin uses PoW requiring ~150 TWh of energy annually; Ethereum completed 'The Merge' in 2022, transitioning from PoW to PoS and reducing network energy consumption by 99.95%."
    ),
    (
        "What is a 51% Attack in Blockchain networks?",
        "**Direct Answer:** A 51% Attack occurs when a malicious entity gains control of more than half of the network's consensus voting power (hash rate in PoW or staked tokens in PoS), allowing them to rewrite recent transaction history, execute double-spend attacks, and censor transactions.\n\n"
        "**Key Characteristics:**\n"
        "• Can re-mine an alternate longer private chain and broadcast it to overwrite valid confirmed blocks.\n"
        "• Cannot fabricate coins out of thin air or steal coins from private keys they do not own (cannot forge digital signatures).\n"
        "• Predominantly threatens smaller altcoins with low total hash rate where renting hash power on NiceHash is inexpensive.\n\n"
        "**Example:** In 2019, Ethereum Classic (ETC) suffered multiple 51% attacks where attackers double-spent over $1 million by reorganizing deep blocks on crypto exchanges."
    ),
    (
        "What is a Merkle Tree and why is it critical for blockchain verification?",
        "**Direct Answer:** A Merkle Tree is an inverted binary cryptographic tree where leaf nodes represent hashes of individual transactions and parent nodes represent the cryptographic hash of their children, culminating in a single Merkle Root stored in the block header.\n\n"
        "**Key Characteristics:**\n"
        "• Enables Simplified Payment Verification (SPV) / Light Clients to verify whether a transaction is included in a block without downloading the entire blockchain.\n"
        "• Verification complexity is $O(\\log_2 N)$ rather than $O(N)$ linear scans.\n"
        "• Any tampering with a single transaction cascades up the tree, invalidating the Merkle Root.\n\n"
        "**Example:** A mobile smartphone wallet verifies that your transaction was included in a block of 4,000 transactions by checking only a 12-hash cryptographic Merkle proof (~384 bytes) instead of downloading the 2MB block."
    ),
    (
        "What is Elliptic Curve Cryptography (ECC) and why is it preferred over RSA in modern security?",
        "**Direct Answer:** ECC is an asymmetric public-key cryptography approach based on the algebraic structure of elliptic curves over finite fields, offering equivalent or superior cryptographic security to RSA with substantially shorter key lengths and lower compute/bandwidth requirements.\n\n"
        "**Key Characteristics:**\n"
        "• Security relies on the Elliptic Curve Discrete Logarithm Problem (ECDLP), which has no known sub-exponential classical solving algorithm.\n"
        "• Key size efficiency: A 256-bit ECC key (e.g. secp256k1 used in Bitcoin) provides identical security to a 3072-bit RSA key.\n"
        "• Faster key generation, signature generation, and smaller packet payload headers; ideal for mobile and blockchain networks.\n\n"
        "**Example:** Bitcoin and Ethereum use the `secp256k1` elliptic curve curve equation $y^2 = x^3 + 7 \\pmod p$ for user wallets, enabling compact 65-byte digital signatures."
    ),
    (
        "What are Reentrancy Attacks in Smart Contracts and how do you prevent them?",
        "**Direct Answer:** A Reentrancy Attack occurs when a vulnerable smart contract makes an external call to an untrusted contract before updating its internal state balance, allowing the recipient contract's fallback function to recursively re-invoke the withdrawal function repeatedly before the balance is zeroed.\n\n"
        "**Key Characteristics:**\n"
        "• Exploits the execution order: External calls transfer control of execution flow to the receiving contract.\n"
        "• Infamous cause of the 2016 DAO hack leading to the Ethereum / Ethereum Classic hard fork ($60M stolen).\n"
        "• Prevented by following the **Checks-Effects-Interactions** pattern (deduct balance before transferring funds) or using ReentrancyGuard mutex locks.\n\n"
        "**Example:** A contract code has: `msg.sender.call.value(amount)(); userBalances[msg.sender] = 0;`—an attacker's contract intercepts the callback and calls `withdraw()` recursively, draining the entire pool balance before the zeroing line executes."
    )
]
