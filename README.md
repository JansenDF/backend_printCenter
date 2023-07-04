# backend_printCenter
Backend do Projeto PrintCenter

### Montar projeto local


Instalar requirements.txt
```
pip install -r requirements.txt
```

### Montando o ambiente:

```bash
git clone https://github.com/jansen/backend_printCenter.git
cd backend_printCenter
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Variaaveis de ambiente relacionadas ao FLASK:
export FLASK_APP=manage.py
export FLASK_DEBUG=true

```
### Inicialização do Banco:

```bash
flask db init
flask db migrate -m 'init'
flask db upgrade
```
### Inicialização do backend:
```bash
flask run
```

### Testes

```bash
flask test
```
