# SDF File Analysis — FULL DUMP

**File:** `/mnt/data/sdf_00000097.bin`  
**Size:** 1386464 bytes

## Header
- Magic: `SDF0`
- Entry count (big-endian): **151**
- Directory length (big-endian raw): **909**
- Flags (hex): **0x800147b2**
- Version (hex): **0xf000a**
- Assumed directory size we used: **906 bytes** (151 × 6)

## Directory (151 × 6-byte records)
Each record is `[A:3 bytes][B:3 bytes]`. Below are raw values followed by our best candidate interpretations.

### Summary of Best Candidates (per record)
*(See the CSV for every interpretation tried.)*

| idx | A_hex | B_hex | Candidate 1 | Candidate 2 |
|-----|-------|-------|-------------|-------------|
| 0 | `a90001` | `0567f5` | — | — |
| 1 | `a07d40` | `f76a84` | — | — |
| 2 | `000100` | `16ed00` | +dir(906), LE A->off, B->size, x0x1 @ off=0x49E, size=60694, magic=unknown | +dir(raw_be=909), LE A->off, B->size, x0x1 @ off=0x4A1, size=60694, magic=unknown |
| 3 | `0004dc` | `6a1b38` | — | — |
| 4 | `7d3b7f` | `a10093` | — | — |
| 5 | `e8ef22` | `376c3e` | — | — |
| 6 | `1c2f72` | `9cbb94` | — | — |
| 7 | `72525f` | `104289` | — | — |
| 8 | `251ffb` | `20ec75` | — | — |
| 9 | `88fffa` | `5ceb84` | — | — |
| 10 | `000100` | `884e00` | +dir(906), LE A->off, B->size, x0x1 @ off=0x49E, size=20104, magic=unknown | +dir(raw_be=909), LE A->off, B->size, x0x1 @ off=0x4A1, size=20104, magic=unknown |
| 11 | `0066db` | `58e23d` | — | — |
| 12 | `75dbc6` | `e30107` | — | — |
| 13 | `09a0a3` | `7bed9d` | — | — |
| 14 | `5d3962` | `32778d` | — | — |
| 15 | `945d5c` | `9229c1` | — | — |
| 16 | `bef00e` | `6da583` | — | — |
| 17 | `e4fd44` | `4346f9` | — | — |
| 18 | `000101` | `400d00` | +dir(906), LE B->off, A->size, x0x1 @ off=0x10DE, size=65792, magic=ASCII(:) | +dir(raw_be=909), LE B->off, A->size, x0x1 @ off=0x10E1, size=65792, magic=ASCII(Nl) |
| 19 | `009aa7` | `159e58` | — | — |
| 20 | `e771af` | `db0124` | — | — |
| 21 | `cf399e` | `cc4fb4` | — | — |
| 22 | `4d6370` | `7b0a01` | — | — |
| 23 | `a7238d` | `baebec` | — | — |
| 24 | `dd8a12` | `b2ecad` | — | — |
| 25 | `aeca7c` | `dedcab` | — | — |
| 26 | `000100` | `0e8b00` | +dir(906), LE A->off, B->size, x0x1 @ off=0x49E, size=35598, magic=unknown | +dir(906), BE A->off, B->size, x0x1 @ off=0x49E, size=953088, magic=unknown |
| 27 | `00823b` | `495f44` | — | — |
| 28 | `f49568` | `290184` | — | — |
| 29 | `450a32` | `3f026b` | — | — |
| 30 | `b06f6a` | `48e678` | — | — |
| 31 | `fe5ef2` | `008349` | — | — |
| 32 | `90aad6` | `a1658b` | — | — |
| 33 | `dd6bc1` | `4b64d3` | — | — |
| 34 | `000100` | `8e7200` | +dir(906), LE A->off, B->size, x0x1 @ off=0x49E, size=29326, magic=unknown | +dir(raw_be=909), LE A->off, B->size, x0x1 @ off=0x4A1, size=29326, magic=unknown |
| 35 | `0067be` | `131aae` | +dir(906), BE A->off, B->size, x0x1 @ off=0x6B5C, size=1252014, magic=ASCII(6) | +dir(raw_be=909), BE A->off, B->size, x0x1 @ off=0x6B5F, size=1252014, magic=unknown |
| 36 | `770114` | `76018d` | — | — |
| 37 | `ab4771` | `9976f7` | — | — |
| 38 | `1c5cc4` | `1f095e` | — | — |
| 39 | `d629ff` | `2615d3` | — | — |
| 40 | `d81b52` | `e65cde` | — | — |
| 41 | `1a9621` | `8a5f90` | — | — |
| 42 | `000100` | `b9d700` | +dir(906), LE A->off, B->size, x0x1 @ off=0x49E, size=55225, magic=unknown | +dir(raw_be=909), LE A->off, B->size, x0x1 @ off=0x4A1, size=55225, magic=unknown |
| 43 | `0003cb` | `0fdcb1` | +dir(906), BE A->off, B->size, x0x1 @ off=0x769, size=1039537, magic=ASCII(Z) | +dir(raw_be=909), BE A->off, B->size, x0x1 @ off=0x76C, size=1039537, magic=ASCII(Za) |
| 44 | `5b42cc` | `0b02d8` | — | — |
| 45 | `44538b` | `40a27a` | — | — |
| 46 | `286894` | `df1e55` | — | — |
| 47 | `5627e8` | `01093d` | — | — |
| 48 | `bade09` | `f53125` | — | — |
| 49 | `81c7c9` | `6da8c4` | — | — |
| 50 | `000100` | `e6e800` | +dir(906), LE A->off, B->size, x0x1 @ off=0x49E, size=59622, magic=unknown | +dir(raw_be=909), LE A->off, B->size, x0x1 @ off=0x4A1, size=59622, magic=unknown |
| 51 | `0081ed` | `8f6406` | — | — |
| 52 | `1c061c` | `2a0329` | — | — |
| 53 | `8b41eb` | `bc7a2b` | — | — |
| 54 | `f84790` | `4bf00a` | — | — |
| 55 | `93547c` | `3e6925` | — | — |
| 56 | `50de09` | `da383e` | — | — |
| 57 | `c7b070` | `b1ad26` | — | — |
| 58 | `000101` | `184500` | +dir(906), LE B->off, A->size, x0x1 @ off=0x48B6, size=65792, magic=unknown | +dir(raw_be=909), LE B->off, A->size, x0x1 @ off=0x48B9, size=65792, magic=unknown |
| 59 | `00888f` | `a902f7` | — | — |
| 60 | `b9b8e8` | `fd033d` | — | — |
| 61 | `424b01` | `38859a` | — | — |
| 62 | `94583b` | `5a2b73` | — | — |
| 63 | `5bfe6d` | `d17409` | — | — |
| 64 | `f068d4` | `50105a` | — | — |
| 65 | `359cdf` | `63e3fd` | — | — |
| 66 | `000101` | `1b7500` | +dir(906), LE B->off, A->size, x0x1 @ off=0x78B9, size=65792, magic=unknown | +dir(raw_be=909), LE B->off, A->size, x0x1 @ off=0x78BC, size=65792, magic=unknown |
| 67 | `009c01` | `d20885` | — | — |
| 68 | `980174` | `1803a2` | — | — |
| 69 | `4ce4e7` | `a028c5` | — | — |
| 70 | `8509a5` | `8e2190` | — | — |
| 71 | `e2b192` | `91c776` | — | — |
| 72 | `855598` | `e70e70` | — | — |
| 73 | `c8a313` | `5c16b2` | — | — |
| 74 | `000100` | `2a1d00` | +dir(906), LE A->off, B->size, x0x1 @ off=0x49E, size=7466, magic=unknown | +dir(raw_be=909), LE A->off, B->size, x0x1 @ off=0x4A1, size=7466, magic=unknown |
| 75 | `006736` | `0354bb` | +dir(906), BE A->off, B->size, x0x1 @ off=0x6AD4, size=218299, magic=unknown | +dir(raw_be=909), BE A->off, B->size, x0x1 @ off=0x6AD7, size=218299, magic=ASCII(g`zn) |
| 76 | `b50ff7` | `760409` | — | — |
| 77 | `a03f08` | `7b523a` | — | — |
| 78 | `86f8c5` | `5f9574` | — | — |
| 79 | `ec1783` | `db62d9` | — | — |
| 80 | `42da95` | `4b0c81` | — | — |
| 81 | `96684b` | `0abecf` | — | — |
| 82 | `000100` | `0bae00` | +dir(906), LE A->off, B->size, x0x1 @ off=0x49E, size=44555, magic=unknown | +dir(906), BE A->off, B->size, x0x1 @ off=0x49E, size=765440, magic=unknown |
| 83 | `00817f` | `aecc4c` | — | — |
| 84 | `3ca806` | `d10428` | — | — |
| 85 | `5574e0` | `a92f71` | — | — |
| 86 | `96d734` | `3a41bc` | — | — |
| 87 | `31fc12` | `9d3266` | — | — |
| 88 | `4bfca1` | `65b01c` | — | — |
| 89 | `7b3991` | `64a8d0` | — | — |
| 90 | `000100` | `e81100` | +dir(906), LE A->off, B->size, x0x1 @ off=0x49E, size=4584, magic=unknown | +dir(raw_be=909), LE A->off, B->size, x0x1 @ off=0x4A1, size=4584, magic=unknown |
| 91 | `00042a` | `5e0bfe` | — | — |
| 92 | `f4270f` | `4808bf` | — | — |
| 93 | `b8968e` | `c0a061` | — | — |
| 94 | `e0b072` | `1c28ff` | — | — |
| 95 | `bfbae7` | `ede5db` | — | — |
| 96 | `fcd537` | `1fa585` | — | — |
| 97 | `47d7c0` | `87d4c8` | — | — |
| 98 | `000100` | `2e1700` | +dir(906), LE A->off, B->size, x0x1 @ off=0x49E, size=5934, magic=unknown | +dir(raw_be=909), LE A->off, B->size, x0x1 @ off=0x4A1, size=5934, magic=unknown |
| 99 | `0004c7` | `d147cf` | — | — |
| 100 | `0db941` | `470994` | — | — |
| 101 | `f20be3` | `3c32f6` | — | — |
| 102 | `651896` | `4fe883` | — | — |
| 103 | `8512c7` | `a57c31` | — | — |
| 104 | `3ebdcb` | `6bc50f` | — | — |
| 105 | `e1dee0` | `8af52f` | — | — |
| 106 | `000101` | `344e00` | +dir(906), LE B->off, A->size, x0x1 @ off=0x51D2, size=65792, magic=ASCII(.) | +dir(raw_be=909), LE B->off, A->size, x0x1 @ off=0x51D5, size=65792, magic=unknown |
| 107 | `009bae` | `b8903a` | — | — |
| 108 | `1520e3` | `f509ca` | — | — |
| 109 | `599911` | `12deda` | — | — |
| 110 | `71cb72` | `d02010` | — | — |
| 111 | `c79745` | `405d89` | — | — |
| 112 | `6decc5` | `12549b` | — | — |
| 113 | `0b4341` | `90668b` | — | — |
| 114 | `000100` | `4eea00` | +dir(906), LE A->off, B->size, x0x1 @ off=0x49E, size=59982, magic=unknown | +dir(raw_be=909), LE A->off, B->size, x0x1 @ off=0x4A1, size=59982, magic=unknown |
| 115 | `00036e` | `57ccab` | — | — |
| 116 | `427016` | `2a0a1a` | — | — |
| 117 | `5b5e35` | `59a4bf` | — | — |
| 118 | `ae0fcf` | `f5a1c2` | — | — |
| 119 | `2b7413` | `8f06cd` | — | — |
| 120 | `a9ea4b` | `fcc0b5` | — | — |
| 121 | `6d24a8` | `ddaa16` | — | — |
| 122 | `000100` | `867000` | +dir(906), LE A->off, B->size, x0x1 @ off=0x49E, size=28806, magic=unknown | +dir(raw_be=909), LE A->off, B->size, x0x1 @ off=0x4A1, size=28806, magic=unknown |
| 123 | `0003c3` | `ac14f7` | — | — |
| 124 | `7398bd` | `4d0a25` | — | — |
| 125 | `7d35c1` | `29fad8` | — | — |
| 126 | `76abc0` | `670d51` | — | — |
| 127 | `c593d7` | `4d81f8` | — | — |
| 128 | `5cc912` | `87773c` | — | — |
| 129 | `085278` | `f2393d` | — | — |
| 130 | `000100` | `925e00` | +dir(906), LE A->off, B->size, x0x1 @ off=0x49E, size=24210, magic=unknown | +dir(raw_be=909), LE A->off, B->size, x0x1 @ off=0x4A1, size=24210, magic=unknown |
| 131 | `000392` | `3ab5d1` | — | — |
| 132 | `ee2433` | `5e0a8a` | — | — |
| 133 | `d7dd7e` | `ebb795` | — | — |
| 134 | `a7035a` | `de0f71` | — | — |
| 135 | `2a9932` | `3875f0` | — | — |
| 136 | `b7b261` | `0aadec` | — | — |
| 137 | `c19f6f` | `712856` | — | — |
| 138 | `000100` | `f33500` | +dir(906), LE A->off, B->size, x0x1 @ off=0x49E, size=13811, magic=unknown | +dir(raw_be=909), LE A->off, B->size, x0x1 @ off=0x4A1, size=13811, magic=unknown |
| 139 | `006716` | `9898da` | — | — |
| 140 | `d4909c` | `200a8b` | — | — |
| 141 | `17bdf4` | `4e2484` | — | — |
| 142 | `4ba013` | `e2d1f6` | — | — |
| 143 | `8a2d04` | `64aa1d` | — | — |
| 144 | `7cfb57` | `cc799f` | — | — |
| 145 | `f01f73` | `44e9df` | — | — |
| 146 | `000101` | `3d2e00` | +dir(906), LE B->off, A->size, x0x1 @ off=0x31DB, size=65792, magic=ASCII(mV) | +dir(raw_be=909), LE B->off, A->size, x0x1 @ off=0x31DE, size=65792, magic=ASCII(8) |
| 147 | `006626` | `bfa8d8` | — | — |
| 148 | `6ba703` | `200b8e` | — | — |
| 149 | `3b354c` | `da073d` | — | — |
| 150 | `a33125` | `680b62` | — | — |

## Hex Previews (Top Picks)
First up to 64 bytes for each chosen candidate interpretation per record.

### Record 2 — A=`000100` B=`16ed00`
**Candidate 1:** +dir(906), LE A->off, B->size, x0x1  
- abs_off: `0x49E`  
- size: `60694`  
- magic: `unknown`
```
d1 f7 00 01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3
```
**Candidate 2:** +dir(raw_be=909), LE A->off, B->size, x0x1  
- abs_off: `0x4A1`  
- size: `60694`  
- magic: `unknown`
```
01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3 58 a8 0f
```

### Record 10 — A=`000100` B=`884e00`
**Candidate 1:** +dir(906), LE A->off, B->size, x0x1  
- abs_off: `0x49E`  
- size: `20104`  
- magic: `unknown`
```
d1 f7 00 01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3
```
**Candidate 2:** +dir(raw_be=909), LE A->off, B->size, x0x1  
- abs_off: `0x4A1`  
- size: `20104`  
- magic: `unknown`
```
01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3 58 a8 0f
```

### Record 18 — A=`000101` B=`400d00`
**Candidate 1:** +dir(906), LE B->off, A->size, x0x1  
- abs_off: `0x10DE`  
- size: `65792`  
- magic: `ASCII(:)`
```
fe ea 3a d8 dd 4e 6c b5 c1 9e f6 28 84 5b dd 6e 38 8b 99 ae be a6 4d 1d fb d9 bb 11 f0 28 e7 a6 0a af 00 01 00 f4 bc 00 00 03 81 b5 bc f0 3f e2 1b d1 3a f3 41 22 77 20 30 cc dd 6c d1 c5 6f 16
```
**Candidate 2:** +dir(raw_be=909), LE B->off, A->size, x0x1  
- abs_off: `0x10E1`  
- size: `65792`  
- magic: `ASCII(Nl)`
```
d8 dd 4e 6c b5 c1 9e f6 28 84 5b dd 6e 38 8b 99 ae be a6 4d 1d fb d9 bb 11 f0 28 e7 a6 0a af 00 01 00 f4 bc 00 00 03 81 b5 bc f0 3f e2 1b d1 3a f3 41 22 77 20 30 cc dd 6c d1 c5 6f 16 eb cf 09
```

### Record 26 — A=`000100` B=`0e8b00`
**Candidate 1:** +dir(906), LE A->off, B->size, x0x1  
- abs_off: `0x49E`  
- size: `35598`  
- magic: `unknown`
```
d1 f7 00 01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3
```
**Candidate 2:** +dir(906), BE A->off, B->size, x0x1  
- abs_off: `0x49E`  
- size: `953088`  
- magic: `unknown`
```
d1 f7 00 01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3
```

### Record 34 — A=`000100` B=`8e7200`
**Candidate 1:** +dir(906), LE A->off, B->size, x0x1  
- abs_off: `0x49E`  
- size: `29326`  
- magic: `unknown`
```
d1 f7 00 01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3
```
**Candidate 2:** +dir(raw_be=909), LE A->off, B->size, x0x1  
- abs_off: `0x4A1`  
- size: `29326`  
- magic: `unknown`
```
01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3 58 a8 0f
```

### Record 35 — A=`0067be` B=`131aae`
**Candidate 1:** +dir(906), BE A->off, B->size, x0x1  
- abs_off: `0x6B5C`  
- size: `1252014`  
- magic: `ASCII(6)`
```
93 a1 9d 36 00 02 00 21 4b 00 00 9a 60 34 9a 9c 09 3b 5b 41 d0 0e 35 88 02 01 3a 33 0a 63 07 c2 4a 5a 61 a3 6a d1 02 3e f8 23 86 0c 46 f4 97 81 a9 a6 80 35 00 02 00 51 7a 00 00 9b c2 0e 33 10
```
**Candidate 2:** +dir(raw_be=909), BE A->off, B->size, x0x1  
- abs_off: `0x6B5F`  
- size: `1252014`  
- magic: `unknown`
```
36 00 02 00 21 4b 00 00 9a 60 34 9a 9c 09 3b 5b 41 d0 0e 35 88 02 01 3a 33 0a 63 07 c2 4a 5a 61 a3 6a d1 02 3e f8 23 86 0c 46 f4 97 81 a9 a6 80 35 00 02 00 51 7a 00 00 9b c2 0e 33 10 83 de 7b
```

### Record 42 — A=`000100` B=`b9d700`
**Candidate 1:** +dir(906), LE A->off, B->size, x0x1  
- abs_off: `0x49E`  
- size: `55225`  
- magic: `unknown`
```
d1 f7 00 01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3
```
**Candidate 2:** +dir(raw_be=909), LE A->off, B->size, x0x1  
- abs_off: `0x4A1`  
- size: `55225`  
- magic: `unknown`
```
01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3 58 a8 0f
```

### Record 43 — A=`0003cb` B=`0fdcb1`
**Candidate 1:** +dir(906), BE A->off, B->size, x0x1  
- abs_off: `0x769`  
- size: `1039537`  
- magic: `ASCII(Z)`
```
c7 b3 a3 5a 9d 61 e8 00 01 00 f0 34 00 00 66 8d 67 44 2e df f4 b9 9a 1a be 3f 63 e5 ff cd b3 21 52 bc 97 de 34 65 1d 2d b5 9d 8f c5 69 dd 95 7d d2 80 35 45 5c 84 f0 00 01 00 e9 63 00 00 82 22
```
**Candidate 2:** +dir(raw_be=909), BE A->off, B->size, x0x1  
- abs_off: `0x76C`  
- size: `1039537`  
- magic: `ASCII(Za)`
```
5a 9d 61 e8 00 01 00 f0 34 00 00 66 8d 67 44 2e df f4 b9 9a 1a be 3f 63 e5 ff cd b3 21 52 bc 97 de 34 65 1d 2d b5 9d 8f c5 69 dd 95 7d d2 80 35 45 5c 84 f0 00 01 00 e9 63 00 00 82 22 90 a7 bd
```

### Record 50 — A=`000100` B=`e6e800`
**Candidate 1:** +dir(906), LE A->off, B->size, x0x1  
- abs_off: `0x49E`  
- size: `59622`  
- magic: `unknown`
```
d1 f7 00 01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3
```
**Candidate 2:** +dir(raw_be=909), LE A->off, B->size, x0x1  
- abs_off: `0x4A1`  
- size: `59622`  
- magic: `unknown`
```
01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3 58 a8 0f
```

### Record 58 — A=`000101` B=`184500`
**Candidate 1:** +dir(906), LE B->off, A->size, x0x1  
- abs_off: `0x48B6`  
- size: `65792`  
- magic: `unknown`
```
00 73 14 00 ee dc 25 b2 18 f5 37 0f b2 c7 f8 5c 86 0b 03 db 2b 10 d6 49 b4 b3 b2 05 89 ed d0 ee c7 2f 8b 6f a2 fc 8b e0 52 61 00 02 01 1d b9 00 00 9c a4 ca 61 06 84 d9 09 6d 37 3d 10 09 5a 55
```
**Candidate 2:** +dir(raw_be=909), LE B->off, A->size, x0x1  
- abs_off: `0x48B9`  
- size: `65792`  
- magic: `unknown`
```
00 ee dc 25 b2 18 f5 37 0f b2 c7 f8 5c 86 0b 03 db 2b 10 d6 49 b4 b3 b2 05 89 ed d0 ee c7 2f 8b 6f a2 fc 8b e0 52 61 00 02 01 1d b9 00 00 9c a4 ca 61 06 84 d9 09 6d 37 3d 10 09 5a 55 14 5c d4
```

### Record 66 — A=`000101` B=`1b7500`
**Candidate 1:** +dir(906), LE B->off, A->size, x0x1  
- abs_off: `0x78B9`  
- size: `65792`  
- magic: `unknown`
```
06 02 cd 66 b6 1b 54 18 98 c8 18 f6 e9 4b f2 55 46 1a d6 50 7e 8e ef 6b e0 7c 96 4f a0 26 e0 88 76 3b 24 cb 8a 2a b3 00 05 00 e8 15 00 00 a8 e2 9e 0f 65 bd e4 7a 53 1b ba bc de 20 f5 d2 f3 be
```
**Candidate 2:** +dir(raw_be=909), LE B->off, A->size, x0x1  
- abs_off: `0x78BC`  
- size: `65792`  
- magic: `unknown`
```
66 b6 1b 54 18 98 c8 18 f6 e9 4b f2 55 46 1a d6 50 7e 8e ef 6b e0 7c 96 4f a0 26 e0 88 76 3b 24 cb 8a 2a b3 00 05 00 e8 15 00 00 a8 e2 9e 0f 65 bd e4 7a 53 1b ba bc de 20 f5 d2 f3 be a0 d4 01
```

### Record 74 — A=`000100` B=`2a1d00`
**Candidate 1:** +dir(906), LE A->off, B->size, x0x1  
- abs_off: `0x49E`  
- size: `7466`  
- magic: `unknown`
```
d1 f7 00 01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3
```
**Candidate 2:** +dir(raw_be=909), LE A->off, B->size, x0x1  
- abs_off: `0x4A1`  
- size: `7466`  
- magic: `unknown`
```
01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3 58 a8 0f
```

### Record 75 — A=`006736` B=`0354bb`
**Candidate 1:** +dir(906), BE A->off, B->size, x0x1  
- abs_off: `0x6AD4`  
- size: `218299`  
- magic: `unknown`
```
c6 00 00 67 60 7a 6e 39 c5 43 9c 75 ce af 02 79 25 a3 b9 5b 5d 30 40 e6 20 54 4e 37 c0 77 8b 2c c6 d2 38 22 46 ed 07 73 8e 5a 8a 54 00 02 00 e0 c0 00 00 65 e3 df 10 d2 d8 75 91 5b cf 6c 41 a7
```
**Candidate 2:** +dir(raw_be=909), BE A->off, B->size, x0x1  
- abs_off: `0x6AD7`  
- size: `218299`  
- magic: `ASCII(g`zn)`
```
67 60 7a 6e 39 c5 43 9c 75 ce af 02 79 25 a3 b9 5b 5d 30 40 e6 20 54 4e 37 c0 77 8b 2c c6 d2 38 22 46 ed 07 73 8e 5a 8a 54 00 02 00 e0 c0 00 00 65 e3 df 10 d2 d8 75 91 5b cf 6c 41 a7 c2 c3 23
```

### Record 82 — A=`000100` B=`0bae00`
**Candidate 1:** +dir(906), LE A->off, B->size, x0x1  
- abs_off: `0x49E`  
- size: `44555`  
- magic: `unknown`
```
d1 f7 00 01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3
```
**Candidate 2:** +dir(906), BE A->off, B->size, x0x1  
- abs_off: `0x49E`  
- size: `765440`  
- magic: `unknown`
```
d1 f7 00 01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3
```

### Record 90 — A=`000100` B=`e81100`
**Candidate 1:** +dir(906), LE A->off, B->size, x0x1  
- abs_off: `0x49E`  
- size: `4584`  
- magic: `unknown`
```
d1 f7 00 01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3
```
**Candidate 2:** +dir(raw_be=909), LE A->off, B->size, x0x1  
- abs_off: `0x4A1`  
- size: `4584`  
- magic: `unknown`
```
01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3 58 a8 0f
```

### Record 98 — A=`000100` B=`2e1700`
**Candidate 1:** +dir(906), LE A->off, B->size, x0x1  
- abs_off: `0x49E`  
- size: `5934`  
- magic: `unknown`
```
d1 f7 00 01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3
```
**Candidate 2:** +dir(raw_be=909), LE A->off, B->size, x0x1  
- abs_off: `0x4A1`  
- size: `5934`  
- magic: `unknown`
```
01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3 58 a8 0f
```

### Record 106 — A=`000101` B=`344e00`
**Candidate 1:** +dir(906), LE B->off, A->size, x0x1  
- abs_off: `0x51D2`  
- size: `65792`  
- magic: `ASCII(.)`
```
95 b8 2e c0 8d ab ba 94 6a f1 ab 9c 6b 78 00 02 00 2d 68 00 00 03 9a ba 85 8f 9e cd 49 5f 62 ee 52 05 43 82 0f e3 8b 11 4a 65 13 13 92 fa 40 28 39 5e 0c 40 27 57 76 a1 84 ec 90 b7 57 3d 00 02
```
**Candidate 2:** +dir(raw_be=909), LE B->off, A->size, x0x1  
- abs_off: `0x51D5`  
- size: `65792`  
- magic: `unknown`
```
c0 8d ab ba 94 6a f1 ab 9c 6b 78 00 02 00 2d 68 00 00 03 9a ba 85 8f 9e cd 49 5f 62 ee 52 05 43 82 0f e3 8b 11 4a 65 13 13 92 fa 40 28 39 5e 0c 40 27 57 76 a1 84 ec 90 b7 57 3d 00 02 01 4c 54
```

### Record 114 — A=`000100` B=`4eea00`
**Candidate 1:** +dir(906), LE A->off, B->size, x0x1  
- abs_off: `0x49E`  
- size: `59982`  
- magic: `unknown`
```
d1 f7 00 01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3
```
**Candidate 2:** +dir(raw_be=909), LE A->off, B->size, x0x1  
- abs_off: `0x4A1`  
- size: `59982`  
- magic: `unknown`
```
01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3 58 a8 0f
```

### Record 122 — A=`000100` B=`867000`
**Candidate 1:** +dir(906), LE A->off, B->size, x0x1  
- abs_off: `0x49E`  
- size: `28806`  
- magic: `unknown`
```
d1 f7 00 01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3
```
**Candidate 2:** +dir(raw_be=909), LE A->off, B->size, x0x1  
- abs_off: `0x4A1`  
- size: `28806`  
- magic: `unknown`
```
01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3 58 a8 0f
```

### Record 130 — A=`000100` B=`925e00`
**Candidate 1:** +dir(906), LE A->off, B->size, x0x1  
- abs_off: `0x49E`  
- size: `24210`  
- magic: `unknown`
```
d1 f7 00 01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3
```
**Candidate 2:** +dir(raw_be=909), LE A->off, B->size, x0x1  
- abs_off: `0x4A1`  
- size: `24210`  
- magic: `unknown`
```
01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3 58 a8 0f
```

### Record 138 — A=`000100` B=`f33500`
**Candidate 1:** +dir(906), LE A->off, B->size, x0x1  
- abs_off: `0x49E`  
- size: `13811`  
- magic: `unknown`
```
d1 f7 00 01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3
```
**Candidate 2:** +dir(raw_be=909), LE A->off, B->size, x0x1  
- abs_off: `0x4A1`  
- size: `13811`  
- magic: `unknown`
```
01 00 15 15 00 00 66 5a 68 2d 57 b9 e8 2f 1c 0f ee 8b 92 a3 5d 95 f4 a3 6e 59 a2 f5 ce c8 8b 9c 37 ca e4 8e 7b f8 14 15 bd 3f a0 1a f0 79 24 00 01 00 80 23 00 00 9a 0e 8d b1 d8 8a a3 58 a8 0f
```

### Record 146 — A=`000101` B=`3d2e00`
**Candidate 1:** +dir(906), LE B->off, A->size, x0x1  
- abs_off: `0x31DB`  
- size: `65792`  
- magic: `ASCII(mV)`
```
6d c0 56 c5 d9 d1 38 48 3b 91 f9 b0 cf c0 96 98 ed 50 b5 20 98 b8 57 e1 9b 5c a4 c1 8e c1 dc 5f 27 7f 2f c7 0a 00 01 00 31 20 00 00 68 33 d5 94 b6 64 9e dd de d1 4a 79 08 ba af 1a 7f b7 ae d7
```
**Candidate 2:** +dir(raw_be=909), LE B->off, A->size, x0x1  
- abs_off: `0x31DE`  
- size: `65792`  
- magic: `ASCII(8)`
```
c5 d9 d1 38 48 3b 91 f9 b0 cf c0 96 98 ed 50 b5 20 98 b8 57 e1 9b 5c a4 c1 8e c1 dc 5f 27 7f 2f c7 0a 00 01 00 31 20 00 00 68 33 d5 94 b6 64 9e dd de d1 4a 79 08 ba af 1a 7f b7 ae d7 30 54 bd
```


## Artifacts
- Directory dump CSV: [`sdf_directory_dump.csv`](sandbox:/mnt/data/sdf_directory_dump.csv)
- All candidate interpretations: [`sdf_all_candidates.csv`](sandbox:/mnt/data/sdf_all_candidates.csv)