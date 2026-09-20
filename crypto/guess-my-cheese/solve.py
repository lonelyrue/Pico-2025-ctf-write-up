from math import gcd
plain = "CHEDDAR"
cipher = "MHKLLOX"
target = "JABVOGBKNDKOUKDS"

#  (a, b)
for a in [x for x in range(1, 26) if gcd(x, 26) == 1]:
    for b in range(26):

        ok = all(
            (a * (ord(p) - ord('A')) + b) % 26 == ord(c) - ord('A')
            for p, c in zip(plain, cipher)
        )
        if ok:
            a_inv = pow(a, -1, 26)
            result = ''.join(
                chr((a_inv * (ord(ch) - ord('A') - b)) % 26 + ord('A'))
                for ch in target
            )
            print(f"a={a}, b={b} → {result}")




