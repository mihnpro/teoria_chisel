def find_missing_letter(chars):
    chars = [ord(i) for i in chars]
    for i in range(len(chars)-1):
        if chars[i+1] - chars[i] == 2:
            return(chr(chars[i]+1))
            break

res = find_missing_letter(["A", "B", "C", "E"])
print(res)