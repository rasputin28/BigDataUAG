from cryptography.fernet import Fernet

# Generate a new Fernet key
secret_key = Fernet.generate_key()

# Print the generated key (you should save this for later use)
print("Generated Fernet Key:", secret_key)
