"""
Script for counting how many CityObjects share a shared vertex.
It writes a CSV file with the shared vertex count for each vertex, to the same
directory as the input file.
"""
import json
import sys
from pathlib import Path
import sys
import csv

if __name__ == '__main__':
    inpath = Path(sys.argv[1]).resolve()

    with inpath.open("r") as f:
        data = json.load(f)

    vertex_counts = {i: set() for i in range(len(data['vertices']))}

    for co_id, co in data["CityObjects"].items():
        for geometry in co["geometry"]:
            for surface in geometry["boundaries"]:
                for ring in surface:
                    for vertex in ring:
                        vertex_counts[vertex].add(co_id)

    vertex_counts_sorted = dict(sorted(vertex_counts.items(), key=lambda item: len(item[1]), reverse=True))

    nr_shared = 0
    size_vertex = sys.getsizeof(data['vertices'][0])
    total_size_vertices = size_vertex * len(data['vertices'])
    total_size_vertices_unshared = 0
    with inpath.parent.joinpath(inpath.stem).with_suffix(".csv").open("w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(["Vertex", "Count"])
        for vertex, ids in vertex_counts_sorted.items():
            if len(ids) > 1:
                nr_shared += 1
                total_size_vertices_unshared += size_vertex * len(ids)
                csv_writer.writerow([vertex, len(ids)])
            else:
                total_size_vertices_unshared += size_vertex

    print(f"Nr. vertices: {len(vertex_counts)}")
    print(f"Nr. shared vertices: {nr_shared}")
    print(f"Memory size vertices: {total_size_vertices} bytes")
    print(f"Memory size vertices if none of them are shared: {total_size_vertices_unshared} bytes")
