#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ,��R`G5e���3������t
}�%&�	r8������H���E9g��Q0�g(.�Jʔ
�g�W_�c2AU�)��ܸ���HZ�+��;`H��Uh�G?\8;�Zp�舁�x��D
z���8�I"""
from hashlib import sha256
id = sha256(blob).hexdigest()
if id == "37edda9235b241b585200a14ca2f4dfada3822225e3cf614a17f6bd2b7717aeb":
    print "I come in peace."
elif id == "1c9ce7362dabdfb0635799faefe4edecb782b7534708d84c558bc07a66484cc5":
    print "Prepare to be destroyed!"
