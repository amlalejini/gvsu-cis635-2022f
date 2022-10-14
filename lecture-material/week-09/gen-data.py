import random

def main():
  centroids = [
    [5, 5],
    [25, 25],
    [5, 25],
    [25, 5]
  ]
  output_fname = "points.csv"
  dist = 7
  points_per_centroid = 100
  dimensions = len(centroids[0])
  data_points = []
  for centroid in centroids:
    # dimensions = len(centroid)
    points = [ [random.uniform(c - dist, c + dist) for c in centroid] for _ in range(points_per_centroid)]
    data_points += points
    # print(data_points)

  # Shuffle the data points (so clusters aren't already together)
  random.shuffle(data_points)

  header = ",".join([f"attr{i}" for i in range(dimensions)])
  lines = [",".join(map(str, point)) for point in data_points]
  with open(output_fname, "w") as fp:
    fp.write(header + "\n")
    fp.write("\n".join(lines))


if __name__ == "__main__":
  main()