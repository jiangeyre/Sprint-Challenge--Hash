def finder(files, queries):
    # create dict for the files
    dict_files = {}
    # instantiate array of results
    result = []

    for file in files:
        path = file.split('/')[-1]
        
        if path in dict_files:
            dict_files[path].append(file)

        else:
            dict_files[path] = [file]

    for query in queries:
        if query in dict_files:
            for f in dict_files[query]:
                result.append(f)

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
