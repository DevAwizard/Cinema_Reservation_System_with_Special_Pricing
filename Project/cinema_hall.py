import time
from seat import Asiento
from show_summary import mostrar_resumen

class SalaCine: # Cinema Hall
	def __init__(self):
		"""
        Initializes a new cinema hall (SalaCine) instance.

        Attributes:
        - _asientos: A list that will hold the seat (Asiento) objects in the cinema hall.
        - _limite_butacas: An integer representing the maximum number of seats in the cinema hall.
        """
		self._asientos = []
		self._limite_butacas = 0

	def inicializar_asientos(self, filas=7, asientos_por_fila=6):
		"""
		Creates all available seats in the cinema hall.

		Parameters:
		- filas: The number of rows of seats (default is 7).
		- asientos_por_fila: The number of seats per row (default is 5).
		"""
		
		for fila in range(filas): 
			fila_letra = chr(65 + fila)
			for numero in range(1, asientos_por_fila + 1): 
				nueva_butaca = Asiento(numero, fila_letra, asientos_por_fila)
				self._asientos.append(nueva_butaca)

		self._limite_butacas = len(self._asientos)
		time.sleep(1)
		print(f"\n ✅ There are {len(self._asientos)} seats in the hall.\n")
		print("=" * 82 + "\n")

	def calcular_totales(self):
		"""
		Calculates the total number of seats, available seats, and reserved seats in the cinema hall.

		Returns:
			- total_butacas: The total number of seats in the hall.
			- butacas_disponibles: The number of available (not reserved) seats.
			- butacas_reservadas: The number of reserved seats.
		"""
		total_butacas = len(self._asientos)
		butacas_disponibles = sum(1 for asiento in self._asientos if not asiento.reservado)
		butacas_reservadas = total_butacas - butacas_disponibles
		return total_butacas, butacas_disponibles, butacas_reservadas

	def agregar_asiento(self, dia_input):
		"""
		Adds a new seat if it is not already registered.

		Parameters:
		- dia_input: The day for which the seat price will be calculated.
		"""
		while True:
			try:
				numero = int(input(" Seat number: "))
				fila = input(" Row of the seat: ").upper()
				limite_butacas = len(self._asientos)
				for asiento in self._asientos:
					if asiento.numero == numero and asiento.fila == fila:
						print(" ❌ Seat is already registered.")
						continuar = input(" Do you want to try another seat? (y/n): ")
						if continuar != 'y':
							print(" ❌ Operation to add seat canceled.")
							return
						break
				else:
					nuevo_asiento = Asiento(numero, fila, limite_butacas)
					nuevo_asiento.calcular_precio_final(dia=dia_input)
					nuevo_asiento.reservado = False
					self._asientos.append(nuevo_asiento)
					self._asientos.sort(key=lambda x: (x.fila, x.numero))
					print(f" ✅ Seat {numero}-{fila} added successfully. Price: {nuevo_asiento.precio_final:.2f} euros.")
					break
			except ValueError:
				print("❌ Error: Invalid input. Please select a valid value.")

	def buscar_asiento(self, numero, fila, dia):
		"""
		Searches for a seat by its number and row.

		Parameters:
			- numero: The seat number to search for.
			- fila: The row letter of the seat to search for.
			- dia: The day for which the seat is being searched (not used in this method).

		Returns:
			- The Asiento object if found, otherwise raises an error.
		"""
		if not isinstance(numero, int) or numero < 1:
			raise ValueError(" ❌ “Invalid seat number. It must be greater than 0.")
		if not isinstance(fila, str) or len(fila) != 1 or not ('A' <= fila <= 'Z'):
			raise ValueError(" ❌ Invalid row. It must be a letter between A and Z.")
		for asiento in self._asientos:
			if asiento.numero == numero and asiento.fila == fila:
				if asiento.reservado:
					asiento.reservado = True
				return asiento
		raise ValueError(" ❌ Butaca no existe.")
	
	def reservar_asiento(self, numero, fila):
		"""
		Reserves a seat if it is available.

		Parameters:
			- numero: The seat number to reserve.
			- fila: The row letter of the seat to reserve.
		"""
		for asiento in self._asientos:
			if asiento.numero == numero and asiento.fila == fila:
				if asiento.reservado:
					raise ValueError(" ❌ The seat is already reserved.")
				asiento.reservado = True
				print(f" ✅ Seat {numero}-{fila} reserved successfully.")
				return
		raise ValueError(" ❌ Seat does not exist.")


	def reservar_asiento_adicional(self, dia_input, edades, detalles_personas, precio_total):
		"""
		Reserves one or more additional seats, requesting ages to apply discounts.

		Parameters:
		- dia_input: The day for which the seats are being reserved.
		- edades: A list to store the ages of the people reserving seats.
		- detalles_personas: A list to store details about each person.
		- precio_total: The total price of all reserved seats.

		Returns:
		- Updated edades, detalles_personas, and precio_total.
		"""

		while True:
			try:
				butacas_reservadas = sum(1 for asiento in self._asientos if asiento.reservado)
				if butacas_reservadas >= 10:
					print(" ❌ Cannot make more reservations. There are already 10 seats reserved. \n")
					return edades, detalles_personas, precio_total
				
				max_reservas_disponibles = 10 - butacas_reservadas
				numero_personas = int(input(f" How many seats do you want to reserve (Maximum {max_reservas_disponibles})?: "))
				if numero_personas <= 0 or numero_personas > max_reservas_disponibles:
					print(" ❌ The maximum number of reservations is 10. \n")
					continue
				break
			except ValueError:
				print(" ⚠️ That doesn't seem to be a valid number. Please try again. \n")
		for i in range(1, numero_personas + 1):
			while True:
				try:
					edad = int(input(f" Age of Person #{len(detalles_personas) + 1}: "))
					if edad < 0 or edad > 120:
						print(" ❌ Invalid age. Please enter an age between 0 and 120. \n")
					else:
						edades.append(edad)
						break
				except ValueError:
					print(" ⚠️ That doesn't seem to be a valid number. Please try again. \n")

			print("\n______________Available Seats_______________ \n")
			self.mostrar_asientos(dia_input)

			for i in range(1, numero_personas + 1):
				print(f" Reserving seat for Person #{i}") 

			while True:
				try:
					numero_asiento = int(input("\n Select the seat number: "))
					fila = input(" Select the row of the seat: ").upper()

					if any(detalle['asiento'] == f"{numero_asiento}-{fila}" for detalle in detalles_personas):
						print("\n ❌ This seat has already been selected for another person. Please select another. \n")  
						continue

					asiento_encontrado = False
					for asiento in self._asientos:
						if asiento.numero == numero_asiento and asiento.fila == fila:
							if asiento.reservado:
								print("\n ❌ This seat is already reserved. Please select another. \n")
								break
							asiento.calcular_precio_final(edad=edad, dia=dia_input)
							asiento.reservado = True
							detalles_personas.append({"persona": len(detalles_personas) + 1,"edad": edad,
								"asiento": f"{numero_asiento}-{fila}","precio_final": asiento.precio_final})
							precio_total += asiento.precio_final
							print(f"\n ✅ Seat {numero_asiento}-{fila} reserved successfully. Final price: {asiento.precio_final:.2f} euros.")
							asiento_encontrado = True
							break

					if not asiento_encontrado:
						print(" ❌ Seat does not exist or is not available. Please select another. \n")
						continue
					break
				except ValueError as e:
					print(f" ❌ Error: Invalid input ({e}). Please try again. \n")
				total_butacas, butacas_disponibles, butacas_reservadas = self.calcular_totales()
				mostrar_resumen(dia_input, len(detalles_personas), edades,detalles_personas, precio_total, 
					total_butacas, butacas_disponibles, butacas_reservadas)

		return edades, detalles_personas, precio_total


	def cancelar_reserva(self, numero, fila, detalles_personas, dia_input, precio_total):
		"""
		Cancels a reservation if it is reserved and makes it available for reservation again.

		Parameters:
			- numero: The seat number to cancel.
			- fila: The row letter of the seat to cancel.
			- detalles_personas: A list containing details about each reserved person.
			- dia_input: The day for which the reservation is being canceled (not used in this method).
			- precio_total: The total price of all reserved seats.

		Returns:
			- Updated precio_total after cancellation.
		"""

		asiento_encontrado = False
		
		for asiento in self._asientos:
			if asiento.numero == numero and asiento.fila == fila:
				asiento_encontrado = True 
				if not asiento.reservado:
					print(f" ❌ The seat {numero}-{fila} is not reserved. No need to cancel. \n")
					return
				asiento.reservado = False
				precio_total -= asiento.precio_final
				print(f" ✅ Reservation for seat {numero}-{fila} canceled successfully.")
				for detalle in detalles_personas:
					if detalle['asiento'] == f"{numero}-{fila}":
						detalles_personas.remove(detalle)
						break
					if not detalles_personas:
						precio_total = 0
					break
		if not asiento_encontrado:
			print(f" ❌ Seat {numero}-{fila} does not exist.")
			return
		total_butacas = len(self._asientos)
		butacas_disponibles = sum(1 for butaca in self._asientos if not butaca.reservado)
		butacas_reservadas = total_butacas - butacas_disponibles

		edades = [detalle['edad'] for detalle in detalles_personas]
		mostrar_resumen(dia_input, len(detalles_personas), edades,
						detalles_personas, precio_total,
						total_butacas, butacas_disponibles,
						butacas_reservadas)
		return precio_total

	def mostrar_asientos(self, dia):
		"""
		List all seats, indicating whether they are reserved and their price (applying discounts).
		"""
		if not self._asientos:
			print(" ❌ No seats have been registered.")
			return
		asientos_disponibles = 0
		asientos_ocupados = 0
		for asiento in self._asientos:
			estado = "__🔴__Booked" if asiento.reservado else "__🟢__Available"
			if asiento.reservado:
				precio_para_mostrar = asiento.precio_final
				asientos_ocupados += 1
			else:
				precio_para_mostrar = asiento.precio
				if dia.lower() == "wednesday":
					precio_para_mostrar *= 0.8
				asientos_disponibles += 1			
			print(f"Seat {asiento.numero}-{asiento.fila}:{estado}, Price: {precio_para_mostrar:.2f} euros")

		time.sleep(1)
		total_butacas, butacas_disponibles, butacas_reservadas = self.calcular_totales()
		print(f"\n ✅ There are {total_butacas} seats in total.")
		print(f" 🟢 Available seats: {butacas_disponibles}")
		print(f" 🔴 Reserved seats: {butacas_reservadas}\n")

	def buscar_asiento(self, numero, fila, dia):
		"""
		Search for seats by number and row.
		"""
		if not isinstance(numero, int) or numero < 1:
			raise ValueError(" ❌ Invalid seat number. It must be a number greater than 0.")
		
		if not isinstance(fila, str) or len(fila) != 1 or not ('A' <= fila <= 'Z'):
			raise ValueError(" ❌ Invalid row. It must be a letter between A and Z.")

		for asiento in self._asientos:
			if asiento.numero == numero and asiento.fila == fila:
				if asiento.reservado:
					asiento.reservado = True
				else:
					asiento.reservado = False
				return asiento
		raise ValueError(" ❌ Seat does not exist.")