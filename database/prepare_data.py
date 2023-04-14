import bcrypt, os
from dateutil import tz
from datetime import datetime, timedelta
from database import insert


def datetime_now(tzone):
    return datetime.now(tz=tz.gettz(tzone))


def prepapre_date(data, process_name):
    # ---------------------------------------------
    _product_name = data["item"]["product_name"]
    order_status = data["status"]
    
    periodo_dias = 0
    lista_planos = ["Tecnologia Z - Plano Anual", "Tecnologia Z - Plano Semestral", "Tecnologia Z - Plano Trimestral", "Tecnologia Z - Plano Mensal"]
    if _product_name == "Tecnologia Z - Plano Anual":
        periodo_dias = 366
    elif _product_name == "Tecnologia Z - Plano Semestral":
        periodo_dias = 183
    elif _product_name == "Tecnologia Z - Plano Trimestral":
        periodo_dias = 91
    elif _product_name == "Tecnologia Z - Plano Mensal":
        periodo_dias = 30
    
    print(f"**************  _product_name: {_product_name} | periodo_dias: {periodo_dias}")
    # ----------------------------------------------------------------------------------------------
    if process_name == "paid" and _product_name == "Receba o Dobro de Sinais Diariamente":
        data_db = process_paid_services(data=data, process_name=process_name)
        insert.insert_database_services(
            data=data_db["data"],
            service_name="extra_signs",
            status_service=1)
    # ---------
    elif process_name == "chargeback" and _product_name == "Receba o Dobro de Sinais Diariamente":
        data_db =  process_chargeback_services(data=data)
        insert.update_chargeback_database_services(
            data=data_db["data"],
            service_name="extra_signs",
            status_service=0)
    # -----------------------------------------------------
    elif process_name == "paid" and _product_name == "Automatize suas Operações":
        data_db = process_paid_services(data=data, process_name=process_name)
        insert.insert_database_services(
            data=data_db["data"],
            service_name="automatic_robot",
            status_service=1)
    elif process_name == "chargeback" and _product_name == "Automatize suas Operações":
        data_db =  process_chargeback_services(data=data)
        insert.update_chargeback_database_services(
            data=data_db["data"],
            service_name="automatic_robot",
            status_service=0)
    # ----------------------------------------------------------------------------------------------
    elif process_name == "paid" and _product_name == "Paienl de Controle":
        data_db = process_paid_services(data=data, process_name=process_name)
        insert.insert_database_services(
            data=data_db["data"],
            service_name="control_panel",
            status_service=1)
    elif process_name == "chargeback" and _product_name == "Paienl de Controle":
        data_db =  process_chargeback_services(data=data)
        insert.update_chargeback_database_services(
            data=data_db["data"],
            service_name="control_panel",
            status_service=0)
    # ----------------------------------------------------------------------------------------------

    elif process_name == "paid" and _product_name in lista_planos:
        data_db = process_paid(data=data, process_name=process_name, periodo_dias=periodo_dias)
        insert.insert_database(data=data_db["data"])
    elif process_name == "chargeback" and _product_name in lista_planos:
        data_db =  process_chargeback(data=data, process_name=order_status, periodo_dias=periodo_dias)
        insert.update_chargeback_database(data=data_db["data"])

# Receba o Dobro de Sinais Diariamente
# Automatize suas Operações
# Paienl de Controle
# Tecnologia Z - Plano Anual
# Tecnologia Z - Plano Semestral
# Tecnologia Z - Plano Trimestral
# Tecnologia Z - Plano Mensal
def process_chargeback_services(data):
    process_name = "chargeback"
    dt_timenow = datetime_now(tzone="UTC-3")
    updated_at =  datetime.strftime((dt_timenow), "%Y-%m-%d %H:%M:%S")

    _useremail = data["customer"]["email"]
    _username = data["customer"]["name"]
    _order_status = data["status"]
    obj_database = {
        "useremail": _useremail,
        "username": _username,
        "updated_at": updated_at,
        "order_status": _order_status,
    }
    return {"process_name": process_name, "data": obj_database}

def process_chargeback(data, process_name, periodo_dias):
    process_name = "chargeback"
    dt_timenow = datetime_now(tzone="UTC-3")
    updated_at =  datetime.strftime((dt_timenow), "%Y-%m-%d %H:%M:%S")
    updated_at_dt =  datetime.strptime(updated_at, "%Y-%m-%d %H:%M:%S")

    _useremail = data["customer"]["email"]
    _username = data["customer"]["name"]
    _order_status = data["status"]
    obj_database = {
        "useremail": _useremail,
        "username": _username,
        "order_status": _order_status,
        "plan_expiration": updated_at,
        "free_trial": 0,
        "updated_at": updated_at,
        "dt_timenow": dt_timenow,
        "updated_at_dt": updated_at_dt,
        "periodo_dias": periodo_dias,
        "process_name": process_name,
    }
    return {"process_name": process_name, "data": obj_database}

def process_paid(data, process_name, periodo_dias):
    process_name = "paid"
    dt_timenow = datetime_now(tzone="UTC-3")
    # ---------------------------------------------
    _useremail = data["customer"]["email"]
    _username = data["customer"]["name"]
    _password = "123456"
    _password_hash_4 = bcrypt.hashpw(_password.encode("utf8"), bcrypt.gensalt()).decode("utf-8")
    order_status = data["status"]
    # _token = data["token"]
    _token_os = os.urandom(50).hex()
    _plan_started_at = dt_timenow.strftime("%Y-%m-%d %H:%M:%S")
    _plan_expiration = datetime.strftime((dt_timenow + timedelta(days=periodo_dias)), "%Y-%m-%d %H:%M:%S")
    _plan_expiration_dt = datetime.strptime(_plan_expiration, "%Y-%m-%d %H:%M:%S")

    updated_at =  datetime.strftime((dt_timenow), "%Y-%m-%d %H:%M:%S")
    obj_database = {
        "useremail": _useremail,
        "username": _username,
        "password_hash_4": _password_hash_4,
        "order_status": order_status,
        "token": _token_os,
        "plan_started_at": _plan_started_at,
        "plan_expiration": _plan_expiration,
        "free_trial":0,
        "updated_at": updated_at,
        "dt_timenow": dt_timenow,
        "_plan_expiration_dt": _plan_expiration_dt,
        "process_name": process_name,
    }
    return {"process_name": process_name, "data": obj_database}

def process_paid_services(data, process_name):
    process_name = "paid"
    dt_timenow = datetime_now(tzone="UTC-3")
    # ---------------------------------------------
    _useremail = data["customer"]["email"]
    _username = data["customer"]["name"]
    _password = "123456"
    _password_hash_4 = bcrypt.hashpw(_password.encode("utf8"), bcrypt.gensalt()).decode("utf-8")
    order_status = data["status"]
    _token_os = os.urandom(50).hex()
    _plan_started_at = dt_timenow.strftime("%Y-%m-%d %H:%M:%S")

    updated_at =  datetime.strftime((dt_timenow), "%Y-%m-%d %H:%M:%S")
    obj_database = {
        "useremail": _useremail,
        "username": _username,
        "password_hash_4": _password_hash_4,
        "order_status": order_status,
        "token": _token_os,
        "plan_started_at": _plan_started_at,
        "updated_at": updated_at,
        "dt_timenow": dt_timenow,
        "process_name": process_name,
    }

    return {"process_name": process_name, "data": obj_database}