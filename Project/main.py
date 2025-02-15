import time
from cinema_hall import SalaCine
from welcoming_messages import mostrar_bienvenida, mostrar_opciones
from booking_system import seleccionar_dia, preguntar_numero_personas, registrar_edades_y_calcular_precio
from show_summary import mostrar_resumen
from display_menu import mostrar_menu

# Main function
def cine():
	numero_personas = 0 # Total number of people
	edades = [] # Ages of attendees
	detalles_personas = [] # Details of each attendee
	precio_total = 0 # Total amount due

	mostrar_bienvenida()
	mostrar_opciones()

	sala = SalaCine()  # Cinema hall (Sala -> hall)
	sala.inicializar_asientos(filas=7, asientos_por_fila=6)  # Setting up the number of rows and seats

	print(" 🎥 Welcome to the ticket buying process!")
	dia_input, precio_base = seleccionar_dia()

	if not isinstance(dia_input, str):
		raise ValueError(" ❌ Error: The input must be a valid day.")

	precio_base = 10.40
	precio_descuento = precio_base * 0.8

	if dia_input == "wednesday":
		time.sleep(1)
		print(f" 🎉 You have selected {dia_input.capitalize()} with a special discount price of €{precio_descuento:.2f} euros. Save big and enjoy your movie!. 🎉")
		print("\n")
		time.sleep(1)
	else:
		time.sleep(1)
		print(f" 🎟️ You have selected {dia_input.capitalize()} with a standard ticket price of €{precio_base:.2f}. Enjoy your cinema experience! 🍿")
		print("\n")
		time.sleep(1)

	numero_personas = preguntar_numero_personas()
	time.sleep(1)

	if numero_personas is not None:
		print(f"\n Managing seats for {numero_personas} person(s)...")
		try:
			edades, precio_total, detalles_personas = registrar_edades_y_calcular_precio(numero_personas, dia_input, sala)

			total_butacas = len(sala._asientos)
			butacas_disponibles = sum(1 for asiento in sala._asientos if not asiento.reservado)
			butacas_reservadas = total_butacas - butacas_disponibles

			time.sleep(1)
			mostrar_resumen(dia_input=dia_input, edades=edades, numero_personas=numero_personas,
				detalles_personas=detalles_personas, precio_total=precio_total, 
				total_butacas=total_butacas, butacas_disponibles=butacas_disponibles, butacas_reservadas=butacas_reservadas)

			time.sleep(1)
			limite_butacas = len(sala._asientos)
			mostrar_menu(sala, dia_input, numero_personas, edades, detalles_personas, precio_total, limite_butacas)
		
		except Exception as e:
			print(f" ❌ An error occurred while managing reservations: {e}")
	else:
		print(" ❌ The number of people must be greater than 0.")

if __name__ == "__main__":
	try:
		cine()
	except KeyboardInterrupt:
		print("\nProgram interrupted. Exiting...")


