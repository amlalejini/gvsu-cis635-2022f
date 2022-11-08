import argparse

def read_docword(fpath):
    with open(fpath, "r") as fp:
        lines = fp.readlines()
    words = lines[3:]
    document_words = {}
    for word in words:
        word = word.split(" ")
        doc_id = word[0]
        word_id = word[1]
        occurrences = word[2]
        if not doc_id in document_words:
            document_words[doc_id] = set()
        document_words[doc_id].add(word_id)
        # Ignore occurrences for transactions
        # if not word_id in document_words[doc_id]:
        #     document_words[doc_id][word_id] = occurrences
    return document_words

def read_vocab(fpath):
    with open(fpath, "r") as fp:
        lines = [line.strip() for line in fp.readlines()]
    return lines

def main():
    # Process inputs.
    parser = argparse.ArgumentParser()
    parser.add_argument("--docword", type=str)
    parser.add_argument("--vocab", type=str)
    parser.add_argument("--output", "-o", type=str)
    args = parser.parse_args()

    docword_fpath = args.docword
    vocab_fpath = args.vocab
    output_fpath = args.output

    docwords = read_docword(docword_fpath)
    vocab = read_vocab(vocab_fpath)
    # print(docwords[list(docwords.keys())[0]])

    # Generate word => id map
    word_to_id = {}
    id_to_word = {}
    for i in range(0, len(vocab)):
        word = vocab[i]
        id = str(i + 1) # Vocab words are 1-indexed
        word_to_id[word] = id
        id_to_word[id] = word

    # Generate transaction for each document
    transactions = []
    for doc in docwords:
        transaction = [id_to_word[word_id] for word_id in docwords[doc]]
        transactions.append(transaction)

    # Generate output file (in transaction format)
    output_content = "\n".join([",".join(transaction) for transaction in transactions])
    with open(output_fpath, "w") as fp:
        fp.write(output_content)


if __name__ == "__main__":
    main()