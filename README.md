# picoCTF 2025 — Write-ups

**Author:** Anastasia Vasilyeva  
**Event:** picoCTF 2025

A collection of detailed write-ups for nine challenges across Web Exploitation, Forensics, Reverse Engineering, Cryptography, and Steganography. Each write-up explains the vulnerability or technique from first principles, documents the full solve path with screenshots, and discusses root causes and mitigations where applicable.

---

## Challenge Index

| # | Challenge | Category | Difficulty | Flag |
|---|-----------|----------|------------|------|
| 1 | [n0s4n1ty](web/n0s4n1ty/) | Web Exploitation | Easy | `picoCTF{wh47_c4n_u_d0_wPHP_5fd11be6}` |
| 2 | [Cookie Monster's Secret Recipe](web/cookie-monster/) | Web Exploitation | Easy | `picoCTF{c00k1e_m0nster_l0ves_c00kies_B3AD94C2}` |
| 3 | [Apriti Sesamo](web/apriti-sesamo/) | Web Exploitation | Medium | `picoCTF{s3ss4m0_0p3n_u9030ze4}` |
| 4 | [Ph4nt0m 1ntrud3r](forensics/ph4nt0m-intruder/) | Forensics | Easy | `picoCTF{1t_w4snt_th4t_34sy_tbh_4r_d1065384}` |
| 5 | [RED](forensics/red/) | Forensics / Stego | Medium | `picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}` |
| 6 | [perplexed](reverse/perplexed/) | Reverse Engineering | Medium | `picoCTF{0n3_bi7_4t_a_7im3}` |
| 7 | [Tap into Hash](reverse/tap-into-hash/) | Reverse Engineering | Medium | `picoCTF{block_3SRhViRbT1qcX_XUjM0r49cH_qCzmJZzBK_41c10331}` |
| 8 | [Guess My Cheese (Part 1)](crypto/guess-my-cheese/) | Cryptography | Easy | `picoCTF{ChEeSy7df82c21}` |
| 9 | [flags are stepic](stego/flags-are-stepic/) | Steganography | Easy | `picoCTF{fl4g_h45_f14g76ad3830}` |

---

## Techniques Covered

| Technique | Challenge(s) |
|-----------|--------------|
| Unrestricted file upload → RCE | n0s4n1ty |
| Privilege escalation via misconfigured `sudo` | n0s4n1ty |
| Sensitive data leakage in cookies (Base64) | Cookie Monster |
| Emacs backup file disclosure (`.php~`) | Apriti Sesamo |
| PHP type juggling (`sha1()` on arrays) | Apriti Sesamo |
| PCAP timing-channel analysis | Ph4nt0m 1ntrud3r |
| PNG metadata (tEXt chunk) + acrostic cipher | RED |
| LSB steganography across RGBA channels | RED |
| ELF binary reverse engineering (`objdump`) | perplexed |
| Bit-level state-machine simulation | perplexed |
| Secret key leakage via debug `print()` | Tap into Hash |
| Repeating-key XOR decryption | Tap into Hash |
| Affine cipher brute-force | Guess My Cheese |
| `stepic` LSB image steganography | flags are stepic |

---

## Repository Structure

```
.
├── web/
│   ├── n0s4n1ty/
│   ├── cookie-monster/
│   └── apriti-sesamo/
├── forensics/
│   ├── ph4nt0m-intruder/
│   └── red/
├── reverse/
│   ├── perplexed/
│   └── tap-into-hash/
├── crypto/
│   └── guess-my-cheese/
└── stego/
    └── flags-are-stepic/
```

Each challenge directory contains:
- `README.md` — full write-up with methodology, annotated screenshots, and mitigations
- `solve.py` — standalone Python solve script (where applicable)
- `assets/` — screenshots taken during the solve
