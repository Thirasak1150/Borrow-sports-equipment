#การเชื่อมต่อระบบการจัดการฐานข้อมูล (MySQL) ชื่อว่า school2
import mysql.connector
from datetime import datetime, timedelta
mycursor = ...

mycursor = None
mydb = None

def connectdatabase():
    global mycursor, mydb  # กำหนดให้ mycursor และ mydb เป็นตัวแปร global
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="plankton273855",
        database="school2"
    )
    try:
        if mydb.is_connected():
            print('เชื่อมต่อกับฐานข้อมูล MySQL สำเร็จ')
    except mysql.connector.Error as error:
        print(f'เกิดข้อผิดพลาดในการเชื่อมต่อ: {error}')
    mycursor = mydb.cursor()
    return

connectdatabase()




# ฟังก์ชันสำหรับการยืมอุปกรณ์กีฬา
def borrow_equipment():
    student_id = input("ป้อนรหัสประจำตัวนักเรียน: ")
    equipment_id = input("ป้อนรหัสอุปกรณ์กีฬาที่ต้องการยืม: ")
    # ตรวจสอบว่าอุปกรณ์สามารถยืมได้หรือไม่
    query = "SELECT * FROM sports_equipment WHERE  sport_id = %s"
    query2 = "SELECT s_name FROM student WHERE id = %s"
    params = (equipment_id,)
    params2 = (student_id,)
    mycursor.execute(query,params)
    tb = mycursor.fetchone()
    mycursor.execute(query2,params2)
    tb2 = mycursor.fetchone()
    if tb is None and tb2 is None:
        print('ไม่พบข้อมูลอุปกรณ์เเละข้อมูลนักเรียน')
        borrow_equipment()
        return
    elif tb is None :
        print('ไม่พบข้อมูลอุปกรณ์')
        borrow_equipment()
        return
    elif tb2 is None :
        print('ไม่พบข้อมูลนักเรียน')
        borrow_equipment()
        return
    else:
        print('พบข้อมูลนักเรียนเเละข้อมูลอุปกรณ์')
        print("ชื่ออุปกรณ์: "+tb[1])
        print("ชื่อผู้ยืม: "+tb2[0])
        query = "SELECT * FROM borrow WHERE status_ = %s AND id_student = %s "
        val = ("ยังไม่คืน",student_id)
        mycursor.execute(query,val)
        equipment_data = mycursor.fetchall()
        if equipment_data is None:
            print("ไม่เจอข้อมูลที่ยังไม่คืน")
              # บันทึกข้อมูลการยืม
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            due_time = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S')  # กำหนดเวลาคืนในอีก 7 วัน
            print("เริ่มยืม " + current_time)
            print("วันคืน " + due_time)
            check = input("ยืนยันให้ :" + tb2[0] + " ยืม " + tb[1] +  " หรือไม่ (yes/no):")
            if check == "yes":
                query3 = "SELECT count_equipment FROM sports_equipment WHERE sport_id = %s"
                params3 = (equipment_id,)
                mycursor.execute(query3, params3)
                myresult = mycursor.fetchone()

                if myresult:
                    updated_value = myresult[0] - 1
                
                    print("ยืมไปเเล้วจำนวนอุปกรณ์กีฬาคงเหลือ:", updated_value)

                    # อัปเดตจำนวนอุปกรณ์ในสต็อก
                    query4 = "UPDATE sports_equipment SET count_equipment = %s WHERE sport_id = %s"
                    params4 = (updated_value, equipment_id)
                    mycursor.execute(query4, params4)
                    mydb.commit()  # Commit การเปลี่ยนแปลงข้อมูล
                # เพิ่มข้อมูลการยืมป
                sqlInsert = "INSERT INTO borrow (id_student, id_sport_equiment, start_borrow_date, start_return_date,status_) VALUES (%s, %s, %s, %s,%s)"
                val = (student_id, equipment_id, current_time, due_time,"ยังไม่คืน")
                mycursor.execute(sqlInsert, val)
                mydb.commit()
                print("ทำการยืมอุปกรณ์กีฬาเรียบร้อยแล้ว")
                return
        else:
            print("พบอุปกรณ์ที่ยังไม่คืน")
            for equipment in equipment_data:
                print("รหัสนักเรียน: " + str(equipment[0]) + " รหัสอุปกรณ์: " + str(equipment[1]) + " วันเริ่มยืม: " + str(equipment[2])
                    + " วันที่คืน: " + str(equipment[3])+ " สถานะ: " + str(equipment[4]))
              # บันทึกข้อมูลการยืม
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        due_time = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S')  # กำหนดเวลาคืนในอีก 7 วัน
        print("เริ่มยืม " + current_time)
        print("วันคืน " + due_time)
        check = input("ยืนยันให้ :" + tb2[0] + " ยืม " + tb[1] +  " หรือไม่ (yes/no):")
        if check == "yes":
            query3 = "SELECT count_equipment FROM sports_equipment WHERE sport_id = %s"
            params3 = (equipment_id,)
            mycursor.execute(query3, params3)
            myresult = mycursor.fetchone()

            if myresult:
                updated_value = myresult[0] - 1
            
                print("ยืมไปเเล้วจำนวนอุปกรณ์กีฬาคงเหลือ:", updated_value)

                # อัปเดตจำนวนอุปกรณ์ในสต็อก
                query4 = "UPDATE sports_equipment SET count_equipment = %s WHERE sport_id = %s"
                params4 = (updated_value, equipment_id)
                mycursor.execute(query4, params4)
                mydb.commit()  # Commit การเปลี่ยนแปลงข้อมูล
            # เพิ่มข้อมูลการยืมป
            sqlInsert = "INSERT INTO borrow (id_student, id_sport_equiment, start_borrow_date, start_return_date,status_) VALUES (%s, %s, %s, %s,%s)"
            val = (student_id, equipment_id, current_time, due_time,"ยังไม่คืน")
            mycursor.execute(sqlInsert, val)
            mydb.commit()
            print("ทำการยืมอุปกรณ์กีฬาเรียบร้อยแล้ว")
            return
      


# ฟังก์ชันสำหรับการคืนอุปกรณ์กีฬา
def return_equipment():
    student_id = input("ป้อนรหัสประจำตัวนักเรียน: ")
    equipment_id = input("ป้อนรหัสอุปกรณ์กีฬาที่คืน: ")
    # ตรวจสอบว่าอุปกรณ์สามารถคืนได้หรือไม่
    query = "SELECT * FROM sports_equipment WHERE  sport_id = %s"
    query2 = "SELECT s_name FROM student WHERE id = %s"
    params = (equipment_id,)
    params2 = (student_id,)
    mycursor.execute(query,params)
    tb = mycursor.fetchone()
    mycursor.execute(query2,params2)
    tb2 = mycursor.fetchone()
    if tb is None and tb2 is None:
        print('ไม่พบข้อมูลอุปกรณ์เเละข้อมูลนักเรียน')
        return_equipment()
        return
    elif tb is None :
        print('ไม่พบข้อมูลอุปกรณ์')
        return_equipment()
        return
    elif tb2 is None :
        print('ไม่พบข้อมูลนักเรียน')
        return_equipment()
        return
    else:
        print('พบข้อมูลนักเรียนเเละข้อมูลอุปกรณ์กีฬา')
        print("ชื่ออุปกรณ์กีฬา: "+tb[0])
        print("ชื่อผู้ยืม: "+tb2[0])
    # บันทึกข้อมูลการคืน
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    check = input("ยืนยันให้ :" + tb2[0] + " คืน " + tb[1] +  " หรือไม่ (yes/no):")
    if check == "yes":
        sql = "UPDATE borrow SET end_return_date = %s, 	status_ = %s WHERE 	id_student = %s AND id_sport_equiment = %s AND status_  = %s "
        val = (current_time,"คืนเเล้ว",student_id,equipment_id,"ยังไม่คืน")
        mycursor.execute(sql, val)
        mydb.commit()
        print("ทำการคืนอุปกรณ์กีฬาเรียบร้อยแล้ว")
        query3 = "SELECT count_equipment FROM sports_equipment WHERE sport_id = %s"
        params3 = (equipment_id,)
        mycursor.execute(query3, params3)
        myresult = mycursor.fetchone()

        if myresult:
            updated_value = myresult[0] + 1
        
            print("จำนวนอุปกรณ์คงเหลือ:", updated_value)

            # อัปเดตจำนวนอุปกรณ์ในสต็อก
            query4 = "UPDATE sports_equipment SET count_equipment = %s WHERE sport_id = %s"
            params4 = (updated_value, equipment_id)
            mycursor.execute(query4, params4)
            mydb.commit()  # Commit การเปลี่ยนแปลงข้อมูล
            return
    else:
        return
# ฟังก์ชันสำหรับเเก้ไขจำนวนอุปกรณ์กีฬา
def editcount_equipment():
    sql_query = "SELECT * FROM sports_equipment"
    mycursor.execute(sql_query)
    equipment_data = mycursor.fetchall()
    for equipment in equipment_data:
        print("รหัสอุปกรณ์: " + str(equipment[0]) + " ชื่ออุปกรณ์: " + equipment[1] + " จำนวนคงเหลือ: " + str(equipment[2]))
    equipment_id = input("ป้อนรหัสอุปกรณ์กีฬาที่ต้องการแก้ไขจำนวน: ")
    # ตรวจสอบว่าอุปกรณ์สามารถยืมได้หรือไม่
    query = "SELECT * FROM sports_equipment WHERE  sport_id = %s"
    params = (equipment_id,)
    mycursor.execute(query,params)
    tb = mycursor.fetchone()
    if tb is None and tb2 is None:
        print('ไม่พบข้อมูลอุปกรณ์กรุณาเลือกใหม่')
        editcount_equipment()
        return
    else:
        print('พบข้อมูลอุปกรณ์')
        count_equipment = input("ต้องการแก้จำนวนอุปกรณ์  "+tb[1] +" เป็นเท่าไหร่ = ")
        query4 = "UPDATE sports_equipment SET count_equipment = %s WHERE sport_id = %s"
        params4 = (count_equipment, equipment_id)
        mycursor.execute(query4, params4)
        mydb.commit()  # Commit การเปลี่ยนแปลงข้อมูล
        print("แก้ไขจำนวนคงเหลือ"+tb[1]+"เป็น "+count_equipment+ " เรียบร้อบ")
# ฟังก์ชันสำหรับลบอุปกรณ์กีฬา
def delete_equipment():
    sql_query = "SELECT * FROM sports_equipment"
    mycursor.execute(sql_query)
    equipment_data = mycursor.fetchall()
    for equipment in equipment_data:
        print("รหัสอุปกรณ์: " + str(equipment[0]) + " ชื่ออุปกรณ์: " + equipment[1] + " จำนวนคงเหลือ: " + str(equipment[2]))
    equipment_id = input("ป้อนรหัสอุปกรณ์กีฬาที่ต้องการลบ: ")
    # ตรวจสอบว่าอุปกรณ์สามารถยืมได้หรือไม่
    query = "SELECT * FROM sports_equipment WHERE  sport_id = %s"
    params = (equipment_id,)
    mycursor.execute(query,params)
    tb = mycursor.fetchone()
    if tb is None and tb2 is None:
        print('ไม่พบข้อมูลอุปกรณ์กรุณาเลือกใหม่')
        editcount_equipment()
        return
    else:
        print('พบข้อมูลอุปกรณ์')
        check = input("ต้องการลบอุปกรณ์  "+tb[1] +" ใช่หรือไม่ (yes/no) :")
        if check == "yes":
            delete_query = "DELETE FROM sports_equipment WHERE sport_id = %s"
            params4 = (equipment_id,)
            mycursor.execute(delete_query, params4)
            mydb.commit()  # Commit การเปลี่ยนแปลงข้อมูล
            print("ลบ"+tb[1]+ "เรียบร้อบ!!")
            return
        
# ฟังก์ชันสำหรับเพิ่มอุปกรณ์กีฬา
def Add_equipment():
    sql_query = "SELECT * FROM sports_equipment"
    mycursor.execute(sql_query)
    equipment_data = mycursor.fetchall()
    for equipment in equipment_data:
        print("รหัสอุปกรณ์: " + str(equipment[0]) + " ชื่ออุปกรณ์: " + equipment[1] + " จำนวนคงเหลือ: " + str(equipment[2]))
    name_equipment = input("ป้อนชื่ออุปกรณ์กีฬาที่ต้องการสร้าง: ")
    countt_equipment = int(input("ป้อนจำนวนอุปกรณ์กีฬาที่ต้องการสร้าง: ")) 
    # ตรวจสอบว่าอุปกรณ์สามารถยืมได้หรือไม่
    query = "SELECT * FROM sports_equipment ORDER BY sport_id DESC"
    mycursor.execute(query)
    tb = mycursor.fetchone()
    if countt_equipment > 0 :
        tmpnew_sport_id = int(tb[0]) + 1
        new_sport_id = "00"+str(tmpnew_sport_id)
        check = input("ยืนยันที่จะสร้าง id:" + new_sport_id + " ชื่อ " + name_equipment + " จำนวน " + str(countt_equipment) + " หรือไม่ (yes/no):")
        if check == "yes":
            connectdatabase()
            print(new_sport_id,name_equipment,countt_equipment)
            sqlInsert_T = "INSERT INTO sports_equipment (sport_id, sport_name, count_equipment) VALUES (%s, %s, %s)"
            valABC = (new_sport_id,name_equipment,countt_equipment)
            mycursor.execute(sqlInsert_T, valABC)
            mydb.commit()
            print("ทำการสร้างอุปกรณ์กีฬาใหม่ id:" + new_sport_id + " ชื่อ " + name_equipment + " จำนวน " + str(countt_equipment) + " เรียบร้อยแล้ว")
            return
        else:
            print("ยกเลิกการสร้างอุปกรณ์กีฬา")
            return
    else:
        print('กรุณากรอกจำนวนให้ถูกต้อง')
        Add_equipment()
        return

      
# ฟังก์ชันเมนูเก้ไขอุปกรณ์กีฬา        
def edit_equipment():
    sql_query = "SELECT * FROM sports_equipment"
    mycursor.execute(sql_query)
    equipment_data = mycursor.fetchall()
    for equipment in equipment_data:
        print("รหัสอุปกรณ์: " + str(equipment[0]) + " ชื่ออุปกรณ์: " + equipment[1] + " จำนวนคงเหลือ: " + str(equipment[2]))
    print("1. แก้อุปกรณ์กีฬาจำนวน")
    print("2. ลบอุปกรณ์กีฬา")
    print("3. เพิ่มอุปกรณ์กีฬา")
    print("0. ออกจากแก้ไขอุปกรณ์กีฬา")
    choice = input("เลือกทำรายการ: ")
    if choice == '1':
            editcount_equipment()
            return
    elif choice == '2':
            delete_equipment()
            return
    elif choice == '3':
            Add_equipment()
            return
    elif choice == '0':
            return
    else:
            print("กรุณาเลือกรายการให้ถูกต้อง")
            edit_equipment()

def list_borrow():
    print("1. แสดงสถานะเฉพาะที่ยังไม่คืน")
    print("2. แสดงสถานะเฉพาะที่ยังคืนเเล้ว")
    print("3. แสดงสถานะทั้งหมด")
    choice = input("เลือกทำรายการ: ")
    if choice == '1':
            query = "SELECT * FROM borrow WHERE status_ = %s  "
            val = ("ยังไม่คืน",)
            mycursor.execute(query,val)

            equipment_data = mycursor.fetchall()
            for equipment in equipment_data:
                print("รหัสนักเรียน: " + str(equipment[0]) + " รหัสอุปกรณ์: " + str(equipment[1]) + " วันเริ่มยืม: " + str(equipment[2])
                      + " วันที่คืน: " + str(equipment[3])+ " สถานะ: " + str(equipment[4]))

    elif choice == '2':
            query = "SELECT * FROM borrow WHERE status_ = %s  "
            val = ("คืนเเล้ว",)
            mycursor.execute(query,val)

            equipment_data = mycursor.fetchall()
            for equipment in equipment_data:
                print("รหัสนักเรียน: " + str(equipment[0]) + " รหัสอุปกรณ์: " + str(equipment[1]) + " วันเริ่มยืม: " + str(equipment[2])
                      + " วันที่คืน: " + str(equipment[3])+ " สถานะ: " + str(equipment[4]))
    elif choice == '3':
            query = "SELECT * FROM borrow  "
            mycursor.execute(query)
            equipment_data = mycursor.fetchall()
            for equipment in equipment_data:
                print("รหัสนักเรียน: " + str(equipment[0]) + " รหัสอุปกรณ์: " + str(equipment[1]) + " วันเริ่มยืม: " + str(equipment[2])
                      + " วันที่คืน: " + str(equipment[3])+ " สถานะ: " + str(equipment[4]))

    elif choice == '0':
             return
    return
    
# เมนู
def menu():
    while True:
        print("\nระบบยืม-คืนอุปกรณ์กีฬา")
        print("1. ยืมอุปกรณ์กีฬา")
        print("2. คืนอุปกรณ์กีฬา")
        print("3. แก้ไขอุปกรณ์กีฬา")
        print("4. เช็คการสถาณะการยืม")
        print("0. ออกจากระบบ")
        choice = input("เลือกทำรายการ: ")
        if choice == '1':
            borrow_equipment()
        elif choice == '2':
            return_equipment()
        elif choice == '3':
             edit_equipment()
        elif choice == '4':
             list_borrow()
        elif choice == '0':
            break
        else:
            print("กรุณาเลือกรายการให้ถูกต้อง")
menu()