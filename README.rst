WTA2015 - Adaptatividade em Python
----------------------------------

Repositório com o código utilizado no tutorial "*Adaptatividade em Python*"
ministrado no Workshop de Tecnologia Adaptativa de 2015 (WTA2015) na Escola
Politécnica da Universidade de São Paulo (Poli-USP) nos dias 2015-01-29 e
2015-01-30.

A ideia de adaptatividade do tutorial remete a uma parte do dinamismo inerente
ao Python, enfatizando as possibilidades de utilização dos recursos da
linguagem avaliados em tempo de execução, em particular aqueles relativos à
[auto-]modificação/geração de objetos/código/AST/bytecode, à mutabilidade
(e.g. monkeypatching) e à reflexão. Para maiores informações sobre o conceito
de adaptatividade nesse e em outros contextos, veja as publicações disponíveis
no site do LTA (e.g. o artigo "Um Glossário sobre Adaptatividade" de 2009 por
J. J. Neto):

http://lta.poli.usp.br/


Assuntos
--------

O tutorial foi separado em 9 partes, sendo a última parte, uma conclusão que
incluiu uma breve discussão sobre o contexto prático atual, a única sem
exemplos em código. Cada uma das demais partes reúne um grupo de assuntos com
aplicabilidade prática em Python que possibilitam a adaptatividade:

1. Geradores, iteradores e iteráveis
2. "Primeira classe" e closures
3. Namespaces, dicionários e escopo (léxico)
4. Fallback e reflexão (reflection) para itens e atributos
5. MRO, herança múltipla, __new__, metaclasses
6. Importação: arquivos, módulos e pacotes
7. JIT, exec, eval, compile
8. AST e bytecode
9. Contexto, aplicações e futuro


Organização dos arquivos
------------------------

Cada arquivo Python que inicia com dois dígitos tem como primeiro dígito a
parte em que o código foi utilizado no tutorial, seguindo a numeração dos
assuntos. O segundo desses dígitos é a ordem de aparecimento do código no
tutorial. Arquivos que iniciam com ``presentation_`` trazem conteúdos
digitados durante o tutorial. Há ainda dois scripts, um deles escrito
para automatizar o git evitando um commit único com todos os exemplos, e o
outro para gerar arquivos RTF com o pygments e permitir assim "copiar e colar"
o conteúdo colorido do LibreOffice Writer para o LibreOffice Impress.


----

Conteúdo feito por Danilo J. S. Bellini

