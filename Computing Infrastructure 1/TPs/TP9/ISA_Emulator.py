instruction_set = {"0001": 'MOV', "0010": 'ADD', "0011": 'SUB', "0100": 'MUL',
                   "0101": 'DIV', "0110": 'CMP', "0111": 'BRLT', "1000": 'BR'}

Main_Memory = {10: "0001000001111100",  # MOV R1, A
               11: "0001000010111101",  # MOV R2, B
               12: "0110000001000010",  # CMP R1, R2
               13: "0111000000010000",  # BRLT 16
               14: "0011000001000010",  # SUB R1, R2
               15: "1000000000001100",  # BR 12
               16: "0001111110000001",  # MOV C, R1
               28: "0000000000001011",  # variable A=11
               29: "0000000000000101",  # variable B=5
               30: "0000000000000000"}  # variable C, by default 0

Instruction_Register = []
Program_Counter_Register = [10]
FLAG_Register = ["False"]
General_Purpose_Registers = {"R0": [0],  # General register R0
                             "R1": [0],  # General register R1
                             "R2": [0]}  # General register R2

# -----------------------------------------------------------------------------------------------# 

def fetch_instruction(memory, program_counter_register, instruction_register):
    """Retrieves the instruction form the specified address in memory"""
    address = program_counter_register[0]
    instruction_register.append(memory[address])


def update_program_counter(program_counter_register, x):
    """Updates the program counter register value"""
    if x == 1:
        program_counter_register[0] += 1 # Increment for sequential execution
    else:
        program_counter_register[0] = x # Jump to specific address of branch operation


def decode_instruction(instruction_register):
    """Decodes the instruction from the instruction_register"""
    current_instruction = instruction_register.pop(0)
    opcode = current_instruction[:4]

    # Handle branch operation (1-address instructions)
    if opcode in ["0111", "1000"]: # BRLT, BR
        operand1_address = int(current_instruction[4:], 2)
        operand2_address = None
    else:
        # Handle branch operation (2-address instructions)
        operand1_address = int(current_instruction[5:10], 2)
        operand2_address = int(current_instruction[11:], 2)

    # Returns opcode and both operand addresses 
    return (instruction_set[opcode]), operand1_address, operand2_address


def execute_instruction(opcode, operand1_address, operand2_address, memory, general_purpose_registers, program_counter_register, flag_register):
    """Executes the instruction based on decoded opcode and operands"""
    print("Step-4: executing the instruction: ", opcode, operand1_address, operand2_address)
    
    if opcode == "MOV": # MOV (move) 0001
        # Identifiying if it's a register-to-memory or a memory-to-register or register-to-register operation
        # Check if operand2_address is a register or a memory address
        if isinstance(operand2_address, int):
            if f'R{operand2_address}' in general_purpose_registers:
                # It's a register-to-register or memory-to-register operation
                source = general_purpose_registers[f'R{operand2_address}'][0]
            elif operand2_address in memory:
                # It's a memory-to-register operation
                source = int(memory[operand2_address], 2)  # Convert binary string from memory to integer
            else:
                raise ValueError(f"Invalid source operand address: {operand2_address}") # for debugging purposes
        else:
            raise ValueError(f"Source operand not an integer, got {type(operand2_address)}") # for debugging purposes

        # Determine destination
        if isinstance(operand1_address, int):
            if f'R{operand1_address}' in general_purpose_registers:
                # Store in register
                general_purpose_registers[f'R{operand1_address}'][0] = source
                result = f"MOV operation performed. {source} moved to R{operand1_address}"
            elif operand1_address in memory:
                # Store in memory
                memory[operand1_address] = bin(source)[2:].zfill(16)  # Store as binary string
                result = f"MOV operation performed. {source} moved to memory address {operand1_address}"
            else:
                raise ValueError(f"Invalid destination operand address: {operand1_address}") # for debugging purposes
        else:
            raise ValueError(f"Destination operand not an integer, got {type(operand1_address)}") # for debuggin purposes
        

    elif opcode == "CMP": # CMP (compare) 0110
        # Assuming both operands are register addresses 
        value1 = general_purpose_registers[f'R{operand1_address}'][0]
        value2 = general_purpose_registers[f'R{operand2_address}'][0]

        # Compare both values
        if value1 < value2:
            flag_register[0] = "True"
            result = f"CMP operation performed. Compare R{operand1_address} with R{operand2_address}, FLAG set to {FLAG_Register}"
        else:
            flag_register[0] = "False"
            result = f"CMP operation performed. Compare R{operand1_address} with R{operand2_address}, FLAG set to {FLAG_Register}"
        

    elif opcode == "BR": # BR (branch) 1000
        # Update the program counter to the operand1_address
        update_program_counter(Program_Counter_Register, operand1_address)
        result = f"BR operation performed. Jumped to address {operand1_address}"


    elif opcode == "BRLT": # BRLT (conditional branch) 0111
        if flag_register[0] == "True":
            update_program_counter(Program_Counter_Register, operand1_address)
            result = f"BRLT operation performed. Condition met, jumped to address {operand1_address}"
            flag_register[0] = "False" # Restes the Flag register after use
        else:
            result = f"BRLT operation not performed. Condition not met."


    elif opcode == "SUB": # SUB (subtract) 0011
        # Retrieve values for subtraction based on addressing mode
        value1 = general_purpose_registers[f'R{operand1_address}'][0] if operand1_address < 16 else memory[operand1_address]
        value2 = general_purpose_registers[f'R{operand2_address}'][0] if operand2_address < 16 else memory[operand2_address]

        # Performe subtraction operation and update to correct location
        subtraction_result = value1 - value2
        general_purpose_registers[f'R{operand1_address}'][0] = subtraction_result
        result = f"SUB operation performed. Subtracted {value2} from R{operand1_address} (previously {value1}). Subtraction result {subtraction_result} is written to R{operand1_address}"


    elif opcode == "ADD": # ADD (add) 0010
        # Retrieve values for subtraction based on addressing mode
        value1 = general_purpose_registers[f'R{operand1_address}'][0] if operand1_address < 16 else memory[operand1_address]
        value2 = general_purpose_registers[f'R{operand2_address}'][0] if operand2_address < 16 else memory[operand2_address]

        # Performe subtraction operation and update to correct location
        addition_result = value1 + value2
        general_purpose_registers[f'R{operand1_address}'][0] = addition_result
        result = f"ADD operation performed. Added {value2} to R{operand1_address} (previously {value1}). Addition result {addition_result} is written to R{operand1_address}"


    elif opcode == "MUL": # MUL (multiply) 0100
        # Retrieve values for subtraction based on addressing mode
        value1 = general_purpose_registers[f'R{operand1_address}'][0] if operand1_address < 16 else memory[operand1_address]
        value2 = general_purpose_registers[f'R{operand2_address}'][0] if operand2_address < 16 else memory[operand2_address]

        # Performe subtraction operation and update to correct location
        multiplication_result = value1 * value2
        general_purpose_registers[f'R{operand1_address}'][0] = multiplication_result
        result = f"MUL operation performed. Multiplied {value2} with R{operand1_address} (previously {value1}). Multiplication result {multiplication_result} is written to R{operand1_address}"


    elif opcode == "DIV": # DIV (divide) 0101
        # Retrieve values for subtraction based on addressing mode
        value1 = general_purpose_registers[f'R{operand1_address}'][0] if operand1_address < 16 else memory[operand1_address]
        value2 = general_purpose_registers[f'R{operand2_address}'][0] if operand2_address < 16 else memory[operand2_address]

        # Performe subtraction operation and update to correct location
        division_result = value1 // value2 # Assuming integer division
        general_purpose_registers[f'R{operand1_address}'][0] = division_result
        result = f"DIV operation performed. Divided R{operand1_address} (previously {value1}) by {value2}. Division result {division_result} is written to R{operand1_address}"

    else:
        result = "Unrecognized opcode!"

    return result


i = 0
# Main loop for instruction cycle
while Program_Counter_Register[0] <= 16:
    print("\033[94mRound: " + str(i) + "\033[00m")
    i += 1
    
    # Step 1
    print("Step-1: Fetch the next instruction at memory address: ", Program_Counter_Register[0])
    if Program_Counter_Register[0] not in Main_Memory:
        print("No instruction at this address, exiting.")
        break # Exits loop if program counter points to an non-instruction address, also used for debug purposes
    fetch_instruction(Main_Memory, Program_Counter_Register, Instruction_Register)
    print("Step-1: Fetched! The instruction to be executed next is: ", Instruction_Register[0])

    # Step 2
    update_program_counter(Program_Counter_Register, 1)
    print("Step-2: The Program Counter has been updated to: ", Program_Counter_Register[0])

    # Step 3
    Opcode, Operand1_Address, Operand2_Address = decode_instruction(Instruction_Register)
    print("Step-3: Decoded! The instruction is:", Opcode, Operand1_Address, Operand2_Address)

    # Step 4
    execution_result = execute_instruction(Opcode, Operand1_Address, Operand2_Address, Main_Memory, General_Purpose_Registers, Program_Counter_Register, FLAG_Register)
    print("Step-4: Executed! The execution result is: ", execution_result)

    # Output state of Registers and Program Counter 
    print("Result-1: The Program Counter is: ", Program_Counter_Register[0])
    print("Result-2: The General Purpose Registers contains: ", General_Purpose_Registers)
    print("Result-3: The FLAG Registers contains: ", FLAG_Register[0])
    print("\n")

# Output final result
print("\033[94mThe final result after executing the instructions is: \033[00m", int(Main_Memory[30],2))