from django.shortcuts import render
from django.http import JsonResponse
from .models import Belajar #jika .models di definisikan di sini, maka tidak perlu di deklarasi di def*
# Create your views here.
#(4) def halloworld (sebagai index) #def:definisikan
def halloworld(req): #def = definisikan halloworld (meminta)
    belajar = Belajar.objects.all()  # belajar = meminta database(model).objeknya.all (meminta semua yang ada di belajar)  #def*
    html = list(belajar) #variabel lagi, tujuan membuat [link yang berbentuk list] yang akan di panggil di return
    
    return JsonResponse({'html':html}) #(6) memanggil variabel html

def jsonc(req): #isi tampilan aja
    data = Belajar.objects.all()
    isidata =[]#bikin kaleng    
    for b in data :
        isidata.append({
            'nama':b.nama,
            'motto':b.motto
        })
    return JsonResponse({
        'data': isidata
    })
def Create(req): #membuat create
    buat = Belajar.object.all()
    isibuat =[
        for c in buat   :
            isibuat.append()
    ]