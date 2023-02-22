# python - scraping - beautiful soup

## Introdução
Muitos projetos de análise de dados, big data, e aprendizado de máquina exigem o scraping de websites para coletar os dados com os quais você irá trabalhar. A linguagem de programação Python é largamente utilizada na comunidade de data science, e, portanto, tem um ecossistema de módulos e ferramentas que você pode usar em seus próprios projetos. Neste tutorial estaremos nos concentrando no módulo Beautiful Soup.

Beautiful Soup, uma alusão à música Mock Turtle’s encontrada no Capítulo 10 de Alice no País das Maravilhas, de Lewis Carroll, é uma biblioteca do Python que permite um retorno rápido em projetos de web scraping. Atualmente disponível como Beautiful Soup 4 e compatível tanto com Python 2.7 quanto com Python 3, o Beautiful Soup cria uma árvore de análise a partir de documentos HTML e XML analisados (incluindo documentos com tags não fechadas ou tag soup e outras marcações malformadas).

Neste tutorial, iremos coletar e analisar uma página web de forma a pegar dados textuais e gravar as informações que tivermos recolhido em um arquivo CSV.

# Pré-requisitos
Antes de trabalhar com este tutorial, você deve ter um ambiente de programação Python local ou baseado em servidor configurado em sua máquina.

Você deve ter os módulos Requests (pip install requests) e Beautiful Soup (pip install beautifulsoup4) instalados. 

Adicionalmente, uma vez que vamos trabalhar com dados extraídos da web, você deve estar confortável com a estrutura e a marcação de tags HTML.

# Entendendo os Dados
Neste tutorial, iremos trabalhar com dados do site oficial do National Gallery of Art nos Estados Unidos. O National Gallery é um museu de arte localizado no National Mall em Washington, D.C. Ele possui mais de 120.000 peças datadas desde o Renascimento aos dias atuais feitas por mais de 13.000 artistas.

Gostaríamos de pesquisar o Índice de Artistas, que, no momento da atualização deste tutorial, estava disponível via Internet Archive’s Wayback Machine na seguinte URL:

https://web.archive.org/web/20170131230332/https://www.nga.gov/collection/an.shtm

Nota: A longa URL acima é devido a este site ter sido arquivado pelo Internet Archive.

O Internet Archive é uma biblioteca digital sem fins lucrativos que fornece acesso livre a sites da internet e outras mídias digitais. A organização tira instantâneos de websites para preservar a história dos sites, e atualmente, podemos acessar uma versão mais antiga do site da National Gallery que estava disponível quando este tutorial foi escrito pela primeira vez. O Internet Archive é uma boa ferramenta para se ter em mente sempre que estiver fazendo qualquer tipo de scraping de dados históricos, incluindo a comparação entre iterações do mesmo site e dados disponíveis.

Logo abaixo do cabeçalho do Internet Archive, você verá uma página como esta:

<p align="center">
  <img alt="mulheres-vozes-escuta" src="./assets/img1.png" width="100%">
</p><br>

Como estamos fazendo esse projeto para aprender sobre o web scraping com o Beautiful Soup, não precisamos extrair muitos dados do site, por isso, vamos limitar o escopo dos dados do artista que estamos tentando capturar. Vamos, portanto, escolher uma letra — em nosso exemplo escolheremos a letra Z — e veremos uma página como esta:

<p align="center">
  <img alt="mulheres-vozes-escuta" src="./assets/img2.png" width="100%">
</p><br>

Na página acima, vemos que o primeiro artista listado no momento da escrita é Zabaglia, Niccola, o que é uma boa coisa a se notar quando começamos a extrair dados. Começaremos trabalhando com essa primeira página, com a seguinte URL para a letra Z:

https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ1.htm

É importante observar, para análise posterior, quantas páginas existem para a letra que você está escolhendo listar, o que você pode descobrir clicando na última página de artistas. Nesse caso, existe um total de 4 páginas, e o último artista listado no momento da escrita é Zykmund, Václav. A última página de artistas com Z tem a seguinte URL:

https://web.archive.org/web/20121010201041/http://www.nga.gov/collection/anZ4.htm

Contudo, você também pode acessar a página acima usando a mesma string numérica do Internet Archive da primeira página:

https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ4.htm

É importante observar isso, pois mais adiante neste tutorial faremos a iteração dessas páginas.

Para começar a se familiarizar com a forma que essa página web é configurada, você pode dar uma olhada em seu DOM, que o ajudará a entender como o HTML é estruturado. Para inspecionar o DOM, você pode abrir Ferramentas do Desenvolvedor do seu navegador.

# Importando as Bibliotecas
Para iniciar nosso projeto de codificação, vamos ativar nosso ambiente de programação. Certifique-se de que você está no diretório onde o seu ambiente de desenvolvimento está localizado, e execute o seguinte comando.

my_env/bin/activate

Com o nosso ambiente de programação ativado, vamos criar um novo arquivo, com o nano por exemplo. Você pode nomear seu arquivo como quiser, vamos chamá-lo de nga_z_artists.py nesse tutorial.

nano nga_z_artists.py

Nesse arquivo, podemos começar a importar as bibliotecas que iremos utilizar — Requests e Beautiful Soup.

A biblioteca Requests lhe permite fazer uso do HTTP dentro dos seus programas Python em um formato legível, e o módulo Beautiful Soup é projetado para fazer web scraping rapidamente.

Vamos importar tanto o Requests quanto o Beautiful Soup com a declaração import. Para o Beautiful Soup iremos importá-lo do bs4, o pacote no qual o Beautiful Soup 4 é encontrado.

Com os módulos Requests e Beautiful Soup importados, podemos passar a trabalhar para coletar primeiro uma página e analisá-la.

# Coletando e Analisando uma Página Web

O próximo passo que precisaremos fazer é coletar a URL da primeira página web com o Requests. Iremos atribuir a URL da primeira página à variável page usando o método requests.get().

Nota: Como a URL é longa, o código acima, bem como todo este tutorial não passarão no PEP 8 E501, que sinaliza linhas com mais de 79 caracteres. Você pode querer atribuir a URL a uma variável para tornar o código mais legível nas versões finais. O código neste tutorial é para fins de demonstração e permitirá que você troque URLs mais curtas como parte de seus próprios projetos.

Agora iremos criar o objeto BeautifulSoup, ou uma árvore de análise. Esse objeto utiliza como argumento o documento page.text do Requests (o conteúdo da resposta do servidor) e então o analisa através do html.parser interno do Python.

Com a nossa página coletada, analisada e configurada como um objeto BeautifulSoup, podemos passar para a coleta dos dados que gostaríamos.

# Pegando Texto de uma Página Web

Para este projeto, iremos coletar nomes de artistas e os links relevantes disponíveis no website. Você pode querer coletar dados diferentes, tais como a nacionalidade dos artistas e datas. Para quaisquer dados que você queira coletar, você precisa descobrir como ele é descrito pelo DOM da página web.

Para fazer isso, no seu navegador web, clique com o botão direito — ou CTRL + clique no macOS — no nome do primeiro artista, Zabaglia, Niccola. Dentro do menu de contexto que aparece, você deve ver um item de menu semelhante ao Inspecionar Elemento (Firefox) ou Inspecionar (Chrome).

<p align="center">
  <img alt="mulheres-vozes-escuta" src="./assets/img3.png" width="100%">
</p><br>

Após clicar no item de menu relevante Inspecionar, as ferramentas para desenvolvedores web devem aparecer no seu navegador. Queremos procurar pela classe e as tags associadas aos nomes dos artistas nessa lista.

<p align="center">
  <img alt="mulheres-vozes-escuta" src="./assets/img4.png" width="100%">
</p><br>

Veremos primeiro que a tabela de nomes está dentro de tags <div> onde class="BodyText". É importante observar isso, para que só procuremos texto nessa seção da página web. Também notamos que o nome Zabaglia, Niccola está em uma tag de link, já que o nome faz referência a uma página web que descreve o artista. Então, vamos querer referenciar a tag <a> para links. O nome de cada artista é uma referência a um link.

Para fazer isso, iremos utilizar os métodos find() e find_all() do Beautiful Soup a fim de extrair o texto dos nomes dos artistas do BodyText <div>.

A seguir, na parte inferior do nosso arquivo de programa, criaremos um loop for para iterar todos os nomes de artistas que acabamos de colocar na variável artist_name_list_items.

Vamos imprimir esses nomes com o método prettify() para transformar a árvore de análise do Beautiful Soup em uma string Unicode bem formatada.

Vamos executar o programa como ele está até agora:

Assim que fizermos isso, receberemos a seguinte saída:

O que vemos na saída nesse ponto é o texto completo e as tags relativas a todos os nomes de artistas dentro de tags <a> encontradas na tag <div class="BodyText"> na primeira página, bem como algum texto de link adicional na parte inferior. Como não queremos essa informação extra, vamos trabalhar para remover isso na próxima seção.

# Removendo Dados Supérfluos

Até agora, conseguimos coletar todos os dados de texto do link dentro de uma seção <div> da nossa página web. No entanto, não queremos ter os links inferiores que não fazem referência aos nomes dos artistas. Por isso, vamos trabalhar para remover essa parte.

Para remover os links inferiores da página, vamos clicar novamente com o botão direito e Inspecionar o DOM. Veremos que os links na parte inferior da seção <div class="BodyText"> estão contidos em uma tabela HTML: <table class="AlphaNav">:

<p align="center">
  <img alt="mulheres-vozes-escuta" src="./assets/img5.png" width="100%">
</p><br>

Podemos, portanto, usar o Beautiful Soup para encontrar a classe AlphaNav e usar o método decompose() para remover uma tag da árvore de análise e depois destruí-la juntamente com seu conteúdo.

Usaremos a variável last_links para fazer referência a esses links inferiores e adicioná-los ao arquivo do programa:

Agora, quando executarmos o programa com o comando python nga_z_artist.py, receberemos a seguinte saída:

Nesse ponto, vemos que a saída não inclui mais os links na parte inferior da página web e agora exibe apenas os links associados aos nomes dos artistas.

Até agora, focamos especificamente os links com os nomes dos artistas, mas temos os dados de tags extras que realmente não queremos. Vamos remover isso na próxima seção.

# Pegando o Conteúdo de uma Tag
Para acessar apenas os nomes reais dos artistas, queremos focar no conteúdo das tags <a> em vez de imprimir toda a tag de link.

Podemos fazer isso com o .contents do Beautiful Soup, que irá retornar a tag filha com um tipo de dados lista do Python.

Vamos revisar o loop for para que, em vez de imprimir o link inteiro e sua tag, façamos a impressão da lista das filhas (ou seja, os nomes completos dos artistas).

Note que estamos iterando na lista acima chamando o número do índice de cada item.

Podemos executar o programa com o comando python para ver a seguinte saída:

Recebemos de volta uma lista de todos os nomes dos artistas disponíveis na primeira página da letra Z.

Mas, e se quisermos também capturar as URLs associadas a esses artistas? Podemos extrair URLs encontradas dentro de tags <a> utilizando o método get('href') do Beautiful Soup.

A partir da saída dos links acima, sabemos que a URL inteira não está sendo capturada, então vamos concatenar a string do link com o início da string da URL (nesse caso https://web.archive.org/).

Estas linhas também serão adicionadas ao loop for:

Quando executamos o programa acima, receberemos tanto os nomes dos artistas quanto as URLs para os links que nos dizem mais sobre eles:

Embora estejamos agora recebendo informações do site, ele está apenas imprimindo em nossa janela de terminal. Em vez disso, vamos capturar esses dados para podermos usá-los em outro lugar, gravando-os em um arquivo.

# Gravando os Dados em um Arquivo CSV

Coletar dados que só residem em uma janela de terminal não é muito útil. Arquivos de valores separados por vírgulas (CSV) nos permitem armazenar dados tabulares em texto plano, e é um formato comum para planilhas e bancos de dados. Antes de iniciar esta seção, você deve familiarizar-se com como manipular arquivos de texto sem formatação em Python.

Primeiro, precisamos importar o módulo interno csv do Python junto com os outros módulos no topo do arquivo de código:

Em seguida, vamos criar e abrir um arquivo chamado z-artist-names.csv para que possamos gravar nele (iremos utilizar aqui a variável f para o arquivo), utilizando o modo 'w'. Também vamos escrever os cabeçalhos da primeira linha: Name and Link que iremos passar para o método writerow() como uma lista.

Finalmente, dentro do nosso loop for, vamos escrever cada linha com os names ou nomes dos artistas e seus links associados:

Você pode ver as linhas para cada uma dessas tarefas no arquivo abaixo:

Quando você executar o programa agora com o comando python, nenhuma saída será retornada para sua janela de terminal. Em vez disso, um arquivo será criado no diretório em que você está trabalhando, chamado z-artist-names.csv.

Dependendo do que você usa para abrí-lo, ele deve ser algo assim:

<p align="center">
  <img alt="mulheres-vozes-escuta" src="./assets/img6.png" width="100%">
</p><br>

Em ambos os casos, agora você pode usar esse arquivo para trabalhar com os dados de maneiras mais significativas, já que as informações coletadas agora estão armazenadas no disco do seu computador.
# Recuperando Páginas Relacionadas

Criamos um programa que extrairá dados da primeira página da lista de artistas cujos sobrenomes começam com a letra Z. Porém, existem 4 páginas desses artistas no total, disponíveis no website.

Para coletar todas essas páginas, podemos executar mais iterações com loops for. Isso revisará a maior parte do código que escrevemos até agora, mas empregará conceitos semelhantes.

Para começar, vamos inicializar uma lista para manter as páginas:

Vamos preencher essa lista inicializada com o seguinte loop for:

Anteriormente neste tutorial, observamos que devemos prestar atenção ao número total de páginas que contêm nomes de artistas começando com a letra Z (ou qualquer letra que estivermos utilizando). Uma vez que existem 4 páginas para a letra Z, construímos o loop foracima com um intervalo de 1 a 5 de modo que ele vai iterar através de cada uma das 4 páginas.

Para este website específico, as URLs começam com a string https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZe são seguidas com um número de página (que será o inteiro i do loop for que convertemos para uma string) e terminam com .htm. Iremos concatenar estas strings e depois acrescentar o resultado à lista pages.

Além desse loop, teremos um segundo loop que passará por cada uma das páginas acima. O código nesse loop for será parecido com o código que criamos até agora, já que ele está executando a tarefa que completamos para a primeira página dos artistas com a letra Z para cada um das 4 páginas do total. Observe que, como colocamos o programa original no segundo loop for, agora temos o loop original como um loop for aninhado contido nele.

Os dois loops for ficarão assim:

No código acima, você deve ver que o primeiro loop for está iterando nas páginas e o segundo loop for está extraindo dados de cada uma dessas páginas e, em seguida, adicionando os nomes e links dos artistas, linha por linha, em cada linha de cada página.

Estes dois loops for estão abaixo das declaraçõs import, da criação e escrita do arquivo CSV (com a linha para a escrita dos cabeçalhos do arquivo), e a inicialização da variável pages (atribuída a uma lista).

Dentro de um contexto macro do arquivo de programação, o código completo se parece com isto:

Como esse programa está fazendo um trabalho, levará algum tempo para criar o arquivo CSV. Depois de concluído, a saída estará comleta, mostrando os nomes dos artistas e seus links associados de Zabaglia, Niccola até Zykmund, Václav.

# Sendo Cuidadoso

Ao fazer scraping em páginas web, é importante manter-se cuidadoso com os servidores dos quais você está pegando informações.

Verifique se o site tem termos de serviço ou termos de uso relacionados ao web scraping. Além disso, verifique se o site tem uma API que permite coletar dados antes de você mesmo fazer scraping.

Certifique-se de não acessar continuamente os servidores para coletar dados. Depois de coletar o que você precisa de um site, execute scripts que vasculhem pelos dados localmente, em vez de sobrecarregar os servidores de outra pessoa.

Adicionalmente, é uma boa ideia fazer web scraping com um cabeçalho que tenha o seu nome e e-mail para que o website possa identificá-lo e fazer o acompanhamento caso tenha alguma dúvida. Um exemplo de cabeçalho que você pode usar com a biblioteca Requests do Python é o seguinte:

import requests

headers = {
    'User-Agent': 'Seu nome, example.com',
    'From': 'email@example.com'
}

url = 'https://example.com'

page = requests.get(url, headers = headers)

A utilização de cabeçalhos com informações identificáveis ​​garante que as pessoas que acessam os logs de um servidor possam entrar em contato com você.

# Conclusão

Este tutorial usou o Python e o Beautiful Soup para coletar dados de um website. Armazenamos o texto que reunimos em um arquivo CSV.

Você pode continuar trabalhando neste projeto coletando mais dados e tornando seu arquivo CSV mais robusto. Por exemplo, você pode querer incluir as nacionalidades e os anos de cada artista. Você também pode usar o que aprendeu para coletar dados de outros sites.

Créditos: https://www.digitalocean.com/community/tutorials/como-fazer-scraping-em-paginas-web-com-beautiful-soup-and-python-3-pt