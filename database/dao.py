from database.DB_connect import DBConnect

class DAO:
    def __init__(self):
        pass

    def read_role(self):
        cnx=DBConnect.get_connection()
        if cnx is None:
            print("Errore di connessione")
            return []
        results=[]
        cursor = cnx.cursor(dictionary=True)
        query="""select distinct role from authorship order by role asc;"""
        try:
            cursor.execute(query)
            rows=cursor.fetchall()
            for row in rows:
                results.append(row)
        except Exception as e:
            print(f"Errore nella esecuzione della query: {e}")
        finally:
            cursor.close()
            cnx.close()
        return results
d=DAO()
print(d.read_role())

