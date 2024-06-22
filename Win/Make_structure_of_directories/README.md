# Matrure
É um programa executável que encontra-se na pasta "dist", usado para criar uma estrutura de pastas e arquivos de forma rápida, poupando trabalho e deixando o seu projeto mais organizado.
 - Para que ele desempenhe todas as funções corretamente não é preciso executá-lo como administrador.
 - Ou seja, executando ele com dois cliques é possível usá-lo normalmente.
 - É preciso de um arquivo onde a hierarquia é indicada por indentação com espaços, e os arquivos e diretórios são representados como uma árvore.

### Orientação sobre o arquivo usado
 1. Indentação com Espaços: A função calcula o nível de cada linha com base no número de espaços (4 espaços por nível neste exemplo).
 2. Hierarquia de Diretórios: path_atual é atualizado conforme o nível de indentação.
 3. Criação de Pastas e Arquivos:
    - Pastas terminam com / e são criadas com os.makedirs.
    - Arquivos são criados com conteúdo padrão dependendo da extensão (.md e .ps1).

## Como Usar
 1. Arquivo de Entrada: Crie um arquivo estrutura.txt com a estrutura desejada.
 2. Executar o Script: Execute o script Python ou o arquivo executável, certificando-se de que ele está apontando para o caminho correto do arquivo estrutura.txt.
    - Deixei um arquivo com uma estrutura como exemplo nessa mesma pasta para servir de modelo de como você deve criar o seu arquivo.
    - Dica: Você pode pedir para o ChatGPT ou outra IA criar uma estrutura seguindo esse modelo para você. Depois basta copiar o conteúdo para um arquivo .txt e rodar o programa Matrute para que ele transforme sua ideia em uma estrutura de projeto incrível.

## Proposito
Afim de otimizar o tempo das pessoas que precisam ficar arrastando pasta por pasta, arquivo por arquivo, de um lugar para o outro, com esse programa você deixa tudo em uma pasta raíz e depois manda para outro diretório que queira guardar. Seja em outro HD, ou no drive do Google instalado na máquina, ou pendrive, etc..