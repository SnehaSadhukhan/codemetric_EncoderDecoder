import base64

def encode_text(text):
    if not text:
        return "Error: Cannot encode empty input."
    try:
        encoded_bytes = base64.b64encode(text.encode('utf-8'))
        return encoded_bytes.decode('utf-8')
    except Exception as e:
        return f"Encoding Error: {e}"

def decode_text(text):
    if not text:
        return "Error: Cannot decode empty input."
    try:
        decoded_bytes = base64.b64decode(text.encode('utf-8'))
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        return f"Decoding Error: {e}"

def main():
    print("=== Base64 Encoder / Decoder ===")
    action = input("Would you like to encode or decode? ").strip().lower()

    if action not in ['encode', 'decode']:
        print("Invalid option. Please type 'encode' or 'decode'.")
        return

    text = input("Enter your text: ").strip()

    if action == "encode":
        result = encode_text(text)
    else:
        result = decode_text(text)

    print("\nResult:")
    print(result)

if __name__ == "__main__":
    main()
