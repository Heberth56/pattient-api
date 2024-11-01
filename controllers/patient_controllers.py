from config.database import conn
from schema.response_schema import server_error, standar_response, value_error, not_found
from bson import ObjectId


def get_code(model, cant):
    code = f"{model.name[0].upper()}{model.paterno[0].upper()}{model.materno[0].upper()}-{str(cant).zfill(3)}"
    return code


def add_patient(model):
    """
        Método para agregar un paciente
    """
    try:
        cant = conn.patients.count_documents({})+1
        data_patient = {
            'codigo': get_code(model, cant),
            'nombre': model.name,
            'paterno': model.paterno,
            'materno': model.materno,
            'age': model.age,
            'phone': model.phone,
            'status': True
        }
        res = conn.patients.insert_one(data_patient)
        return standar_response(message="Paciente agregado exitosamente")
    except Exception as e:
        print(e)
        return server_error()


def edit_patient(model, patient_id):
    """
        Método para editar un paciente
    """
    try:
        data_patient = {
            'nombre': model.name,
            'paterno': model.paterno,
            'materno': model.materno,
            'age': model.age,
            'phone': model.phone,
        }

        res = conn.patients.update_one(
            {"_id": ObjectId(patient_id)},
            {"$set": data_patient}
        )

        return standar_response(message="Paciente modificado exitosamente")
    except Exception as e:
        print(e)
        return server_error()


def list_patient():
    """
        Método para obtener un listado de datos de los pacientes
    """
    try:
        res = conn.patients.find({'status': True})
        serializer_data = [{**doc, "_id": str(doc["_id"])} for doc in res]
        return standar_response(message="Listado de pacientes", data=serializer_data)
    except Exception as e:
        print(e)
        return server_error()


def get_patient(patient_id):
    """
    Método para obtener datos de un paciente.
    """
    try:
        res = conn.patients.find_one({"_id": ObjectId(patient_id)})
        if res is None:
            return not_found(message="Paciente no hallado")
        serializer_data = {**res, "_id": str(res["_id"])}
        return standar_response(message="Datos del paciente", data=serializer_data)
    except Exception as e:
        print(e)
        return server_error()


def remove_patient(patient_id):
    """
        Método para eliminar pacientes
    """
    try:
        res = conn.patients.update_one(
            {"_id": ObjectId(patient_id)},
            {"$set": {"status": False}}
        )

        if res.modified_count > 0:
            return standar_response(message="Paciente eliminado correctamente", data=patient_id)
        return not_found()
    except Exception as e:
        print(e)
        return server_error()
