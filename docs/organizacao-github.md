# Organização de pastas para GitHub

## Objetivo

Organizar os projetos locais de forma clara, para que cada pasta tenha um propósito definido e fique mais fácil de publicar no GitHub.

## Estrutura recomendada

```text
FASUP/
├── atividade-disciplina-denisson-gabrielaalmeida/
├── condigos.py/
├── estudos/
├── projgithub/
├── docs/
└── README.md
```

## Como usar

### 1. Um projeto = uma pasta = um repositório
Se uma pasta for um projeto independente, ela deve virar um repositório próprio no GitHub.

### 2. Organizar por categoria
- faculdade: atividades e trabalhos acadêmicos
- estudos: exercícios, anotações e aprendizado
- projetos-pessoais: ideias e experimentos próprios
- docs: documentação e planos

### 3. Nomear pastas com clareza
Use nomes curtos, em minúsculas e sem espaços.

Exemplos:
- atividade-disciplina-denisson-gabrielaalmeida
- condigos-python
- estudos-web
- projeto-pessoal

### 4. Adicionar README em cada projeto
Cada repositório deve ter um README com:
- descrição do projeto
- tecnologias usadas
- como executar
- autor ou disciplina

### 5. Manter apenas arquivos relevantes
Evite salvar:
- arquivos temporários
- pastas de build desnecessárias
- arquivos pesados sem necessidade

## Fluxo básico no GitHub

```bash
git init
git add .
git commit -m "Primeiro commit"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
git push -u origin main
```

## Sugestão prática para o seu caso

- [atividade-disciplina-denisson-gabrielaalmeida](../atividade-disciplina-denisson-gabrielaalmeida) → repositório de faculdade
- [condigos.py](../condigos.py) → repositório de exercícios e scripts em Python
- [estudos](../estudos) → repositório de estudos e práticas
- [projgithub](../projgithub) → repositório de projetos pessoais
