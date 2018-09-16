def tp1():
	H = [[0, 1, 2, 3],
		[2, 3, 0, 1],
		[3, 0, 1, 2],
		[0, 1, 2, 3]
	]
	Pw = [[1, 2, 3, 0],
		[2, 3, 0, 1],
		[0, 1, 2, 3],
		[0, 1, 2, 3]
	]
	
	#esto es una pila donde van todos los hombres que no tienen pareja
	Hlibres = [0, 1, 2, 3]
	
	#Cada posicion es un hombre, el contenido indica que mujer invita
	Sig_muj = [0, 0, 0, 0]
	
	#cada posicion es una mujer, el contenido indica el hombre que es su pareja 
	Pareja_muj = [-1, -1, -1, -1]
	
	while not (len(Hlibres) == 0):
		m = Hlibres.pop()
		w = H[m][Sig_muj[m]]
		m_act = Pareja_muj[w]
		if m_act == -1:
			Pareja_muj[w] = m
		else:
			if Pw[w][m_act] < Pw[w][m]:
				Pareja_muj[w] = m
				Hlibres.append(m_act)
			else:
				Hlibres.append(m)
		Sig_muj[m] += 1
	return Pareja_muj
print(tp1())
