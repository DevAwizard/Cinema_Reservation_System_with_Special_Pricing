import time
from cinema_hall import SalaCine

def seleccionar_dia():
	"""
	Prompt the user to select a valid day of the week from the available options.
	"""
	valid_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
	precio_base = 10.40
	time.sleep(1)
	print("\n 🗓️ Choose the day you want to enjoy the movie: 🗓️ \n")

	for i, dia in enumerate(valid_days, start=1):
		print(f" {i}. {dia.capitalize()}")
	while True:
		try:
			option = int(input("\n Choose an option (1-7): "))
			if 1 <= option <= 7:
				dia_input = valid_days[option - 1]
				if  dia_input == "wednesday":
					precio_descuento = precio_base * 0.8
					print(f" 🏷️  Regular price: {precio_base:.2f} euros")
					time.sleep(1)
					print(" 🎉 Congratulations! You have chosen Spectator’s Day, enjoy a 20% discount on your ticket!")
					print(f"\n 💸 Discounted price: {precio_descuento:.2f} euros \n")
					return dia_input, precio_descuento 
				else:
					print(f" 🏷️  Regular price: {precio_base:.2f} euros \n")
					return dia_input, precio_base 
		except ValueError:
			print(" ❌ Error: Invalid input. Please select a number between 1 and 7.")

def preguntar_numero_personas():
	"""
	Asks the user how many people will attend the movie.  
	Returns a valid integer greater than 0.
    """
	while True:
		try:
			print(" 🔔 Note: The maximum number of reservations allowed for online booking is 10.")
			numero_personas = int(input(" How many people will attend the movie?: "  ))
			if numero_personas > 0 and numero_personas <= 10:
				time.sleep(1)
				print(f"\n Perfect! There will be {numero_personas} people attending. Let’s proceed with seat booking!!\n")
				return numero_personas
			elif numero_personas > 10:
				print("\n ❌ For groups larger than 10 people, online booking is not available.")
				print(" 📧 For a personalized experience, contact us at: tickets@luminaris.com \n")
				continue
			else:
				print(" ❌ The number of people must be greater than 0. Please try again. \n")
		except ValueError:
			print("❌ Error: Invalid input. Please select a valid value. \n" )


def registrar_edades_y_calcular_precio(numero_personas, dia_input, sala):
	"""
	Asks for the ages of the attendees, calculates individual prices, and the total cost.
	"""
	edades = []
	precio_total = 0
	detalles_personas = []

	time.sleep(1)
	print("\n 👥 Now we need to know each person’s age to calculate their ticket price")

	for i in range(1, numero_personas + 1):
		while True:
			try:
				edad = int(input(f" \n Enter the person’s age #{i}: "))
				if edad <= 0:
					print(" ❌ Please try again. \n")
				elif edad >= 120:
					print(" ❌The maximum age is 120 years. Please try again. \n")
				else:
					print(" ✅ Age successfully recorded. \n")
					edades.append(edad) 
					break
			except ValueError:
				print(" ❌ Error: Invalid input. Please select a valid value. \n")

		time.sleep(1)
		print("\n Available seats \n")
		sala.mostrar_asientos(dia_input)

		while True:
			try:
				numero_asiento = int(input(f" Select the seat number for the #{i} person: "))
				fila = input(" Select the seat row: ").upper()

				asiento = sala.buscar_asiento(numero_asiento, fila, dia=dia_input)
				if asiento.reservado:
					print(" ❌ The seat is already reserved. Please select another one.")
				else:
					sala.reservar_asiento(numero_asiento, fila)
					asiento.edad = edad
					asiento.calcular_precio_final(edad=edad, dia=dia_input)

					print(f" 💰 The price of seat {asiento.numero}-{asiento.fila} is: {asiento.precio_final:.2f} euros.")
		
					precio_total += asiento.precio_final 
					detalles_personas.append({"persona": len(detalles_personas) + 1,"edad": edad, 
							"asiento": f"{numero_asiento}-{fila}", "precio_final": asiento.precio_final})
					break
			except ValueError:
				print("❌ Error: Invalid input. Please select a valid value. \n")

	if len(edades) == 1:
		print("\n 🎟️ Perfect! We have recorded the person’s age.")
	else:
		print(f"\n 🎟️ Perfect! We have recorded the ages of all {len(edades)} attendees.")

	return edades, precio_total, detalles_personas