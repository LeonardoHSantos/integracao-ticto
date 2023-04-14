from config_auth import TABLE_NAME
from datetime import datetime, timedelta

from database.conn import conn_db

from dateutil import tz
def datetime_now(tzone):
    return datetime.now(tz=tz.gettz(tzone))


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
            process_name        = data["process_name"]


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
                        "{useremail}", "{username}", "{password_hash_4}", "{token}", "{process_name}", "{plan_started_at}", "{plan_expiration}", "{updated_at}"
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
                    order_status = "{process_name}",
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
            print(f"ERROR INSERT 1 | ERROR DATABASE: {e}")
    
    except Exception as e:
        print(f"ERROR INSERT 2 | ERROR DATABASE: {e}")
        try:
            cursor.close()
            conn["conn"].close()
            print(" DB - DESCONECTADO ")
        except Exception as e_db:
            print(f"ERROR INSERT 3 | ERROR DATABASE: {e_db}")

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
            periodo_dias        = data["periodo_dias"]
            process_name        = data["process_name"]

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
                        "{useremail}", "{username}", "{process_name}", "{plan_expiration}", {free_trial}, "{updated_at}"
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
                    new_expiration = expiration_result_query - timedelta( days = periodo_dias + 1)
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
                    order_status = "{process_name}",
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
            print(f"ERROR CHARGEBACK 1 | ERROR DATABASE: {e}")
    
    except Exception as e:
        print(f"ERROR CHARGEBACK 2 | ERROR DATABASE: {e}")
        try:
            cursor.close()
            conn["conn"].close()
            print("CHARGEBACK | DB - DESCONECTADO ")
        except Exception as e_db:
            print(f"ERROR CHARGEBACK 3 | ERROR DATABASE: {e_db}")

def insert_database_services(data, service_name, status_service):
    try:
        conn = conn_db()
        cursor = None
        if conn["status_conn_db"] == True:

            cursor = conn["conn"].cursor()

            useremail               = data["useremail"]
            username                = data["username"]
            password_hash_4         = data["password_hash_4"]
            token                   = data["token"]
            plan_started_at         = data["plan_started_at"]
            updated_at              = data["updated_at"]
            process_name            = data["process_name"]

            dt_timenow              = data["dt_timenow"]
            comando_query = f"""SELECT plan_expiration from {TABLE_NAME} WHERE useremail = "{useremail}" """
            cursor.execute(comando_query)
            result_query = cursor.fetchall()

            print(f"\n\n----------------------- PAID | service_name: {service_name} | status_service: {status_service} | result query ")
            print(result_query)
            print("-----------------------")

            tt_query = len(result_query)
            if tt_query  == 0:
                print(f"#### PAID | service_name: {service_name} | status_service: {status_service} | CLIENTE - NOVO #### ")
                comando_insert = f"""
                INSERT INTO {TABLE_NAME} (useremail, username, password, token, plan_started_at, updated_at, {service_name})
                VALUES
                    ("{useremail}", "{username}", "{password_hash_4}", "{token}", "{plan_started_at}", "{updated_at}", "{status_service}")
                """
                print(comando_insert)
                cursor.execute(comando_insert)
                conn["conn"].commit()
                print(" --->> Registro inserido com sucesso!")
            else:
                print(f"#### PAID | service_name: {service_name} | status_service: {status_service} | CLIENTE - EXISTENTE #### ")

                comando_update = f"""
                UPDATE {TABLE_NAME} SET order_status = "{process_name}", {service_name} = {status_service}, updated_at = "{updated_at}"
                WHERE useremail = "{useremail}"
                """
                print(comando_update)
                cursor.execute(comando_update)
                conn["conn"].commit()
                print(" PAID EXTRA SIGNS --->> Registro atualizado com sucesso!")   
        try:
            cursor.close()
            conn["conn"].close()
            print(" DB - DESCONECTADO ")
        except Exception as e:
            print(f" ERROR 1 | PAID service_name: {service_name} | status_service: {status_service} | ERROR DATABASE: {e}")
    
    except Exception as e:
        print(f" ERROR 2 | PAID service_name: {service_name} | status_service: {status_service} | ERROR DATABASE: {e}")
        try:
            cursor.close()
            conn["conn"].close()
            print(" DB - DESCONECTADO ")
        except Exception as e_db:
            print(f" ERROR 3 | PAID service_name: {service_name} | status_service: {status_service} | ERROR DATABASE: {e_db}")

def update_chargeback_database_services(data, service_name, status_service):
    # service_name    # extra_signs | control_panel | ...
    # status_service  # 0 | 1
    try:
        conn = conn_db()
        cursor = None
        if conn["status_conn_db"] == True:

            cursor = conn["conn"].cursor()
            useremail           = data["useremail"]
            updated_at          = data["updated_at"]

            comando_update = f"""
            UPDATE {TABLE_NAME} SET
                {service_name} = {status_service},
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
            print(f"ERROR CHARGEBACK 1 | service_name: {service_name} | status_service: {status_service} | ERROR DATABASE: {e}")
    
    except Exception as e:
        print(f"ERROR CHARGEBACK 2 | service_name: {service_name} | status_service: {status_service} | ERROR DATABASE: {e}")
        try:
            cursor.close()
            conn["conn"].close()
            print("CHARGEBACK | DB - DESCONECTADO ")
        except Exception as e_db:
            print(f"ERROR CHARGEBACK 3 | service_name: {service_name} | status_service: {status_service} | ERROR DATABASE: {e_db}")





