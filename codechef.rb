def max(a,b)
    if a>b
        ans = a 
    else
        ans =b 
    end 
    return ans 
end 
def is_subs(s)
    n=s.size
    arr0=[0]*(n+1) 
    arr1=[0]*(n+1) 
    dp0=[0]*(n+1) 
    dp1=[0]*(n+1)
    lp0=-1;
    lp1=-1;
    i=0
    while i<n 
        if(s[i] == '1')
            j=lp1+1
            while j<(i+1)
                arr1[j]=i
                j+=1
            end
            lp1=i
        end
        i+=1
    end
    i=0
    while i<n 
        if(s[i] == '0')
            j=lp0+1
            while j<(i+1) 
                arr0[j]=i
                j+=1
            end
            lp0=i
        end 
        i+=1
    end
    i=lp0+1
    while i<n
        arr0[i]=n
        i+=1 
    end
    i=lp1+1
    while i<n 
        arr1[i]=n
        i+=1
    end
    if(arr0[0] == n)
        return '0'
    end
    i=n-1 
    while i>=0
        dp0[i]=dp0[i+1]
        if(s[i] == '0' and arr1[i] < n)
            dp0[i]=max(dp0[i],dp0[arr1[i]+1]+1)
        end
        if(s[i] == '1' and arr0[i] <n)
            dp0[i]=max(dp0[i],dp0[arr0[i]+1]+1) 
        end     
        dp1[i]=dp1[i+1]
        if(arr1[i] < n)
            dp1[i]=max(dp1[i],dp0[arr1[i]+1]+1) 
        end
        i-=1 
    end
    ln=dp1[0]+1
    ci=arr1[0]+1
    ans="1"
    i=1
    while i<ln 
        if(ci >= n)
            ans+='0'
            i+=1
            next
        end
        if(arr0[ci] >= n)
            ans+='0'
            ci=arr0[ci]+1
            i+=1
            next
        end
        if(dp0[arr0[ci]+1] <ln-i-1)
            ans+='0'
            ci=arr0[ci]+1
        else
            ans+='1'
            ci=arr1[ci]+1
        end
        i+=1
    end
    return ans 
end
t=gets.chomp.to_i
i=0
while (i<t) 
    s=gets.chomp
    puts(is_subs(s))
    i+=1 
end 