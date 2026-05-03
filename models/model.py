import sqlite3 as lite


ESTOQUE = 'estoques.db'

class Estoque:
    def __init__(self):
        self.db_path = ESTOQUE
        self.table()

    def get_con(self):
        conn = lite.connect(self.db_path)
        conn.row_factory = lite.Row
        return conn
    
    def table(self):
        try:
            with self.get_con() as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS produtos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        produto TEXT UNIQUE NOT NULL,
                        preco FLOAT NOT NULL,
                        quantidade INTEGER NOT NULL,
                        horario_cadastrado TEXT NOT NULL,
                        data_cadastramento DATE NOT NULL                  
                    )
                """)
                conn.commit()
            return conn
        except lite.Error as e:
            raise ValueError("Erro ao criar tabela: ", e)
        
    def cad_produtos(self, produto, preco, quantidade, horario_cadastrado, data_cadastramento):
        try:
            with self.get_con() as conn:
                cur = conn.execute("INSERT INTO produtos (produto,preco,quantidade,horario_cadastrado,data_cadastramento) VALUES(?,?,?,?,?)",
                                   (produto,preco,quantidade,horario_cadastrado,data_cadastramento)
                            )
                id_produto = cur.lastrowid
                return {
                    'id': id_produto, 
                    'produto': produto, 
                    'preco': preco, 
                    'quantidade': quantidade, 
                    'horario_cadastrado': horario_cadastrado, 
                    'data_cadastramento': data_cadastramento
                }       
        except lite.IntegrityError as e:
            return False
        except lite.Error as e:
            raise ValueError("Erro ao cadastrar produto", e)
    
    def list_produtos(self):
        try:
            with self.get_con() as conn:
                cur = conn.execute("SELECT * FROM produtos")
                produtos = cur.fetchall()
            return [dict(produto) for produto in produtos]
        except lite.Error as e:
            raise ValueError("Erro ao listar produtos: ", e)
        
    def get_produto(self, id_produto):
        try:
            with self.get_con() as conn:
                cur = conn.execute("SELECT * FROM produtos WHERE id = ?",(id_produto,))
                produto = cur.fetchone()
            return dict(produto) if produto else None
        except lite.Error as e:
            raise ValueError("Erro ao buscar produto", e)
    
    def delete_produto(self, id_produto):
        try:
            with self.get_con() as conn:
                cur = conn.execute("DELETE FROM produtos WHERE id = ?",(id_produto,))
                conn.commit()
            return cur.rowcount > 0
        except lite.Error as e:
            raise ValueError("Erro ao deletar produto", e)
        
    def update_produto_all(self, produto, preco, quantidade, id):
        try:
            with self.get_con() as conn:
                cur = conn.execute("UPDATE produtos SET produto = ?, preco = ?, quantidade = ? WHERE id = ?",(produto,preco,quantidade,id))
                conn.commit()
            return cur.rowcount > 0 
        except lite.Error as e:
           raise ValueError(f"Erro ao fazer atualização >> {e}")
        
    def update_produto_one(self, produto, preco, quantidade, id_produto):
        try:
            with self.get_con() as conn:
                #Campos permitido para poder atualizar apenas um.
                campos_permitido = {"nome": produto, "preco": preco, "quantidade": quantidade}

                #Percorrendo as chaves e valores dentro no dicionario e verificando se não são None
                #Exemplo o usuario atualizou apenas o preço, então o nome e a quantidade ficaram com o mesmo valor que tinha antes
                #Ou None ou o valor que ele cadastrou
                campos = {k: v for k, v in campos_permitido.items() if v is not None}

                #Criando duas listas vazias onde vou adicionar dentro do sets os campos = Chaves do dict
                #E a lista params adicionando os valores = Valores do dict "nome": "Valor"
                sets,params = [], []

                for campo, valor in campos.items():
                    sets.append(f"{campo} = ?") #Adicionando o campo junto com uma query sql
                    params.append(valor) #Apenas adicionando os parametros da função

                params.append(id_produto) #Adicionando o id por ultimo pois a ordem que ele esta e por ultimo na função
                
                #Usando codigo sql conctenando as chaves adicionada na lista sets
                query = f"UPDATE produtos SET {','.join(sets)} WHERE id = ?"
                cur = conn.execute(query,tuple(params)) #Executando e convertendo para tupla os parametros
                conn.commit()
            return cur.rowcount > 0 
        except lite.Error as e:
           raise ValueError(f"Erro ao fazer atualização >> {e}")