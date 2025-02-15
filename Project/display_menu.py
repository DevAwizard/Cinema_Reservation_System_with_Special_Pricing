import time
from cinema_hall import SalaCine
from show_summary import mostrar_resumen

# Displays the menu
def mostrar_menu(sala, dia_input, numero_personas, edades, detalles_personas, precio_total, limite_butacas):
	total_butacas = len(sala._asientos)
	butacas_disponibles = sum(1 for asiento in sala._asientos if not asiento.reservado)
	butacas_reservadas = total_butacas - butacas_disponibles
	
	while True:
		print("\n⌛️ Please wait while we load the main menu... ⌛️")
		time.sleep(1)

		print("\n" + "=" * 30)
		print("\n ____MAIN MENU____")
		print(" [1] Add seat(s) ")
		print(" [2] Reserve Seat(s) ")
		print(" [3] Cancel Seat(s) ")
		print(" [4] View Available Seats")
		print(" [5] Search for Specific Seat(s) ")
		print(" [6] Show Reservation Summary ")
		print(" [7] Exit the Menu \n")
		print("=" * 30)

		opcion = input(" 🎬 What would you like to do? Please choose an option (1-7): ")

		try:

			# Add seats
			if opcion == '1':
				print(" ⌛️ Loading option 1: Add seat(s)…... ⌛️ \n")
				time.sleep(1)
				sala.agregar_asiento(dia_input)

			# Reserve seats
			elif opcion == '2':
				print(" ⌛️ Loading option 2: Reserve seat(s)... ⌛️ \n")
				time.sleep(1)
				numero = int(input( " Seat number (e.g., 1): "))
				fila = input(" Seat row (e.g., A): ").upper()
				try:
					asiento = sala.buscar_asiento(numero, fila, dia=dia_input)
					if asiento.reservado:
						print(f" ❌ Seat {numero}-{fila} is already reserved and cannot be booked again.")
						continue
					else:
						print(f" 🟢 Seat {numero}-{fila} is available.")
						es_reserva_adicional = input(" Is this an extra seat? (y/n): ").lower()
						if es_reserva_adicional == 'y':
							edades, detalles_personas, precio_total = sala.reservar_asiento_adicional(
								dia_input, edades, detalles_personas, precio_total)
						elif es_reserva_adicional == 'n':
							print(" ⌛️ Returning to the main menu...")
							continue
						else:
							raise ValueError(" ❌ Error: Invalid input. Please select a valid value. \n")
				except ValueError as e:
					print(f" ❌ Error: {e}")

			# Cancel seats
			elif opcion == '3':
				print(" ⌛️ Loading option 3: Cancel seat(s)... ⌛️ \n")
				time.sleep(1)
				numero = int(input(" Enter the seat number to cancel (e.g., 1): "))
				fila = input(" Seat row (e.g., A): ").upper()
				sala.cancelar_reserva(numero, fila, detalles_personas, dia_input, precio_total)

			# Show seats
			elif opcion == '4':
				print(" ⌛️“Loading option 4: Show seats... ⌛️")
				time.sleep(1)
				sala.mostrar_asientos(dia_input)
				print(" ⌛️ Action completed. Returning to the main menu....")

			# Search seats
			elif opcion == '5':
				print(" ⌛️ Loading option 5: Search seats... ⌛️ \n")
				try:
					numero = int(input(" Enter the seat number to search (e.g., 1): "))
					fila = input("  Seat row (e.g., A): ").upper()
					asiento_encontrado = sala.buscar_asiento(numero, fila, dia_input)
					print(asiento_encontrado)
				except ValueError:
					print("❌ Invalid input. Please enter a valid seat number.")
					continuar = input(" Would you like to try again? (y/n) ").lower()
					if continuar != 'y':
						print(" ⌛️ Returning to the main menu...")
						continue

			# Shows summary
			elif opcion == '6':
				total_butacas = len(sala._asientos)
				butacas_disponibles = sum(1 for asiento in sala._asientos if not asiento.reservado)
				butacas_reservadas = total_butacas - butacas_disponibles
				print(" ⌛️ Loading option 6: Show summary... ⌛️ \n")
				mostrar_resumen(dia_input=dia_input, numero_personas=numero_personas, edades=edades,
					detalles_personas=detalles_personas, precio_total=precio_total, total_butacas=total_butacas,
					butacas_disponibles=butacas_disponibles, butacas_reservadas=butacas_reservadas)

			# Exiting the menu
			elif opcion == '7':
				print(" ⌛️ Exiting the reservation menu... ⌛️ \n")
				time.sleep(1)
				print("\n".join([
				" 🎬 Thank you for visiting Luminaris Cinemas!",
				"We hope you had a fantastic time and enjoyed the film.",
				"Remember, every great story deserves a sequel—see you next time! 👋"
				]))
				break
			else:
				print(" ❌ Error: Invalid input. Please select a valid value. \n")

			total_butacas = len(sala._asientos) # Total seats
			butacas_disponibles = sum(1 for asiento in sala._asientos if not asiento.reservado) # Available seats
			butacas_reservadas = total_butacas - butacas_disponibles # Booked seats
			time.sleep(1)

		except ValueError as e:
			print(f" ❌ Error: {e}")
