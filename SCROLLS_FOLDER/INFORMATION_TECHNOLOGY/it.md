<!-- C:\Users\razer\Desktop\walkerrh.github.io\SCROLLS_FOLDER\INFORMATION_TECHNOLOGY\it.md -->




[Home](/index.html)

# JumpCloud 

* JumpCloud MDM - Mobile Device Management


# Sophos 

- SOPHOS Endpoint - an on-premise solution that offers anti-malware, application control, DLP, IPS, and MDM features
* Sophos EndPoint Protection -
- SOPHOS MDR - Managed Detection and Response
- Sophos Intercept X - proactively monitors for malware and exploits to block and remove threats from networks
- Sophos Mobile MDM - Mobile Device Management
- Sophos Central -
- Sophos Firewall -

# APPLE

* Apple DEP - Device Enrollment Program



* SSO - Single Sign on
* TOTP - Time-based One-Time Password
* AD - Active Directory 
* AAD - Azure Active Directory 
* VPP - Vector Packet Processing
* APN - Access Point Name
* ADE - Automated Device Enrollment (Apple’s MDM)
* CSR - Certificate Signing Request (trust between Apple and Org. Jumpcloud MDM)
* ABM - Apple Business Manager 
* VLAN - virtual local area network
* RADIUS - lets users securely authenticate their devices to WiFi, VPN, or other supported networks using JumpCloud
* LDAP - Lightweight Directory Access Protocol
* GPO - Group Policy analytics
* MDM - Microsoft Managed Desktop (Mobile Device Management)
* Sophos Windows Uninstall - C:\Program Files\Sophos\Sophos Endpoint Agent
* SDK - Software Development Kit
* MSI - Microsoft Software Installer
* MST - Windows Installer Setup Transform
* APN - Apple Push Notification service
* SAML - security Assertion Markup Language
* IDE - Integrated development environment
* ISE - Integrated Scripting Environment



A staged user won't have access to any assigned resources until their user state is changed to Active





# Reset a Bootable USB

1. plug in usb
2. open command prompt (cmd) 
3. type: diskpart
4. type: list disk
5. type: select disk x (disk 0 is the computer via large storage, disk 1 is usb)
6. type: clean
7. list partition
8. type: create partition primary
9. list partition
10. type: active
11. type: Format FS=fat32 quick (or xfat or NTFS)
12. select partition 1
13. assign letter=Z
14. type: Exit

# Ports

* RANGE: 0-65535
* System/Well-known-ports: 0-1023
* User/Registered-ports: 1024-49151 
* Dynamic/Privite-ports: 49152-65535
* 80:(http)web pages 
* 443:(https)web pages
* 21:FTP(file transfer protocol)

# Tor

* Never use logins
* Never reuse logins
* Never mention logins
* Do not change any Tor settings
* Do not discuss personal info
* Use end-to-end encryption
* Install firewall
* Update OS daily
* Use burner laptop
* Randomize mac address



QUIC (Quick UDP Internet Connections)
UDP (User Datagram Protocol)
SSL (Secure Sockets Layer)
    standard security technology for establishing an encrypted link between a server and a client—typically a web server (website) and a browser, or a mail server and a mail client (e.g., Outlook)
TLS (Transport Layer Security)
    a protocol that encrypts email messages for security and privacy

MTP (Media Transfer Protocal)
PTP (Picture Transfer Protocal)




### access usb path in wsl
- cd /mnt
- sudo mkdir f
- sudo mount -t drvfs F: f
    - (NOTE: F: was the name of my usb drive)








## Steps to Get an SSL Certificate

1. **Choose the Type of SSL Certificate**
   - Domain Validated (DV)
   - Organization Validated (OV)
   - Extended Validation (EV)

2. **Generate a Certificate Signing Request (CSR)**
   - On Apache (Linux):
     ```bash
     openssl req -new -newkey rsa:2048 -nodes -keyout yourdomain.key -out yourdomain.csr
     ```
   - On IIS (Windows):
     1. Open IIS Manager.
     2. Select the server name.
     3. Double-click “Server Certificates.”
     4. Click “Create Certificate Request…”
     5. Fill in the required fields.
     6. Save the CSR file.

3. **Choose a Certificate Authority (CA)**
   - Let’s Encrypt
   - DigiCert
   - GlobalSign
   - Comodo

4. **Submit the CSR to the CA**
   - Copy the contents of your CSR file.
   - Paste it into the CA’s web form.
   - Verify domain ownership.

5. **Install the SSL Certificate**
   - On Apache (Linux):
     ```plaintext
     <VirtualHost *:443>
         ServerName yourdomain.com
         DocumentRoot /var/www/yourdomain

         SSLEngine on
         SSLCertificateFile /path/to/yourdomain.crt
         SSLCertificateKeyFile /path/to/yourdomain.key
         SSLCertificateChainFile /path/to/CA_bundle.crt
     </VirtualHost>
     ```
     - Restart Apache:
       ```bash
       sudo service apache2 restart
       ```
   - On IIS (Windows):
     1. Open IIS Manager.
     2. Select the server name.
     3. Double-click “Server Certificates.”
     4. Click “Complete Certificate Request…”
     5. Locate your certificate file and provide a friendly name.
     6. Bind the SSL certificate to your site:
        - Select the site.
        - Click “Bindings…”
        - Click “Add…”
        - Select “https” and choose your SSL certificate from the dropdown.






In a terminal, you can:

Navigate the file system (cd, ls, pwd).
Manipulate files and directories (cp, mv, mkdir, rm).
Search and manipulate file content (grep, sed, awk).
Download files from the internet (wget, curl).
Monitor system resources and processes (top, ps, free).
Manage system services and processes (systemctl, kill).
Use network utilities (ping, ssh, scp).
Manage packages and software (apt, yum, pip).
Access and manipulate databases (mysql, psql).
Write and execute scripts (bash, python).
Use version control systems (git).
And much more, depending on the installed programs and scripts.