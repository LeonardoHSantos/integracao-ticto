from config_auth import TABLE_NAME
from datetime import datetime, timedelta

from database.conn import conn_db

from dateutil import tz
def datetime_now(tzone):
    return datetime.now(tz=tz.gettz(tzone))

def process_database(data):
    if data["process_name"] == "paid":
        return insert_database(data["data"])
    elif data["process_name"] == "waiting_payment":
        return insert_database(data["data"])
    elif data["process_name"] == "chargeback":
        return update_chargeback_database(data["data"])



def insert_database(data):
    try:
        conn = conn_db()
        cursor = None
        if conn["status_conn_db"] == True:

            cursor = conn["conn"].cursor()

            useremail           = data["useremail"]
            username            = data["username"]
            password_hash_4     = data["password_hash_4"]
            order_status        = data["order_status"]
            token               = data["token"]
            plan_started_at     = data["plan_started_at"]
            plan_expiration     = data["plan_expiration"]
            free_trial          = data["free_trial"]
            updated_at           = data["updated_at"]
            dt_timenow          = data["dt_timenow"]
            plan_expiration_dt  = data["_plan_expiration_dt"]


            comando_query = f"""SELECT plan_expiration from {TABLE_NAME} WHERE useremail = "{useremail}" """
            cursor.execute(comando_query)
            result_query = cursor.fetchall()

            print("\n\n----------------------- result query ")
            print(result_query)
            print("-----------------------")

            tt_query = len(result_query)

            if tt_query  == 0:
                print("#### CLIENTE - NOVO #### ")
                comando_insert = f"""
                INSERT INTO {TABLE_NAME}
                    (useremail, username, password, token, order_status, plan_started_at, plan_expiration, updated_at)
                VALUES
                    (
                        "{useremail}", "{username}", "{password_hash_4}", "{token}", "{order_status}", "{plan_started_at}", "{plan_expiration}", "{updated_at}"
                    )"""
                print(comando_insert)
                cursor.execute(comando_insert)
                conn["conn"].commit()
                print(" --->> Registro inserido com sucesso!")

            else:
                # calcular datas
                expiration_result_query = result_query[0][0]
                dt = datetime.now()
                new_expiration = plan_expiration_dt + timedelta(days=abs(dt - expiration_result_query).days + 1 )

                print("#### CLIENTE - EXISTENTE #### ")
                print(" **************** DATAS **************** ")
                print(f"DT-NOW: {dt_timenow}")
                print(f"expiration_result_query: {expiration_result_query}")
                print(f"new_expiration: {new_expiration}")


                comando_update = f"""
                UPDATE {TABLE_NAME} SET
                    order_status = "{order_status}",
                    free_trial = {free_trial},
                    plan_expiration = "{new_expiration}",
                    updated_at = "{updated_at}"
                WHERE
                    useremail = "{useremail}"
                """
                print(comando_update)
                cursor.execute(comando_update)
                conn["conn"].commit()
                print(" --->> Registro atualizado com sucesso!")   
        try:
            cursor.close()
            conn["conn"].close()
            print(" DB - DESCONECTADO ")
        except Exception as e:
            print(f"#1 - ERRO DATABASE: {e}")
    
    except Exception as e:
        print(f"#4 ERRO DATABASE: {e}")
        try:
            cursor.close()
            conn["conn"].close()
            print(" DB - DESCONECTADO ")
        except Exception as e_db:
            print(f"#2 ERRO DATABASE: {e_db}")

def update_chargeback_database(data):
    try:
        conn = conn_db()
        cursor = None
        if conn["status_conn_db"] == True:

            cursor = conn["conn"].cursor()

            useremail           = data["useremail"]
            username            = data["username"]
            order_status        = data["order_status"]
            plan_expiration     = data["plan_expiration"]
            free_trial          = data["free_trial"]
            updated_at          = data["updated_at"]
            dt_timenow          = data["dt_timenow"]
            updated_at_dt       = data["updated_at_dt"]
            periodo_dias        = data["periodo_dias"]

            comando_query = f"""SELECT plan_expiration from {TABLE_NAME} WHERE useremail = "{useremail}" """
            cursor.execute(comando_query)
            result_query = cursor.fetchall()

            print("\n\n----------------------- result query ")
            print(result_query)
            print("-----------------------")

            tt_query = len(result_query)

            if tt_query  == 0:
                print("#### CLIENTE - NOVO #### ")
                comando_insert = f"""
                INSERT INTO {TABLE_NAME}
                    (useremail, username, order_status, plan_expiration, free_trial, updated_at)
                VALUES
                    (
                        "{useremail}", "{username}", "{order_status}", "{plan_expiration}", {free_trial}, "{updated_at}"
                    )"""
                print(comando_insert)
                cursor.execute(comando_insert)
                conn["conn"].commit()
                print(" --->> Registro inserido com sucesso!")

            else:
                print("#### CLIENTE - EXISTENTE #### ")
                expiration_result_query = result_query[0][0]
                
                try:
                    dt = datetime.now()
                    new_expiration = expiration_result_query - timedelta( days = periodo_dias)
                    if new_expiration <= dt:
                        new_expiration = dt.replace(hour=0, minute=0, second=0)
                    
                    print("#### CLIENTE - EXISTENTE #### ")
                    print(" **************** DATAS **************** ")
                    print(f"DT-NOW: {updated_at}")

                    print(f"expiration_result_query: {expiration_result_query}")
                    print(f"new_expiration: {new_expiration}")
                
                except Exception as e:
                    print(f"CHARGEBACK | Error: {e}")

                comando_update = f"""
                UPDATE {TABLE_NAME} SET
                    order_status = "{order_status}",
                    plan_expiration = "{new_expiration}",
                    free_trial = {free_trial},
                    updated_at = "{updated_at}"
                WHERE
                    useremail = "{useremail}"
                """
                print(comando_update)
                cursor.execute(comando_update)
                conn["conn"].commit()
                print(" --->> CHARGEBACK | Registro atualizado!")   
        try:
            cursor.close()
            conn["conn"].close()
            print("CHARGEBACK | DB - DESCONECTADO ")
        except Exception as e:
            print(f"CHARGEBACK |#1 - ERRO DATABASE: {e}")
    
    except Exception as e:
        print(f"CHARGEBACK | #2 ERRO DATABASE: {e}")
        try:
            cursor.close()
            conn["conn"].close()
            print("CHARGEBACK | DB - DESCONECTADO ")
        except Exception as e_db:
            print(f"CHARGEBACK | #3 ERRO DATABASE: {e_db}")


