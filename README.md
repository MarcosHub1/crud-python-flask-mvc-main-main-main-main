
# Documentação Tecnica BomPraPet

### - Objetivos do Projeto:

Este projeto tem o objetivo de desenvolver e implementar um software voltado para petshops e organizações de proteção animal, com foco na gestão de cadastros, processos de adoção e histórico de saúde dos animais. O projeto busca organizar informações de forma eficiente, permitindo acesso seguro e atualizado por estabelecimentos, tutores e potenciais adotantes.

O sistema também visa aprimorar a comunicação entre os envolvidos no cuidado animal, tornando o processo de adoção mais transparente e responsável. Com isso, contribui para a conscientização sobre a guarda responsável e apoia ações de prevenção ao abandono, integrando tecnologia e bem-estar animal.

### - Justificativa:

Este software é voltado ao incentivo da guarda responsável. Além de aprimorar os processos internos das instituições, o sistema tem como finalidade melhorar a comunicação entre tutores, profissionais e organizações, estimulando ações de prevenção e cuidado contínuo. Assim, a tecnologia deixa de ter um papel apenas operacional e passa a contribuir diretamente para a diminuição de casos de abandono e negligência.




## Linguagens de Programação:

### Programming Languages
**Python (Version 3.12.4)**

- Python é a linguagem principal utilizada no backend da aplicação. Ela oferece uma sintaxe simples, alto nível de legibilidade e uma ampla coleção de bibliotecas, o que facilita o desenvolvimento de sistemas web.
No contexto desta solução, Python é responsável por gerenciar rotas, processar requisições e renderizar páginas usando Flask.
Sua leveza e eficiência fazem dele uma escolha ideal para aplicações que precisam ser executadas em ambientes com hardware reduzido e que exigem respostas rápidas do servidor.

### Frontend Interactivity
**Alpine.js** 

- Alpine.js é o framework JavaScript utilizado no frontend para adicionar interatividade leve e direta aos templates HTML renderizados pelo Flask.
Ele funciona por meio de atributos inseridos no próprio HTML, tornando desnecessário o uso de arquivos JavaScript separados.
- No contexto desta aplicação, Alpine.js é essencial principalmente para funcionalidades como: gerenciamento de estado simples na interface, controle de exibição de elementos, manipulação de eventos diretamente nos componentes, pré-visualização de arquivos de imagem escolhidos pelo usuário antes do envio.
- Essa última capacidade — pré-visualizar imagens — permite que o usuário selecione um arquivo e veja imediatamente o conteúdo sem recarregar a página, garantindo uma experiência mais fluida e intuitiva.
Com comandos como x-on:change e x-bind:src, Alpine.js identifica o arquivo selecionado e atualiza dinamicamente a imagem exibida na interface.
- Sua abordagem minimalista torna-o perfeito para projetos pequenos e médios, oferecendo comportamento moderno sem a complexidade de frameworks maiores.

## Estrutura:

**Framework
Flask**

- Flask é um microframework Python utilizado para construir aplicações web leves e modulares.
Ele fornece os componentes fundamentais para definir rotas, processar requisições HTTP e renderizar templates HTML por meio do motor de templates Jinja2.
- Por ser minimalista, Flask permite uma estrutura flexível onde a lógica da aplicação pode ser concentrada diretamente nos arquivos de rota, sem necessidade de camadas adicionais como controllers separados.
Isso torna o desenvolvimento mais rápido e facilita a manutenção do código, sendo ideal para aplicações web de baixa e média complexidade, APIs simples e projetos que exigem agilidade no desenvolvimento.

## Linguagens de Marcação:

**Markup Languages
HTML**

- HTML (HyperText Markup Language) é a linguagem responsável pela estrutura de todas as páginas da aplicação.
No Flask, o HTML é renderizado dinamicamente através de templates Jinja2, permitindo a inserção de dados, repetição de elementos e componentes reutilizáveis.
Ele define toda a organização das páginas — formulários, tabelas, botões e imagens — servindo como base da camada visual do sistema.

**Tailwind CSS**

- Tailwind CSS é um framework de estilização baseado em classes utilitárias, permitindo que o estilo seja aplicado diretamente no HTML sem a necessidade de arquivos CSS extensos.
Ele oferece classes prontas para controle de layout, espaçamento, tipografia, cores e responsividade, tornando o desenvolvimento visual mais rápido e padronizado.
- Sua integração com Flask é direta: ao aplicar as classes nos templates HTML, o desenvolvedor obtém páginas consistentes, modernas e de fácil manutenção.
Essa abordagem reduz o tempo de desenvolvimento e mantém o visual da aplicação limpo e organizado.

## Protótipo:

### Figma

O Figma é uma solução online voltada para criação de interfaces e experiência do usuário, projetada para funcionar inteiramente na nuvem. Sua principal característica é permitir que equipes inteiras trabalhem juntas no mesmo arquivo, visualizando alterações em tempo real sem necessidade de envio de versões ou arquivos separados. A plataforma oferece ferramentas completas para desenho de layouts, criação de componentes padronizados, montagem de fluxos navegáveis e registro de feedback dentro do próprio projeto.

## Metodologia:

### **Scrum**

A metodologia **Scrum** é uma abordagem ágil que busca organizar e tornar mais eficiente a colaboração entre todos os participantes de um projeto. Seu objetivo principal é garantir que a equipe trabalhe de forma integrada, com comunicação clara e foco em entregar um produto de qualidade.

Ela é especialmente indicada para **ambientes dinâmicos e complexos**, onde os requisitos podem mudar rapidamente e é necessário ter flexibilidade para se adaptar a novas prioridades. O Scrum favorece esse tipo de contexto porque trabalha com ciclos curtos de desenvolvimento, permitindo ajustes constantes ao longo do processo.

Para funcionar de maneira eficaz, o Scrum se baseia em um conjunto de **papéis, eventos e artefatos**. Os papéis definem as responsabilidades de cada integrante; os eventos — como as Sprints, as reuniões diárias e as revisões — ajudam a manter o andamento do projeto organizado; e os artefatos, como o Product Backlog, garantem clareza sobre o que deve ser feito.

Assim, o Scrum oferece uma estrutura que facilita o trabalho em equipe, permite respostas rápidas a mudanças e contribui para um desenvolvimento ágil e de alta qualidade.

## Arquitetura:

### **Use Case Diagram**:

<img width="406" height="331" alt="image" src="https://github.com/user-attachments/assets/269e0c6b-a2da-40b3-a4b6-2071f4cbd61f" />

## Site maps:

<img width="512" height="316" alt="image (1)" src="https://github.com/user-attachments/assets/06b63dbd-838b-42e8-9da0-43bcc65a4d18" />

## User Flow:

<img width="1122" height="583" alt="image (2)" src="https://github.com/user-attachments/assets/3af1d1b7-fc83-4e79-911a-860e83d5dddc" />

<img width="1196" height="431" alt="image (3)" src="https://github.com/user-attachments/assets/bc6e958a-21d5-430b-99b8-49a79955c098" />

<img width="1120" height="422" alt="image (4)" src="https://github.com/user-attachments/assets/2573a940-d8a8-4ba0-8479-d1dbf843b692" />

<img width="688" height="360" alt="image (5)" src="https://github.com/user-attachments/assets/e45fe8e2-8a38-4f49-8c5e-7fcb90694e70" />

<img width="1540" height="508" alt="image (6)" src="https://github.com/user-attachments/assets/143232c7-0586-42b9-8d8d-8c4189405676" />

## Project process diagram:

<img width="897" height="632" alt="image (7)" src="https://github.com/user-attachments/assets/f6643a24-9aef-4009-8711-e9afbe4192af" />

## **Levantamento de Requisitos**

### REQUISITOS FUNCIONAIS:

Os requisitos funcionais descrevem o que um sistema deve fazer para atender às expectativas e necessidades do usuário. Estão diretamente relacionados às funções e operações que o sistema deve realizar, como processar informações ou executar tarefas específicas. Esses requisitos são a base para determinar como o sistema irá se comportar durante a interação com o usuário, garantindo que ele atenda aos seus objetivos de forma prática e eficiente.

Lista de Requisitos Funcionais

[RF001] – Permitir o registro de animais com informações como nome, espécie, raça, idade, sexo, estado de saúde e histórico veterinário.

[RF002] – Registrar dados dos tutores e adotantes, incluindo informações de contato, endereço e histórico de adoções.

[RF003] – Registrar vacinas, consultas, tratamentos e gerar alertas automáticos para próximas aplicações ou retornos veterinários.

[RF004] – Permitir a divulgação de animais disponíveis para adoção com fotos e perfil descritivo utilizando IA.

[RF005] – Enviar notificações ou lembretes aos tutores/adotantes.

[RF006] – Enviar alertas automáticos sobre vacinas, consultas, renovações e acompanhamento pós-adoção.

[RF007] – Permitir diferentes tipos de acesso (administrador, funcionário, voluntário).

[RF008] – Permitir a inclusão de casos de animais resgatados das ruas, com local, condições e responsável pelo resgate.

### REQUISITOS NÃO FUNCIONAIS:

Os requisitos não funcionais são basicamente as características e restrições que um sistema deve cumprir para garantir sua qualidade e desempenho. Não descreve o que o sistema faz, mas sim como o sistema deve operar. Questões como tempo de resposta, segurança, disponibilidade, compatibilidade e escalabilidade se encaixam neste contexto. Esses requisitos garantem que o sistema funcione de forma adequada, seja confiável e atenda aos padrões esperados pelos usuários e desenvolvedores.

Lista de Requisitos Não Funcionais

[RNF001] – O sistema deve responder às requisições do usuário para operações comuns (ex: consulta de produtos, agendamento, cadastro de cliente).

[RFN002] – O sistema de IA deve processar e identificar a imagem do animal e irá dizer se ele está em estado de abandono ou não.

[RNF003] – Os dados dos clientes e dos pets devem ser armazenados de forma criptografada no banco de dados.

[RNF004] – O sistema deve implementar autenticação e controle de acesso baseado em papéis.

[RNF005] – A interface deve ser intuitiva e responsiva, acessível em todas as redes de sites.

[RNF006] – O sistema deve utilizar design limpo e amigável, com ícones e cores que remetam ao universo pet.

[RNF007] – O sistema deve ter taxa de disponibilidade mínima de 99% durante o horário comercial.

[RNF008] – Deve realizar backups automáticos diários do banco de dados.

[RNF009] – Em caso de falha da IA, o sistema deve continuar operando com funcionalidades básicas.

[RNF010] – O sistema deve ser compatível com os navegadores mais utilizados (Chrome, Edge, Firefox).


## Componentes Principais:

- Login
- Cadastro
- Homepage
- Publicar um pet para adoção
- Ver quais os pets cadastrados
- Cadastro de animais para adoção



