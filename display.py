import system
import instruction_queue
import reservation_station
import adder
import cdb

def show():
	print("clock cycle: ", system.clock)

	if system.stall == 1:
		print("stall")

	# ##Instruction queue
	print("Instruction queue:", instruction_queue.instruction)

	for i in range(system.add_number):
		print("reservation_station_adder", i,  "busy", adder.busy_add[i], "dest", reservation_station.dest_add[i], "operand", reservation_station.op_res_add[i], "v1", reservation_station.v1_add[i], "v2", reservation_station.v2_add[i])

	for i in range(system.add_number):
		if adder.start_add[i] == 1 and system.clock == adder.start_clock_add[i]:
			print("Adder", i, " has started operation", adder.op_add[i], adder.add1[i], adder.add2[i], " - dest", adder.dest_add[i])

		if adder.start_clock_add[i] != 0 and system.clock == (adder.start_clock_add[i] + system.add_time):
	 		print("Adder", i, " has finished operation", adder.op_add[i], adder.add1[i], adder.add2[i], " - dest", adder.dest_add[i], "sent on CDB")

	for i in range(len(system.register)):
		print("R", i, ": ", system.register[i], sep='')
	for i in range(len(system.register)):
		print("Busy R", i, ": ", system.busy_reg[i], sep='')
	# for i in range(len(system.register)):
	# 	print("Empty R", i, ":", system.empty_reg[i], sep='')

	print()