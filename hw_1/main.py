from rsa import rsa


def try_read_from_file(file_path):
    try:
        with open(file_path) as file:
            return file.read()
    except:
        print("File not found in destination: " + file_path)
        return None


def write_to_file_output(text: str):
    try:
        with open("output.txt", "w") as output:
            output.write(str(text))
    except FileNotFoundError:
        print("File not found.")


def digital_signature_example():
    print('Enter path to the .txt file:')
    file_path = input("> ")
    text = try_read_from_file(file_path)
    if text is None:
        print("Nothing to encrypt.")
        return
    rsa_algo = rsa.RSA_algorithm()
    Pk, pk = rsa_algo.generate_Pk_and_pk(11, 13)
    signature = rsa_algo.sign_string(text, pk)
    signature_valid = rsa_algo.verify_signature(signature, text, Pk)
    if signature_valid:
        write_to_file_output(signature)
        print("Encryption done.")
        print("Original message was: " + text)
        print()
        print('Signature validity: ' + str(signature_valid) + ".")
    else:
        print("Something went wrong.")
        print()
        print('Signature validity: ' + str(signature_valid) + ".")


if __name__ == '__main__':
    digital_signature_example()