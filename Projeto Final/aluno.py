import sqlite3

class Aluno:
    def conexao(self):
        conexao = sqlite3.connect("academia.db")
        consulta = conexao.cursor()
        tabela = """
        CREATE TABLE IF NOT EXISTS alunos(
        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100),
        idade INTEGER,
        plano VARCHAR(100),
        data_inicio DATE
        );
        """
        consulta.execute(tabela)
        return conexao
    
    def cadastrarAluno(self, nome, idade, plano, data_inicio):
        conexao = self.conexao()
        sql = "INSERT INTO alunos (nome, idade, plano, data_inicio) VALUES (?, ?, ?, ?)"
        campos = (nome, idade, plano, data_inicio)
        consulta = conexao.cursor()
        consulta.execute(sql, campos)
        conexao.commit()
        if plano == "1":
            print("Você assinou o Plano Day Use, Treino experimental de 1 dia, válido para musculação, ergometria e cross training.")
        elif plano == "2":
            print("Você assinou o Plano Light, treine na unidade de sua matrícula. Inclui musculação, ergometria e 30 dias gratuitos do app Weburn.")
        elif plano == "3":
            print("Você assinou o Plano Plus, treine em qualquer unidade do Brasil, com acompanhante gratuito 5x por mês e acesso ao app Weburn. Inclui musculação, ergometria, ginástica, danças, cross training e Self Digital.")
        elif plano == "4":
            print("Você assinou o Plano Premium Plus, treine em qualquer unidade do Brasil, com acompanhante gratuito 10x por mês e acesso ao app Weburn. Inclui musculação, ergometria, ginástica, danças, cross training e Self Digital.")
        else:
            print("Plano inválido")
        print(consulta.rowcount, "Linha(s) inserida(s) com sucesso")
        conexao.close()

    def consultarAlunos(self):
        conexao = self.conexao()
        consulta = conexao.cursor()
        sql = "SELECT * FROM alunos"
        consulta.execute(sql)
        resultado = consulta.fetchall()
        for itens in resultado:
            print(f"Código: {itens[0]}")
            print(f"Nome: {itens[1]}")
            print(f"Idade: {itens[2]}")
            print(f"Plano: {itens[3]}")
            print(f"Data de Início: {itens[4]}\n")
        conexao.close()

    def deletarAluno(self, codigo_aluno):
        conexao = self.conexao()
        sql = "DELETE FROM alunos WHERE codigo = ?"
        campos = (codigo_aluno,)
        consulta = conexao.cursor()
        consulta.execute(sql, campos)
        conexao.commit()
        print(consulta.rowcount, "Linha(s) excluída(s) com sucesso")
        conexao.close()

    def atualizarAluno(self, codigo_aluno, nome, idade, data_inicio):
        conexao = self.conexao()
        sql = "UPDATE alunos SET nome = ?, idade = ?, data_inicio = ? WHERE codigo = ?"
        campos = (nome, idade, data_inicio, codigo_aluno)
        consulta = conexao.cursor()
        consulta.execute(sql, campos)
        conexao.commit()
        print(consulta.rowcount, "Linha(s) atualizada(s) com sucesso")
        conexao.close()

    def consultarAlunoIndividual(self, codigo_aluno):
        conexao = self.conexao()
        consulta = conexao.cursor()
        sql = "SELECT * FROM alunos WHERE codigo = ?"
        campos = (codigo_aluno,)
        consulta.execute(sql, campos)        
        resultado = consulta.fetchall()
        for itens in resultado:
            print(f"Código: {itens[0]}")
            print(f"Nome: {itens[1]}")
            print(f"Idade: {itens[2]}")
            print(f"Plano: {itens[3]}")
            print(f"Data de Início: {itens[4]}\n")
        conexao.close()