
def suzni_tugri_yoz(txt):
    return txt[0] + ''.join(txt[i] for i in range(1,len(txt)) if txt[i] != txt[i-1])
print(suzni_tugri_yoz("PPYYYTTHON"))
print(suzni_tugri_yoz("PPyyythonnn"))
print(suzni_tugri_yoz("Java"))
print(suzni_tugri_yoz("PPPHHHPPP"))
