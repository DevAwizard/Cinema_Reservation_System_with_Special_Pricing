import time

# Edades -> ages
# Numero_personas -> Number of people
# Detalles_personal --> Attendee details
# Precio total --> total price
# Total butacas --> total seats
# Butacas disponibles --> Available seats
# Butacas reservadas --> Booked seats

def mostrar_resumen(dia_input, edades, numero_personas, detalles_personas, precio_total, total_butacas, butacas_disponibles, butacas_reservadas):
	
	precio_total = sum(detalle['precio_final'] for detalle in detalles_personas)
	print("\n" + "*" * 50)  
	print("\n⌛️ Loading the reservation statu...⌛️ ")
	print("\n _________Current Summary__________")
	time.sleep(1)
	print(f" 🗓️  Selected day: {dia_input.capitalize()}")
	print(f" 👥 Total number of people: {len(detalles_personas)}")
	for detalle in detalles_personas:
		print(f" 👤 Attendee #{detalle['persona']}: Age: {detalle['edad']}, Seat: {detalle['asiento']}")
	print(f" 🛒 Total amount due: {precio_total:.2f} euros.")
	print("\n ✅ There are {} seats in total." .format(total_butacas))
	print(f" 🟢 Available seats: {butacas_disponibles}")
	print(f" 🔴 Booked seats: {butacas_reservadas}")
	print("\n" + "*" * 50)
