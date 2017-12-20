import ethdb

bad_nodes_file = open("bad_nodes", "r")
sources = bad_nodes_file.readlines()

print("Searching related nodes with %s" % sources[0])

ls = ethdb.load_db(filter_source=sources[0], nb=10)

for t in ls :
    print(t.source)

bad_nodes_file.close()
