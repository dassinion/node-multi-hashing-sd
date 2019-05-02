{
    "targets": [
        {
            "target_name": "multihashing",
            "sources": [
                "multihashing.cc",
                "scryptn.c",
                "keccak.c",
                "skein.c",
                "x11.c",
		"equi.c",
                "quark.c",
                "bcrypt.c",
                "groestl.c",
                "blake.c",
                "fugue.c",
                "qubit.c",
                "hefty1.c",
                "shavite3.c",
                "cryptonight.c",
                "x13.c",
                "x14.c",
                "boolberry.cc",
                "nist5.c",
                "sha1.c",
                "x15.c",
                "fresh.c",
                "s3.c",
                "neoscrypt.c",
                "dcrypt.c",
                "jh.c",
                "c11.c",
                "sha3/sph_hefty1.c",
                "sha3/sph_fugue.c",
                "sha3/aes_helper.c",
                "sha3/sph_blake.c",
                "sha3/sph_bmw.c",
                "sha3/sph_cubehash.c",
                "sha3/sph_echo.c",
                "sha3/sph_groestl.c",
                "sha3/sph_jh.c",
                "sha3/sph_keccak.c",
                "sha3/sph_luffa.c",
                "sha3/sph_shavite.c",
                "sha3/sph_simd.c",
                "sha3/sph_skein.c",
                "sha3/sph_whirlpool.c",
                "sha3/sph_shabal.c",
                "sha3/sph_sha2.c",
                "sha3/sph_sha2big.c",
                "sha3/sph_haval.c",
                "sha3/hamsi.c",
                "xevan.c",
                "phi1612.c",
                "lyra2v2.c",
                "lyra2re.c",
                "lyra2z.c",
                "crypto/oaes_lib.c",
                "crypto/c_keccak.c",
                "crypto/c_groestl.c",
                "crypto/c_blake256.c",
                "crypto/c_jh.c",
                "crypto/c_skein.c",
                "crypto/hash.c",
                "crypto/aesb.c",
                "crypto/wild_keccak.cpp",
		"x17.c",
		"yespower/sha256.c",
		"yespower/yespower-opt.c",
		"yespower/yespower.c"
            ],
            "include_dirs": [
                "crypto",
                "<!(node -e \"require('nan')\")"
            ],
            "cflags": [
                "-D_GNU_SOURCE -maes -fPIC -Ofast -flto -fuse-linker-plugin -funroll-loops -funswitch-loops -fpeel-loops"
            ],
            "cflags!": [ 
                "-O2", "-fno-strict-aliasing", "-fno-tree-vrp", "-fno-omit-frame-pointer"
            ],
            "ldflags": [
                "-fPIC -Ofast -flto -fuse-linker-plugin"
            ],
            "cflags_cc": [
                "-std=c++11"
            ]
        }
    ]
}
