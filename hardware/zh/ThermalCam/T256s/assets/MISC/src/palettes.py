"""Exact copies of the T256S firmware palettes (T256s/src/utils/palette/mod.rs)."""
import numpy as np
import base64

NAMES = ["White Hot","Black Hot","Ironbow","Rainbow","Rainbow HC","Arctic","Lava","Red Hot","Fusion",
         "Ice & Fire","Sepia","Amber","Green Hot","Medical","Magma","Gray","Hot","Cool","Inferno","Turbo"]
NAMES_ZH = ["白热","黑热","铁红","彩虹","高对比彩虹","北极","熔岩","红热","融合","冰火",
            "褐色","琥珀","绿热","医疗","熔岩紫","灰度","热色","冷色","炼狱","涡轮"]
STOPS = [
 [(0,0,0,0),(1000,255,255,255)],
 [(0,255,255,255),(1000,0,0,0)],
 [(0,0,0,8),(200,35,8,58),(450,132,25,74),(680,232,78,35),(860,255,190,74),(1000,255,255,238)],
 [(0,10,0,38),(180,22,37,180),(380,0,178,223),(580,58,210,73),(780,255,215,30),(1000,244,28,18)],
 [(0,0,0,0),(120,42,0,128),(280,0,64,255),(430,0,230,230),(570,20,210,20),(720,255,245,0),(860,255,80,0),(1000,255,255,255)],
 [(0,0,4,22),(280,18,45,112),(520,45,139,183),(700,80,61,115),(840,242,171,43),(1000,255,250,213)],
 [(0,0,0,0),(280,43,0,54),(500,132,12,111),(700,235,55,51),(880,255,164,40),(1000,255,251,205)],
 [(0,0,0,0),(500,70,0,0),(720,225,10,10),(900,255,170,18),(1000,255,255,235)],
 [(0,3,3,24),(240,46,18,105),(470,17,90,171),(670,187,40,132),(840,245,105,43),(1000,255,237,131)],
 [(0,0,10,70),(250,0,105,220),(490,183,240,255),(510,255,242,190),(750,235,74,16),(1000,96,0,0)],
 [(0,8,5,3),(350,75,43,25),(700,177,125,79),(1000,255,244,218)],
 [(0,0,0,0),(420,79,33,0),(760,225,111,0),(1000,255,232,153)],
 [(0,0,3,0),(450,0,79,23),(780,36,205,80),(1000,224,255,222)],
 [(0,0,0,20),(180,34,24,115),(360,0,124,223),(540,0,211,142),(700,230,226,29),(860,240,66,24),(1000,255,255,255)],
]
BIN_ORDER = ["magma","gray","hot","cool","inferno","turbo"]

def _interp(stops):
    lut = np.zeros((256,3), np.uint8)
    for i in range(256):
        pos = (i*1000 + 127)//255
        upper = next((k for k,s in enumerate(stops) if pos <= s[0]), len(stops)-1)
        upper = max(upper, 1)
        a, b = stops[upper-1], stops[upper]
        span = max(b[0]-a[0], 1); off = min(max(pos-a[0], 0), span)
        lut[i] = [ (a[c]*(span-off) + b[c]*off + span//2)//span for c in (1,2,3) ]
    return lut

BIN_LUTS_B64 = {
    "magma": (
        "BAAABQABBgEBCAEBCQECCwICDQICDwMDEgMDFAQEFgQFGAUGGgUGHAYHHgcIIAcJIggKJAkLJgkMKQoNKwsOLQsQLwwRMQ0S"
        "NA0TNg4UOA4VOw8WPQ8YPxAZQhAaRBAcRxEdSREeSxEgThEhUBEiUxIkVRIlWBInWhEpXBEqXxEsYREtYxEvZRExZxAzaRA0"
        "axA2bBA4bg85cA87cQ89cg8/dA9AdQ9Cdg9EdxBFeBBHeBBJeRBKehFMexFOexJPfBJRfBNSfRNUfRRWfhVXfhVZfhZafxZc"
        "fxddfxhfgBhggBligBpkgBplgBtngRxogRxqgR1rgR1tgR5ugR9wgR9ygSBzgSF1gSF2gSJ4giJ5giN7giN8giR+giWAgSWB"
        "gSaDgSaEgSeGgSeIgSiJgSmLgSmMgSqOgSqQgSuRgCuTgCyUgCyWgC2YgC2Zfy6bfy6cfy+efy+gfjChfjCjfjGlfTGmfTKo"
        "fTOqfDOrfDStezSuezWwezWyejazeja1eTe3eTe4eDi6eDm8dzm9dzq/djrAdTvCdTzEdDzFcz3Hcz7Icj7KcT/McUDNcEDP"
        "b0HQb0LSbkPTbUTVbEXWbEXYa0bZakfbaUjcaEneaErfZ0zgZk3iZU7jZE/kZFDlY1LnYlPoYlTpYVbqYFfrYFjsX1rtXlvu"
        "Xl3vXl/wXWDxXWLyXGTyXGXzXGf0XGn0XGv1XGz2XG72XHD3XHL3XHT4XHb4XXj5XXn5XXv5Xn36Xn/6X4H6X4P7YIX7YYf7"
        "YYn8Yor8Y4z8ZI78ZZD8ZpL9Z5T9aJb9aZj9apr9a5v9bJ3+bZ/+bqH+b6P+caX+cqf+c6n+dKr+dqz+d67+eLD+erL+e7T+"
        "fLb+frf+f7n+gbv+gr3+hL/+hcH+h8L+iMT+isb+jMj+jcr+j8z+kM3+ks/+lNH+ldP+l9X+mdf+mtj+nNr9ntz9oN79oeD9"
        "o+L9peP9p+X9qef9qun9rOv9ruz8sO78svD8tPL8tvT8uPb8uff8u/n8vfv8v/38"
    ),
    "gray": (
        "AAAAAQEBAgICAwMDBAQEBQUFBgYGBwcHCAgICQkJCgoKCwsLDAwMDQ0NDg4ODw8PEBAQEREREhISExMTFBQUFRUVFhYWFxcX"
        "GBgYGRkZGhoaGxsbHBwcHR0dHh4eHx8fICAgISEhIiIiIyMjJCQkJSUlJiYmJycnKCgoKSkpKioqKysrLCwsLS0tLi4uLy8v"
        "MDAwMTExMjIyMzMzNDQ0NTU1NjY2Nzc3ODg4OTk5Ojo6Ozs7PDw8PT09Pj4+Pz8/QEBAQUFBQkJCQ0NDRERERUVFRkZGR0dH"
        "SEhISUlJSkpKS0tLTExMTU1NTk5OT09PUFBQUVFRUlJSU1NTVFRUVVVVVlZWV1dXWFhYWVlZWlpaW1tbXFxcXV1dXl5eX19f"
        "YGBgYWFhYmJiY2NjZGRkZWVlZmZmZ2dnaGhoaWlpampqa2trbGxsbW1tbm5ub29vcHBwcXFxcnJyc3NzdHR0dXV1dnZ2d3d3"
        "eHh4eXl5enp6e3t7fHx8fX19fn5+f39/gICAgYGBgoKCg4ODhISEhYWFhoaGh4eHiIiIiYmJioqKi4uLjIyMjY2Njo6Oj4+P"
        "kJCQkZGRkpKSk5OTlJSUlZWVlpaWl5eXmJiYmZmZmpqam5ubnJycnZ2dnp6en5+foKCgoaGhoqKio6OjpKSkpaWlpqamp6en"
        "qKioqampqqqqq6urrKysra2trq6ur6+vsLCwsbGxsrKys7OztLS0tbW1tra2t7e3uLi4ubm5urq6u7u7vLy8vb29vr6+v7+/"
        "wMDAwcHBwsLCw8PDxMTExcXFxsbGx8fHyMjIycnJysrKy8vLzMzMzc3Nzs7Oz8/P0NDQ0dHR0tLS09PT1NTU1dXV1tbW19fX"
        "2NjY2dnZ2tra29vb3Nzc3d3d3t7e39/f4ODg4eHh4uLi4+Pj5OTk5eXl5ubm5+fn6Ojo6enp6urq6+vr7Ozs7e3t7u7u7+/v"
        "8PDw8fHx8vLy8/Pz9PT09fX19vb29/f3+Pj4+fn5+vr6+/v7/Pz8/f39/v7+////"
    ),
    "hot": (
        "AAAAAAACAAAFAAAIAAAKAAAMAAAPAAASAAAUAAAWAAAZAAAbAAAeAAAgAAAjAAAmAAAoAAAqAAAtAAAwAAAyAAA0AAA3AAA5"
        "AAA8AAA+AABBAABEAABGAABIAABLAABOAABQAABSAABVAABYAABaAABcAABfAABiAABkAABmAABpAABsAABuAABwAABzAAB1"
        "AAB4AAB6AAB9AACAAACCAACEAACHAACKAACMAACOAACRAACUAACWAACYAACbAACeAACgAACiAAClAACoAACqAACsAACvAACy"
        "AAC0AAC2AAC5AAC8AAC+AADAAADDAADGAADIAADKAADNAADQAADSAADUAADXAADaAADcAADfAADhAADkAADmAADoAADrAADu"
        "AADwAADzAAD1AAD4AAD6AAD8AAL9AAT+AAb+AAj/AAr/AA3/AA//ABL/ABT/ABb/ABn/ABz/AB7/ACD/ACP/ACb/ACj/ACr/"
        "AC3/ADD/ADL/ADT/ADf/ADr/ADz/AD7/AEH/AET/AEb/AEj/AEv/AE7/AFD/AFL/AFX/AFj/AFr/AFz/AF//AGL/AGT/AGb/"
        "AGn/AGz/AG7/AHD/AHP/AHb/AHj/AHr/AH3/AID/AIL/AIT/AIf/AIr/AIz/AI7/AJH/AJT/AJb/AJj/AJv/AJ7/AKD/AKL/"
        "AKX/AKj/AKr/AKz/AK//ALL/ALT/ALb/ALn/ALz/AL7/AMD/AMP/AMb/AMj/AMr/AM3/AND/ANL/ANT/ANf/ANr/ANz/AN7/"
        "AOH/AOT/AOb/AOj/AOv/AO7/APD/APL/APX/APj/APr/Avz/Bf3/CP7/C///D///FP//Gf//Hv//I///KP//Lf//Mv//N///"
        "PP//Qf//Rv//S///UP//Vf//Wv//X///ZP//af//bv//c///eP//ff//gv//h///jP//kf//lv//m///oP//pf//qv//r///"
        "tP//uf//vv//w///yP//zf//0v//1///3P//4f//5v//6///8P//9f//+v//////"
    ),
    "cool": (
        "//8A//4B//0C//wD//sE//oF//kG//gH//cI//YJ//UK//QL//MM//IN//EO//AP/+8Q/+4R/+0S/+wT/+sU/+oV/+kW/+gX"
        "/+cY/+YZ/+Ua/+Qb/+Mc/+Id/+Ee/+Af/98g/94h/90i/9wj/9sk/9ol/9km/9gn/9co/9Yp/9Uq/9Qr/9Ms/9It/9Eu/9Av"
        "/88w/84x/80y/8wz/8s0/8o1/8k2/8g3/8c4/8Y5/8U6/8Q7/8M8/8I9/8E+/8A//79A/75B/71C/7xD/7tE/7pF/7lG/7hH"
        "/7dI/7ZJ/7VK/7RL/7NM/7JN/7FO/7BP/69Q/65R/61S/6xT/6tU/6pV/6lW/6hX/6dY/6ZZ/6Va/6Rb/6Nc/6Jd/6Fe/6Bf"
        "/59g/55h/51i/5xj/5tk/5pl/5lm/5hn/5do/5Zp/5Vq/5Rr/5Ns/5Jt/5Fu/5Bv/49w/45x/41y/4xz/4t0/4p1/4l2/4h3"
        "/4d4/4Z5/4V6/4R7/4N8/4J9/4F+/4B//3+A/36B/32C/3yD/3uE/3qF/3mG/3iH/3eI/3aJ/3WK/3SL/3OM/3KN/3GO/3CP"
        "/2+Q/26R/22S/2yT/2uU/2qV/2mW/2iX/2eY/2aZ/2Wa/2Sb/2Oc/2Kd/2Ge/2Cf/1+g/16h/12i/1yj/1uk/1ql/1mm/1in"
        "/1eo/1ap/1Wq/1Sr/1Os/1Kt/1Gu/1Cv/0+w/06x/02y/0yz/0u0/0q1/0m2/0i3/0e4/0a5/0W6/0S7/0O8/0K9/0G+/0C/"
        "/z/A/z7B/z3C/zzD/zvE/zrF/znG/zjH/zfI/zbJ/zXK/zTL/zPM/zLN/zHO/zDP/y/Q/y7R/y3S/yzT/yvU/yrV/ynW/yjX"
        "/yfY/ybZ/yXa/yTb/yPc/yLd/yHe/yDf/x/g/x7h/x3i/xzj/xvk/xrl/xnm/xjn/xfo/xbp/xXq/xTr/xPs/xLt/xHu/xDv"
        "/w/w/w7x/w3y/wzz/wv0/wr1/wn2/wj3/wf4/wb5/wX6/wT7/wP8/wL9/wH+/wD/"
    ),
    "inferno": (
        "BAAABQABBgEBCAEBCgECDAICDgICEAIDEgMEFAMEFwQFGQQGGwUHHQUIHwYJIgcKJAcLJggMKQgNKwkOLQkQMAoRMgoSNAsU"
        "NwsVOQsWPAwYPgwZQQwbQwwcRQweSAwfSgwhTAwjTwwkUQwmUwsoVQspVwsrWQstWwovXAoxXgoyXwo0YQk2Ygk4Ywk5ZAk7"
        "ZQk9Zgk+ZwpAaApCaApEaQpFagtHagtJawxKawxMbA1NbA1PbA5RbQ5SbQ9UbQ9VbhBXbhBZbhFabhJcbhJdbhNfbhNhbhRi"
        "bhVkbhVlbhZnbhZpbhdqbhhsbhhtbhlvbhlxbhpybhp0bht1bRx3bRx4bR16bR18bR59bB5/bB+AbCCCayCEayGFayGHaiKI"
        "aiKKaSOMaSONaSSPaCWQaCWSZyaTZyaVZieXZieYZSiaZCmbZCmdYyqfYyqgYiuiYSyjYCylYC2mXy6oXi6pXi+rXTCtXDCu"
        "WzGwWjKxWjKzWTO0WDS2VzW3VjW5VTa6VDe8Uzi9Ujm/UTrAUDrBTzvDTjzETT3GTD7HSz/ISkDKSUHLSELMR0PORkTPRUXQ"
        "REbSQ0fTQkjUQUrVP0vXPkzYPU3ZPE7aO1DbOlHdOFLeN1PfNlXgNVbhNFfiM1njMVrkMFzlL13mLl7nLWDoK2HpKmPqKWTr"
        "KGbrJmfsJWntJGruI2zvIW7vIG/wH3HxHXPxHHTyG3bzGXjzGHn0F3v1FX31FH72E4D2EoL3EIT3D4X4Dof4DIn4C4v5Coz5"
        "CY75CJD6B5L6B5T6Bpb7Bpf7Bpn7Bpv7B537B5/8CKH8CaP8CqX8DKb8Daj8D6r8Eaz8Eq78FLD8FrL8GLT8Grb7Hbj7H7r7"
        "Ibz7I777JsD6KML6KsT6Lcb6L8f5Msn5Ncv5N834Os/4PdH3QNP3Q9X2Rtf2Sdn1TNv1T930U9/0VuH0WuPzXeXzYebyZejy"
        "aerybezxce3xde/xefHxffLygvTyhvXzivbzjvj0kvn1lvr2mvv4nfz5of36pP/8"
    ),
    "turbo": (
        "OxIwQxUyShgzURs0WB41XyE2ZiQ3bSc4cyo5eS06gC87hjI8izU9kTg+lzs/nD4/okBAp0NBrEZBsUlCtUtCuk5Dv1FEw1RE"
        "x1ZEy1lFz1xF015F1mFG2mRG3WZG4GlG42tG5m5H6XFH63NH7nZH8HhH8ntH9H1G9oBG+IJG+oVG+4dG/IpF/YxF/o9E/pFD"
        "/5RC/5ZB/5lA/ps+/p49/aA7/KM6+6U4+qg3+Ks1960z9a8x9LIv8rQu8Lcs7rkq67wo6b4n58Al5MMj4sUi38cg3ckf2sse"
        "2M0c1dAb0tIa0NQazdUZytcYyNkYxdsYwt0YwN4YveAYu+IZueMZtuQatOYcsucdr+kfrOogqusip+wlpO4noe8qnvAsm/Ev"
        "mPIylPM1kfQ4jvU8ivY/h/dDhPhGgPhKfflOevpSdvpVc/tZb/xdbPxhaf1lZv1pYv5tX/5xXP51Wf55Vv99U/+AUf+ETv+I"
        "S/+LSf+PR/+SRP6WQv6ZQP6cP/2fPf2hPPykOvynOfupOPusN/qvNvmxNvi0Nfe3Nfa5NPW8NPS+NPPBNPHDNPDGNO/INO3L"
        "NOzNNOrQNenSNefUNeXXNuTZNuLbN+DdN9/fN93hONvjONnlOdfnOdXpOdPrOtHsOs/uOs3vOsvxOsnyOsf0OsX1OsP2OsH3"
        "Ob74Obz5Obr6OLj7N7b7NrP8NrH8Na79NKz9M6n+Mqf+MaT+MKH+L57+LZv+LJn+K5b+KpP+KZD+J439Jor9JYf8I4T8IoH7"
        "IX77H3v6Hnj5HXX5HHL4Gm/3GWz2GGn1F2b0FWPzFGDyE13xElvwEVjvEFXtD1PsDlDrDU7qDEvoDEnnC0flCkXkCkPiCUHh"
        "CD/fCD3dBzvcBznaBjfYBjXWBTPUBTHSBS/QBC3OBCvMBCrKAyjIAybFAyXDAiPBAiG+AiC8Ah65Ah23ARu0ARqyARivARes"
        "ARapARSnAROkARKhARCeAQ+bAQ6YAQ2VAQuSAQqOAgmLAgiIAgeFAgaBAgV+AwR6"
    ),
}


def load_luts():
    """Return the 20 palettes as (256, 3) uint8 RGB arrays, in device order."""
    luts = [_interp(s) for s in STOPS]
    for name in BIN_ORDER:
        raw = np.frombuffer(base64.b64decode(BIN_LUTS_B64[name]), np.uint8).reshape(256, 3)
        luts.append(raw[:, ::-1].copy())          # the firmware stores these six as BGR
    assert len(luts) == 20
    return luts
