# app/rag_service/store.py
import sqlite3, pickle, json, faiss
from pathlib import Path

DB_PATH = Path("data/vectors.db")
INDEX_PATH = Path("data/vectors.index")

class DiskVectorStore:
    def __init__(self, dim: int) -> None:
        DB_PATH.parent.mkdir(exist_ok=True)
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS vectors (
                id INTEGER PRIMARY KEY,
                meta TEXT NOT NULL
            )
        """)
        self.conn.commit()
        self.index = faiss.read_index(str(INDEX_PATH)) if INDEX_PATH.exists() \
                     else faiss.IndexFlatIP(dim)

    def add(self, vecs, metas):
        self.index.add(vecs)
        self.conn.executemany("INSERT INTO vectors(meta) VALUES (?)",
                              [(json.dumps(m),) for m in metas])
        self.conn.commit()
        faiss.write_index(self.index, str(INDEX_PATH))

    def search(self, q, k):
        scores, ids = self.index.search(q, k)
        cur = self.conn.execute("SELECT meta FROM vectors WHERE id IN (%s)"
                                % ",".join("?" * len(ids[0])), ids[0].tolist())
        return scores[0], [json.loads(r[0]) for r in cur.fetchall()]