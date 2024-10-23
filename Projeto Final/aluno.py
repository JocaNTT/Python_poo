import sqlite3

class Aluno:
    def conexao(self):
        try:
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
        except sqlite3.Error as erro:
            print(f"Erro ao conectar ao banco de dados: {erro}")
            return None
    
    def cadastrarAluno(self, nome, idade, plano, data_inicio):
        try:
            conexao = self.conexao()
            if conexao is None:
                return
                
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
                print("Plano inválido")
                
            print(consulta.rowcount, "Linha(s) inserida(s) com sucesso")
            
        except sqlite3.Error as erro:
            print(f"Erro ao cadastrar aluno: {erro}")
        finally:
            if conexao:
                conexao.close()

    def consultarAlunos(self):
        try:
            conexao = self.conexao()
            if conexao is None:
                return
                
            consulta = conexao.cursor()
            sql = "SELECT * FROM alunos"
            consulta.execute(sql)
            resultado = consulta.fetchall()
            
            if not resultado:
                print("Nenhum aluno cadastrado.")
                return
                
            for itens in resultado:
                print(f"Código: {itens[0]}")
                print(f"Nome: {itens[1]}")
                print(f"Idade: {itens[2]}")
                print(f"Plano: {itens[3]}")
                print(f"Data de Início: {itens[4]}\n")
                
        except sqlite3.Error as erro:
            print(f"Erro ao consultar alunos: {erro}")
        finally:
            if conexao:
                conexao.close()

    def deletarAluno(self, codigo_aluno):
        try:
            conexao = self.conexao()
            if conexao is None:
                return
                
            sql = "DELETE FROM alunos WHERE codigo = ?"
            campos = (codigo_aluno,)
            consulta = conexao.cursor()
            consulta.execute(sql, campos)
            conexao.commit()
            
            if consulta.rowcount > 0:
                print(consulta.rowcount, "Linha(s) excluída(s) com sucesso")
            else:
                print(f"Nenhum aluno encontrado com o código {codigo_aluno}")
                
        except sqlite3.Error as erro:
            print(f"Erro ao deletar aluno: {erro}")
        finally:
            if conexao:
                conexao.close()

    def atualizarAluno(self, codigo_aluno, nome, idade, data_inicio):
        try:
            conexao = self.conexao()
            if conexao is None:
                return
                
            if data_inicio == '':
                data_inicio = None
                
            sql = "UPDATE alunos SET nome = ?, idade = ?, data_inicio = ? WHERE codigo = ?"
            campos = (nome, idade, data_inicio, codigo_aluno)
            consulta = conexao.cursor()
            consulta.execute(sql, campos)
            conexao.commit()
            
            if consulta.rowcount > 0:
                print(consulta.rowcount, "Linha(s) atualizada(s) com sucesso")
            else:
                print(f"Nenhum aluno encontrado com o código {codigo_aluno}")
                
        except sqlite3.Error as erro:
            print(f"Erro ao atualizar aluno: {erro}")
        finally:
            if conexao:
                conexao.close()

    def consultarAlunoIndividual(self, codigo_aluno):
        try:
            conexao = self.conexao()
            if conexao is None:
                return
                
            consulta = conexao.cursor()
            sql = "SELECT * FROM alunos WHERE codigo = ?"
            campos = (codigo_aluno,)
            consulta.execute(sql, campos)        
            resultado = consulta.fetchall()
            
            if not resultado:
                print(f"Nenhum aluno encontrado com o código {codigo_aluno}")
                return
                
            for itens in resultado:
                print(f"Código: {itens[0]}")
                print(f"Nome: {itens[1]}")
                print(f"Idade: {itens[2]}")
                print(f"Plano: {itens[3]}")
                print(f"Data de Início: {itens[4]}\n")
                
        except sqlite3.Error as erro:
            print(f"Erro ao consultar aluno: {erro}")
        finally:
            if conexao:
                conexao.close()