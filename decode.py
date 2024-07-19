from PIL import Image
import csv


def read_and_invert_color_mappings(filepath):
    color_mappings = {}
    with open(filepath, newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # cus no header row
        for row in reader:
            char, color = row[0], row[1].upper()
            color_mappings[color] = char
    return color_mappings


def decode_image_to_text(image_path, inverted_color_mappings):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    decoded_text = ""
    for pixel in pixels:
        hex_color = "#{:02x}{:02x}{:02x}".format(*pixel).upper()
        decoded_text += inverted_color_mappings.get(
            hex_color, "?"
        ) # will return '?' if no mapping is found
    return decoded_text


def main(image_path, csv_filepath):
    inverted_color_mappings = read_and_invert_color_mappings(csv_filepath)
    decoded_text = decode_image_to_text(image_path, inverted_color_mappings)
    print("Decoded text:", decoded_text)


if __name__ == "__main__":
    main("encoded_text.png", "colors/colors.csv")
# replace with ur own file name and csv path here