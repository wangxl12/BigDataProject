import sqlite3

class DataBaseOP():
    def __init__(self, database='src/db.sqlite3') -> None:
        self.connect = sqlite3.connect(database)
        self.cur = self.connect.cursor()
        self.table = None
    
    def select_table(self, table):
        try:
            sql = f'select * from {table}'
            self.cur.execute(sql)
        except:
            print(f"{table} 数据表不存在！")
            return
        self.table = table
    
    def insert(self, attr, val, mode='insert'):
        assert isinstance(attr, str) and isinstance(val, str),\
            print('输入的属性和值必须是字符串!')
        assert mode == 'insert' or mode == 'test', print("mode is uncorrect!")

        sql = f'insert into {self.table} ({attr}) values({val})'
        if mode == 'test':
            print(sql)
        elif mode == 'insert':
            self.cur.execute(sql)
            self.connect.commit()
    
    def update(self, change, condition):
        assert isinstance(change, str) and isinstance(condition, str),\
            print("输入的修改和条件必须是字符串!")
            
        sql = f'updata {self.table} set {change} where {condition}'
        self.cur.execute(sql)
        self.connect.commit()
    
    def delete(self, condition):
        assert isinstance(condition, str), print("条件必须是字符串!")
        
        sql = f'delete from {self.table} where {condition}'
        self.cur.execute(sql)
        self.connect.commit()
    
    def display(self, index=None):
        sql = f'select * from {self.table}'
        result = self.cur.execute(sql)
        
        if index is None:
            print(result.fetchall())
        else:
            print(result.fetchall()[index])
    
    def drop(self, table):
        sql = f'drop table {table}'
        self.cur.execute(sql)
        self.connect.commit()
        print(f'Dropped table {table}')

    def close(self):
        self.cur.close()
        self.connect.close()