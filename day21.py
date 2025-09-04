def insert_bottom(st, x):
    if not st:
        st.append(x)
        return
    t = st.pop()
    insert_bottom(st, x)
    st.append(t)

def rev(st):
    if not st:
        return
    t = st.pop()
    rev(st)
    insert_bottom(st, t)

s = [1, 2, 3, 4]
rev(s)
print(s)
