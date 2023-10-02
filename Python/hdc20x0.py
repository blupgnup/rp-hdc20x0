


HDC20X0_ADDRESS =                       (0x41)    # 01000001 
# Register
#2 bytes
HDC20X0_TEMPERATURE_REGISTER =          (0x00)
HDC20X0_HUMIDITY_REGISTER =             (0x02)
HDC20X0_CONFIG_REGISTER        =         (0x0E)
HDC20X0_MEAS_CONFIG_REGISTER =        (0x0F)
HDC20X0_MANUFACTURERID_REGISTER =       (0xFC)
HDC20X0_DEVICEID_REGISTER =         (0xFE)


#Configuration Register Bits

HDC20X0_RESET_RESET_BIT =              (0x80)
HDC20X0_HEATER_ENABLE =          (0x8)
HDC20X0_CONFIG_GO =       (0x1)

I2C_SLAVE=0x0703

import struct, array, time, io, fcntl

HDC20X0_fw= 0
HDC20X0_fr= 0

class Hdc20x0:

        def readManufacturerID(self):
            s = [HDC20X0_MANUFACTURERID_REGISTER] 
            HDC20X0_fw.write( bytearray( s ) )
            time.sleep(0.0625)          
            data = HDC20X0_fr.read(2) #read 2 byte config data
            buf = array.array('B', data)
            return buf[0] * 256 + buf[1]

        def readDeviceID(self):
            s = [HDC20X0_DEVICEID_REGISTER] 
            HDC20X0_fw.write( bytearray( s ) )
            time.sleep(0.0625)              
            data = HDC20X0_fr.read(2) #read 2 byte config data
            buf = array.array('B', data)
            return buf[0] * 256 + buf[1]


        def __init__(self, twi=0, addr=HDC20X0_ADDRESS ):
                global HDC20X0_fr, HDC20X0_fw
                
                HDC20X0_fr= io.open("/dev/i2c-"+str(twi), "rb", buffering=0)
                HDC20X0_fw= io.open("/dev/i2c-"+str(twi), "wb", buffering=0)

                a1 = fcntl.ioctl(HDC20X0_fr, I2C_SLAVE, HDC20X0_ADDRESS)
                a2 = fcntl.ioctl(HDC20X0_fw, I2C_SLAVE, HDC20X0_ADDRESS)
                if (a1 <0 or a2 < 0):
                    exit() #abort
                time.sleep(0.1) 
                config = HDC20X0_RESET_RESET_BIT
                s = [HDC20X0_CONFIG_REGISTER,config]
                HDC20X0_fw.write( bytearray( s ) ) 
                time.sleep(0.1)             
                if(self.readManufacturerID() != 0x4954):
                    print("ERROR CRITICAL MANUFACTURE ID NOT MATCH")
                    exit()
                if(self.readDeviceID() != 0xD007):
                    print("ERROR CRITICAL DEVICE ID NOT MATCH")
                    exit()


        # public functions

        def readTemperature(self):
                s = [HDC20X0_MEAS_CONFIG_REGISTER, HDC20X0_CONFIG_GO ]
                HDC20X0_fw.write(bytearray(s)) #GO
                s = [HDC20X0_TEMPERATURE_REGISTER] # temp
                HDC20X0_fw.write(bytearray(s))
                time.sleep(0.1)  #wait for measure to be done            
                data = HDC20X0_fr.read(2) 
                buf = array.array('B', data)
                
                # Convert the data
                temp = (buf[0]) + (buf[1]*256)
                cTemp = (temp / 65536.0) * 165.0 - 40
                return cTemp


        def readHumidity(self):
                s = [HDC20X0_MEAS_CONFIG_REGISTER, HDC20X0_CONFIG_GO ]
                HDC20X0_fw.write(bytearray(s)) #GO
                s = [HDC20X0_HUMIDITY_REGISTER] #humidity
                HDC20X0_fw.write(bytearray(s))
                time.sleep(0.1)              
                data = HDC20X0_fr.read(2) #read 2 byte humidity data
                buf = array.array('B', data)
                humidity = (buf[0]) + (buf[1]*256)
                humidity = (humidity / 65536.0) * 100.0
                return humidity
        
        def readConfigRegister(self):
                s = [HDC20X0_CONFIG_REGISTER] # temp
                HDC20X0_fw.write( bytearray( s ) )
                data = HDC20X0_fr.read(1) #read 1 byte config data
                buf = array.array('B', data)
                return buf[0]
        
        def readMeasConfigRegister(self):
                s = [HDC20X0_MEAS_CONFIG_REGISTER] # temp
                HDC20X0_fw.write( bytearray( s ) )
                data = HDC20X0_fr.read(1) #read 1 byte config data
                buf = array.array('B', data)
                return buf[0]

       
        def turnHeaterOn(self):
                config = readConfigRegister()
                # Using OR so that we only activate the Heater bit
                config = config | HDC20X0_HEATER_ENABLE
                s = [HDC20X0_CONFIG_REGISTER,config]
                HDC20X0_fw.write( bytearray( s ) ) 
                return

        def turnHeaterOff(self):
                config = readConfigRegister()
                # Using Logic so that we only deactivate the Heater bit
                config = config & ~HDC20X0_HEATER_ENABLE
                s = [HDC20X0_CONFIG_REGISTER,config]
                HDC20X0_fw.write( bytearray( s ) ) 
                return

        

        def setHumidityResolution(self,resolution):
                # ToDo: implement function
                return

        def setTemperatureResolution(self,resolution):
                # ToDo: implement function
                return


