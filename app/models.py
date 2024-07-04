class Aluno:
    def __init__(self, nome, idade, github, linkedin, mini_bio, foto, serie=None, cpf=None, uf=None, cidade=None):
        self.nome = nome
        self.idade = idade
        self.github = github
        self.linkedin = linkedin
        self.mini_bio = mini_bio
        self.foto = foto
        self.serie = serie
        self.cpf = cpf
        self.uf = uf
        self.cidade = cidade

# Definição da classe Professor
class Professor:
    def __init__(self, nome, github, linkedin, bio, foto, telefone, email, idade):
        self.nome = nome
        self.github = github
        self.linkedin = linkedin
        self.bio = bio
        self.foto = foto
        self.telefone = telefone
        self.email = email
        self.idade = idade