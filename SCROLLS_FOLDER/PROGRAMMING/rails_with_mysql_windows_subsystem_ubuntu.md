<!-- C:\Users\razer\Desktop\walkerrh.github.io\SCROLLS_FOLDER\PROGRAMMING\rails_with_mysql_windows_subsystem_ubuntu.md -->




[Home](/index.html)

## Guides to pull up:

* [Getting Started with Rails](https://guides.rubyonrails.org/getting_started.html)
* [Install Ruby On Rails on Windows 11](https://gorails.com/setup/windows/11)
* [Install and configure a MySQL server](https://ubuntu.com/server/docs/install-and-configure-a-mysql-server)
* [Github SSH keys](https://github.com/settings/keys)
* [How do I uninstall MySQL?](https://askubuntu.com/questions/172514/how-do-i-uninstall-mysql)
* [MySQL root password change](https://stackoverflow.com/questions/7534056/mysql-root-password-change)
* [Rails and Mysql2 Access denied for user 'root'@'localhost' (using password: NO)](https://stackoverflow.com/questions/21719738/rails-and-mysql2-access-denied-for-user-rootlocalhost-using-password-no)
* [Reset a MySQL root password](https://docs.rackspace.com/docs/reset-a-mysql-root-password)

# Setting Up Rails with MySQL on a Windows Machine Using WSL (Ubuntu)

Follow these steps to set up a Rails development environment with MySQL on a Windows machine using the Windows Subsystem for Linux (WSL) with Ubuntu.

## Step 1: Install WSL with Ubuntu

### Open PowerShell and run:

```sh
wsl --install -d Ubuntu
```

## Step 2: Open Ubuntu

### Once installed, open Ubuntu from the Start menu or by typing:

```sh
ubuntu
```

## Step 3: Install Required Packages

### Update the package list and install necessary dependencies:

```sh
sudo apt-get update
sudo apt-get install git-core zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev software-properties-common libffi-dev
```

## Step 4: Install ASDF

### Clone the ASDF repository and set it up:

```sh
cd
git clone https://github.com/excid3/asdf.git ~/.asdf
echo '. "$HOME/.asdf/asdf.sh"' >> ~/.bashrc
echo '. "$HOME/.asdf/completions/asdf.bash"' >> ~/.bashrc
echo 'legacy_version_file = yes' >> ~/.asdfrc
echo 'export EDITOR="code --wait"' >> ~/.bashrc
exec $SHELL
```

## Step 5: Add ASDF Plugins for Ruby and Node.js

### Add the ASDF plugins for Ruby and Node.js:

```sh
asdf plugin add ruby
asdf plugin add nodejs
```

## Step 6: Install Ruby

### Install and set the global version of Ruby:

```sh
asdf install ruby 3.3.2
asdf global ruby 3.3.2
```

### Update to the latest Rubygems version:

```sh
gem update --system
```

### Verify the Ruby installation:

```sh
which ruby
ruby -v
```

## Step 7: Install Node.js

### Install and set the global version of Node.js:

```sh
asdf install nodejs 20.14.0
asdf global nodejs 20.14.0
```

### Verify the Node.js installation:

```sh
which node
node -v
```

### Install Yarn globally:

```sh
npm install -g yarn
```

## Step 8: Configure Git

### Configure Git with your user details:

```sh
git config --global color.ui true
git config --global user.name "YOUR NAME"
git config --global user.email "YOUR@EMAIL.com"
```

### Generate an SSH key:

```sh
ssh-keygen -t ed25519 -C "YOUR@EMAIL.com"
```

### Display the SSH key and add it to your GitHub account:

```sh
cat ~/.ssh/id_ed25519.pub
```

### Test the SSH connection to GitHub:

```sh
ssh -T git@github.com
```

### You should see a message like:

```vbnet
Hi YOURUSERNAME! You've successfully authenticated, but GitHub does not provide shell access.
```

## Step 9: Install Rails

## Install Rails:

```sh
gem install rails -v 7.1.3.4
```

### Verify the Rails installation:

```sh
rails -v
```

## Step 10: Install MySQL

### Install MySQL server:

```sh
sudo apt install mysql-server
```

### Check the status of the MySQL service:

```sh
sudo service mysql status
```

### Check if MySQL is listening for connections:

```sh
sudo ss -tap | grep mysql
```

## Step 11: Install MySQL Client Library and Gem

### Install the MySQL client development libraries:

```sh
sudo apt-get install libmysqlclient-dev
```

### Install the mysql2 gem:

```sh
gem install mysql2
```

### Install all required gems:

```sh
bundle install
```

## 12 Launch rails server

### Create the database:

```sh
rails db:create
```

### Start the Rails server:

```sh
rails server
```

# Trouble shooting

If you encounter issues during setup, the following commands may help resolve them:

## Remove and Reinstall MySQL

### Remove MySQL and all associated files:

```sh
sudo apt-get remove --purge mysql-server mysql-client mysql-common
```

### Remove unnecessary packages and clean up:

```sh
sudo apt-get autoremove
sudo apt-get autoclean
```

### Remove MySQL configuration and data directories:

```sh 
sudo rm -rf /etc/mysql /var/lib/mysql
```

### Reinstall MySQL:

```sh
sudo apt-get install mysql-server mysql-client
```

## Stop the MySQL Daemon

### To stop the MySQL daemon:

```sh
sudo mysqld stop
```

## Create MySQL Directory and Set Permissions

### Create the MySQL directory and set the correct permissions:

```sh
sudo mkdir -p /var/run/mysqld
sudo chown mysql:mysql /var/run/mysqld
```

## Start MySQL in Safe Mode

### Start MySQL without loading the grant tables to bypass authentication:

```sh
sudo mysqld_safe --skip-grant-tables &
```

## Log in to MySQL as Root

### Log in to MySQL as the root user without password:

```sh
mysql -u root
```

## Stop MySQL Service

### Stop the MySQL service using different commands:

```sh
sudo service mysql stop
sudo /etc/init.d/mysql stop
sudo killall -9 mysqld
sudo kill -9 < mysqld id >
```

## Start MySQL Service

### Start the MySQL service:

```sh
sudo service mysql start
```

## Check MySQL Status

### Check the status of the MySQL service:

```sh
sudo service mysql status
```

### Check if MySQL is listening for connections:

```sh
sudo ss -tap | grep mysql
```

## View MySQL Error Log

### View the last 50 lines of the MySQL error log:

```sh
sudo tail -n 50 /var/log/mysql/error.log
```

## List MySQL Processes

### List all MySQL-related processes:

```sh
ps aux | grep mysql
```

## Log in to MySQL with Password

### Log in to MySQL as root with the password:

Enter the password when prompted.

```sh
mysql -u root -p
```

## Reset MySQL Root Password

### Create the MySQL directory and set the correct permissions:

```sh
sudo mkdir -p /var/run/mysqld
sudo chown mysql:mysql /var/run/mysqld
```

### Log in to MySQL:

```sh
mysql -u root
```

### Run the following SQL commands to reset the root password:

```sh
USE mysql;
UPDATE user SET plugin='mysql_native_password' WHERE user='root';
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
FLUSH PRIVILEGES;
```

### Exit the MySQL shell:

```sql
quit
```


