karakterer = {"Jonas": 6, "Henrik": 3, "Erik": 2}
with open ("karakterer.txt", "w", encoding="utf-8") as f:
    for navn, karakterer in karakterer.items():
        f.write(f"{navn}, {karakterer}\n")

with open ("karakterer.txt", "r", encoding="utf8") as  f:
    innhold = f.read()
print(innhold.strip())