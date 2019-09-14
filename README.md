# Natera homework

## Simple Graph utility in Python
Based on https://www.python.org/doc/essays/graphs/

Input:
- JSON with graph
- 2 vertices to find the path between.
 
Output:
- Path between 2 specified vertices.
 
Usage example:
```
echo '{"A": ["B", "C"], "B": ["C", "D"], "C": ["D"]}' | ./graph_path.py -s A -e D 
["A", "B", "C", "D"]
```

## Docker 
Build:
```
docker build -t natera-homework:0.1.0 ./
```
Run:
```
echo '{"A": ["B", "C"], "B": ["C", "D"], "C": ["D"]}' | docker run -i natera-homework:0.1.0 -s A -e D
```

Compose run (with volume):
```
echo '{"A": ["B", "C"], "B": ["C", "D"], "C": ["D"]}' > graph.json
docker-compose run graph_path -s A -e D /graph.json
```


