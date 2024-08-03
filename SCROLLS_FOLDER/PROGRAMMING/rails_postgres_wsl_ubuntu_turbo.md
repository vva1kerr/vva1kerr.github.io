<!-- C:\Users\razer\Desktop\walkerrh.github.io\SCROLLS_FOLDER\PROGRAMMING\rails_postgres_wsl_ubuntu_turbo.md -->




[Home](/index.html)

# Setup Ruby on Rails with Postgresql for Hotrails

### Resources:

* [The Turbo Rails Tutorial](https://www.hotrails.dev/)

1. Install WSL with Ubuntu

Open PowerShell and run:

```sh
wsl --install -d Ubuntu
```

2. Open Ubuntu


Once installed, open Ubuntu from the Start menu or by typing:

```sh
ubuntu
```

3. Update package manager

```sh
sudo apt update
```

4. Install postgresql dependency packages

```sh
sudo apt install libpq-dev
```

5. Install postgresql

```sh
sudo apt install postgresql postgresql-contrib
```

6. Run checks on postgresql

```sh
sudo systemctl start postgresql

sudo systemctl enable postgresql

sudo systemctl status postgresql
```

7. Run postgres

```sh
sudo -i -u postgres
```

8. Check postgresql version

```sh
SELECT version();
```

9. psql

```sh
psql
```

10. Check for existing users

```sh
\du 
```

11. Create a non root user

```sh
CREATE ROLE unix_wrh WITH LOGIN CREATEDB;

ALTER ROLE unix_wrh CREATEROLE;
```

12. exit

```sh
\q 
```

13. exit

```sh
exit 
```

14. check version again

```sh
psql --version
```

15. create rails app with postgresql

```sh
rails new quote-editor --css=sass --javascript=esbuild --database=postgresql
```

16. setup the environment

```sh
bin/setup
```

17. update the Gemfile

```sh
gem "turbo-rails", "~> 1.0"
```

18. install rails bundle

```sh
bundle install
```

19. launch site

```sh
bin/dev
```

