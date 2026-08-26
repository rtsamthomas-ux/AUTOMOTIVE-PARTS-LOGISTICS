import mysql.connector as sqltor

mycon= sqltor.connect(
    host="localhost",
    user="root",
    password="root"
)
cur = mycon.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS automotive_db")
mycon.commit()

cur.execute("USE automotive_db")


cur.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INT,
            name VARCHAR(100),
            phone_number VARCHAR(15)
        )
    """)

cur.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            id INT,
            product_name VARCHAR(100),
            vehicle_type VARCHAR(30),
            quantity INT,
            price FLOAT
        )
    """)


cur.execute("""
        CREATE TABLE IF NOT EXISTS c_payments (
            id INT,
            total_amount INT,
            method VARCHAR(20),
            payment_status VARCHAR(255)
        )
    """)
cur.execute("""
        CREATE TABLE IF NOT EXISTS workers (
            Id VARCHAR(20),
            password VARCHAR(20),
            qualification VARCHAR(30)
        )
    """)

cur.execute("""
        CREATE TABLE IF NOT EXISTS complaint (
            complain VARCHAR(100),
            worker VARCHAR(20)
        )
    """)

cur.execute("""
        CREATE TABLE IF NOT EXISTS demand (
            demanded VARCHAR(100),
            worker VARCHAR(20)
        )
    """)



a4={'Connecting rod':200 ,'Spark plug':150 ,'Engine blocks':5000
    ,'Fly wheel':1500,'Timing belt':400,'Exhaust manifold':1200,'Catalytic converter':10000
    ,'Exhaust pipes':1200 ,'Muffler':5000 ,'Oxygen sensor':2500 ,'Shock absorber':1800 ,'Ball joint':6000
    ,'Stabilizer':7000,'Strut bar': 2000,'Lateral control arm':3250 ,'Brake pedal':200,'Brake booster':1000
    ,'Brake lines':240 ,'Brake caliper':900 ,'Brake piston':1400,'Clutch':500 ,'Gear box':8500,
    'Torque coverter':20000,'Transmission gasket':2000 ,'Live axle':300 ,'Wind shield':3000 ,'Head light':800 ,
    'Side mirror':1000 ,'Bumper':1500,'Wheel':1200, 'Filters':300 ,'Hoses':1000 ,'Coolent oil':800 ,'Brake oil':200 ,
    'Wiper blades':300,'Turbo charges':3000,'Short shifters':1900 ,'High flow air filters':5000 ,'Pressure plates':5000 ,
    'Sway bars':8000, 'Antilog braking system':7000,'Electronic stability controller':6000 ,'Tire monitoring':5000 ,
    'Backup camera':2500 ,'Traction controller':6000,'Radiator':500 ,'Cooling fan':250 ,
    'Overflow tank':3000 ,'Pressure cap':2000 ,'Thermostat':1000 }
l1= list(a4.keys())
l2=list(a4.values())
l1=['invalid']+l1
l2=['invalid']+l2

def reset_customer_data():
    d1={'Connecting rod':0 ,'Spark plug':0 ,'Engine blocks':0
        ,'Fly wheel':0,'Timing belt':0,'Exhaust manifold':0,'Catalytic converter':0
        ,'Exhaust pipes':0 ,'Muffler':0 ,'Oxygen sensor':0 ,'Shock absorber':0 ,'Ball joint':0
        ,'Stabilizer':0,'Strut bar': 0,'Lateral control arm':0 ,'Brake pedal':0,'Brake booster':0
        ,'Brake lines':0 ,'Brake caliper':0 ,'Brake piston':0,'Clutch':0 ,'Gear box':0,
        'Torque coverter':0,'Transmission gasket':0 ,'Live axle':0 ,'Wind shield':0 ,'Head light':0 ,
        'Side mirror':0 ,'Bumper':0,'Wheel':0, 'Filters':0 ,'Hoses':0 ,'Coolent oil':0 ,'Brake oil':0 ,
        'Wiper blades':0,'Turbo charges':0,'Short shifters':0 ,'High flow air filters':0 ,'Pressure plates':0 ,
        'Sway bars':0, 'Antilog braking system':0,'Electronic stability controller':0 ,'Tire monitoring':0 ,
        'Backup camera':0 ,'Traction controller':0,'Radiator':0 ,'Cooling fan':0 ,
        'Overflow tank':0 ,'Pressure cap':0 ,'Thermostat':0 }
    d2={'Connecting rod':0 ,'Spark plug':0 ,'Engine blocks':0
        ,'Fly wheel':0,'Timing belt':0,'Exhaust manifold':0,'Catalytic converter':0
        ,'Exhaust pipes':0 ,'Muffler':0 ,'Oxygen sensor':0 ,'Shock absorber':0 ,'Ball joint':0
        ,'Stabilizer':0,'Strut bar': 0,'Lateral control arm':0 ,'Brake pedal':0,'Brake booster':0
        ,'Brake lines':0 ,'Brake caliper':0 ,'Brake piston':0,'Clutch':0 ,'Gear box':0,
        'Torque coverter':0,'Transmission gasket':0 ,'Live axle':0 ,'Wind shield':0 ,'Head light':0 ,
        'Side mirror':0 ,'Bumper':0,'Wheel':0, 'Filters':0 ,'Hoses':0 ,'Coolent oil':0 ,'Brake oil':0 ,
        'Wiper blades':0,'Turbo charges':0,'Short shifters':0 ,'High flow air filters':0 ,'Pressure plates':0 ,
        'Sway bars':0, 'Antilog braking system':0,'Electronic stability controller':0 ,'Tire monitoring':0 ,
        'Backup camera':0 ,'Traction controller':0,'Radiator':0 ,'Cooling fan':0 ,
        'Overflow tank':0 ,'Pressure cap':0 ,'Thermostat':0 }
    d3={'Connecting rod':0 ,'Spark plug':0 ,'Engine blocks':0
        ,'Fly wheel':0,'Timing belt':0,'Exhaust manifold':0,'Catalytic converter':0
        ,'Exhaust pipes':0 ,'Muffler':0 ,'Oxygen sensor':0 ,'Shock absorber':0 ,'Ball joint':0
        ,'Stabilizer':0,'Strut bar': 0,'Lateral control arm':0 ,'Brake pedal':0,'Brake booster':0
        ,'Brake lines':0 ,'Brake caliper':0 ,'Brake piston':0,'Clutch':0 ,'Gear box':0,
        'Torque coverter':0,'Transmission gasket':0 ,'Live axle':0 ,'Wind shield':0 ,'Head light':0 ,
        'Side mirror':0 ,'Bumper':0,'Wheel':0, 'Filters':0 ,'Hoses':0 ,'Coolent oil':0 ,'Brake oil':0 ,
        'Wiper blades':0,'Turbo charges':0,'Short shifters':0 ,'High flow air filters':0 ,'Pressure plates':0 ,
        'Sway bars':0, 'Antilog braking system':0,'Electronic stability controller':0 ,'Tire monitoring':0 ,
        'Backup camera':0 ,'Traction controller':0,'Radiator':0 ,'Cooling fan':0 ,
        'Overflow tank':0 ,'Pressure cap':0 ,'Thermostat':0 }
    return d1, d2, d3

menu1=("""What are you looking for!
                                                
                                                             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                            ||                                                                             ||
                                                            ||           1. ENGINE COMPONENTS                          ||
                                                            ||                                                                             ||
                                                            ||           2. EXHAUST PARTS                                   ||
                                                            ||                                                                             ||
                                                            ||           3. SUSPENSION PARTS                              ||
                                                            ||                                                                             ||
                                                            ||           4. BRAKING SYSTEM                                  ||    
                                                            ||                                                                             ||
                                                            ||           5. TRANSMISSION PARTS                          ||
                                                            ||                                                                             ||
                                                            ||           6. BODY PARTS                                          ||   """)                                             
menu2=("""                                                            ||                                                                             ||
                                                            ||           7. MAINTAINANCE PARTS                           ||
                                                            ||                                                                             ||
                                                            ||           8. PERFORMANCE PARTS                          ||
                                                            ||                                                                             ||
                                                            ||           9. SAFTY PARTS                                        ||
                                                            ||                                                                             ||
                                                            ||          10. COOLING SYSTEM                                 ||
                                                            ||                                                                             ||
                                                            ||          11. GO BACK ⟵                                         ||
                                                            ||                                                                             || 
                                                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
def customer():
    d1, d2, d3 = reset_customer_data()
    total_amount=0
    cur.execute("SELECT * FROM customers")
    data=cur.fetchall()
    i=1
    for row in data:
        i=i+1
    customer_id=i    
    a1=input("Enter your name:")
    while True:
        a3=input("Enter the phone number: ")
        if len(a3)==10 and a3.isdigit():
            break
        else:
            print("Invalid mobile number!")
            continue
    sam="INSERT INTO customers (id, name, phone_number) VALUES ({},'{}',{})".format(customer_id, a1, a3)
    cur.execute(sam)
    mycon.commit()
    while True:
        print(menu1)
        print(menu2)
        while True:
            a4=int(input("Enter the product number:-"))
            if a4 in range(1,12):
                break
            else:
                print("Invalid number!")
                continue
        if a4==11:
            break
        print("""                                            
                                                                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                                ||                                                              ||
                                                                ||           1. PASSENGER CARS                  ||
                                                                ||                                                              ||
                                                                ||           2. SUVs                                       ||
                                                                ||                                                              ||
                                                                ||           3. TRUCKS                                  ||
                                                                ||                                                              ||
                                                                ||           4. MOTOR CYCLES                      ||
                                                                ||                                                              ||   
                                                                ||           5. COMMERCIAL VEHICLE           ||
                                                                ||                                                              ||
                                                                ||           6. GO BACK ⟵                           ||
                                                                ||                                                              ||
                                                                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                                 
    """)

        while True:
            a5=int(input("Enter the number of your car type:-"))
            if a5 in range(1,7):
                break
            else:
                print("Invalid number!")
                continue
        if a5==6:
            continue
        if a5==1:
            t="Passenger Car"
            pr=2
        elif a5==2:
            t="SUV's"
            pr=4
        elif a5==3:
            t="Trucks"
            pr=5
        elif a5==4:
            t="MotorCycles"
            pr=1
        elif a5==5:
            t="Commercial Vehicle"
            pr=3
        
        for i in range(1,100):
            
            if a4==1:
                a9=l1[1]
                a8=l2[1]
                ti=a8*pr
                print("""                                            
                1. Connecting rod           -  ₹"""+str(l2[1]*pr)+"""              
                                                                            
                2. Spark plug                 -  ₹"""+str(l2[2]*pr)+"""             
                                                                            
                3. Engine blocks            -  ₹"""+str(l2[3]*pr)+"""            
                                                                             
                4. Fly wheel                   -  ₹"""+str(l2[4]*pr)+"""             
                                                                             
                5. Timing belt                 -  ₹"""+str(l2[5]*pr)+"""              
                                                                             
                6. GO BACK ⟵                                    """)
                a6=int(input("Enter product number:-"))
                if a6==6:
                    break
                a9=l1[a6]
                a8=l2[a6]
                ti=a8*pr
                print("Unit cost",ti)

                if d3[a9]!=0:
                    d3[a9+' '*i]=pr
                else:
                    d3[a9]=pr
                a7=int(input("Enter quantity:-"))
                if d3[a9]==pr:
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7
                elif d3[a9]!=pr:
                    d1[a9+' '*i]=a8*a7*pr
                    d2[a9+' '*i]=a7
                else:    
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7
                
                sam="INSERT INTO order_items(id,product_name,vehicle_type,quantity,price)VALUES (%s,%s,%s,%s,%s)"
                cur.execute(sam,(customer_id,a9,t,a7,ti*a7) )
                mycon.commit()
                
                print()
                break
            
            elif a4==2:
                print("""                                            
                1. Exhaust manifold         -  ₹"""+str(l2[6]*pr)+"""            
                                                                             
                2. Catalytic converter       -  ₹"""+str(l2[7]*pr)+"""          
                                                                              
                3. Exhaust pipes              -  ₹"""+str(l2[8]*pr)+"""            
                                                                              
                4. Muffler                         -  ₹"""+str(l2[9]*pr)+"""           
                                                                             
                5. Oxygen sensor             -  ₹"""+str(l2[10]*pr)+"""            
                                                                              
                6. GO BACK ⟵            
        """)
                a6=int(input("Enter product number:-"))
                if a6==6:
                    break
                a9=l1[a6+5]
                a8=l2[a6+5]
                ti=a8*pr
                print("Unit cost",ti)
                 
                if d3[a9]!=0:
                    d3[a9+' '*i]=pr
                else:
                    d3[a9]=pr
                a7=int(input("Enter quantity:-"))
                if d3[a9]==pr:
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7
                elif d3[a9]!=pr:
                    d1[a9+' '*i]=a8*a7*pr
                    d2[a9+' '*i]=a7
                else:    
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7

                sam="INSERT INTO order_items(id,product_name,vehicle_type,quantity,price)VALUES (%s,%s,%s,%s,%s)"
                cur.execute(sam,(customer_id,a9,t,a7,ti*a7) )
                mycon.commit() 
                    
                break
            elif a4==3:
                print("""                                            
                1. Shock absorber             -  ₹"""+str(l2[11]*pr)+"""            
                                                                               
                2. Ball joint                       -  ₹"""+str(l2[12]*pr)+"""            
                                                                               
                3. Stabilizer bar                 -  ₹"""+str(l2[13]*pr)+"""            
                                                                               
                4. Strut bar                       -  ₹"""+str(l2[14]*pr)+"""            
                                                                               
                5. Lateral control arm         -  ₹"""+str(l2[15]*pr)+"""            
                                                                              
                6. GO BACK ⟵                       """)
                a6=int(input("Enter product number:-"))
                if a6==6:
                    break
                a9=l1[a6+10]
                a8=l2[a6+10]
                ti=a8*pr
                print("Unit cost",ti)
                 
                if d3[a9]!=0:
                    d3[a9+' '*i]=pr
                else:
                    d3[a9]=pr
                a7=int(input("Enter quantity:-"))
                if d3[a9]==pr:
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7
                elif d3[a9]!=pr:
                    d1[a9+' '*i]=a8*a7*pr
                    d2[a9+' '*i]=a7
                else:    
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7

                sam="INSERT INTO order_items(id,product_name,vehicle_type,quantity,price)VALUES (%s,%s,%s,%s,%s)"
                cur.execute(sam,(customer_id,a9,t,a7,ti*a7) )
                mycon.commit()
                    
                break

            elif a4==4:
                print("""                                            
                1. Brake pedal             -  ₹"""+str(l2[16]*pr)+"""            
                                                                        
                2. Brake booster          -  ₹"""+str(l2[17]*pr)+"""          
                                                                        
                3. Brake lines              -  ₹"""+str(l2[18]*pr)+"""            
                                                                        
                4. Brake caliper           -  ₹"""+str(l2[19]*pr)+"""            
                                                                        
                5. Brake piston            -  ₹"""+str(l2[20]*pr)+"""          
                                                                        
                6. GO BACK ⟵                             
                                                                     
        """)
                a6=int(input("Enter product number:-"))
                if a6==6:
                    break
                a9=l1[a6+15]
                a8=l2[a6+15]
                ti=a8*pr
                print("Unit cost",ti)
        
                 
                if d3[a9]!=0:
                    d3[a9+' '*i]=pr
                else:
                    d3[a9]=pr
                a7=int(input("Enter quantity:-"))
                if d3[a9]==pr:
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7
                elif d3[a9]!=pr:
                    d1[a9+' '*i]=a8*a7*pr
                    d2[a9+' '*i]=a7
                else:    
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7

                sam="INSERT INTO order_items(id,product_name,vehicle_type,quantity,price)VALUES (%s,%s,%s,%s,%s)"
                cur.execute(sam,(customer_id,a9,t,a7,ti*a7) )
                mycon.commit()
                
                break

            elif a4==5:
                print("""                                            
                1. Clutch                            -  ₹"""+str(l2[21]*pr)+"""           
                                                                              
                2. Gear box                        -  ₹"""+str(l2[22]*pr)+"""         
                                                                              
                3. Torque converter             -  ₹"""+str(l2[23]*pr)+"""       
                                                                              
                4. Transmission gasket        -  ₹"""+str(l2[24]*pr)+"""         
                                                                              
                5. Live axle                         -  ₹"""+str(l2[25]*pr)+"""          
                                                                             
                6. GO BACK ⟵                         
                                                                     
        """)
                a6=int(input("Enter product number:-"))
                if a6==6:
                    break
                a9=l1[a6+20]
                a8=l2[a6+20]
                ti=a8*pr
                print("Unit cost",ti)

                 
                if d3[a9]!=0:
                    d3[a9+' '*i]=pr
                else:
                    d3[a9]=pr
                a7=int(input("Enter quantity:-"))
                if d3[a9]==pr:
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7
                elif d3[a9]!=pr:
                    d1[a9+' '*i]=a8*a7*pr
                    d2[a9+' '*i]=a7
                else:    
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7

                sam="INSERT INTO order_items(id,product_name,vehicle_type,quantity,price)VALUES (%s,%s,%s,%s,%s)"
                cur.execute(sam,(customer_id,a9,t,a7,ti*a7) )
                mycon.commit()     
                
                break

            elif a4==6:
                print("""                                            
                1. Wind shield              -  ₹"""+str(l2[26]*pr)+"""            
                                                                          
                2. Head light                -  ₹"""+str(l2[27]*pr)+"""              
                                                                          
                3. Side mirror               -  ₹"""+str(l2[28]*pr)+"""            
                                                                          
                4. Bumper                    -  ₹"""+str(l2[29]*pr)+"""            
                                                                         
                5. Wheel                      -  ₹"""+str(l2[30]*pr)+"""            
                                                                      
                6. GO BACK ⟵                                              
      
                                                                     
        """)
                a6=int(input("Enter product number:-"))
                if a6==6:
                    break
                a9=l1[a6+25]
                a8=l2[a6+25]
                ti=a8*pr
                print("Unit cost",ti)

                 
                if d3[a9]!=0:
                    d3[a9+' '*i]=pr
                else:
                    d3[a9]=pr
                a7=int(input("Enter quantity:-"))
                if d3[a9]==pr:
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7
                elif d3[a9]!=pr:
                    d1[a9+' '*i]=a8*a7*pr
                    d2[a9+' '*i]=a7
                else:    
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7

                sam="INSERT INTO order_items(id,product_name,vehicle_type,quantity,price)VALUES (%s,%s,%s,%s,%s)"
                cur.execute(sam,(customer_id,a9,t,a7,ti*a7) )
                mycon.commit()    
                
                break
            
            elif a4==7:
                print("""                                            
                1. Filters                     -  ₹"""+str(l2[31]*pr)+"""           
                                                                      
                2. Hoses                     -  ₹"""+str(l2[32]*pr)+"""         
                                                                       
                3. Coolant oil               -  ₹"""+str(l2[33]*pr)+"""           
                                                                       
                4. Brake oil                  -  ₹"""+str(l2[34]*pr)+"""           
                                                                       
                5. Wiper blades            -  ₹"""+str(l2[35]*pr)+"""           
                                                                       
                6. GO BACK ⟵                     
                                                                     
        """)
                a6=int(input("Enter product number:-"))
                if a6==6:
                    break
                a9=l1[a6+30]
                a8=l2[a6+30]
                ti=a8*pr
                print("Unit cost",ti) 
        
                 
                if d3[a9]!=0:
                    d3[a9+' '*i]=pr
                else:
                    d3[a9]=pr
                a7=int(input("Enter quantity:-"))
                if d3[a9]==pr:
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7
                elif d3[a9]!=pr:
                    d1[a9+' '*i]=a8*a7*pr
                    d2[a9+' '*i]=a7
                else:    
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7
                sam="INSERT INTO order_items(id,product_name,vehicle_type,quantity,price)VALUES (%s,%s,%s,%s,%s)"
                cur.execute(sam,(customer_id,a9,t,a7,ti*a7) )
                mycon.commit()    
                
                break
            
            elif a4==8:
                print("""                                            
                1. Turbo charges            -  ₹"""+str(l2[36]*pr)+"""        
                                                                        
                2. Short shifters             -  ₹"""+str(l2[37]*pr)+"""        
                                                                        
                3. High flow air filters      -  ₹"""+str(l2[38]*pr)+"""        
                                                                        
                4. Pressure plates          -  ₹"""+str(l2[39]*pr)+"""        
                                                                        
                5. Sway bars                  -  ₹"""+str(l2[40]*pr)+"""       
                                                                        
                6. GO BACK ⟵                                            
                                                                     
        """)
                a6=int(input("Enter product number:-"))
                if a6==6:
                    break
                a9=l1[a6+35]
                a8=l2[a6+35]
                ti=a8*pr
                print("Unit cost",ti)
            
                 
                if d3[a9]!=0:
                    d3[a9+' '*i]=pr
                else:
                    d3[a9]=pr
                a7=int(input("Enter quantity:-"))
                if d3[a9]==pr:
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7
                elif d3[a9]!=pr:
                    d1[a9+' '*i]=a8*a7*pr
                    d2[a9+' '*i]=a7
                else:    
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7
                    
                sam="INSERT INTO order_items(id,product_name,vehicle_type,quantity,price)VALUES (%s,%s,%s,%s,%s)"
                cur.execute(sam,(customer_id,a9,t,a7,ti*a7) )
                mycon.commit()
                    
                break
            
            elif a4==9:
                print("""                                            
                1. Antilock braking system               -  ₹"""+str(l2[41]*pr)+"""         
                                                                                          
                2. Electronic stability controller         -  ₹"""+str(l2[42]*pr)+"""         
                                                                                          
                3. Tire monitoring                             -  ₹"""+str(l2[43]*pr)+"""        
                                                                                          
                4. Backup camera                            -  ₹"""+str(l2[44]*pr)+"""        
                                                                                          
                5. Traction controller                        -  ₹"""+str(l2[45]*pr)+"""        
                                                                                          
                6. GO BACK ⟵                                                                                                                    
        """)
                a6=int(input("Enter product number:-"))
                if a6==6:
                    break
                a9=l1[a6+40]
                a8=l2[a6+40]
                ti=a8*pr
                print("Unit cost",ti)
    
                 
                if d3[a9]!=0:
                    d3[a9+' '*i]=pr
                else:
                    d3[a9]=pr
                a7=int(input("Enter quantity:-"))
                if d3[a9]==pr:
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7
                elif d3[a9]!=pr:
                    d1[a9+' '*i]=a8*a7*pr
                    d2[a9+' '*i]=a7
                else:    
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7
                    
                sam="INSERT INTO order_items(id,product_name,vehicle_type,quantity,price)VALUES (%s,%s,%s,%s,%s)"
                cur.execute(sam,(customer_id,a9,t,a7,ti*a7) )
                mycon.commit()
            
                break
               
            elif a4==10:
                print("""                                            
                1. Radiator                -  ₹"""+str(l2[46]*pr)+"""               
                                                                        
                2. Cooling fan            -  ₹"""+str(l2[47]*pr)+"""               
                                                                         
                3. Overflow tank        -  ₹"""+str(l2[48]*pr)+"""              
                                                                         
                4. Pressure cap         -  ₹"""+str(l2[49]*pr)+"""              
                                                                          
                5. Thermostat            -  ₹"""+str(l2[50]*pr)+"""              
                                                                          
                6. GO BACK ⟵                                              

                                                                     
        """)
                a6=int(input("Enter product number:-"))
                if a6==6:
                    break
                a9=l1[a6+45]
                a8=l2[a6+45]
                ti=a8*pr
                print("Unit cost",ti) 
                 
                if d3[a9]!=0:
                    d3[a9+' '*i]=pr
                else:
                    d3[a9]=pr
                a7=int(input("Enter quantity:-"))
                if d3[a9]==pr:
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7
                elif d3[a9]!=pr:
                    d1[a9+' '*i]=a8*a7*pr
                    d2[a9+' '*i]=a7
                else:    
                    d1[a9]=d1[a9]+a8*a7*pr
                    d2[a9]=d2[a9]+a7
                sam="INSERT INTO order_items(id,product_name,vehicle_type,quantity,price)VALUES (%s,%s,%s,%s,%s)"
                cur.execute(sam,(customer_id,a9,t,a7,ti*a7) )
                mycon.commit()  
                
                break
            
            elif a4==11:
                break
            else:
                print("Invalid number")
                continue
            
            
        l4=list(d1.keys())
        l5=list(d2.values())
        l7=list(d3.values())
        l6=list(d1.values())
        a13=0
        x=len(l6)
        for i in range(0,x):
            a13=a13+int(l6[i])
       
        print("1.Want to BUY some more product")
        print("2.Proceed for payment")
        print("3.GO BACK ⟵")
        print('')
        while True:
            a11=int(input("Enter the number:-"))
            if a11==1 or a11==2 or a11==3:
                break
            else:
                print("Invalid number!")
                continue
        if a11==1:
            print('')
            continue
        elif a11==2:
            a12=0
            x=len(l6)
            for i in range(0,x):
                a12=a12+int(l6[i])
           
            if a12>0:
                s=len(l4)
                if s>0:

                    print("Here is your BILL!")
                    print("""
           Name of the CUSTOMER :- """, "'",a1,"'" ,"""

                  *****************************************************************************************************************************
                           s.no                    PRODUCT                     QUANTITY             VEHICLE TYPE                PRICE 
                  *****************************************************************************************************************************   
                        """)
                    q=0
                    for pi in range(0,s):
                        
                        if l7[pi]==2:
                            t1="Passenger Car"
                            
                        elif l7[pi]==4:
                            t1="SUV's"
                            
                        elif l7[pi]==5:
                            t1="Trucks"
                            
                        elif l7[pi]==1:
                            t1="MotorCycles"
                            
                        else:
                            t1="Commercial Vehicle"
                    
                        if l5[pi]==0:
                            continue
                        else:
                            if l5[pi]>0:
                                q=q+1
                            for w in range(0,1):
                                serial_str = str(q)
                                product_str = l4[pi]
                                quantity_str = str(l5[pi])
                                price_str = str(l6[pi])
                                
                                serial_space = ' ' * (8 - len(serial_str))
                                product_space = ' ' * (40 - len(product_str))
                                quantity_space = ' ' * (18 - len(quantity_str))
                                vehicle_space = ' ' * (28 - len(t1))
                                price_space = ' ' * (12 - len(price_str))
                                
                                print('                             '+serial_str+'               '+serial_space+product_str+product_space+quantity_str+'     '+quantity_space+t1+vehicle_space+price_str)
                                print('            '+'*'*130)
                    print('')
                    print('                                                          '+"TOTAL AMOUNT = ",a12," rupees")
                    print('')
            else:
                print("NO PRODUCTS WERE PURCHASED!")
                print("TRY AGAIN!")
                break

            print('')
            print("Select the payment mode")
            print('')
            print("1.UPI")
            print("2.BANK ACCOUNT")
            print("3.GO BACK ⟵")
            print('')
            while True:
                g=int(input("Enter the number="))
                print('')
                if g==1 or g==2 or g==3:
                    break
                else:
                    print("Invalid number!")
                    continue
            if g==3:
                continue
            if g==1:
                while True:
                    h=input("Enter your UPI ID(username@bankname)= ")
                    print('')
                            
                    if h.count('@')==1:
                        while True:
                            i=input("Enter UPI PIN(four or six digit)=")
                            print('')
                            k=len(i)
                            j=str(i)
                            if(k==4 or k==6):
                                if(j.isdigit()==True):
                                    print("""PAYMENT HAS DONE SUCCESSFULLY

                                                                    
                                                                               ****************************************
                                                                        |                                                                      |
                                                                                THANK YOU FOR PURCHASING!      
                                                                        |                                                                      |
                                                                                             COME AGAIN!                  
                                                                        |                                                                      |
                                                                              ****************************************

                """  )
                                    tri="DONE"
                                    me="UPI"
         
                        
                   
                                    cur.execute("INSERT INTO c_payments(id,total_amount,method,payment_status)VALUES ({},{},'{}','{}')"
                                                .format(customer_id,a12,me,tri) )
                                    mycon.commit() 
                                    # After payment, return to main menu
                                    return
                                
                            else:
                                print("Invalid UPI Pin")
                                print('')
                                continue
                            break
                 
                    else:
                        print("Invalid UPI ID")
                        print('')
                        continue
                    break
            elif g==2:
                while True:
                    h=int(input("Enter your MOBILE NUMBER(registered in bank) = "))
                    l=str(h)
                    print('')
                    if len(l)==10:
                        while True:
                            s8=input("Enter your NAME(registered in bank) =")
                            print('')
                                    
                            if (s8.isalpha()==True):
                                while True:
                                    r=int(input("Enter your ACCOUNT NUMBER = "))
                                    j=str(r)
                                    print('')
                                    if len(j)>10 and len(j)<16:
                                        while True:
                                            k=int(input("Enter your CARD`S CVV number = "))
                                            k1=str(k)
                                            print('')
                                            if len(k1)==3:
                                                print("""PAYMENT HAS DONE SUCCESSFULLY

                                                                            
                                                                                        ****************************************
                                                                                |                                                                      |
                                                                                        THANK YOU FOR PURCHASING!      
                                                                                |                                                                      |
                                                                                                     COME AGAIN!                  
                                                                                |                                                                      |
                                                                                        ****************************************

                        """  )
                                                tri="DONE"
                                                me="BANK ACCOUNT"
                                                cur.execute("INSERT INTO c_payments(id,total_amount,method,payment_status)VALUES ({},{},'{}','{}')"
                                                            .format(customer_id,a12,me,tri) )
                                                mycon.commit()
                                                # After payment, return to main menu
                                                return
                                            else:
                                                print("Invalid number")
                                                print("Try Again!")
                                                continue
                                        break
                                    else:
                                        print("Invalid number")
                                        print("Try Again!")
                                        continue
                                break
                            else:
                                print("Invalid number")
                                print("Try Again!")
                                continue
                        break
            else:
                print("Invalid number")
                print("Try Again!")
                continue
            continue
        elif a11==3:
            continue
        else:
            print("Invalid number")
            print("Try Again!")
            continue
        continue     
            
                            
        
def seller():
    x=[1,]
    u=['a',]
    v=['w',]

    cur.execute("""
                CREATE TABLE IF NOT EXISTS sellers (
                    id INT,
                    name VARCHAR(100),
                    phone_number VARCHAR(100)
                )
            """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS purchased_items (
                   
                    id INT,
                    product_name VARCHAR(100),
                    quantity INT,
                    price FLOAT
                )
            """)
    cur.execute("""
            CREATE TABLE IF NOT EXISTS s_payments (
                id INT,
                total_amount INT,
                method VARCHAR(20),
                payment_status VARCHAR(255)
            )
        """)

    while True:
        x=[1,]
        u=['a',]
        v=['w',]
        u1=input("Enter your name :-  ")
        while True:
            a3=input("Enter the phone number: ")
            if len(a3)==10 and a3.isdigit():
                break
            else:
                print("Invalid mobile number!")
                continue
        Totalamount=0
        cur.execute("SELECT * FROM sellers")
        data1=cur.fetchall()
        i=1
        for row in data1:
            i=i+1  
        seller_id=i
        
        jj="INSERT INTO sellers(id,name,phone_number)VALUES (%s,%s,%s)"
        cur.execute(jj,(seller_id,u1,a3) )
        mycon.commit()
        while True:
            print("""Which raw material do you want to sell:

                                                                                                             
                                                                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                                 ||                                                                 ||
                                                                 ||               1. STEEL                                    ||
                                                                 ||                                                                 ||
                                                                 ||               2. GLASS                                    ||
                                                                 ||                                                                  ||
                                                                 ||               3. PLASTIC                                 ||
                                                                 ||                                                                  ||
                                                                 ||               4. ALUMINIUM                             ||
                                                                 ||                                                                  ||
                                                                 ||               5. RUBBER                                  ||
                                                                 ||                                                                  ||
                                                                 ||               6. OILS                                        ||""")
            print("""                                                                 ||                                                                  ||
                                                                 ||               7. COPPER                                  ||
                                                                 ||                                                                  ||
                                                                 ||               8. CARBON FIBRE                       ||
                                                                 ||                                                                  ||
                                                                 ||               9. FIBER GLASS                          ||
                                                                 ||                                                                  ||
                                                                 ||              10. LEAD                                      ||
                                                                 ||                                                                  ||
                                                                 ||              11. REFRIGERANT                        ||
                                                                 ||                                                                  ||
                                                                 ||              12. FABRIC                                   ||
                                                                 ||                                                                   ||
                                                                 ||              13. GO BACK ⟵                                      ||
                                                                 ||                                                                   ||
                                                                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                   """)
            while True:
                b=int(input("Enter a product u want to sell : "))
                print('')
                if b in range(1,14):
                    break
                else:
                    print("Invalid number!")
                    continue
            if b==13:
                break
            if b==1:
                print("price=500 rupees per kg ")
                d=int(input("Enter the quantity(in kg)="))
                e=d*500
                x.append('STEEL   ')
                u.append(d)
                v.append(e)
                jj="INSERT INTO purchased_items (id,product_name,quantity,price)VALUES (%s,%s,%s,%s)"
                cur.execute(jj,(seller_id,'STEEL   ',d,e) )
                mycon.commit()
            elif b==2:
                print("price=50 rupees per kg ")
                d=int(input("Enter the quantity(in kg)="))
                e=d*50
                x.append('GLASS   ')
                u.append(d)
                v.append(e)
                jj="INSERT INTO purchased_items (id,product_name,quantity,price)VALUES (%s,%s,%s,%s)"
                cur.execute(jj,(seller_id,'GLASS   ',d,e) )
                mycon.commit()
            elif b==3:
                print("price=100 rupees per kg ")
                d=int(input("Enter the quantity(in kg)="))
                e=d*100
                x.append('PLASTIC   ')
                u.append(d)
                v.append(e)
                jj="INSERT INTO purchased_items (id,product_name,quantity,price)VALUES (%s,%s,%s,%s)"
                cur.execute(jj,(seller_id,'PLASTIC   ',d,e) )
                mycon.commit()
            elif b==4:
                print("price=600 rupees per kg ")
                d=int(input("Enter the quantity(in kg)="))
                e=d*600
                x.append('ALUMINIUM ')
                u.append(d)
                v.append(e)
                jj="INSERT INTO purchased_items (id,product_name,quantity,price)VALUES (%s,%s,%s,%s)"
                cur.execute(jj,(seller_id,'ALUMINIUM ',d,e) )
                mycon.commit()
            elif b==5:
                print("price=400 rupees per kg ")
                d=int(input("Enter the quantity(in kg)="))
                e=d*400
                x.append('RUBBER   ')
                u.append(d)
                v.append(e)
                jj="INSERT INTO purchased_items (id,product_name,quantity,price)VALUES (%s,%s,%s,%s)"
                cur.execute(jj,(seller_id,'RUBBER   ',d,e) )
                mycon.commit()
            elif b==6:
                print("price=200 rupees per kg ")
                d=int(input("Enter the quantity(in kg)="))
                e=d*200
                x.append('OILS      ')
                u.append(d)
                v.append(e)
                jj="INSERT INTO purchased_items (id,product_name,quantity,price)VALUES (%s,%s,%s,%s)"
                cur.execute(jj,(seller_id,'OILS      ',d,e) )
                mycon.commit()
            elif b==7:
                print("price=450 rupees per kg ")
                d=int(input("Enter the quantity(in kg)="))
                e=d*450
                x.append('COPPER   ')
                u.append(d)
                v.append(e)
                jj="INSERT INTO purchased_items (id,product_name,quantity,price)VALUES (%s,%s,%s,%s)"
                cur.execute(jj,(seller_id,'COPPER   ',d,e) )
                mycon.commit()
            elif b==8:
                print("price=2500 rupees per kg ")
                d=int(input("Enter the quantity(in kg)="))
                e=d*2500
                x.append('CARBON FIBRE')
                u.append(d)
                v.append(e)
                jj="INSERT INTO purchased_items (id,product_name,quantity,price)VALUES (%s,%s,%s,%s)"
                cur.execute(jj,(seller_id,'CARBON FIBRE',d,e) )
                mycon.commit()
            elif b==9:
                print("price=1800 rupees per kg ")
                d=int(input("Enter the quantity(in kg)="))
                e=d*1800
                x.append('FIBER GLASS ')
                u.append(d)
                v.append(e)
                jj="INSERT INTO purchased_items (id,product_name,quantity,price)VALUES (%s,%s,%s,%s)"
                cur.execute(jj,(seller_id,'FIBER GLASS ',d,e) )
                mycon.commit()
            elif b==10:
                print("price=300 rupees per kg ")
                d=int(input("Enter the quantity(in kg)="))
                e=d*300
                x.append('LEAD       ')
                u.append(d)
                v.append(e)
                jj="INSERT INTO purchased_items (id,product_name,quantity,price)VALUES (%s,%s,%s,%s)"
                cur.execute(jj,(seller_id,'LEAD      ',d,e) )
                mycon.commit()
            elif b==11:
                print("price=800 rupees per kg ")
                d=int(input("Enter the quantity(in kg)="))
                e=d*800
                x.append('REFRIGERANT')
                u.append(d)
                v.append(e)
                jj="INSERT INTO purchased_items (id,product_name,quantity,price)VALUES (%s,%s,%s,%s)"
                cur.execute(jj,(seller_id,'REFRIGERANT',d,e) )
                mycon.commit()
            elif b==12:
                print("price=350 rupees per kg ")
                d=int(input("Enter the quantity(in kg)="))
                e=d*350
                x.append('FABRIC       ')
                u.append(d)
                v.append(e)
                jj="INSERT INTO purchased_items (id,product_name,quantity,price)VALUES (%s,%s,%s,%s)"
                cur.execute(jj,(seller_id,'FABRIC       ',d,e) )
                mycon.commit()
            
            else:
                print("Invalid number")
                print('')
                continue
            if e>0:
                print("""
                                                                              ********************************************
                                                                            |            AMOUNT = """, e ,""" rupees              |                                                                   
                                                                              ********************************************""")
              
            else:
                print("Invalid ")
                continue
            Totalamount=Totalamount+e 
            print("1.Want to SELL some more product")
            print("2.Proceed for payment")
            print("3.GO BACK ⟵")
            print('')
            while True:
                f=int(input("Enter the number="))
                if f==1 or f==2 or f==3:
                    break
                else:
                    print("Invalid number!")
                    continue
            if f==1:
                print('')
                continue
            elif f==2:
                    
                print("""
                                                                             ********************************************************************************
                                                                             
                                                                         |                        TOTAL AMOUNT = """,Totalamount,"""                                                |

                                                                             ********************************************************************************
          """)
                print('')
                print("Here is your BILL!")
                print("""
           Name of the SELLER :- ""","'" ,u1,"'","""

                                              *******************************************************************************************************
                                                  s.no                        PRODUCT                               QUANTITY                    PRICE
                                              *******************************************************************************************************     
                              """) 
                for pi in range (1,len(x)):
                    serial_str = str(pi)
                    product_str = x[pi]
                    quantity_str = str(u[pi])
                    price_str = str(v[pi])
                    
                    serial_space = ' ' * (12 - len(serial_str))
                    product_space = ' ' * (38 - len(product_str))
                    quantity_space = ' ' * (28 - len(quantity_str))
                    price_space = ' ' * (18 - len(price_str))
                    
                    print('                                                       '+serial_str+serial_space+'                 '+product_str+product_space+quantity_str+quantity_space+price_str)
                    print('                                                '+'*'*100)
                print('')
                print('                                                          '+"TOTAL AMOUNT = ",Totalamount)
                print('')
                print("Select the payment mode")
                print('')
                print("1.UPI")
                print("2.BANK ACCOUNT")
                print("3.GO BACK ⟵")
                print('')
                while True:
                    g=int(input("Enter the mode of transaction="))
                    print('')
                    if g==3:
                        break
                    if g==1:
                        while True:
                            h=input("Enter your UPI ID(username@bankname) = ")
                            print('')
                            if h.count('@')==1:
                                print("""PAYMENT WILL BE DONE TO THIS UPI ID

                                                                
                                                                      ***************************************************
                                                                    |                                                                      |
                                                                                THANK YOU FOR SELLING!      
                                                                    |                                                                      |
                                                                                          COME AGAIN!                  
                                                                    |                                                                      |
                                                                      ***************************************************

                """  )
                                me="UPI"
                                tri="DONE"
                                cur.execute("INSERT INTO s_payments(id,total_amount,method,payment_status)VALUES ({},{},'{}','{}')"
                                            .format(seller_id,Totalamount,me,tri) )
                                mycon.commit()
                                # After payment, return to main menu
                                return
                               
                            else:
                                print("Invalid UPI ID")
                                print('')
                                continue
              
                   
                    elif g==2:
                        while True:
                            h=input("Enter your MOBILE NUMBER(registered in bank) = ")
                            print('')
                            if len(h)==10 and h.isdigit():
                                while True:
                                    i=input("Enter your NAME(registered in bank) =")
                                    print('')
                                    if (i.replace(' ','').isalpha()==True):
                                        while True:
                                            r=input("Enter your ACCOUNT NUMBER = ")
                                            print('')
                                            if len(r)>10 and len(r)<16 and r.isdigit():
                                                print("""PAYMENT WILL BE DONE TO THIS ACCOUNT NUMBER

                                                                                     
                                                                                           ***************************************************
                                                                                         |                                                                      |
                                                                                                    THANK YOU FOR SELLING!      
                                                                                         |                                                                      |
                                                                                                                COME AGAIN!                  
                                                                                         |                                                                      |

                                                                                           ***************************************************""")
                                                me="BANK ACCOUNT"
                                                tri="DONE"
                                                cur.execute("INSERT INTO s_payments(id,total_amount,method,payment_status)VALUES ({},{},'{}','{}')"
                                                            .format(seller_id,Totalamount,me,tri) )
                                                mycon.commit() 
                                                # After payment, return to main menu
                                                return
                                            else:
                                                print("Invalid ACCOUNT NUMBER")
                                                continue
                                        break
                                    else:
                                        print("Invalid NAME")
                                        continue
                                break
                    else:
                        print("Invalid number")
                        print("Try Again!")
                        continue
                    break
                if g==3:
                    continue
            elif f==3:
                break

            break
        break

def industrial_staff():    
    w1=[]
    w2=[]
    w3=[]
    w4=[]
    w5=[]
    w6=[]
    w7=[]
    
    c1=cur
    
    def admin_add_worker(c1, mycon):
        n=int(input("Number of entries:"))
        for i in range(n):
            while True:
                x=input("Enter ID( 4 Digits:")
                p=len(x)
                if p==4 and x.isdigit():
                    break
                else:
                    print("Invalid")
            
            s=input("Enter name of worker:")
            y=s+'@'+x
            print("Password created:",y) 
            z=input("Qualification:")
            c1.execute("Insert into workers values ('{}','{}','{}')".format(x,y,z))
            mycon.commit()
            print('')
            print("Added worker with ID",x,"successfully!")

    def admin_remove_worker(c1, mycon):
        n=int(input("Number of entries"))
        for i in range(n):
            y2=input("Enter Worker's ID:")
            c1.execute("Delete from workers where Id = '{}'".format(y2))
            mycon.commit()
            print("Deleted worker with ID",y2,"successfully")

    def admin_view_workers(c1):
        w1.clear()
        w2.clear()
        w3.clear()
        c1.execute("select * from workers")
        data=c1.fetchall()
        for i in data:
            s=list(i)
            s1=s[0]
            s2=s[1]
            s3=s[2]
            w1.append(s1)
            w2.append(s2)
            w3.append(s3)
        E=len(w1)
        if E==0:
            print("NO WORKER EXIST!")
        else:     
            print("""

                                             ******************************************************************************************
                                                 ID                            PASSWORD                      QUALIFICATION                 
                                             ******************************************************************************************     
                             """) 
        for i in range(0,E):
            id_str = w1[i]
            pass_str = w2[i]
            qual_str = w3[i]
            
            id_space = ' ' * (22 - len(id_str))
            pass_space = ' ' * (28 - len(pass_str))
            
            print('                                                 '+id_str+id_space+'      '+pass_str+pass_space+qual_str)
            print('                                        '+'*'*90)

        

    def admin_view_complaints(c1):
        w5.clear()
        w6.clear()
        c1.execute("select * from complaint")
        data=c1.fetchall()
        for i in data:
            s=list(i)
            s1=s[0]
            s2=s[1]
            w5.append(s1)
            w6.append(s2)
        E=len(w5)
        if E==0:
            print("There are no complaints")
        else:
            
            
            print("""

                                            ******************************************************************************************
                                               SNO             ID                            Complaint                   
                                            ******************************************************************************************     
                            """) 
            for i in range(0,E):
                sno_str = str(i+1)
                comp_str = w5[i]
                id_str = w6[i]
                
                sno_space = ' ' * (17 - len(sno_str))
                id_space = ' ' * (22 - len(id_str))
                
                print('                                                    '+sno_str+sno_space+id_str+id_space+'       '+comp_str)
                print('                                   '+'*'*100)


        if E==0:
            print(' ')
        else:
            print("""If you want to remove any COMPLAINT enter '1',
else enter "2".""")
            r=input("Enter choice")
            if r=='1':
                y3=int(input("Enter the complain number:"))
                z=w6[y3-1]
                c1.execute("Delete from complaint where complain = '{}'".format(z))
                mycon.commit()
               

    def admin_view_demands(c1):
        w7.clear()
        w4.clear()
        c1.execute("select * from demand")
        data=c1.fetchall()
     
        for i in data:
            s=list(i)
            s1=s[0]
            s2=s[1]
            w7.append(s1)
            w4.append(s2)
        E=len(w7)
        if E==0:
            print("")
        else:
            
            
            print("""

                                            ******************************************************************************************
                                                SNO              ID                            DEMAND                  
                                            ******************************************************************************************     
                            """) 
            for i in range(0,E):
                sno_str = str(i+1)
                dem_str = w7[i]
                id_str = w4[i]
                
                sno_space = ' ' * (17 - len(sno_str))
                id_space = ' ' * (22 - len(id_str))
                
                print('                                                       '+sno_str+sno_space+id_str+id_space+'         '+dem_str)
                print('                                   '+'*'*100)


        if E==0:
            print(' ')

        if E==0:
            print("There are no demands")
        else:
            print("""If you want to remove any DEMAND enter '1',
else enter "2".""")
            r=input("Enter choice")
            if r=='1':
                y5=int(input("Enter the demand number:"))
                z5=w4[y5-1]
                c1.execute("Delete from demand where demanded = '{}'".format(z5))
                mycon.commit()
                
    def admin_view_customerdetails(c1):
        c1.execute("select * from customers")
        data=c1.fetchall()
        cid=[] 
        cnm=[] 
        cph=[] 
        for i in data:
            d=list(i)
            d1=d[0]
            d2=d[1]
            d3=d[2]
            cid.append(d1)
            cnm.append(d2)
            cph.append(d3)
        de=len(cid)
        if de==0:
            print("There are no details")
            
        else:
        
        
            print("""

                                            ***********************************************************************
                                               ID             NAME                            PHONE                 
                                            ***********************************************************************    
                            """) 
            for i in range(0,de):
                id_str = str(cid[i])
                name_str = cnm[i]
                phone_str = str(cph[i])
                
                id_space = ' ' * (17 - len(id_str))
                name_space = ' ' * (28 - len(name_str))
                
                print('                                                '+id_str+id_space+name_str+name_space+phone_str)
                print('                                            '+'*'*70)
        while True and de!=0:
            j=int(input("Enter id  to view customer details :"))
            print('''To view order details-Press 1
To view payment details-Press 2
To view both order and payment details-Press 3
To delete customer details-Press 4
5. GO BACK ⟵''')
            n=int(input("Enter the number :"))
            if n in [1,2,3,4,5]:
                pass
            else:
                print("Invalid number!")
                continue
            if n==5:
                break

            if n==1:
                c1.execute("select * from order_items where id={}".format(j))
                data=c1.fetchall()
                oid=[] 
                opr=[] 
                ovt=[] 
                oq=[]
                oprs=[]
                for i in data:
                    s=list(i)
                    s1=s[0]
                    s2=s[1]
                    s3=s[2]
                    s4=s[3]
                    s5=s[4]
                    oid.append(s1)
                    opr.append(s2)
                    ovt.append(s3)
                    oq.append(s4)
                    oprs.append(s5)
                le=len(oid)
                if le==0:
                    print("There are no details")
                    break
                else:
                    
                
                
                    print("""

                                                    ******************************************************************************************
                                                       ID           Product name           Vehicle type               Quantity          Price                 
                                                    ******************************************************************************************     
                                    """) 
                    for i in range(0,le):
                        id_str = str(oid[i])
                        prod_str = opr[i]
                        vehicle_str = ovt[i]
                        qty_str = str(oq[i])
                        price_str = str(oprs[i])
                        
                        id_space = ' ' * (12 - len(id_str))
                        prod_space = ' ' * (22 - len(prod_str))
                        vehicle_space = ' ' * (22 - len(vehicle_str))
                        qty_space = ' ' * (17 - len(qty_str))
                        
                        print('                                                       '+id_str+id_space+prod_str+prod_space+'        '+vehicle_str+vehicle_space+'    '+qty_str+qty_space+price_str)
                        print('                                                  '+'*'*90)


                
                break
            elif n==2:
                c1.execute("select * from c_payments where id={}".format(j))
                data=c1.fetchall()
                poid=[] 
                pot=[] 
                pom=[] 
                pos=[]
        
                for i in data:
                    s=list(i)
                    s1=s[0]
                    s2=s[1]
                    s3=s[2]
                    s4=s[3]
                    poid.append(s1)
                    pot.append(s2)
                    pom.append(s3)
                    pos.append(s4)

                le=len(poid)
                if le==0:
                    print("There are no details")
                else:
                
                
                    print("""

                                                    ******************************************************************************************
                                                       ID           total amount      Method      Payment status              
                                                    ******************************************************************************************     
                                    """) 
                    for i in range(0,le):
                        id_str = str(poid[i])
                        amount_str = str(pot[i])
                        method_str = pom[i]
                        status_str = pos[i]
                        
                        id_space = ' ' * (12 - len(id_str))
                        amount_space = ' ' * (17 - len(amount_str))
                        method_space = ' ' * (17 - len(method_str))
                        
                        print('                                                   '+id_str+id_space+amount_str+amount_space+method_str+method_space+status_str)
                        print('                                                   '+'*'*80)


                break
            elif n==3:
                c1.execute("select * from order_items where id={}".format(j))
                data=c1.fetchall()
                oid=[] 
                opr=[] 
                ovt=[] 
                oq=[]
                oprs=[]
                for i in data:
                    s=list(i)
                    s1=s[0]
                    s2=s[1]
                    s3=s[2]
                    s4=s[3]
                    s5=s[4]
                    oid.append(s1)
                    opr.append(s2)
                    ovt.append(s3)
                    oq.append(s4)
                    oprs.append(s5)
                le=len(oid)
                if le==0:
                    print("There are no order details")
                else:
                    
                
                
                    print("""

                                                    ******************************************************************************************
                                                       ID           Product name           Vehicle type               Quantity          Price                 
                                                    ******************************************************************************************     
                                    """) 
                    for i in range(0,le):
                        id_str = str(oid[i])
                        prod_str = opr[i]
                        vehicle_str = ovt[i]
                        qty_str = str(oq[i])
                        price_str = str(oprs[i])
                        
                        id_space = ' ' * (12 - len(id_str))
                        prod_space = ' ' * (22 - len(prod_str))
                        vehicle_space = ' ' * (22 - len(vehicle_str))
                        qty_space = ' ' * (17 - len(qty_str))
                        
                        print('                                                       '+id_str+id_space+prod_str+prod_space+'        '+vehicle_str+vehicle_space+'    '+qty_str+qty_space+price_str)
                        print('                                                  '+'*'*90)

                c1.execute("select * from c_payments where id={}".format(j))
                data=c1.fetchall()
                poid=[] 
                pot=[] 
                pom=[] 
                pos=[]
        
                for i in data:
                    s=list(i)
                    s1=s[0]
                    s2=s[1]
                    s3=s[2]
                    s4=s[3]
                    poid.append(s1)
                    pot.append(s2)
                    pom.append(s3)
                    pos.append(s4)

                le=len(poid)
                if le==0:
                    print("There are no payment details")
                else:
                
                
                    print("""

                                                    ******************************************************************************************
                                                       ID           total amount      Method      Payment status              
                                                    ******************************************************************************************     
                                    """) 
                    for i in range(0,le):
                        id_str = str(poid[i])
                        amount_str = str(pot[i])
                        method_str = pom[i]
                        status_str = pos[i]
                        
                        id_space = ' ' * (12 - len(id_str))
                        amount_space = ' ' * (17 - len(amount_str))
                        method_space = ' ' * (17 - len(method_str))
                        
                        print('                                                     '+id_str+id_space+amount_str+amount_space+'      '+method_str+method_space+status_str)
                        print('                                                     '+'*'*80)


                break
            elif n==4:
                confirm = input("Are you sure you want to delete customer details? (yes/no): ")
                if confirm.lower() == 'yes':
                    c1.execute("DELETE FROM order_items WHERE id={}".format(j))
                    c1.execute("DELETE FROM c_payments WHERE id={}".format(j))
                    c1.execute("DELETE FROM customers WHERE id={}".format(j))
                    mycon.commit()
                    print("Customer details deleted successfully!")
                else:
                    print("Deletion cancelled")
                break
            else:
                print("INVALID NUMBER!!!")
                continue


    def admin_view_sellerdetails(c1):
        
        c1.execute("select * from sellers")
        data=c1.fetchall()
        sid=[] 
        snm=[] 
        sph=[] 
        for i in data:
            s=list(i)
            s1=s[0]
            s2=s[1]
            s3=s[2]
            sid.append(s1)
            snm.append(s2)
            sph.append(s3)
        le=len(sid)
        if le==0:
            print("There are no details")
        else:
        
        
            print("""

                                            **************************************************************************
                                               ID             NAME                            PHONE                 
                                            ************************************************************************** 
                            """) 
            for i in range(0,le):
                id_str = str(sid[i])
                name_str = snm[i]
                phone_str = str(sph[i])
                
                id_space = ' ' * (17 - len(id_str))
                name_space = ' ' * (28 - len(name_str))
                
                print('                                              '+id_str+id_space+name_str+name_space+phone_str)
                print('                                             '+'*'*70)
            while True:
                 j=int(input("Enter id  to view seller details :"))
                 print('''To view order details-Press 1
To view payment details-Press 2
To view both order and payment details-Press 3
To delete seller details-Press 4
5. GO BACK ⟵''')
                 n=int(input("Enter the number :"))
                 if n in [1,2,3,4,5]:
                     pass
                 else:
                     print("Invalid number!")
                     continue
                 if n==5:
                     break

                 if n==1:
                     c1.execute("select * from purchased_items where id={}".format(j))
                     data=c1.fetchall()
                     pid=[] 
                     ppr=[] 
                     pq=[] 
                     pprs=[]
             
                     for i in data:
                         s=list(i)
                         s1=s[0]
                         s2=s[1]
                         s3=s[2]
                         s4=s[3]
                         pid.append(s1)
                         ppr.append(s2)
                         pq.append(s3)
                         pprs.append(s4)

                     le=len(pid)
                     if le==0:
                         print("There are no details")
                     else:
                     
                     
                         print("""

                                                         ******************************************************************************************
                                                            ID           Product name       quantity      price                 
                                                         ******************************************************************************************     
                                         """) 
                         for i in range(0,le):
                             id_str = str(pid[i])
                             prod_str = ppr[i]
                             qty_str = str(pq[i])
                             price_str = str(pprs[i])
                             
                             id_space = ' ' * (12 - len(id_str))
                             prod_space = ' ' * (27 - len(prod_str))
                             qty_space = ' ' * (17 - len(qty_str))
                             
                             print('                                                              '+id_str+id_space+'    '+prod_str+prod_space+qty_str+qty_space+price_str)
                             print('                                                                  '+'*'*80)


                     
                     break
                 elif n==2:
                     c1.execute("select * from s_payments where id={}".format(j))
                     data=c1.fetchall()
                     pooid=[] 
                     poot=[] 
                     poom=[] 
                     poos=[]
             
                     for i in data:
                         s=list(i)
                         s1=s[0]
                         s2=s[1]
                         s3=s[2]
                         s4=s[3]
                         pooid.append(s1)
                         poot.append(s2)
                         poom.append(s3)
                         poos.append(s4)

                     le=len(pooid)
                     if le==0:
                         print("There are no details")
                     else:
                     
                     
                         print("""

                                                         ******************************************************************************************
                                                            ID           total amount      Method      Payment status              
                                                         ******************************************************************************************     
                                         """) 
                         for i in range(0,le):
                             id_str = str(pooid[i])
                             amount_str = str(poot[i])
                             method_str = poom[i]
                             status_str = poos[i]
                             
                             id_space = ' ' * (12 - len(id_str))
                             amount_space = ' ' * (17 - len(amount_str))
                             method_space = ' ' * (17 - len(method_str))
                             
                             print('                                                             '+id_str+id_space+amount_str+amount_space+method_str+method_space+status_str)
                             print('                                                               '+'*'*80)


                     break
                 elif n==3:
                     c1.execute("select * from purchased_items where id={}".format(j))
                     data=c1.fetchall()
                     pid=[] 
                     ppr=[] 
                     pq=[] 
                     pprs=[]
             
                     for i in data:
                         s=list(i)
                         s1=s[0]
                         s2=s[1]
                         s3=s[2]
                         s4=s[3]
                         pid.append(s1)
                         ppr.append(s2)
                         pq.append(s3)
                         pprs.append(s4)

                     le=len(pid)
                     if le==0:
                         print("There are no order details")
                     else:
                     
                     
                         print("""

                                                         ******************************************************************************************
                                                            ID           Prouduct name       quantity      price                 
                                                         ******************************************************************************************     
                                         """) 
                         for i in range(0,le):
                             id_str = str(pid[i])
                             prod_str = ppr[i]
                             qty_str = str(pq[i])
                             price_str = str(pprs[i])
                             
                             id_space = ' ' * (12 - len(id_str))
                             prod_space = ' ' * (27 - len(prod_str))
                             qty_space = ' ' * (17 - len(qty_str))
                             
                             print('                                                            '+id_str+id_space+prod_str+prod_space+qty_str+qty_space+price_str)
                             print('                                                           '+'*'*80)

                     c1.execute("select * from s_payments where id={}".format(j))
                     data=c1.fetchall()
                     pooid=[] 
                     poot=[] 
                     poom=[] 
                     poos=[]
             
                     for i in data:
                         s=list(i)
                         s1=s[0]
                         s2=s[1]
                         s3=s[2]
                         s4=s[3]
                         pooid.append(s1)
                         poot.append(s2)
                         poom.append(s3)
                         poos.append(s4)

                     le=len(pooid)
                     if le==0:
                         print("There are no payment details")
                     else:
                     
                     
                         print("""

                                                         ******************************************************************************************
                                                            ID           total amount      Method      Payment status              
                                                         ******************************************************************************************     
                                         """) 
                         for i in range(0,le):
                             id_str = str(pooid[i])
                             amount_str = str(poot[i])
                             method_str = poom[i]
                             status_str = poos[i]
                             
                             id_space = ' ' * (12 - len(id_str))
                             amount_space = ' ' * (17 - len(amount_str))
                             method_space = ' ' * (17 - len(method_str))
                             
                             print('                                                         '+id_str+id_space+amount_str+amount_space+method_str+method_space+status_str)
                             print('                                                            '+'*'*80)


                     break
                 elif n==4:
                     confirm = input("Are you sure you want to delete seller details? (yes/no): ")
                     if confirm.lower() == 'yes':
                         c1.execute("DELETE FROM purchased_items WHERE id={}".format(j))
                         c1.execute("DELETE FROM s_payments WHERE id={}".format(j))
                         c1.execute("DELETE FROM sellers WHERE id={}".format(j))
                         mycon.commit()
                         print("Seller details deleted successfully!")
                     else:
                         print("Deletion cancelled")
                     break
                 else:
                     print("INVALID NUMBER!!!")
                     continue



 

    def admin_menu(c1, mycon):
        while True:
            print("""
            --- Admin Menu ---
            1. Add new worker
            2. Remove existing worker
            3. View workers details
            4. View complaints
            5. View demands
            6. View Customer details
            7. View Seller details
            8. GO BACK ⟵
            """)
            choice = input("Enter choice: ")

            if choice == '1':
                admin_add_worker(c1, mycon)
            elif choice == '2':
                admin_remove_worker(c1, mycon)
            elif choice == '3':
                admin_view_workers(c1)
            elif choice == '4':
                admin_view_complaints(c1)
            elif choice == '5':
                admin_view_demands(c1)
            elif choice == '6':
                admin_view_customerdetails(c1)
            elif choice == '7':
                admin_view_sellerdetails(c1)
            elif choice == '8':
                print("Going back...")
                break
            else:
                print("Invalid choice, please try again.")

    def worker_login(c1):
        worker_id = input("Enter your ID(4-digit number): ")
        password = input("Enter your Password(name@id): ")
        c1.execute("SELECT * FROM workers WHERE Id = %s AND Password = %s", (worker_id, password))
        if c1.fetchone():
            return worker_id
          
        else:
            print("Invalid ID or Password.")
            return None

    def worker_complain(c1, mycon, worker_id):
        complaint = input("Enter your complaint: ")
     
        c1.execute("INSERT INTO complaint (complain,worker) VALUES (%s, %s)", ( complaint,worker_id))
        mycon.commit()
        print("Complaint submitted successfully.")

    def worker_demand(c1, mycon, worker_id):
        demand = input("Enter your demand: ")
        c1.execute("INSERT INTO demand (demanded, worker) VALUES (%s, %s)", ( demand,worker_id))
        mycon.commit()
        print("Demand submitted successfully.")

    def worker_menu(c1, mycon):
        worker_id = worker_login(c1)
        if not worker_id:
            return
       
        while True:
            print("""
            --- Worker Menu ---
            1. Complain
            2. Demand products
            3. GO BACK ⟵
            """)
            choice = input("Enter choice: ")

            if choice == '1':
                worker_complain(c1, mycon, worker_id)
            elif choice == '2':
                worker_demand(c1, mycon, worker_id)
            elif choice == '3':
                print("Going back...")
                break
            else:
                print("Invalid choice, please try again.")

    def main():
       
        while True:
            print("""
            --- Welcome ---
            1. Admin
            2. Worker
            3. GO BACK ⟵
            """)
            role_choice = input("Enter your position: ")

            if role_choice == '1':
             
                while True:
                    pwd = input("Enter Admin Password(name@id): ")
                    if '@' in pwd:
                        print("Welcome Admin!")
                        admin_menu(c1, mycon)
                        break
                    else:
                        print("Invalid password, try again.")
            elif role_choice == '2':
                worker_menu(c1, mycon)
            elif role_choice == '3':
                print("Going back...")
                break
            else:
                print("Invalid choice, please try again.")

        c1.close()
        mycon.close()

    if __name__ == "__main__":
        main()
               
   
while True:
    print('='*94)
    print("""

                                                                       AUTOMOTIVE  PARTS  LOGISTICS
                                                                       
     """)
                                                                       
    print('='*94)
    print("""                                            
                                                                  ~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                                 ||                                               ||
                                                                 ||           1. CUSTOMER              ||
                                                                 ||                                               ||
                                                                 ||             2. SELLER                  ||
                                                                 ||                                               ||
                                                                 ||      3. INDUSTRIAL STAFF       ||
                                                                 ||                                               ||
                                                                 ||                 4.EXIT                    ||
                                                                  ~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                                  
     """) 
    a=int(input("Enter the number:"))
    if a==1:
        customer()
        continue
    elif a==2:
        seller()
        continue
    elif a==3:
        industrial_staff()
        continue
    elif a==4:
        print("THANK YOU")
        break
    else:
        print("Invalid number")
