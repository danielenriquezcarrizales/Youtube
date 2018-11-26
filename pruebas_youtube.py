import unittest
from unittest.mock import Mock
from dos_youtube import AppYoutube
from main import *
from Youtube import Video, AbstractRepo, AbstractYoutube
from base_de_datos import SQlite

class TestYTapp(unittest.TestCase):

    def setUp(self):

        self.yt = AppYoutube()
        self.videomock = Mock(ID="5", Titulo = "MIRANDA.-PERFECTA", Duracion = "PT3M45S", NombreCanal = "Xaxiri Castro",  Fecha= "2008-03-28T21:54:50.000Z", Likes = self.yt.InfoVideo("https://www.youtube.com/watch?v=dDmhThqxDw0").Likes, Vistas = self.yt.InfoVideo("https://www.youtube.com/watch?v=dDmhThqxDw0").Vistas, Descripcion = "BUENA ROLA DE ESTE GRUPO ARGENTINO!!!",Compartidas="150")
        self.video = Video(self.videomock.Titulo,self.videomock.Duracion,self.videomock.NombreCanal,self.videomock.Fecha,self.videomock.Likes,self.videomock.Vistas,self.videomock.Descripcion)
        #self.sql = GuardarVideo()
        #self.sql.GuardarVideo(self.video)
        print(self.videomock)

        ################################
        self.video2 = Video("video1",12,"El video", "12 nov 2018", '2500', '10000',"video")
        self.video2.Id=1
        self.video2.Compartidas=100
    #Hace las pruebas de guardar un video y que todos sus atributos estén almacenados correctamente
    def test_Video(self):

        print("test_Video")
        self.assertEqual(self.video2.Id, 1)
        self.assertEqual(self.video2.Titulo, "video1")
        self.assertEqual(self.video2.Duracion, 12 )
        self.assertEqual(self.video2.NombreCanal, "El video")
        self.assertEqual(self.video2.Fecha, "12 nov 2018" )
        self.assertEqual(self.video2.Likes, "2500")
        self.assertEqual(self.video2.Vistas, "10000")
        self.assertEqual(self.video2.Descripcion, "video")




    

    def test_borrar(self):

        print("test_borrar")
        SQlite.BorrarVideo(self.video2.Id)
        actual=SQlite.MostrarVideo(self.video2.Id)
        expected=[]
        self.assertListEqual(expected,actual)

    def mostrar_video(self):
        print("Test_Mostrar")
        x=SQlite.MostrarVideo(self.video2.Id)
        expected=['video1','12','El video', "12 nov 2018", '2500', '10000','video']
        self.assertListEqual(expected,x)

    def test_infoVideo(self):

        print("test_infoVideo")
        #self.assertEqual((5), self.video.ID)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=dDmhThqxDw0").Titulo, self.video.Titulo)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=dDmhThqxDw0").Duracion, self.video.Duracion)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=dDmhThqxDw0").NombreCanal, self.video.NombreCanal)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=dDmhThqxDw0").Fecha, self.video.Fecha)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=dDmhThqxDw0").Likes, self.video.Likes)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=dDmhThqxDw0").Vistas, self.video.Vistas)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=dDmhThqxDw0").Descripcion, self.video.Descripcion)
        #self.assertEqual((150), self.video.Compartidas)


if __name__ == '__main__':
    unittest.main()
