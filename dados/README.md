# Projeto de Dados com IA
Dia1 - Treinamento - Resumo

Contexto: sou trainee em desenvolvimento com IA. Estou no Dia 2 do plano de 7 dias.
Repositório GitHub: moniquesilva-oinc/projeto-dados-teste
Sistema: Windows

═══════════════════════════════════════
ROTINA DE COMANDOS — referência rápida
═══════════════════════════════════════

ABRIR CLAUDE NO TERMINAL:
claude

FLUXO COMPLETO A CADA SESSÃO DE TRABALHO:

1. Antes de começar — atualizar o local:
git pull origin main

2. Criar branch para a tarefa:
git checkout -b feat/nome-da-tarefa

3. A cada alteração concluída — commitar:
git add .
git commit -m "prefixo: descritivo do que foi feito"

PREFIXOS DE COMMIT:
feat:      Criou algo novo que executa       → feat: adiciona planilha financeira
fix:       Corrigiu algo errado              → fix: corrige formula saldo acumulado
docs:      Documentação, README, .md         → docs: adiciona claude.md
chore:     Organização, renomear, mover      → chore: organiza pastas do projeto
refactor:  Melhorou sem mudar o resultado    → refactor: simplifica formula somarproduto

REGRA: feat = arquivo que FAZ algo | docs = arquivo que EXPLICA algo

O QUE É UMA BRANCH:
- Branch é uma cópia de trabalho do projeto
- Você trabalha nela sem afetar o main
- Só vai para o main depois de revisada via PR
- git branch → mostra em qual branch você está (a com * é a atual)

O QUE É git add . :
- O Git não salva automaticamente o que você alterou
- git add . → prepara TUDO que foi alterado para o próximo commit
- git add arquivo.md → prepara só um arquivo específico
- Analogia: separar os itens que vão para a caixa antes de lacrar

O QUE É git commit:
- Salva um ponto na história do projeto
- É uma foto do projeto naquele momento
- Você pode voltar para qualquer foto se algo der errado
- Commite sempre que terminar algo que funciona — não espere terminar tudo

4. Subir a branch para o GitHub:
git push -u origin nome-da-branch

5. Criar o PR no GitHub (feito no site):
- base (destino): main
- compare (origem): nome-da-branch

6. Mergear o PR no GitHub (feito no site):
- Abrir o PR no GitHub
- Clicar em "Merge pull request"
- Clicar em "Confirm merge"

7. Sincronizar o main local após o merge:
git pull origin main

═══════════════════════════════════════
GIT — aprendizados
═══════════════════════════════════════
- Fluxo completo de equipe praticado desde o Dia 1: branch → push → PR → merge → pull
- PR: base = destino (main) / compare = origem (sua branch)
- Nunca push direto no main
- Commits pequenos e frequentes — cada commit é um ponto de retorno seguro

═══════════════════════════════════════
PROMPT ENGINEERING — aprendizados
═══════════════════════════════════════
- Técnica 1: Persona + Contexto + Formato + Restrições
- Técnica 3: Revisão crítica — erros lógicos, casos extremos, visão sênior
- Quanto mais contexto, melhor a resposta do Claude

═══════════════════════════════════════
LOOKER STUDIO + SHEETS — aprendizados e decisões
═══════════════════════════════════════
- Erro corrigido: Adm e Repasse CF usavam subtração (-) em vez de multiplicação (*)
- Adm: 30% NIJ e DIAG, 10% Geral | Repasse CF: 30% NIJ apenas até maio/2026
- Saldo Inicial 2025 adicionado como linhas na aba Lançamentos (30/12/2024)
- Saldo Acumulado por projeto: coluna G com SOMARPRODUTO
- Saldo Acumulado total geral: coluna H com SOMARPRODUTO sem filtro de projeto
- Repasse CF limitado até 31/05/2026 com DATA(2026;5;31) na fórmula
- Separador decimal no Sheets PT-BR é vírgula (0,6) não ponto (0.6)
- Looker: Saldo Acumulado por projeto usa agregação MAX
- Looker: total geral em scorecard separado com MAX, protegido de filtro de projeto
- Limitação aceita: seleção dinâmica de múltiplos projetos não é suportada nativamente

═══════════════════════════════════════
PENDENTE PARA O DIA 2
═══════════════════════════════════════
PRIORIDADE — praticar o fluxo abaixo pelo menos 4 vezes:

RODADA 1:
git pull origin main
git checkout -b docs/adiciona-anotacoes-dia1
git add .
git commit -m "docs: adiciona anotacoes do dia 1"
git push -u origin docs/adiciona-anotacoes-dia1
→ PR no GitHub → merge → git pull origin main

RODADA 2:
git pull origin main
git checkout -b feat/adiciona-script-limpeza
git add .
git commit -m "feat: adiciona script de limpeza de dados"
git push -u origin feat/adiciona-script-limpeza
→ PR no GitHub → merge → git pull origin main

RODADA 3:
git pull origin main
git checkout -b fix/corrige-formula-saldo
git add .
git commit -m "fix: corrige separador decimal na formula saldo acumulado"
git push -u origin fix/corrige-formula-saldo
→ PR no GitHub → merge → git pull origin main

RODADA 4:
git pull origin main
git checkout -b chore/organiza-pastas
git add .
git commit -m "chore: organiza estrutura de pastas do projeto"
git push -u origin chore/organiza-pastas
→ PR no GitHub → merge → git pull origin main

DEMAIS PENDÊNCIAS DO DIA 2:
- Instalar Claude Code.
- Criar primeira Skill.
- Aprender VSCode avançado para dados.

## Aprendizados Dia 1
- Fluxo Git: branch → commit → push → PR → merge → pull
- Conventional Commits: feat / fix / docs / chore / refactor
- SOMARPRODUTO para saldo acumulado por projeto no Sheets
- Separador decimal no Sheets PT-BR é vírgula, não ponto