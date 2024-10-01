import sys, numpy as np  # Use numpy for int64 type

class Validator:
    def __init__(self):
        # Hardcoded attributes, with proper initialization for byte arrays
        self.pubkey = b'\x00' * 96  # 96 bytes initialized to zero
        self.withdrawal_credentials = b'\x00' * 32  # 32 bytes initialized to zero
        self.slashed = True
        # Use numpy int64 for fixed-size 64-bit integers
        self.activation_eligibility_epoch = np.int64(0)
        self.activation_epoch = np.int64(0)
        self.exit_epoch = np.int64(0)
        self.withdrawable_epoch = np.int64(0)

    # Method to calculate the memory of the instance and its attributes
    def calculate_memory(self):
        total_memory = sys.getsizeof(self)  # Memory of the instance itself
        
        # Memory of individual attributes
        total_memory += sys.getsizeof(self.pubkey)
        total_memory += sys.getsizeof(self.withdrawal_credentials)
        total_memory += sys.getsizeof(self.slashed)
        total_memory += sys.getsizeof(self.activation_eligibility_epoch)
        total_memory += sys.getsizeof(self.activation_epoch)
        total_memory += sys.getsizeof(self.exit_epoch)
        total_memory += sys.getsizeof(self.withdrawable_epoch)
        
        return total_memory

class Delegator:
    def __init__(self):
        # Hardcoded attributes, with proper initialization for byte arrays
        self.pubkey = b'\x00' * 96  # 96 bytes initialized to zero
        self.withdrawal_credentials = b'\x00' * 32  # 32 bytes initialized to zero
        # Use numpy int64 for fixed-size 64-bit integers
        self.activation_epoch = np.int64(0)
        self.exit_epoch = np.int64(0)
        self.delegated_pubkey = b'\x00' * 96  # 96 bytes initialized to zero

    # Method to calculate the memory of the instance and its attributes
    def calculate_memory(self):
        total_memory = sys.getsizeof(self)  # Memory of the instance itself
        
        # Memory of individual attributes
        total_memory += sys.getsizeof(self.pubkey)
        total_memory += sys.getsizeof(self.withdrawal_credentials)
        total_memory += sys.getsizeof(self.activation_epoch)
        total_memory += sys.getsizeof(self.exit_epoch)
        total_memory += sys.getsizeof(self.delegated_pubkey)
        
        return total_memory