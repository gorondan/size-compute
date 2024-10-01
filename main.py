from my_class import Validator, Delegator  # Import the class from the separate file

# Creates Validator instances
def create_Validator_instances(num_instances):
    Validator_instances = []
    for _ in range(num_instances):
        Validator_instance = Validator()  # Creates Validator instance with hardcoded attributes
        Validator_instances.append(Validator_instance)
    return Validator_instances

# Create Delegator instances
def create_Delegator_instances(num_instances):
    Delegator_instances = []
    for _ in range(num_instances):
        Delegator_instance = Delegator()  # Creates Delegator instance with hardcoded attributes
        Delegator_instances.append(Delegator_instance)
    return Delegator_instances

# Function to calculate total allocated memory for all instances
def calculate_total_memory(instances):
    total_memory = 0
    for instance in instances:
        total_memory += instance.calculate_memory()  # Use the class method
    return total_memory

# Number of instances to create
num_instances = 100

# Create instances
Validator_instances = create_Validator_instances(num_instances)
Delegator_instances = create_Delegator_instances(num_instances)

# Calculate total memory
total_Validators_memory = calculate_total_memory(Validator_instances)
total_Delegators_memory = calculate_total_memory(Delegator_instances)

total_memory = total_Validators_memory + total_Delegators_memory

print(f"Total memory allocated for {num_instances} instances: Validators memory {total_Validators_memory} bytes + Delegators memory {total_Delegators_memory} bytes, total memory : {total_memory} bytes")