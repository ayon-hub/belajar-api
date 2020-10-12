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
def create(req):
    if req.method == 'POST':
        data_byte = req.body
        data_string = str(data_byte, 'utf-8')
        data = json.loads(data_string)

        a = Task.objects.create(
            judul=data['judul'], 
            genre=data['genre'])
        return JsonResponse({
            'data': model_to_dict(a),
        })
        def delete(req, id):
    if req.method == 'DELETE':
        a = Task.objects.filter(pk=id).delete()
    return JsonResponse({
            'msg': 'data sudah terhapus'
        })

def detail(req, id):
    if req.method == 'GET':
        a = Task.objects.filter(pk=id).first()
    return JsonResponse({
        'data': model_to_dict(a),
    })

def update(req, id):
    if req.method == 'PUT':
        data_byte = req.body
        data_string = str(data_byte,'utf-8')
        data = json.loads(data_string)

        a = Task.objects.filter(pk=id).update(
            judul=data['judul'], 
            genre=data['genre']
        )
        a = Task.objects.filter(pk=id).first()

        return JsonResponse({
            'data': model_to_dict(a),
        }) 