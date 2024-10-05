infile = "input.txt"

data = []
passport = {}
for line in open(infile):
    if line == "\n":
        data.append(passport)
        passport = {}
    else:
        line = line.strip()
        lst = line.split(" ")
        for l in lst:
            tag, input = l.split(":")
            passport[tag] = input

#part 1
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid = []
for p in data:
    contains_all = True
    for f in fields:
        if f not in p:
            contains_all = False
    if contains_all:
        valid.append(p)
print(len(valid))

#part 2
valid_counter = 0
for p in valid:
    valid_info = True
    for tag in p:
        f = p[tag]
        match tag:
            case "byr":
                f = int(f)
                if len(str(f)) != 4 or f < 1920  or f > 2002:
                    valid_info = False
            case "iyr":
                f = int(f)
                if len(str(f)) != 4 or  f < 2010 or f > 2020:
                    valid_info = False
            case "eyr":
                f = int(f)
                if len(str(f)) != 4 or f < 2020 or f > 2030:
                    valid_info = False
            case "hgt":
                if "cm" in f:
                    n = int(f.replace("cm", ""))
                    if n < 150 or n > 193:
                        valid_info = False
                elif "in" in f:
                    n = int(f.replace("in", ""))
                    if n < 59 or n > 76:
                        valid_info = False
                if "cm" not in f and "in" not in f :
                    valid_info = False
            case "hcl":
                if "#" not in f:
                    valid_info = False
                else:
                    if len(f) != 7:
                        valid_info = False
            case "ecl":
                if len(f) != 3 or f not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    valid_info = False
            case "pid":
                if len(str(f)) != 9:
                    valid_info = False
    if valid_info:
        valid_counter += 1
print(valid_counter)