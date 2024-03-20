from django.shortcuts import render, redirect, get_object_or_404
from .models import Division, Pais, Cliente, Ingreso, Costo, Gasto_Operacional
from .forms import NuevoIngreso, NuevoCosto, NuevoGastoOperacional,NuevoCliente,EditarIngreso,EditarCosto,EditarGastoOperacionales
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from datetime import datetime
import calendar
from django.utils.translation import activate


def home(request):
    activate('es')
    division = Division.objects.all()
    pais = Pais.objects.all()
    anno_actual = datetime.now().year
    annos = range(anno_actual - 1, anno_actual + 4) 
    meses = [
        'Enero', 'Febrero', 'Marzo', 'Abril',
        'Mayo', 'Junio', 'Julio', 'Agosto',
        'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]   
    if request.method == 'POST':
        division_seleccionada = request.POST.get('divisionSelect')
        pais_seleccionado = request.POST.get('paisSelect')
        tipo_data_seleccionado = request.POST.get('dataSelect')
        anno_seleccionado = request.POST.get('annoSelect')
        mes_seleccionado = request.POST.get('mesSelect')
        pais_filtrado = Pais.objects.get(pais_nombre=pais_seleccionado)
        pais_filtrado_id = pais_filtrado.id_pais
        cliente = Cliente.objects.filter(cliente_pais=pais_filtrado_id)

        if tipo_data_seleccionado == 'Ingreso':
            url = reverse('ingresos') + f"?division={division_seleccionada}&pais={pais_seleccionado}&tipo_data={tipo_data_seleccionado}&annos={anno_seleccionado}&mes={mes_seleccionado}"
            return redirect(url)
        elif tipo_data_seleccionado == 'Costos':
            url = reverse('costos') + f"?division={division_seleccionada}&pais={pais_seleccionado}&tipo_data={tipo_data_seleccionado}&annos={anno_seleccionado}&mes={mes_seleccionado}"
            return redirect(url)
        elif tipo_data_seleccionado == 'Gastos Operacionales':
            url = reverse('gastos_operacionales') + f"?division={division_seleccionada}&pais={pais_seleccionado}&tipo_data={tipo_data_seleccionado}&annos={anno_seleccionado}&mes={mes_seleccionado}"
            return redirect(url)
    else: 
        return render(request, 'home.html', {'division': division, 'pais': pais, 'annos':annos,'meses':meses})
    
def ingresos(request, division_seleccionada=None, pais_seleccionado=None, tipo_data_seleccionado=None, cliente=None, anno_seleccionado=None, mes_seleccionado=None):
    division = Division.objects.all()
    pais = Pais.objects.all()
    mes_seleccionado = request.GET.get('mes')
    anno_seleccionado = request.GET.get('annos')
    division_seleccionada = request.GET.get('division')
    pais_seleccionado = request.GET.get('pais')
    tipo_data_seleccionado = request.GET.get('tipo_data')
    pais_filtrado = Pais.objects.get(pais_nombre=pais_seleccionado)
    pais_filtrado_id = pais_filtrado.id_pais
    division_filtrada = Division.objects.get(division_nombre=division_seleccionada)
    division_filtrada_id = division_filtrada.id_division
    cliente = Cliente.objects.filter(cliente_pais=pais_filtrado.id_pais, cliente_division=division_filtrada.id_division)

    if request.method == 'GET':
        print('es GET tab ingresos')
        mes_seleccionado = request.GET.get('mes')
        anno_seleccionado = request.GET.get('annos')
        division_seleccionada = request.GET.get('division')
        pais_seleccionado = request.GET.get('pais')
        tipo_data_seleccionado = request.GET.get('tipo_data')
        division = Division.objects.all()
        pais = Pais.objects.all()
        division_filtrada = Division.objects.get(division_nombre=division_seleccionada)
        cliente = Cliente.objects.filter(cliente_pais=pais_filtrado.id_pais, cliente_division=division_filtrada.id_division)
        ingresos = Ingreso.objects.filter(ingreso_pais=pais_seleccionado, ingreso_mes=mes_seleccionado, ingreso_anno=anno_seleccionado,ingreso_division=division_seleccionada)
        ingreso_existente = ingresos.exists()
        if ingreso_existente:
            ingreso = ingresos
        # ingreso_existente = Ingreso.objects.filter(
        #     ingreso_mes=mes_seleccionado,
        #     ingreso_anno=anno_seleccionado,
        #     ingreso_division=division_seleccionada,
        #     ingreso_pais=pais_seleccionado
        # ).exists()
        
        # if ingreso_existente:
        #     ingreso = Ingreso.objects.filter(
        #         ingreso_mes=mes_seleccionado,
        #         ingreso_anno=anno_seleccionado,
        #         ingreso_division=division_seleccionada,
        #         ingreso_pais=pais_seleccionado
        #     )
            return render(request, 'ingresos_editar.html', {'division': division_seleccionada, 'pais': pais_seleccionado, 'tipo_data': tipo_data_seleccionado, 'cliente': cliente,'anno': anno_seleccionado,'mes':mes_seleccionado, 'ingreso': ingreso,'ingresos':ingresos})
        else:
            form = NuevoIngreso()
            print('no hay ingreso')
            return render(request, 'ingresos.html', {'division': division_seleccionada, 'pais': pais_seleccionado, 'tipo_data': tipo_data_seleccionado,'mes':mes_seleccionado, 'anno': anno_seleccionado,'cliente': cliente, 'form': form,'ingresos':ingresos})

    elif request.method == 'POST':
        print('es POST')
        form = NuevoIngreso()
        for key, value in request.POST.items():
            print('Paso 1')
            if key.startswith('ingreso_cliente_'):
                print('Paso 2')
                cliente_id = key.split('_')[-1]
                cliente = Cliente.objects.get(pk=cliente_id)
                ingreso_forecast = request.POST.get(f"ingreso_forecast_{cliente_id}", "")
                ingreso_real = request.POST.get(f"ingreso_real_{cliente_id}", "")
                form_data = {
                    'ingreso_pais': request.POST.get(f'ingreso_pais_{cliente_id}', ''),
                    'ingreso_ceco': request.POST.get(f'ingreso_ceco_{cliente_id}', ''),
                    'ingreso_cliente': request.POST.get(f'ingreso_cliente_{cliente_id}', ''),
                    'ingreso_division': request.POST.get(f'ingreso_division_{cliente_id}', ''),
                    'ingreso_mes': request.POST.get(f'ingreso_mes_{cliente_id}', ''),
                    'ingreso_anno': request.POST.get(f'ingreso_anno_{cliente_id}', ''),
                    'ingreso_forecast': ingreso_forecast,
                    'ingreso_real': ingreso_real
                }
                form = Ingreso.objects.create(**form_data)
                print('Ingreso creado...')
        print('Saliendo del form')
        cliente = Cliente.objects.filter(cliente_pais=pais_filtrado_id, cliente_division=division_filtrada.id_division)    
        return render(request, 'ingresos.html',{'division': division_seleccionada, 'pais': pais_seleccionado, 'tipo_data': tipo_data_seleccionado, 'cliente': cliente,'anno': anno_seleccionado,'mes':mes_seleccionado, 'form': form})

def ingresos_editar(request, division_seleccionada=None, pais_seleccionado=None, tipo_data_seleccionado=None, cliente=None, anno_seleccionado=None, mes_seleccionado=None):
    mes_seleccionado = request.GET.get('mes')
    anno_seleccionado = request.GET.get('annos')
    division_seleccionada = request.GET.get('division')
    pais_seleccionado = request.GET.get('pais')
    tipo_data_seleccionado = request.GET.get('tipo_data')
    print(f"Pais",pais_seleccionado)
    print(f"DVI",division_seleccionada)
    pais_filtrado = Pais.objects.get(pais_nombre=pais_seleccionado)
    pais_filtrado_id = pais_filtrado.id_pais
    division_filtrada = Division.objects.get(division_nombre=division_seleccionada)
    division_filtrada_id = division_filtrada.id_division
    cliente = Cliente.objects.filter(cliente_pais=pais_filtrado.id_pais, cliente_division=division_filtrada.id_division)
    ingresos = Ingreso.objects.all()
    if request.method == 'POST':
        print('es POST')
        ingresos = Ingreso.objects.filter(ingreso_pais=pais_filtrado, ingreso_division=division_seleccionada, ingreso_mes=mes_seleccionado, ingreso_anno=anno_seleccionado)
        for key in request.POST.keys():
            print('Key:', key)
            if key.startswith('ingreso_real_'):
                print('Ingresa')
                ingreso_id = key.replace('ingreso_real_', '')
                ingreso_real = request.POST[key]
                ingreso = get_object_or_404(Ingreso, id_ingreso=ingreso_id)
                ingreso.ingreso_real = ingreso_real
                ingreso.save()
                messages.success(request, "Editado editado correctamente...")
                print('Cambio REALIZADO para ingreso ID', ingreso_id)
            elif key.startswith('ingreso_cliente_'):
                print('Ingresa forecast')
                ingreso_id = key.replace('ingreso_cliente_', '')
                ingreso_forecast = request.POST[key]
                if ingreso_forecast.strip():
                    cliente_nombre = ingreso_forecast.strip()  # Cliente que se utilizará para guardar el forecast
                    # Buscar si el cliente ya existe en la base de datos de ingresos
                    ingreso_existente = Ingreso.objects.filter(ingreso_cliente=cliente_nombre).exists()
                    if not ingreso_existente:  # Si el cliente no está registrado en la tabla de ingresos, crear un nuevo ingreso con los datos del cliente
                        nuevo_ingreso = Ingreso.objects.create(
                            ingreso_cliente=cliente_nombre,
                            ingreso_pais=pais_filtrado,
                            ingreso_division=division_seleccionada,
                            ingreso_mes=mes_seleccionado,
                            ingreso_anno=anno_seleccionado,
                            ingreso_forecast=ingreso_forecast
                        )
                        messages.success(request, "Nuevo cliente ingresado y editado correctamente...")
                        print('Nuevo cliente ingresado y editado correctamente...')
                    else:  # Si el cliente ya está registrado, simplemente actualizar el forecast
                        ingreso = get_object_or_404(Ingreso, id_ingreso=ingreso_id)
                        ingreso.ingreso_forecast = ingreso_forecast
                        ingreso.save()
                        messages.success(request, "Editado editado correctamente...")
                        print('Cambio KEY para ingreso ID', ingreso_id)
        return render(request, 'ingresos_editar.html', {'division': division_seleccionada, 'pais': pais_seleccionado, 'tipo_data': tipo_data_seleccionado, 'mes': mes_seleccionado, 'anno': anno_seleccionado, 'cliente': cliente, 'ingresos': ingresos})
    else:
        mes_seleccionado = request.GET.get('mes')
        anno_seleccionado = request.GET.get('annos')
        division_seleccionada = request.GET.get('division')
        pais_seleccionado = request.POST.get('pais')
        tipo_data_seleccionado = request.GET.get('tipo_data')
        ingresos = Ingreso.objects.filter(ingreso_pais=pais_filtrado, ingreso_division=division_seleccionada,ingreso_mes=mes_seleccionado,ingreso_anno=anno_seleccionado)
        print('Es GET')

        form = EditarIngreso()
        return render(request, 'ingresos_editar.html', {'division': division_seleccionada, 'pais': pais_seleccionado, 'tipo_data': tipo_data_seleccionado,'mes':mes_seleccionado, 'anno': anno_seleccionado,'cliente': cliente, 'form': form, 'ingresos':ingresos})
    #return render(request, 'ingresos_editar.html', {'division': division_seleccionada, 'pais': pais_seleccionado, 'tipo_data': tipo_data_seleccionado,'mes':mes_seleccionado, 'anno': anno_seleccionado,'cliente': cliente, 'form': form, 'ingresos':ingresos})


def costos(request, division_seleccionada=None, pais_seleccionado=None, tipo_data_seleccionado=None, cliente=None, anno_seleccionado=None, mes_seleccionado=None):
    mes_seleccionado = request.GET.get('mes')
    anno_seleccionado = request.GET.get('annos')
    division_seleccionada = request.GET.get('division')
    pais_seleccionado = request.GET.get('pais')
    tipo_data_seleccionado = request.GET.get('tipo_data')
    pais_filtrado = Pais.objects.get(pais_nombre=pais_seleccionado)
    pais_filtrado_id = pais_filtrado.id_pais
    division_filtrada = Division.objects.get(division_nombre=division_seleccionada)
    cliente = Cliente.objects.filter(cliente_pais=pais_filtrado.id_pais, cliente_division=division_filtrada.id_division)
    
    if request.method == 'GET':
        mes_seleccionado = request.GET.get('mes')
        anno_seleccionado = request.GET.get('annos')
        division_seleccionada = request.GET.get('division')
        pais_seleccionado = request.GET.get('pais')
        tipo_data_seleccionado = request.GET.get('tipo_data')
        division = Division.objects.all()
        pais = Pais.objects.all()
        division_filtrada = Division.objects.get(division_nombre=division_seleccionada)
        cliente = Cliente.objects.filter(cliente_pais=pais_filtrado.id_pais, cliente_division=division_filtrada.id_division)
        costos = Costo.objects.filter(costo_pais=pais_seleccionado, costo_mes=mes_seleccionado, costo_anno=anno_seleccionado, costo_division=division_seleccionada)
        costo_existente = Costo.objects.filter(
            costo_mes=mes_seleccionado,
            costo_anno=anno_seleccionado,
            costo_division=division_seleccionada,
            costo_pais=pais_seleccionado
        ).exists()

        if costo_existente:
            costo = Costo.objects.filter(
                costo_mes=mes_seleccionado,
                costo_anno=anno_seleccionado,
                costo_division=division_seleccionada,
                costo_pais=pais_seleccionado
            )
            return render(request,'costos_editar.html',{'division': division_seleccionada, 'pais': pais_seleccionado, 'tipo_data': tipo_data_seleccionado, 'cliente': cliente,'anno': anno_seleccionado,'mes':mes_seleccionado, 'costo':costo,'costos':costos})
        else:
            form = NuevoCosto()
            return render(request,'costos.html',{'division': division_seleccionada, 'pais': pais_seleccionado, 'tipo_data': tipo_data_seleccionado, 'cliente': cliente,'anno': anno_seleccionado,'mes':mes_seleccionado, 'costos':costos})
    elif request.method == 'POST':
        print('es POST')
        form = NuevoCosto()
        for key, value in request.POST.items():
            print('Paso 1')
            if key.startswith('costo_cliente_'):
                print('Paso 2')
                cliente_id = key.split('_')[-1]
                cliente = Cliente.objects.get(pk=cliente_id)
                costo_forecast = request.POST.get(f"costo_forecast_{cliente_id}","")
                costo_real = request.POST.get(f"costo_real_{cliente_id}","")
                form_data={
                    'costo_pais': request.POST.get(f'costo_pais_{cliente_id}', ''),
                    'costo_ceco': request.POST.get(f'costo_ceco_{cliente_id}', ''),
                    'costo_cliente': request.POST.get(f'costo_cliente_{cliente_id}', ''),
                    'costo_division': request.POST.get(f'costo_division_{cliente_id}', ''),
                    'costo_mes': request.POST.get(f'costo_mes_{cliente_id}', ''),
                    'costo_anno': request.POST.get(f'costo_anno_{cliente_id}', ''),
                    'costo_forecast': costo_forecast,
                    'costo_real': costo_real

                }
                form = Costo.objects.create(**form_data)
                print('Costo Creado ...')
        print('Saliendo del form')
        cliente = Cliente.objects.filter(cliente_pais=pais_filtrado_id, cliente_division=division_filtrada.id_division)    
        return render(request, 'costos.html',{'division': division_seleccionada, 'pais': pais_seleccionado, 'tipo_data': tipo_data_seleccionado, 'cliente': cliente, 'form': form})
    

def costos_editar(request, division_seleccionada=None, pais_seleccionado=None, tipo_data_seleccionado=None, cliente=None, anno_seleccionado=None, mes_seleccionado=None):
    mes_seleccionado = request.GET.get('mes')
    anno_seleccionado = request.GET.get('annos')
    division_seleccionada = request.GET.get('division')
    pais_seleccionado = request.GET.get('pais')
    tipo_data_seleccionado = request.GET.get('tipo_data')
    pais_filtrado = Pais.objects.get(pais_nombre=pais_seleccionado)
    pais_filtrado_id = pais_filtrado.id_pais
    division_filtrada = Division.objects.get(division_nombre=division_seleccionada)
    division_filtrada_id = division_filtrada.id_division
    cliente = Cliente.objects.filter(cliente_pais=pais_filtrado.id_pais, cliente_division=division_filtrada.id_division)
    costos = Costo.objects.all()  
    if request.method == 'POST':
        print('es POST')
        costos = Costo.objects.filter(costo_pais=pais_filtrado,costo_division=division_seleccionada,costo_mes=mes_seleccionado,costo_anno=anno_seleccionado)
        for key in request.POST.keys():
            print('Key:', key)
            if key.startswith('costo_real_'):
                print('Ingresa')
                costo_id = key.replace('costo_real_', '')
                costo_real = request.POST[key]
                costo = get_object_or_404(Costo, id_costo=costo_id)
                costo.costo_real = costo_real
                costo.save()
                print('Cambio realizado para costo ID', costo_id)
            elif key.startswith('costo_forecast_'):
                print('Ingresa forecast')
                costo_id = key.replace('costo_forecast_', '')
                costo_forecast = request.POST[key]
                if costo_forecast.strip():
                    costo = get_object_or_404(Costo, id_costo=costo_id)
                    costo.costo_forecast = costo_forecast
                    costo.save()
                    print('Cambio realizado para costo ID', costo_id)    
        return render(request, 'costos_editar.html',{'division':division_seleccionada,'pais':pais_seleccionado,'tipo_data':tipo_data_seleccionado,'mes':mes_seleccionado,'anno':anno_seleccionado,'cliente':cliente,'costos':costos})
    else:
        mes_seleccionado = request.GET.get('mes')
        anno_seleccionado = request.GET.get('annos')
        division_seleccionada = request.GET.get('division')
        pais_seleccionado = request.GET.get('pais')
        tipo_data_seleccionado = request.GET.get('tipo_data')
        costos = Costo.objects.filter(costo_pais=pais_filtrado, costo_division=division_seleccionada,costo_mes=mes_seleccionado,costo_anno=anno_seleccionado)
        print('Es GET')
        form = EditarCosto()
        return render(request, 'costos_editar.html', {'division': division_seleccionada, 'pais': pais_seleccionado, 'tipo_data': tipo_data_seleccionado,'mes':mes_seleccionado, 'anno': anno_seleccionado,'cliente': cliente, 'form': form, 'costos':costos})


def gastos_operacionales(request, division_seleccionada=None, pais_seleccionado=None, tipo_data_seleccionado=None, cliente=None):
    mes_seleccionado = request.GET.get('mes')
    anno_seleccionado = request.GET.get('annos')
    division_seleccionada = request.GET.get('division')
    pais_seleccionado = request.GET.get('pais')
    tipo_data_seleccionado = request.GET.get('tipo_data')
    division_filtrada = Division.objects.get(division_nombre=division_seleccionada)
    pais_filtrado = Pais.objects.get(pais_nombre=pais_seleccionado)
    pais_filtrado_id=pais_filtrado.id_pais
    cliente = Cliente.objects.filter(cliente_pais=pais_filtrado.id_pais, cliente_division=division_filtrada.id_division)
    
    if request.method == 'GET':
        mes_seleccionado = request.GET.get('mes')
        anno_seleccionado = request.GET.get('annos')
        division_seleccionada = request.GET.get('division')
        pais_seleccionado = request.GET.get('pais')
        tipo_data_seleccionado = request.GET.get('tipo_data')
        division_filtrada = Division.objects.get(division_nombre=division_seleccionada)
        pais_filtrado = Pais.objects.get(pais_nombre=pais_seleccionado)
        pais_filtrado_id=pais_filtrado.id_pais
        cliente = Cliente.objects.filter(cliente_pais=pais_filtrado.id_pais, cliente_division=division_filtrada.id_division)
        gas_ops = Gasto_Operacional.objects.filter(gas_op_pais=pais_seleccionado,gas_op_mes=mes_seleccionado,gas_op_anno=anno_seleccionado,gas_op_division=division_seleccionada)
        gas_op_existente = Gasto_Operacional.objects.filter(
            gas_op_mes=mes_seleccionado,
            gas_op_anno=anno_seleccionado,
            gas_op_division=division_seleccionada,
            gas_op_pais=pais_seleccionado
        ).exists()

        if gas_op_existente:
            gas_op = Gasto_Operacional.objects.filter(
                gas_op_mes=mes_seleccionado,
                gas_op_anno=anno_seleccionado,
                gas_op_division=division_seleccionada,
                gas_op_pais=pais_seleccionado
            )
            return render(request,'gastos_operacionales_editar.html',{'division': division_seleccionada, 'pais': pais_seleccionado, 'tipo_data': tipo_data_seleccionado, 'cliente': cliente,'anno': anno_seleccionado,'mes':mes_seleccionado, 'gas_op': gas_op,'gas_ops':gas_ops})
        else:
            form = NuevoGastoOperacional()
            return render(request, 'gastos_operacionales.html',{'division': division_seleccionada, 'pais': pais_seleccionado, 'tipo_data': tipo_data_seleccionado, 'cliente': cliente,'anno': anno_seleccionado,'mes':mes_seleccionado,'gas_ops':gas_ops})

    elif request.method == 'POST':
        print('es POST')
        form = NuevoGastoOperacional()
        for key, value in request.POST.items():
            print('Paso 1')
            if key.startswith('gas_op_cliente_'):
                print('Paso 2')
                cliente_id = key.split('_')[-1]
                cliente = Cliente.objects.get(pk=cliente_id)
                gas_op_forecast = request.POST.get(f"gas_op_forecast_{cliente_id}","")
                gas_op_real = request.POST.get(f"gas_op_real_{cliente_id}","")
                form_data = {
                    'gas_op_pais': request.POST.get(f'gas_op_pais_{cliente_id}', ''),
                    'gas_op_ceco': request.POST.get(f'gas_op_ceco_{cliente_id}', ''),
                    'gas_op_cliente': request.POST.get(f'gas_op_cliente_{cliente_id}', ''),
                    'gas_op_division': request.POST.get(f'gas_op_division_{cliente_id}', ''),
                    'gas_op_mes': request.POST.get(f'gas_op_mes_{cliente_id}', ''),
                    'gas_op_anno': request.POST.get(f'gas_op_anno_{cliente_id}', ''),
                    'gas_op_forecast': gas_op_forecast,
                    'gas_op_real': gas_op_real
                }
                form = Gasto_Operacional.objects.create(**form_data)
                print('GastoOP Creado...')    
        print('Saliendo del form')
        cliente = Cliente.objects.filter(cliente_pais=pais_filtrado_id,  cliente_division=division_filtrada.id_division)    
        return render(request, 'gastos_operacionales.html',{'division': division_seleccionada, 'pais': pais_seleccionado, 'tipo_data': tipo_data_seleccionado, 'cliente': cliente, 'form': form})

def gastos_operacionales_editar(request, division_seleccionada=None, pais_seleccionado=None, tipo_data_seleccionado=None, cliente=None, anno_seleccionado=None, mes_seleccionado=None):
    mes_seleccionado = request.GET.get('mes')
    anno_seleccionado = request.GET.get('annos')
    division_seleccionada = request.GET.get('division')
    pais_seleccionado = request.GET.get('pais')
    tipo_data_seleccionado = request.GET.get('tipo_data')
    pais_filtrado = Pais.objects.get(pais_nombre=pais_seleccionado)
    pais_filtrado_id = pais_filtrado.id_pais
    division_filtrada = Division.objects.get(division_nombre=division_seleccionada)
    division_filtrada_id = division_filtrada.id_division
    cliente = Cliente.objects.filter(cliente_pais=pais_filtrado.id_pais, cliente_division=division_filtrada.id_division)
    gas_ops = Gasto_Operacional.objects.all()  
    if request.method == 'POST':
        print('es POST')
        gas_ops= Gasto_Operacional.objects.filter(gas_op_pais=pais_filtrado,gas_op_division=division_seleccionada,gas_op_mes=mes_seleccionado,gas_op_anno=anno_seleccionado)
        for key in request.POST.keys():
            print('Key:', key)
            if key.startswith('gas_op_real_'):
                print('Ingresa')
                gas_op_id = key.replace('gas_op_real_', '')
                gas_op_real = request.POST[key]
                gas_op = get_object_or_404(Gasto_Operacional, id_gas_op=gas_op_id)
                gas_op.gas_op_real = gas_op_real
                gas_op.save()
                print('Cambio REALIZADO para gas_op ID', gas_op_id)
            elif key.startswith('gas_op_forecast_'):
                print('Ingresa forecast')
                gas_op_id = key.replace('gas_op_forecast_', '')
                gas_op_forecast = request.POST[key]
                if gas_op_forecast.strip():
                    gas_op = get_object_or_404(Gasto_Operacional, id_gas_op=gas_op_id)
                    gas_op.gas_op_forecast = gas_op_forecast
                    gas_op.save()
                    print('Cambio KEY para gas_op ID', gas_op_id)    
        return render(request, 'gastos_operacionales_editar.html',{'division':division_seleccionada,'pais':pais_seleccionado,'tipo_data':tipo_data_seleccionado,'mes':mes_seleccionado,'anno':anno_seleccionado,'gas_ops':gas_ops})
    else:
        mes_seleccionado = request.GET.get('mes')
        anno_seleccionado = request.GET.get('annos')
        division_seleccionada = request.GET.get('division')
        pais_seleccionado = request.GET.get('pais')
        tipo_data_seleccionado = request.GET.get('tipo_data')
        gas_ops = Gasto_Operacional.objects.filter(gas_op_pais=pais_filtrado,gas_op_division=division_seleccionada,gas_op_mes=mes_seleccionado,gas_op_anno=anno_seleccionado)
        print('Es GET')
        form = EditarGastoOperacionales()
        return render(request, 'gastos_operacionales_editar.html', {'division': division_seleccionada, 'pais': pais_seleccionado, 'tipo_data': tipo_data_seleccionado,'mes':mes_seleccionado, 'anno': anno_seleccionado,'cliente': cliente, 'form': form, 'gas_ops':gas_ops})

def agregar_cliente(request):
    if request.method == 'POST':  
        form = NuevoCliente(request.POST)  
        if form.is_valid():
            form.save()  
            
            division = Division.objects.all()
            pais = Pais.objects.all()
            return render(request,'home.html',{'pais':pais,'division':division}) 
    else:
        form = NuevoCliente()  # Si no es un POST, simplemente crea un formulario en blanco
    return render(request, 'agregar_cliente.html', {'form': form})