import serial

class HINDSPEM100control():
	def __init__(self, serport='/dev/ttyUSB0'):
		# all serial parameters are fixed since they are not chanagble in the controller
		# no handshake, 8N1, no nullmodem cable
		self.conn = serial.Serial(serport,baudrate=2400,timeout=2)
		if self.conn.isOpen():
			print('connection to HINDS PEM100 established')
	
	def setWavelength(self, wavelength):
		if wavelength <0 or wavelength >= 20000:
			print ('wavelength out of range')
		else:
			cmd = 'W:{:07.1f}\r'.format(wavelength) # needs zero padded 6 digits fixed
			self.conn.write(cmd[:7]+cmd[8:]) # without ythe period
			print(cmd[:7]+cmd[8:])
			cmd = 'W\r'
			self.conn.write(cmd)
			ret = self.conn.readall()
			return ret
	def setRetardation(self, retardation):
		"""
		set retardation in waveunits. 1000 is one lambda, 250 is a quarter lambda
		"""
		if retardation < 0 or retardation > 1000:                        
                        print ('retardation out of range 0 > ret > 1000')
                else:
                        cmd = 'R:{:04.0f}\r'.format(retardation) # needs zero padding
                        self.conn.write(cmd)
			cmd = 'R\r'
                        self.conn.write(cmd)
                        ret = self.conn.readall()
                        return ret

	def closeConnection(self):
		self.conn.close()
