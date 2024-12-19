from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Trivia,Pregunta,Respuesta,Descuentos
from Usuario_app.models import Usuario
from django.utils import timezone
import datetime

# Admin.
def Trivias(request):
    trivias = Trivia.objects.all()
    actualizar_tiempo()
    data = {'trivias':trivias}
    return render(request,'trivias.html',data)

def Crear_trivia(request):
    if (request.method == "POST"):
        pre_trivia = Trivia()
        pre_trivia.titulo = request.POST["txt_titulo"]
        pre_trivia.descripcion = request.POST["txt_descripcion"]
        pre_trivia.descuentoofrecido = request.POST["txt_descuento"]
        pre_trivia.fechaTermino = request.POST["txt_fecha_maxima"]
        pre_trivia.usuarioCreador = Usuario.objects.get(id = request.session['usuario_id'])
        pre_trivia.estado = "inactivo"
        pre_trivia.save()
        return redirect('trivias')
    else:
        return render(request,"crear_trivia.html")
    
def Editar_Trivia(request, id_trivia):
    if request.method == "POST":
        trivia = Trivia.objects.get(id = id_trivia)
        trivia.titulo = request.POST["txt_titulo"]
        trivia.descripcion = request.POST["txt_descripcion"]
        trivia.descuentoofrecido = request.POST["txt_descuento"]
        trivia.fechaTermino = request.POST["txt_fecha_maxima"]
        trivia.save()
        return redirect('trivias')
    else:
        trivia = Trivia.objects.get(id = id_trivia)
        print(trivia.fechaTermino)
        data = {'trivia':trivia}
        return render(request,'crear_trivia.html',data)
    
def Activar_Trivia(request, id_trivia):
    trivia = Trivia.objects.get(id = id_trivia)
    preguntas = trivia.Preguntas.all()
    examenPreguntas = []
    if (len(preguntas) >= 2):
        for pre in preguntas:
            respuestas = pre.Respuestas.all()
            if (len(respuestas) >= 2):
                if ExisteRespuestaCorrecta(pre.id):
                    examenPreguntas.append(True)
        if all(examenPreguntas):
            trivia.estado = "activo"
            trivia.save()
            print("se activo")
    else:
        print("Preguntas insuficientes")
    
    print(preguntas)
    return redirect('trivias')

def Desactiva_Trivia(request, id_trivia):
    trivia = Trivia.objects.get(id = id_trivia)
    trivia.estado = 'inactivo'
    trivia.save()
    
def Preguntas(request,id_trivia):
    try:
        preguntas = Pregunta.objects.filter(id_trivia = Trivia.objects.get(id = id_trivia))
        data = {'preguntas':preguntas,'trivia':id_trivia}
        return render(request,"preguntas.html",data)
    except Pregunta.DoesNotExist:
         return render(request,"preguntas.html")
        
def Crear_Preguntas(request,id_trivia):
    if request.method == "POST":
        descripcion = request.POST['txt_descripcion']
        NumeroOrden = len(Pregunta.objects.filter(id_trivia = id_trivia))
        pre_pregunta = Pregunta()
        pre_pregunta.descripcion = descripcion
        pre_pregunta.nOrden = NumeroOrden
        pre_pregunta.id_trivia = Trivia.objects.get(id = id_trivia)
        pre_pregunta.save()
        return redirect('preguntas', id_trivia)
    else:
        return render(request,'crear_pregunta.html')
    
def Editar_Pregunta(request,id_pregunta):
    if request.method == "POST":
        pregunta = Pregunta.objects.get(id = id_pregunta)
        pregunta.descripcion = request.POST["txt_descripcion"]
        pregunta.save()
        return redirect('preguntas', pregunta.id_trivia.id)
    else:
        pregunta = Pregunta.objects.get(id = id_pregunta)
        data = {'pregunta':pregunta}
        return render(request,'crear_pregunta.html',data)

def Respuestas(request,id_trivia,id_pregunta):
    try:
        respuestas = Respuesta.objects.filter(id_pregunta = Pregunta.objects.get(id = id_pregunta))
        data = {'respuestas':respuestas, 'pregunta': id_pregunta, 'trivia':id_trivia}
        return render(request,"respuestas.html",data)
    except Pregunta.DoesNotExist:
        return render(request,"respuestas.html")

def Crear_Respuesta(request,id_trivia,id_pregunta):
    existeCorrecta = ExisteRespuestaCorrecta(id_pregunta)
    if request.method == "POST":
        pre_respuesta = Respuesta()
        pre_respuesta.id_pregunta = Pregunta.objects.get(id =  id_pregunta)
        pre_respuesta.descripcion = request.POST["txt_descripcion"]
        print(request.POST.get("check_correcto",False))
        if request.POST.get("check_correcto",False) == "true":
                pre_respuesta.escorrecto = True
        else:
            pre_respuesta.escorrecto = False
        pre_respuesta.save()
        return redirect('respuestas', id_trivia,id_pregunta)
    else:
        data = {'existeCorrecta': existeCorrecta}
        return render(request,'crear_respuesta.html',data)
    
def Editar_Respuesta(request,id_trivia,id_respuesta):
    if request.method == "POST":
        respuesta = Respuesta.objects.get(id = id_respuesta)
        respuesta.descripcion = request.POST["txt_descripcion"]
        
        if ExisteRespuestaCorrecta(respuesta.id_pregunta.id):
            respuesta.escorrecto = False
        else:
            if request.POST.get("check_correcto",False):
                    respuesta.escorrecto = True
            else:
                respuesta.escorrecto = False
        respuesta.save()
        return redirect('respuestas', id_trivia,respuesta.id_pregunta.id)
    else:
        respuesta = Respuesta.objects.get(id = id_respuesta)
        data = {'respuesta':respuesta}
        return render(request,'crear_respuesta.html',data)

def ExisteRespuestaCorrecta(id_pregunta):
    respuestas = Respuesta.objects.filter(id_pregunta = Pregunta.objects.get(id = id_pregunta))
    for re in respuestas:
        if re.escorrecto:
            return True
    return False

def EstablecerCorrecta(request,id_trivia,id_respuesta):
    print(id_respuesta)
    respuesta_correcta = Respuesta.objects.get(id = id_respuesta)
    print(respuesta_correcta.descripcion)
    id_pregunta = respuesta_correcta.id_pregunta.id
    respuestas = Respuesta.objects.filter(id_pregunta = respuesta_correcta.id_pregunta)
    for re in respuestas:
        print(re.descripcion)
        print(re.escorrecto)
        if re.escorrecto:
            re.escorrecto = False
            re.save()
    for re in respuestas:
        print(re.escorrecto)
    respuesta_correcta.escorrecto = True
    respuesta_correcta.save()
    respuestas = Respuesta.objects.filter(id_pregunta = respuesta_correcta.id_pregunta)
    print("--------")
    for re in respuestas:
        print(re.escorrecto)
    return redirect('respuestas', id_trivia,id_pregunta)
    
def actualizar_tiempo():
    trivias_activas = Trivia.objects.filter(estado = "activo")
    ahora = timezone.now()
    for trivia in trivias_activas:
        if trivia.fechaTermino.astimezone() >= ahora:
            trivia.estado = 'inactivo' 

#usuario
def Mis_trivias(request):
    id_usuario = request.session['usuario_id']
    actualizar_tiempo()
    trivias = Trivia.objects.filter(estado = "activo").exclude(usuarioRealizados__id = id_usuario)
    print(trivias)
    mis_trivias = Usuario.objects.get(id = id_usuario).descuentos.all()
    data = {'trivias_disponibles':trivias,
            'descuentos':mis_trivias}
    return render(request,'trivias_usuario.html',data)

def Responder_Trivia(request,id_trivia):
    if request.method == "POST":
        pre_respondidas_cor = []
        pts = 0
        trivia = Trivia.objects.get(id = id_trivia)
        preguntas = trivia.Preguntas.all()
        for x,pregunta in enumerate(preguntas):
            respuestas = Respuesta.objects.filter(id_pregunta = pregunta.id)
            for re in respuestas:
                if re.escorrecto:
                    if request.POST.get(str(re.id)) == "on":
                        pre_respondidas_cor.append(True)
                    else:
                        pre_respondidas_cor.append(False)
        for x in pre_respondidas_cor:
            if x:
                pts += 1
        pts_esperados = len(pre_respondidas_cor)
        porcentaje_obtenido = ((pts * 100)/pts_esperados)
        print(porcentaje_obtenido)
        if porcentaje_obtenido >= 50:
            pre_descuento = Descuentos()
            pre_descuento.id_trivia = trivia
            print(pre_descuento.id_trivia)
            pre_descuento.usuPropietario = Usuario.objects.get(id = request.session['usuario_id'])
            print(pre_descuento.usuPropietario)
            pre_descuento.fechaCreacion = timezone.now()
            pre_descuento.fechaTermino = timezone.now()+datetime.timedelta(days=3)
            pre_descuento.valor = round(trivia.descuentoofrecido,2)
            pre_descuento.porcentajeCorrecto = porcentaje_obtenido
            pre_descuento.estado = "valido"
            trivia.usuarioRealizados.add(Usuario.objects.get(id = request.session['usuario_id']))
            pre_descuento.save()
            trivia.save()
        return redirect('mis_trivias')
    else:
        trivia = Trivia.objects.get(id = id_trivia)
        preguntas = trivia.Preguntas.all()
        tiempo_restante = trivia.fechaTermino - timezone.now()
        data = {
            'tiempo_restante':smooth_timedelta(tiempo_restante),
            'trivia':trivia,
            'preguntas': preguntas
        }
        for x,pregunta in enumerate(preguntas):
            respuestas = Respuesta.objects.filter(id_pregunta = pregunta.id)
            data.update({"respuestas"+str(x): respuestas})
        #print(data)
        return render(request,'realizar_trivia.html',data)

def Ver_trivia(request,tri_id):
    trivia = Trivia.objects.get(id = tri_id)
    return render(request,"ver_trivia.html")

def smooth_timedelta(timedeltaobj):
    secs = timedeltaobj.total_seconds()
    timetot = ""
    if secs > 86400:
        days = secs // 86400
        timetot += "{} dias".format(int(days))
        secs = secs - days*86400

    if secs > 3600:
        hrs = secs // 3600
        timetot += " {} horas".format(int(hrs))
        secs = secs - hrs*3600

    if secs > 60:
        mins = secs // 60
        timetot += " {} minutos".format(int(mins))
        secs = secs - mins*60

    if secs > 0:
        timetot += " {} segundos".format(int(secs))
    return timetot