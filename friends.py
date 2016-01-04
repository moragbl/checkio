#!/usr/bin/python

class Friends:
    def __init__(self, connections):
        self.connections = list(connections)
        return None 

    def add(self, connection):
        if connection in self.connections:
            return False
        else:
            self.connections = self.connections + [connection]
            return True

    def remove(self, connection):
        new_connections = [] 
        if connection in self.connections:
            for thing in self.connections:
                 if thing != connection:
                     new_connections = new_connections + [thing]
            self.connections = new_connections
            return True
        else:
            return False

    def names(self):
        stuff = set() 
        for thing in self.connections:
            stuff = stuff.union(thing)
        return set(sorted(list(set(stuff)))) 

    def connected(self, name):
        result = set()
        for thing in self.connections:
            if name in thing:
               result = result.union(thing.difference({name}))
        return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
    f = Friends([{"1", "2"}, {"3", "1"}])
    assert f.add({"2", "4"}) is True, "last add"
    f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))
    assert f.connected("sophia") == {"nikola", "pilot"}, "connected thing"
