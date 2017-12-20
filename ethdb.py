import sqlite3

class Transaction():
    def __init__(self, id_, blockHash, blockNumber, source, destination, value, timestamp=0):
        self.id = id_
        self.blockHash = blockHash
        self.blockNumber = blockNumber
        self.source = source
        self.destination = destination
        self.value = value
        self.timestamp = timestamp

    def __str__(self):
        return str(self.value) + " from " + self.source + " to " + self.destination
        
    def __repr__(self):
        return str(self.value) + " from " + self.source + " to " + self.destination


def load_db(filename = "../transactions_last.db", nb=100000):
    connection = sqlite3.connect(filename)
    cursor = connection.cursor()

    l = cursor.execute("""SELECT id, blockHash, blockNumber, "from", "to", value FROM transactions ORDER BY id DESC LIMIT %d""" % nb).fetchall()
    res = []

    for t in l:
        res.append( Transaction(*t) )

    return res

# TODO fun neighbors(Source) -> Transaction list
# TODO fun build_graph_from_source(Source)