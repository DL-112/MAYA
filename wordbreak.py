def segment_burmese_sentence(s, word_dict):
    word_set = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Base case: empty string can be segmented
    segments = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                segments[i].append(s[j:i])  # Store the valid segment

    if dp[n]:
        # Find the first valid segmentation
        result = []
        end = n
        while end > 0:
            for start in range(end):
                if dp[start] and s[start:end] in word_set:
                    result.append(s[start:end])
                    end = start  # Move to the next segment
                    break
        return result[::-1]  # Reverse to get the correct order

    return []  # Return empty if no segmentation is found

def read_words_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip().split('\n')

def wordbreak(input_string):
    # Read words from files
    dict_words = read_words_from_file("./dict-words.txt")
    stop_words = read_words_from_file("./stop-words.txt")
    common_words = read_words_from_file("./common-words.txt")

    # Combine all the words into a single set
    combined_words = set(dict_words) | set(stop_words) | set(common_words)

    # Preprocess input
    input_string = input_string.replace(" ", "").strip()
    # Get the first valid segmentation
    result = segment_burmese_sentence(input_string, combined_words)

    return result