from app.models import Aluno, Professor

alunos = [
    Aluno("Ana Carolina Nunes", 20, "https://github.com/anacarolina", "https://linkedin.com/in/anacarolina", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Arthur Cantele Palmira", 21, "https://github.com/arthurcantele", "https://linkedin.com/in/arthurcantele", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Arthur Fogaça", 22, "https://github.com/arthurfogaca", "https://linkedin.com/in/arthurfogaca", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Arthur Zinani Pedroni", 23, "https://github.com/arthurzinani", "https://linkedin.com/in/arthurzinani", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Bernardo Mossi", 20, "https://github.com/bernardomossi", "https://linkedin.com/in/bernardomossi", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Carolina Sachet", 21, "https://github.com/carolinasachet", "https://linkedin.com/in/carolinasachet", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Caroline Orlandí Bigolin", 22, "https://github.com/carolinebigolin", "https://linkedin.com/in/carolinebigolin", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Eduarda Salvador Terhorst", 23, "https://github.com/eduardaterhorst", "https://linkedin.com/in/eduardaterhorst", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Eduardo Augusto Picinin", 20, "https://github.com/eduardopicinin", "https://linkedin.com/in/eduardopicinin", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Eduardo Hainzenreder Pedroso", 21, "https://github.com/eduardopedroso", "https://linkedin.com/in/eduardopedroso", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Estevan de Paula", 22, "https://github.com/estevande", "https://linkedin.com/in/estevande", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Gabriel Carvalho Susin", 23, "https://github.com/gabrielsusin", "https://linkedin.com/in/gabrielsusin", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Gabriel Guerra", 20, "https://github.com/gabrielguerra", "https://linkedin.com/in/gabrielguerra", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Gabriel Zorzi Pezzi", 21, "https://github.com/gabrielpezzi", "https://linkedin.com/in/gabrielpezzi", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Giancarlo Zanetti Malgarizi", 22, "https://github.com/giancarlomalgarizi", "https://linkedin.com/in/giancarlomalgarizi", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Giovanni Camargo Gardenal Morandi", 23, "https://github.com/giovannimorandi", "https://linkedin.com/in/giovannimorandi", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Guilherme Resemini Zanol", 20, "https://github.com/guilhermezanol", "https://linkedin.com/in/guilhermezanol", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Heitor Trotto Mesquita", 21, "https://github.com/heitormesquita", "https://linkedin.com/in/heitormesquita", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Igor Rodrigues Ribeiro", 22, "https://github.com/igorribeiro", "https://linkedin.com/in/igorribeiro", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Ivo Viesser Neto", 23, "https://github.com/ivoneto", "https://linkedin.com/in/ivoneto", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("João Vítor Brombatti Feiten", 20, "https://github.com/joaovitorfeiten", "https://linkedin.com/in/joaovitorfeiten", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("João Vítor Mendes", 21, "https://github.com/joaovitormendes", "https://linkedin.com/in/joaovitormendes", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("João Vítor Michelon", 22, "https://github.com/joaovitormichelon", "https://linkedin.com/in/joaovitormichelon", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Kauã Drum Fortuna", 23, "https://github.com/kauafortuna", "https://linkedin.com/in/kauafortuna", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Manoela Gomes Zanotto", 20, "https://github.com/manoelazanotto", "https://linkedin.com/in/manoelazanotto", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Maria Thereza Adamatti Rizzotto", 21, "https://github.com/mariarizzotto", "https://linkedin.com/in/mariarizzotto", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Otávio Griebeler Turra", 22, "https://github.com/otavioturra", "https://linkedin.com/in/otavioturra", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Pedro David Brum", 23, "https://github.com/pedrobrum", "https://linkedin.com/in/pedrobrum", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Pedro do Nascimento", 20, "https://github.com/pedronascimento", "https://linkedin.com/in/pedronascimento", "Estudante de Engenharia.", "https://campsbc.org.br/wp-content/uploads/2021/03/gato-no-pc.gif"),
    Aluno("Pedro Henrique Gasparin Machado", 21, "https://github.com/pedrogasparin", "https://linkedin.com/in/pedrogasparin", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Rafael Armando Zanella", 22, "https://github.com/rafaelzanella", "https://linkedin.com/in/rafaelzanella", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Vítor Augusto Rumke", 23, "https://github.com/vitorrumke", "https://linkedin.com/in/vitorrumke", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Vitória Tumelero dos Santos", 20, "https://github.com/vitoriatumelero", "https://linkedin.com/in/vitoriatumelero", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("William dos Santos da Silva", 21, "https://github.com/williamsilva", "https://linkedin.com/in/williamsilva", "Estudante de Engenharia.", "path/to/photo.jpg"),
]

professores = [
    Professor("Ana Carolina Nunes", "https://github.com/anacarolina", "https://linkedin.com/in/anacarolina", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Professor("Arthur Cantele Palmira", "https://github.com/arthurcantele", "https://linkedin.com/in/arthurcantele", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Professor("Arthur Fogaça", "https://github.com/arthurfogaca", "https://linkedin.com/in/arthurfogaca", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Professor("Arthur Zinani Pedroni", "https://github.com/arthurzinani", "https://linkedin.com/in/arthurzinani", "Estudante de Engenharia.", "path/to/photo.jpg")
]
 