import argparse, random
from PIL import Image

def P(p):
    return True if random.random() < p else False

def main():
    # Process inputs.
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", "-i", type=str, help="File to open to process.")
    parser.add_argument("--output_file", "-o", type=str, help="Output file.")
    args = parser.parse_args()

    # Open input file as image
    image = Image.open(args.input_file)
    # image.height
    # image.width

    prob_incl = 0.30
    prob_noise = 0.0075

    # data = [ {"x":c,"y":r} for r in range(image.height) for c in range(image.width)]
    data = []
    for c in range(image.width):
        for r in range(image.height):
            px = image.getpixel((c,r))
            alpha = px[3]
            if (alpha > 150 and P(prob_incl)) or (alpha <= 150 and P(prob_noise)):
                data.append({"x":c,"y":image.height - r})

    print(len(data))
    assert(len(data) > 0)
    # Output data
    header = ["x","y"]
    lines = "\n".join([ ",".join([str(point[key]) for key in header]) for point in data ])
    with open(args.output_file, "w") as fp:
        fp.write(",".join(header) + "\n")
        fp.write(lines)


    # print(image.width)
    # print(image.height)

    # print(image)

if __name__ == "__main__":
    main()