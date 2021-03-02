import pickle

def desarchivar(archivo):
	with open(archivo, "rb") as f:
		lista = pickle.load(f)
		return lista
		f.close()
def archivar(lista, archivo):
	with open(archivo, "wb") as f:
		pickle.dump(lista, f)
		f.close()