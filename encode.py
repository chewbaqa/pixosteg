from PIL import Image
import csv


def read_color_mappings(filepath):
    color_mappings = {}
    with open(filepath, newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # cus u have to skip header row
        for row in reader:
            char, color = row[0], row[1].upper()
            color_mappings[char] = color
    return color_mappings


def encode_text_to_image(text, color_mappings, image_path):
    width = len(text)
    height = 1
    image = Image.new("RGB", (width, height))
    pixels = []
    for char in text:
        color = color_mappings.get(
            char, "#000000"
        )  # black for unknown chars
        pixels.append(tuple(int(color[i : i + 2], 16) for i in (1, 3, 5)))
    image.putdata(pixels)
    image.save(image_path)


def main(text, csv_filepath, output_image_path):
    color_mappings = read_color_mappings(csv_filepath)
    encode_text_to_image(text, color_mappings, output_image_path)


if __name__ == "__main__":
    main("Hello world. ", "colors/colors.csv", "encoded_text.png")
# replace with ur own file name and csv path here