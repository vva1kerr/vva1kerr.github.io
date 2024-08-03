<!-- C:\Users\razer\Desktop\walkerrh.github.io\SCROLLS_FOLDER\PROGRAMMING\keyboard_shortcuts.md -->




[Home](/index.html)

# WINDOWS

* CTRL + c = copy
* CTRL + v = paste
* CTRL + s = save
* CTRL + f = find
* alt + space (system search)
* Windows key + Down arrow (minimize window)
* Windows key + Up arrow (maximize window)
* Windows key + SHIFT + TAB (rotate between windows)


# CHROME

* CTRL + t = new tab
* CTRL + k = open search on tab
* CTRL + w = close tab
* CTRL + num = go to open tab
* Ctrl + n (open a new window)
* Ctrl + Shift + t (Reopen previously closed tabs in the order they were closed)
* Ctrl + Tab (Jump to the next open tab)
* alt + f (quit chrome)

# VSCODE [LINK](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)

* File > Preferences > Keyboard Shortcuts (get to keyboard shortcuts in vscode)
* CTRL + N = open a new script
* CTRL + O = open a a file
* CTRL + l = select line
* CTRL + d = select word
* CTRL + ` = open & close terminal
* CTRL + SHIFT + V (preview of file in VSCODE)
* CTRL + B (close sidebar)

![](/assets/images/keyboard-shortcuts-windows.pdf)

# GITHUB [LINK](https://docs.github.com/en/get-started/accessibility/keyboard-shortcuts)

# GIT
* cd < into path folder to clone repo to >
* git clone "https://example-repo.com"
* cd < the repo folder > 
* git init
* git pull origin main
* git branch
* git pull origin main
* git status
* git add .
* git commit -m "what did you change"
* git pull
* git push origin main
<!-- * git config --global --add safe.directory C:/< path >/< to >/< repo > -->

## Github Copilot

* CTRL + ALT + I
* CTRL + I (inline chat, also terminal)    
* Alt + [ (left suggestion)
* Alt + ] (right suggestion)
* @workspace /new [ description ] (generates a new VS Code workspace)
* @workspace /newNotebook [ description ] (scaffolds a Jupyter notebook for task in description)
* @workspace /tests [ description ] (create unit tests for specified code)
* @vscode (helps find relevent VS Code command)



### Set Up Git to Use a Different Username and Password

### Configure Git to use a different username for the remote repository:

* git config credential.username second-username

![alt text](readme-gif.gif)

## Powershell (5.1)

* ls
* dir
* where < file >
* Remove-Item $targetDir -Recurse -Force
* mv
* ping (test reachability host on IP)
* ipconfig (displays all current TCP/IP network values, Dynamic Host Configuration Protocol, and DNS)
* netstat (displays network connections for Transmission Control Protocol and routing tables)
* tracert (diagnostic possible routes across IP)
    * map the path packets take to reach a destination
* nslookup (querying DNS mapping of domain name and IP)
* pathping (locate network loss and latency, includes windows NT)
* getmac (find a computer's MAC address)
* netsh (local or remote network configuration interface)

## Common Powershell Commands

* systeminfo (detailed system configuration information)
* Get-ComputerInfo (retrieve extensive system and OS properties)
* $PSVersionTable (PowerShell version and environment)
* Get-NetAdapter (network adapters on the system)
* hostname (device name)
* help < command >
* ls -Force (show hidden files)
* dir -Force (show hidden files)
* netsh wlan show interfaces (check for wireless interfaces on the system)
* Shift + Fn + F10 (open terminal during setup)
* netsh wlan show networks mode=Bssid
* netsh interface ip show address
* netsh wlan show interfaces
* netsh wlan disconnect interface=Wi-Fi  
* netsh wlan connect interface=Wi-Fi name=OSA.io
* Get-ItemProperty HKLM:SOFTWARE\Microsoft\SQMClient | Select -ExpandProperty MachineID (device id)
* dsregcmd /status (device name and Azure AD device ID)
* netsh wlan show networks mode=Bssid (SSID info of WiFi)
* netsh interface show interface (get available Wi-Fi)
* netsh interface set interface name="Wi-Fi" admin=enable (turn on wifi)
* Win + x (get taskbar during setup)
* wmic memorychip get (RAM info)
* sudo lshw -C display
* nvidia-smi

## Command Prompt
* ver

## pip
* python -m pip install < package >

# Mac
* CMD + CTRL + OPTION + T = terminal (when setting up)
* CMD + CTRL + OPTION + C = command prompt (when setting up)
* ifconfig | grep ether (ifconfig)
* dig < domain.com > < mx OR tx > 

# Networking
* IP Address (Internet Protocol)
* IPv4 Address
    * ex. 192.168.1.1
    * 32-bit numeric 
    * four numbers, each 0 to 255
    * about 4.3 billion unique addresses (2^32)
    * does not have built-in security features
    * DHCP
* IPv6 Address
    * ex. 2001:0db8:85a3:0000:0000:8a2e:0370:7334
    * 128-bit alphanumeric
    * hexadecimal 
    * 340 undecillion addresses (2^128)
    * includes IPsec, end-to-end encryption
    * SLAAC
* TTL (Time To Live)
    * how many hops through a router a packet can make before it is discarded
* DNS (Domain Name System)
* A Record (Maps domain to IPv4 address)
* AAAA Record (Maps domain to IPv6 address)
* MX Record (Specifies mail servers for a domain)
* CNAME (Alias one domain to another)
* NS Record (Specifies authoritative DNS servers)
* TXT Record (Stores text information)
* SRV Record (Provides service-specific information)
* ICMP (Internet Control Message Protocol)

### URL Masking / Stealth Redirection / URL Hiding (Enabling URL masking will ensure that your visitors see the source URL and not the destination URL)
* Enabling URL Masking will serve a 'Frames' page to your browser. You can add TITLE and META tags for your 'Frames' page here. eg. < title > Your Webpage title can be mentioned here< /title > < meta name="keywords" CONTENT="Your comma-separated keywords are entered here" > < meta name="description" CONTENT="Enter website description here" >
* Enabling URL masking will serve a 'Frames' page to the browser. You may want to set an alternate < NOFRAMES > page content for search engines. Enter your HTML within < NOFRAMES >< /NOFRAMES > tags in the 'No Frames Page Content' box to set alternate page content.

### Sub Domain Forwarding
* Enabling Sub Domain Forwarding will forward a request made to http://subdomain.domain.com to http://yourdestinationurl/subdomain/

### Path Forwarding
* Enabling Path Forwarding will forward requests made to http://domain.com/some/path to http://yourdestinationurl/some/path

# Bash

* find command options starting/path expression



IPv4 Header (20 bytes)

+--------+--------+--------+--------+

| Version|  IHL   |  Type  |  Total   |

|        |        | of Ser | Length   |

+--------+--------+--------+--------+

|   Identification   |Flags|FragOff   |

+--------+--------+--------+--------+

|   TTL  | Protocol | Header Checksum |

+--------+--------+--------+--------+

|         Source IP Address           |

+--------+--------+--------+--------+

|       Destination IP Address        |

+--------+--------+--------+--------+

|           Options (if any)          |

+--------+--------+--------+--------+



# Bypass Wi-Fi during setup

* Shift + Fn + F10
* cd oobe
* Start BypassNRO.cmd
OR
* No@nothankyou.com
* na@na.com
OR
* Ipconfig /release
OR
* OOBE\BYPASSNRO 

# Create user/admin in terminal

* net user AdminAccountName Password123 /add (create account with terminal)
* wmic useraccount where name='AdminAccountName' get sid (get sid identifier via name)
* net localgroup administrators AdminAccountName /add (add user to admins)
* cd %windir%\system32\oobe 
* msoobe.exe (pulls up windows start menu)






# clone bitbucket repo to WSL
1. get wsl path
    * something like "\\Wsl$\Ubuntu\home\< user >\
2. change vscode settings
    * go to vscode settings
    * go to security
    * unclick Restrict UNCAccess
    * restart vscode
3. clone https link
    * open vscode welcome page
    * click "clone git repository"
    * enter link
    * paste wsl path in file explorer header






# Branching a Repository Without Affecting the Master Branch

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Create a new branch**:
    ```bash
    git checkout -b new-branch-name
    ```

3. **Verify you are on the new branch**:
    ```bash
    git branch
    ```

4. **Make changes and commit**:
    ```bash
    # Make your changes to files
    git add .
    git commit -m "Describe your changes"
    ```

5. **Push the new branch to the remote repository**:
    ```bash
    git push origin new-branch-name
    ```

### Best Practices

- **Regularly update your branch**:
    ```bash
    git checkout master
    git pull origin master
    git checkout new-branch-name
    git merge master
    ```

- **Create Pull Requests (PRs)** for merging changes into `master`.

- **Avoid direct commits to master**: Always work on feature branches and merge changes through PRs.












# Installing Ruby 3.3.0 Using `rbenv`

1. **Install dependencies**:
    ```bash
    sudo apt-get update
    sudo apt-get install -y build-essential libssl-dev libreadline-dev zlib1g-dev
    ```

2. **Install `rbenv`**:
    ```bash
    git clone https://github.com/rbenv/rbenv.git ~/.rbenv
    cd ~/.rbenv && src/configure && make -C src
    echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(rbenv init -)"' >> ~/.bashrc
    exec $SHELL
    ```

3. **Install `ruby-build` as an `rbenv` plugin**:
    ```bash
    git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build
    echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc
    exec $SHELL
    ```

4. **Install Ruby 3.3.0**:
    ```bash
    rbenv install 3.3.0
    ```

5. **Set Ruby 3.3.0 as the global version**:
    ```bash
    rbenv global 3.3.0
    ```

6. **Rehash `rbenv` shims**:
    ```bash
    rbenv rehash
    ```

7. **Verify the installation**:
    ```bash
    ruby -v
    ```




# Authenticate GitHub Account in Terminal to Avoid Entering Username and Password at Every Git Push

This works for both WSL and Git Bash, but you have to do the whole process for each

### Resources
* [StackOverflow](https://stackoverflow.com/questions/8588768/how-do-i-avoid-the-specification-of-the-username-and-password-at-every-git-push)

### Steps to Set Up SSH Authentication

1. **Create Encryption Key**
    * Open terminal and enter:
        ```bash
        ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
        ```
    * Note the path where the key is saved, then get the value using:
        ```bash
        cat <path_to_saved_public_key>
        ```

2. **Add Public Key to GitHub**
    * Go to [GitHub SSH and GPG keys](https://github.com/settings/keys)
    * Click "New SSH key"
    * Give it a descriptive title, and paste the public key into the "Key" box

3. **Set Up GitHub SSH in Terminal**
    * Verify current remote URLs:
        ```bash
        git remote -v
        ```
    * Add your SSH key to the ssh-agent:
        ```bash
        eval "$(ssh-agent -s)"
        ssh-add ~/.ssh/id_rsa
        ```  
    * Update the remote URL to use SSH:
        ```bash
        git remote set-url origin git@github.com:<username>/<repo>.git
        ``` 










# push an existing repository from the command line
```bash
git remote add origin https://github.com/Walkerrh/RAILSGUIDES-Blog.git
git branch -M main
git push -u origin main
```

