from flask import Flask, request, jsonify
from escpos.printer import Network
from flask_cors import CORS, cross_origin

app = Flask(__name__)


#CORS(app, resources={r"/*":{"origins":"http://localhost"}})
CORS(app)
@cross_origin
@app.route('/print_comprobanteq', methods=['POST'])
def print_comprobanteq():  

    response = jsonify(request.json)
    #return response
    content = request.json
    max_length_line = 51
    line_str = '--------------------------\n'

    printer = Network("192.168.0.35") #Printer IP Address

    """ Encabezado BEGIN --------------- """

    printer.set(align='center', font='a')
    printer.text(content['name_comprobante'] + ' ' + content['tipo'] + '\n')

    printer.text("\n")
    
    printer.set(align='center')
    printer.text(line_str)

    printer.set(align='left', font='b')
    printer.text(content['razon_social_empresa'] + '\n')

    printer.text(content['doctype_name_client'] + ': ' + content['cuit_empresa'] + '\n')

    printer.text('Dirección: ' + content['domicilio_comercial_empresa'] + '\n')

    printer.text('Ing. Brutos: ' + content['ing_brutos_empresa'] + '\n')

    printer.text('Inicio de Actividades: ' + content['fecha_inicio_act_empresa'] + '\n')

    printer.set(align='center')
    printer.text(line_str)

    printer.set(align='left', font="b")
    printer.text('Fecha: ' + content['fecha'] + '                          ' + 'Nro: ' + "{:0>5d}".format(int(content['punto_venta'])) + ' - ' + "{:0>8d}".format(int(content['numero']))  + '\n' )

    printer.set(align='center')
    printer.text(line_str)
    
    """ Encabezado END ----------------- """

    """ Cliente BEGIN ------------------ """

    printer.set(align='left', font="b")
    printer.text(content['doctype_name_client'] + ': ' + content['docnumber_client'] +  '\n')
    printer.text('Condición frente al iva: ' + content['ivacondition_name_client'] +  '\n')
    printer.text('Apellido y Nombre / Razón Social: ' + content['nombre_fact_client'] +  '\n')
    printer.text('Condición de venta: ' + content['condicion_venta'] +  '\n')
    printer.text('Domicilio: ' + content['direccion_fact_client'] +  '\n')

    printer.set(align='center', font="b")
    printer.text("-------------------------------\n")

    """ Cliente END -------------------- """

    """ Items BEGIN -------------------- """
    printer.set(align='left', font="b")
    for item in content['items']:
        printer.text(item['cantidad'] + ' x $' + "{:.2f}".format( float(item['precio']) ) + ' (iva ' + item['iva_name'] + ')\n')
    

        subtotal_str = ('$' + "{:.2f}".format( float(item['subtotal']) ) ).rjust(13)
        if len(item['name']) > max_length_line :
            printer.text((item['name'])[0: max_length_line])
        else:
            printer.text( ((item['name'])[0: len(item['name'])]).ljust(max_length_line) + subtotal_str )

    """ Items END ---------------------- """

    """ Items BEGIN -------------------- """

    for comboitem in content['comboitems']:
        printer.text(comboitem['cantidad'] + ' x $' + "{:.2f}".format( float(comboitem['precio']) ) + ' (iva ' + comboitem['iva_name'] + ')\n')
    

        subtotal_str = ('$' + "{:.2f}".format( float(comboitem['subtotal']) ) ).rjust(13)
        if len(comboitem['name']) > max_length_line :
            printer.text((comboitem['name'])[0: max_length_line])
        else:
            printer.text( ((comboitem['name'])[0: len(comboitem['name'])]).ljust(max_length_line) + subtotal_str )

    """ Items END ---------------------- """

    """ Pie BEGIN -------------------- """
    printer.set(align='center', font="b")
    printer.text(line_str)

    printer.set(align='right', font="b")

    printer.text(('Sub Total: $'  +  (content['sub_total']).rjust(15) + '\n').ljust(34))
    
    for ivaaliquot in content['ivaaliquots']:
        printer.text((ivaaliquot['name']  +  (ivaaliquot['valor']).rjust(15) + '\n').ljust(35))
    
    printer.set(align='right', font="a" )


    printer.text(('Total: $'  +  ("{:.2f}".format( float(content['total']) )).rjust(15) + '\n').ljust(35))

    printer.set(align='center', font="b" )

    printer.text(line_str)

    printer.text('CAE: ' + content['cae'] + '  vto: ' + content['cae_fch_vto'] + '\n')

   # printer.qr(content['qr_text'], 0, 3)

    """ Pie END ---------------------- """



    printer.cut()


    
    
    return 'Hello World! I have been dddseen {} times.\n'



@cross_origin
@app.route('/print_comprobante', methods=['POST'])
def print_comprobante():  

    response = jsonify(request.json)
    #return response
    content = request.json
    max_length_line = 51
    line_str = '------------------------------------------------\n'

    printer = Network("192.168.0.35") #Printer IP Address

    """ Encabezado BEGIN --------------- """

    printer.set(align='center', font='a')
    printer.text(content['name_comprobante'] + ' ' + content['tipo'] + '\n')

    printer.text("\n")
    
    printer.set(align='center')
    printer.text(line_str)

    printer.set(align='left', font='b')
    printer.text(content['razon_social_empresa'] + '\n')

    printer.text(content['doctype_name_client'] + ': ' + content['cuit_empresa'] + '\n')

    printer.text('Dirección: ' + content['domicilio_comercial_empresa'] + '\n')

    printer.text('Ing. Brutos: ' + content['ing_brutos_empresa'] + '\n')

    printer.text('Inicio de Actividades: ' + content['fecha_inicio_act_empresa'] + '\n')

    printer.set(align='center')
    printer.text(line_str)

    printer.set(align='left', font="b")
    printer.text('Fecha: ' + content['fecha'] + '                          ' + 'Nro: ' + "{:0>5d}".format(int(content['punto_venta'])) + ' - ' + "{:0>8d}".format(int(content['numero']))  + '\n' )

    printer.set(align='center')
    printer.text(line_str)
    
    """ Encabezado END ----------------- """

    """ Cliente BEGIN ------------------ """

    printer.set(align='left', font="b")
    printer.text(content['doctype_name_client'] + ': ' + content['docnumber_client'] +  '\n')
    printer.text('Condición frente al iva: ' + content['ivacondition_name_client'] +  '\n')
    printer.text('Apellido y Nombre / Razón Social: ' + content['nombre_fact_client'] +  '\n')
    printer.text('Condición de venta: ' + content['condicion_venta'] +  '\n')
    printer.text('Domicilio: ' + content['direccion_fact_client'] +  '\n')

    printer.set(align='center')
    printer.text(line_str)

    """ Cliente END -------------------- """

    """ Items BEGIN -------------------- """
    printer.set(align='left', font="b")
    for item in content['items']:
        printer.text(item['cantidad'] + ' x $' + "{:.2f}".format( float(item['precio']) ) + ' (iva ' + item['iva_name'] + ')\n')
    

        subtotal_str = ('$' + "{:.2f}".format( float(item['subtotal']) ) ).rjust(13)
        if len(item['name']) > max_length_line :
            printer.text((item['name'])[0: max_length_line])
        else:
            printer.text( ((item['name'])[0: len(item['name'])]).ljust(max_length_line) + subtotal_str )

    """ Items END ---------------------- """


    """ Items BEGIN -------------------- """

    for comboitem in content['comboitems']:
        printer.text(comboitem['cantidad'] + ' x $' + "{:.2f}".format( float(comboitem['precio']) ) + ' (iva ' + comboitem['iva_name'] + ')\n')
    

        subtotal_str = ('$' + "{:.2f}".format( float(comboitem['subtotal']) ) ).rjust(13)
        if len(comboitem['name']) > max_length_line :
            printer.text((comboitem['name'])[0: max_length_line])
        else:
            printer.text( ((comboitem['name'])[0: len(comboitem['name'])]).ljust(max_length_line) + subtotal_str )

    """ Items END ---------------------- """

    """ Pie BEGIN -------------------- """
    printer.set(align='center')
    printer.text(line_str)

    printer.set(align='right', font="b")

    printer.text(('Sub Total: $'  +  (content['sub_total']).rjust(20) + '\n'))

    for ivaaliquot in content['ivaaliquots']:
        printer.text((ivaaliquot['name']  +  (ivaaliquot['valor']).rjust(20) + '\n'))

    printer.set(align='right', font="a")
    printer.text(('Total: $'  +  ("{:.2f}".format( float(content['total']) )).rjust(15) + '\n'))


    printer.set(align='center')
    printer.text(line_str)

    printer.text('CAE: ' + content['cae'] + '  vto: ' + content['cae_fch_vto'] + '\n')

    printer.qr(content['qr_text'], 0, 3)
    printer.cut()


    
    
    return 'Hello World! I have been dddseen {} times.\n'
