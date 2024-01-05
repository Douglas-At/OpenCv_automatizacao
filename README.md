# Proposito do progama 

A ideia principal sobre esse programa é automatizar processos de download de arquivos que antes era feito via selenium e envio de teclas do teclado como TAB e ARROWUP/DOWN, e essa ideia vem do principal problema que surge quando se usa esse  tipo de automatização,
caso a estrutura html to site venha a mudar ou novos elementos sejam trocados de lugar todo o programa deve ser refatorado para poder exercer a mesma função enquanto usando a lib Opencv necessita apenas de uma unica atualização da imagem de referencia

### Pontos negativos
Enfrentei um tipo de problema q usando automatização selenium é facilmente feito, por exemplo com as datas: 
![Alt Text](https://github.com/Douglas-At/OpenCv_automatizacao/blob/main/dep_img/Captura%20de%20tela%202024-01-05%20135214.png)

nesse caso, para executar o click na data 202402 que ainda não esta visivel teria que fazer uma autalização mensal da imagem a ser clickada, o que é pior do que sempre selecionar a ultima das opções usando selenium ou usando o index dela

