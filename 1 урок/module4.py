# def strcounter(s): #aab О(N*M) => O(N*N) => O(N^2)
#     for sym in set(s):  #ab M(уник)
#         counter = 0
#         for sub_sym in s: #aab N(все)
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)

# strcounter('aab')

def strcounter(s): #aab О(N*M) => O(N*N) => O(N^2)
    syms_counter = {}
    for sym in s:  #aab
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    for sym, count in syms_counter.items():
        print(sym, count)    
        
strcounter('aaaaaaabbbbbbcddddd')
