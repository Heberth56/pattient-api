from config.database import conn
from schema.response_schema import server_error, standar_response, value_error, not_found
from bson import ObjectId
from datetime import datetime


def add_consult(model):
    """
        Método para agregar una consulta
    """
    try:
        data = {
            'patient_id': ObjectId(model.patient_id),
            'medicion_type': model.medicion_type,
            'costo': model.costo,
            'fecha': datetime.now().strftime('%d/%m/%Y'),
            'status': True
        }
        res = conn.consult.insert_one(data)
        return standar_response(message="Consulta agregado exitosamente")
    except Exception as e:
        print(e)
        return server_error()


def list_consults():
    """
        Método para obtener un listado de las consultas
    """
    try:
        serializer_data = []
        res = conn.consult.aggregate([
            {
                '$match': {'status': True}
            },
            {
                '$lookup': {
                    'from': 'patients',
                    'localField': 'patient_id',
                    'foreignField': '_id',
                    'as': 'patient_info'
                }
            },
            {
                '$unwind': '$patient_info'
            },
            {
                '$sort': {
                    'patient_info.paterno': 1
                }
            }
        ])
        for elem in res:
            serializer_data.append({
                '_id': str(elem['_id']),
                'codigo': elem['patient_info']['codigo'],
                'nombres': f"{elem['patient_info']['paterno']} {elem['patient_info']['materno']} {elem['patient_info']['nombre']}",
                'edad': elem['patient_info']['age'],
                'fecha': elem['fecha'],
                'type': elem['medicion_type'],
                'costo': elem['costo']
            })
        return standar_response(message="Listado de pacientes", data=serializer_data)
    except Exception as e:
        print(e)
        return server_error()
