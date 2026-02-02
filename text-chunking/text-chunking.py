def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    
    # computing the step size between chunk start positions
    step = chunk_size - overlap

    chunks = []

    # loop to split tokens into fixed-size chunks
    for start in range(0, len(tokens), step):
        end = start + chunk_size
        chunk = tokens[start:end]
        if not chunk:
            break
        chunks.append(chunk)

        if end >= len(tokens):
            break
    
    return chunks
