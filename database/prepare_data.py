import bcrypt, os
from dateutil import tz
from datetime import datetime, timedelta

def datetime_now(tzone):
    return datetime.now(tz=tz.gettz(tzone))


def prepapre_date(data):
    # ---------------------------------------------
    _product_id = data["item"]["product_id"]
    _product_name = data["item"]["product_name"]
    order_status = data["status"]

    periodo_dias = 0
    if _product_name == "Tecnologia Z - Plano Anual":
        periodo_dias = 366
    elif _product_name == "Tecnologia Z - Plano Semestral":
        periodo_dias = 183
    elif _product_name == "Tecnologia Z - Plano Trimestral":
        periodo_dias = 91
    elif _product_name == "Tecnologia Z - Plano Mensal":
        periodo_dias = 31
    
    if order_status == "paid":
        return process_paid(data=data, process_name=order_status, periodo_dias=periodo_dias)
    elif order_status == "waiting_payment":
        return process_paid(data=data, process_name=order_status, periodo_dias=periodo_dias)
    elif order_status == "chargeback":
        return process_chargedback(data=data, process_name=order_status, periodo_dias=periodo_dias)
    # elif order_status == "refused":


def process_chargedback(data, process_name, periodo_dias):
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
    }
    return {"process_name": process_name, "data": obj_database}


def process_paid(data, process_name, periodo_dias):
    dt_timenow = datetime_now(tzone="UTC-3")
    _payment_method = data["payment_method"]
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
    }
    return {"process_name": process_name, "data": obj_database}