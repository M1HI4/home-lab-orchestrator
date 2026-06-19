# DevOps Home Lab Orchestrator
Проект демонстрирует развёртывание локальной DevOps-инфраструктуры с
помощью Terraform, Python и Jenkins.
## Описание
- **WSL2 (Ubuntu)** – среда для запуска Linux на Windows.
-
**Terraform** – автоматизирует провиженинг локальной инфраструктуры (в
примере создаётся файл).
- **Python** – скрипты для проверки состояния системы (healthcheck) и
генерации отчёта.
- **Jenkins** – CI/CD-сервер для автоматизации пайплайна (линтинг,
Terraform, Python-скрипты).
- **Git + GitHub** – хранилище кода проекта и управление версиями.
## Структура проекта
- `terraform/` – Terraform-конфигурация (main.tf, variables.tf,
outputs.tf).
- `python/` – скрипты healthcheck.py и report.py.
- `Jenkinsfile` – конфигурация Jenkins-пайплайна.
- `README.md`, `.gitignore` и т.д.
## Установка и запуск
1. Установите WSL2 и Ubuntu (см. инструкцию в [Microsoft Learn](https://
learn.microsoft.com/en-us/windows/wsl/install)).
2. Ubuntu установите инструменты:
 ```bash
sudo apt update
sudo apt install -y git wget gnupg python3 python3-pip openjdk-11-
jre-headless
 ```
3. Установите Terraform:
 ```bash
wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor |
sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archivekeyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs)
main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install -y terraform
 ```
4. Установите Jenkins:
 ```bash
wget -qO /etc/apt/keyrings/jenkins-keyring.asc https://
pkg.jenkins.io/debian-stable/jenkins.io-2026.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc] https://
pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/
sources.list.d/jenkins.list
sudo apt update && sudo apt install -y jenkins
sudo systemctl start jenkins
 ```
5. Создайте репозиторий на GitHub и клонируйте его в WSL. Поместите в
него файлы проекта (Terraform, Python, Jenkinsfile и т.д.), затем
сделайте коммиты и пушите изменения.
## Как использовать
- **Jenkins**: откройте `http://localhost:8080`, настройте задачу
pipeline, укажите репозиторий и Jenkinsfile. Запустите сборку.
- **Terraform**: из каталога `terraform/` команды `terraform plan/
apply` создадут файл `output.txt`.
- **Python**: запустите `python3 healthcheck.py`, потом `python3
report.py`, чтобы увидеть отчёт о системе.
