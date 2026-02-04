from database.DB_connect import DBConnect
from model.connessioni import Connessioni


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

    def read_connessioni(self,role):
        cnx=DBConnect.get_connection()
        if cnx is None:
            print("Errore di connessione")
            return []
        results=[]
        cursor = cnx.cursor(dictionary=True)
        query="""select distinct a1.artist_id as id1,a1.name as name1,a2.artist_id as id2,a2.name as name2,count(distinct o1.object_id)as produttivita1,count(distinct o2.object_id)as produttivita2
        from artists a1,artists a2,authorship at1,authorship at2,objects o1,objects o2 
              where a1.artist_id<>a2.artist_id and a1.artist_id=at1.artist_id and a2.artist_id=at2.artist_id 
              and at1.role=%s and at2.role=%s and at1.object_id=o1.object_id and at2.object_id=o2.object_id 
              and o1.curator_approved<>0 and o2.curator_approved<>0
              group by a1.artist_id,a1.name,a2.artist_id,a2.name;"""
        try:
            cursor.execute(query,(role,role,))
            rows=cursor.fetchall()
            for row in rows:
                results.append(Connessioni(row["id1"],row["name1"],row["id2"],row["name2"],row["produttivita1"],row["produttivita2"]))
        except Exception as e:
            print(f"Errore nella esecuzione della query: {e}")
        finally:
            cursor.close()
            cnx.close()
        return results


    def read_artisti(self,role):
        cnx=DBConnect.get_connection()
        if cnx is None:
            print("Errore di connessione")
            return []
        results=[]
        cursor = cnx.cursor(dictionary=True)
        query="""select  at.artist_id as id,count(distinct at.object_id)as oggetti
        from authorship at,objects o where at.role=%s and at.object_id=o.object_id and o.curator_approved=1
              group by at.artist_id 
              having count(distinct o.object_id)>0;"""
        try:
            cursor.execute(query,(role,))
            rows=cursor.fetchall()
            for row in rows:
                results.append(row)
        except Exception as e:
            print(f"Errore nella esecuzione della query: {e}")
        finally:
            cursor.close()
            cnx.close()
        return results


    def read_name(self):
        cnx=DBConnect.get_connection()
        if cnx is None:
            print("Errore di connessione")
            return []
        results=[]
        cursor = cnx.cursor(dictionary=True)
        query="""select distinct artist_id as id,name as nome
        from artists;"""
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




