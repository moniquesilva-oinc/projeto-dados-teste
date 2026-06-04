# CLAUDE.md

This file provides guidance to Claude Code and to the developer for working with this repository.

## Project

**Meu Projeto de Dados com IA** — an AI/data project in early scaffolding.

- Remote: `https://github.com/moniquesilva-oinc/projeto-dados-teste.git`
- Default branch: `main`
- Local path: `C:\Users\eMotion_1\projeto-dados-teste`

## GitHub workflow

Follow this flow for every task:

1. `git pull origin main`
2. `git checkout -b task/<jira-ticket>`
3. make small, focused changes
4. `git add .`
5. `git commit -m "<uma mensagem clara explicando o porquê da mudança>"`
6. `git push -u origin task/<jira-ticket>`
7. open a Pull Request on GitHub

## PR rules

- 1 tarefa Jira = 1 branch = 1 PR
- prefira PRs pequenos, idealmente < 200 linhas
- não faça push direto no `main`
- não misture refactor com funcionalidade nova no mesmo PR

## Credentials

- nunca commite `.env`
- adicione `.env` em `.gitignore`
- valide com `git check-ignore .env`
- antes de commit, confira `git status`

## Sync / automatic update

- O repositório remoto já existe e está configurado.
- GitHub só é atualizado depois que o branch local for empurrado (`git push`).
- Não há um mecanismo mágico que atualize o GitHub a cada edição sem você fazer o push.
- Se quiser, podemos adicionar um helper script local para facilitar o push após as mudanças.

## Notes

- commits pequenos e frequentes são melhores.
- remova código morto e imports não usados.
- comente só quando explicar o porquê ou documentar uma restrição oculta.
