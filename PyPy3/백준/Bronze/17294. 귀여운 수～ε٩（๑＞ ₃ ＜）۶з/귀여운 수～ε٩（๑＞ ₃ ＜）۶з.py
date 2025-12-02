a=input().strip()
if len(a)<=2:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    r = int(a[0]) - int(a[1])
    for i in range(1, len(a)-1):
        if (int(a[i]) - int(a[i+1])) != r:
            print("흥칫뿡!! <(￣ ﹌ ￣)>")
            exit(0)
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
          