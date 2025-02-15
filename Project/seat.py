import time
class Asiento: # Seat
	"""
        Initializes a new seat instance.
		Parameters:
			- numero: The seat number (must be at least 1).
			- fila: The row letter (must be between A and Z).
			- limite_butacas: The maximum number of seats allowed.
			- precio_base: The base price of the seat (default is 10.40).
			- edad: The age of the person reserving the seat (optional).
	"""
	def __init__(self, numero, fila, limite_butacas, precio_base=10.40, edad=None):
		if numero < 1:
			raise ValueError(" ❌ The seat number must be at least 1.")
		if numero > limite_butacas:
			raise ValueError(f" ❌ The seat number cannot exceed {limite_butacas}. Please try again.")
		if not isinstance(fila, str) or len(fila) != 1 or not ('A' <= fila <= 'Z'):
			raise ValueError(" ❌ The row must be a letter between A and Z, starting from A.")

		# Initialize instance variables
		self._numero_asiento = numero # Seat number
		self._fila_asiento = fila # Row letter
		self._reservado = False # Reservation status 
		self._precio_base = precio_base # Standard price of the seat
		self._precio_final = precio_base # Final price of the seat
		self._edad = edad # Age of the person reserving the seat

	@property
	def numero(self):
		"""Returns the seat number."""
		return self._numero_asiento
    
	@property
	def fila(self):
		"""Returns the row letter."""
		return self._fila_asiento
    
	@property
	def reservado(self):
		"""Returns the reservation status of the seat."""
		return self._reservado
    
	@reservado.setter
	def reservado(self, estado):
		"""Sets the reservation status of the seat."""
		self._reservado = estado
    
	@property
	def precio(self):
		"""Returns the base price of the seat."""
		return self._precio_base
    
	@property
	def precio_final(self):
		"""Returns the final price of the seat."""
		return self._precio_final
	
	@precio_final.setter
	def precio_final(self, nuevo_precio):
		"""Sets a new final price for the seat.
        Raises:
            ValueError: If the new price is negative.
        """
		if nuevo_precio < 0:
			raise ValueError(" ❌ The final price cannot be a negative value.")
		self._precio_final = nuevo_precio

	@property
	def edad(self):
		"""Returns the age of the person reserving the seat."""
		return self._edad
	
	@edad.setter
	def edad(self, nueva_edad):
		"""Sets a new age for the person reserving the seat.

        Raises:
            ValueError: If age is not between 0 and 120.
        """
		if nueva_edad < 0 or nueva_edad > 120:
			raise ValueError(" ❌ The age must be between 0 and 120.")
		else:
			nueva_edad


	def calcular_precio_final(self, dia=None, edad=None):
		"""
		Calculates the final price of the seat based on the spectator's age and the selected day.

		Parameters:
		- day: The day of the week (optional).
		- edad: The age of the spectator (optional).

		Returns:
		- A tuple containing the final price and a list of discount messages.
		"""
		descuento = 0 # Discount
		mensaje_descuento = [] # Discount message

		if dia and dia.lower() == "wednesday":
			descuento += 0.2   # Apply a 20% discount
			mensaje_descuento.append("20% discount on Spectator’s Day")

		if edad is not None and edad >= 65:
			descuento += 0.3  # Apply a 30% discount
			mensaje_descuento.append("30% discount for seniors citizens(65+)")

		self.precio_final = max(self.precio * (1 - descuento), 0)

		self.precio_final = round(self.precio_final, 2)
		
		return self.precio_final, mensaje_descuento

	def __str__(self):
		"""
		Returns a string representation of the seat, including its status, number, row, and final price.

		Returns:
			- A formatted string describing the seat.
		"""
		estado = "__🔴__Booked" if self.reservado else "__🟢__Available"
		return f" Seat - number: {self.numero}, Row: {self.fila}: {estado}, Price: {self.precio_final:.2f} euros"
