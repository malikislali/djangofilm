from urllib import request
from django.shortcuts import render

#dizi oluşturdduk
categories_list=["macera","romantik","komedi"]
#dizi içinde sözlük(dict) oluşturduk
movies_list=[
    {
        "movie_id":1,
        "film_adi":"film 1",
        "aciklama":"film1 açıklama",
        "foto":"https://mttal.meb.k12.tr/meb_iys_dosyalar/07/19/972199/resimler/2020_12/k_10130625_denem.jpg",
        "anasayfa_durumu":False
    },

    {
        "movie_id":2,
        "film_adi":"film 2",
        "aciklama":"film1 açıklama",
        "foto":"foto1.png",
        "anasayfa_durumu":True
    },
    {
        "movie_id":3,
        "film_adi":"film 3",
        "aciklama":"film1 açıklama",
        "foto":"",
        "anasayfa_durumu":True
    }
    ]

# Create your views here.
def home(request):
    data={
         "kategoriler":categories_list,
          "filmler":movies_list
          }
    return render(request,"index.html",data)

def movies(request):
     data={
          "kategoriler":categories_list,
          "filmler":movies_list
          }
     return render(request,"movies.html",data)

def movies_detail(request,movie_id):
     data={
          "movie_id":movie_id
          }
     return render(request,"details.html",data)