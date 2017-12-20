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


def load_db(filename = "../transactions.db", filter_source="", filter_dest="", nb=100000):
    connection = sqlite3.connect(filename)
    cursor = connection.cursor()

    filters = "WHERE"
    if filter_source:
        filters += '"from" = "%s"' % filter_source    
    
    if filter_dest:
        filters += '"to" = "%s"' % filter_dest
        
    if filters == "WHERE":
        l = cursor.execute("""SELECT id, blockHash, blockNumber, "from", "to", value FROM transactions ORDER BY id DESC LIMIT %d""" % nb).fetchall()
    else:
        l = cursor.execute("""SELECT id, blockHash, blockNumber, "from", "to", value FROM transactions %s ORDER BY id DESC LIMIT %d""" % (filters,nb)).fetchall()
    res = []

    for t in l:
        res.append( Transaction(*t) )

    return res
