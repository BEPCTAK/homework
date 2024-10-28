def all_variants(text):
    n = len(text)

    for i in range(1 << n):
        sub = [text[j] for j in range(n) if (i & (1 << j))]
        yield "".join(sub)


a = all_variants("abc")
for i in a:
    print(i)
