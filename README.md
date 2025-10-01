# task.py

Script CLI em Python para gerenciar tarefas com armazenamento em JSON.

## 📦 Comandos

- `python taks.py add <desc> <id>`  
  Adiciona uma nova tarefa.

- `python taks.py update <id> --description <nova_desc>`  
  Atualiza a descrição de uma tarefa.

- `python taks.py update <id> --status <todo|done|in-progress>`  
  Atualiza o status da tarefa.

- `python taks.py delete <id>`  
  Deleta uma tarefa (com confirmação via prompt).

- `python taks.py reader all`  
  Lista todas as tarefas salvas.

- `python taks.py reader <id>`  
  Exibe os detalhes de uma tarefa específica.

## 💻 Exemplo de uso

```bash
python task.py add "Estudar Python" 1
python task.py update 1 --status done
python task.py reader all
```
https://roadmap.sh/projects/task-tracker
