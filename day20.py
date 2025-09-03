def ins(st, x):
    if not st or st[-1] <= x:
        st.append(x)
        return
    t = st.pop()
    ins(st, x)
    st.append(t)

def sort(st):
    if len(st) <= 1:
        return
    t = st.pop()
    sort(st)
    ins(st, t)

s1 = [3, 1, 4, 2]
sort(s1)
print(s1)

s2 = [7, 1, 5]
sort(s2)
print(s2)

s3 = [5]
sort(s3)
print(s3)
