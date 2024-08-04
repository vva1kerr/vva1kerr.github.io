


Generating a new SSH key and adding it to the ssh-agent - GitHub Docs 

Adding a new SSH key to your GitHub account - GitHub Docs

Following the guide bellow allows you to develop in both the WSL Linux environment and on the Windows Environment while being able to access both through WSL and push repo apps to GitHub. No need to switch to other terminals than the WSL bash. No need to add SSH Keys outside of WSL.

# 1. Open WSL

## 2. Enter the WSL .ssh Folder
```bash
$ cd ~/.ssh
```
Takes you to the path /home/<username>/.ssh/

## 3. Enter/Rename the file to save
```bash
$ (/home/username/.ssh/id_rsa): id_rsa_wsl_razer
```

## 4. Paste the text below, replacing the email used in the example with your GitHub email address.
```bash
$ ssh-keygen -t ed25519 -C "your_email@example.com"
```
## 5. Check Key Ownership
```bash
$ ls -l id_rsa_wsl_razer
```
## 6. View your public key
```bash
$ cat ~/.ssh/id_rsa.pub
```

## 7. Verify the SSH key is loaded by the SSH agent
```bash
$ ssh-add -l
```
## 8. Adjust Permission to Only Allow Owner Access
```bash
$ chmod 600 id_rsa_wsl_razer
```

## 9. Add the SSH Key to the SSH Agent
```bash
$ ps aux | grep ssh-agent
$ killall ssh-agent
$ eval "$(ssh-agent -s)"
$ ssh-add id_rsa_wsl_razer
```

## 10. Open Powershell as Administrator

## 11. Go to .ssh Folder
```bash
$ cd C:\Users\razer\.ssh 
```

## 12. Create Symbolic Links To The Windows .ssh Directory
```bash
$ New-Item -ItemType SymbolicLink -Path C:\Users\razer\.ssh\id_rsa_wsl_razer -Target \\wsl$\Ubuntu\home\unix_wrh\.ssh\id_rsa_wsl_razer
$ New-Item -ItemType SymbolicLink -Path C:\Users\razer\.ssh\id_rsa_wsl_razer.pub -Target \\wsl$\Ubuntu\home\unix_wrh\.ssh\id_rsa_wsl_razer.pub
```

## 13. Reopen WSL And Open The .ssh Folder
```bash
$ /home/username/.ssh/
```

## 14. Copy The Key Value
```bash
cat id_rsa_wsl_razer.pub
```

## 15. Open GitHub
Navigate to Settings → SSH and GPG Keys → New SSH Key

## 16. Enter Values

Title: id_rsa_wsl_razer
Key: <paste step 11>

## 17. Click Add SSH Key

## 18. Open WSL

## 19. Open Your Windows repo
```bash
$ cd /mnt/c/Users/<username>/Desktop/<repo>
```

## 20. Establish The Repo And Start Pushing
```bash
$ rm -rf ".git"
$ git init
$ git remote -v
$ git remote add origin git@github.com:<githubusername>/<repo>.git
$ git branch -M main
$ git add .
$ git commit -m "explain changes"
$ git push origin main
```

# NOTE:

I’ve found that the ssh-agent will need to be established each time:

1. A new terminal is opened

2. And a connection to GitHub is tried

In short, you can simply type this to 'fix” it ssh-add ~/.ssh/<TheKeyYouMade>

As WSL searches the Linux environment by default, it will search, attempt, and add the key you stored in the following folder:
```bash
/home/<username>/.ssh/ 
```

Also in WSL, 

if viewing from Windows into Linux the path is:
```bash
\\wsl$\Ubuntu\home\<username>\
```

if viewing from Linux into Windows the path is
```powershell
/mnt/c/Users/<username>/
```
