from controlador import Controlador

controlador = Controlador()
controlador.leerArchivo('datos.data')
controlador.crearVertexCover()
controlador.mostrarVertexCover()
controlador.ejecutarReduccion()
controlador.mostrarReduccion()
