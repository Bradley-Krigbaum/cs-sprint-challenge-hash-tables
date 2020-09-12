# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    paths = {}

    for path in files:
        file_name = path.split('/')[-1]

        if file_name not in paths:
            paths[file_name] = [path]
        else:
            paths[file_name].append(path)

    result = []

    for query in queries:
        if query in paths:
            for q_path in paths[query]:
                result.append(q_path)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
