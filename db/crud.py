'''
Class for do crud
'''
from db.connection import ConnectToDb
from models.produto import Produto
from pandas import DataFrame


class Crud(ConnectToDb):
    def listar_todos(self) -> DataFrame:
        comando_sql = f'SELECT * FROM {self.table}'
        self.cursor.execute(comando_sql)
        query = self.cursor.fetchall()
        query = DataFrame(
            data=query,
            columns=['ID', 'NOME', 'PREÇO']
            )
        df_query = query.copy()
        df_query['PREÇO'] = df_query['PREÇO'].map(lambda price: f'R${price:6.2f}')
        return df_query

    def inserir(self, nome: str, preco: float):
        prod = Produto(nome, preco)
        comando_sql = f'INSERT INTO {self.table} (nome, preco) VALUES ("{prod.nome}", {prod.preco});'
        return self.execute(comando_sql)

    def deletar(self, id_produto: int):
        comando_sql = f'DELETE FROM {self.table} WHERE id={id_produto};'
        return self.execute(comando_sql)

    def alterar(self, id_produto, novo_nome, novo_preco):
        comando_sql = f'UPDATE {self.table} SET nome="{novo_nome}", preco={novo_preco} WHERE id={id_produto}'
        return self.execute(comando_sql)


if __name__ == '__main__':
    print(__doc__)
else:
    produtos_db = Crud(
        database='loja',
        table='produtos',
        db_config_path='./config/env'
    )