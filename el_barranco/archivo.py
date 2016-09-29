import pickle


def desarchivar(texto):

    f = open(texto, 'r')
    lista = pickle.load(f)
    return lista
    f.close()


def archivar(lista, texto):

    f = open(texto, 'w')
    pickle.dump(lista, f)
    f.close()
